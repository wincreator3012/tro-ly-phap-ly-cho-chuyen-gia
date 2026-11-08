#!/usr/bin/env python3
"""Dựng, kiểm, cập nhật trợ lý pháp lý riêng từ bản vẽ; đóng gói skill.

Bản vẽ (repo tro-ly-phap-ly-cho-chuyen-gia) chỉ để đọc. Công cụ chép phần năng
lực sang một thư mục trợ lý riêng của người dùng, tạo phần riêng từ các tệp mẫu,
và về sau cập nhật phần năng lực mà không đụng tới phần riêng.

Cách dùng (chạy bằng python3; Windows dùng `py`):
    python3 <bản vẽ>/cong-cu/dung-tro-ly.py --dung <thư mục trợ lý>
    python3 cong-cu/dung-tro-ly.py --trang-thai          # trong thư mục trợ lý
    python3 cong-cu/dung-tro-ly.py --kiem
    python3 cong-cu/dung-tro-ly.py --so-ban-ve --ban-ve <thư mục bản vẽ>
    python3 cong-cu/dung-tro-ly.py --cap-nhat --ban-ve <thư mục bản vẽ> [--lam]
    python3 cong-cu/dung-tro-ly.py --cap-nhat --ban-ve <bản vẽ> --lay <đường dẫn> --lam
    python3 cong-cu/dung-tro-ly.py --goi-skill [--chi <tên skill>]
Người bảo trì bản vẽ:
    python3 cong-cu/dung-tro-ly.py --lap-danh-muc        # ghi lại BAN-DUNG.json
    python3 cong-cu/dung-tro-ly.py --goi-skill --chung   # gói chung vào dong-goi/

Ba loại tệp trong BAN-DUNG.json:
- chep: năng lực, chép nguyên văn sang trợ lý, cập nhật được về sau.
- mau: tệp mẫu tạo phần riêng (chỉ tạo khi chưa có, không bao giờ ghi đè).
- chi-ban-ve: chỉ ở bản vẽ (giới thiệu, quy trình dựng, nhật ký thay đổi).
Chỉ dùng thư viện chuẩn của Python 3.9 trở lên.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import sys
import zipfile
from pathlib import Path

DANH_MUC = "BAN-DUNG.json"
CAU_HINH = "TRO-LY.json"
TEN_BAN_VE = "tro-ly-phap-ly-cho-chuyen-gia"
CHI_BAN_VE_GOC = {"README.md", "BAT-DAU.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md",
                  "DUNG-TRO-LY.md", "CHANGELOG.md", DANH_MUC, ".gitignore", ".gitattributes"}
CHI_BAN_VE_THU_MUC = ("docs/", "dong-goi/")
BO_QUA = re.compile(r"(^|/)(\.git|__pycache__|\.DS_Store|_skill|ho-so-viec/(?!README\.md$)|chu-the/rieng)(/|$)|\.pyc$|~\$")
# Tệp mẫu: nguồn trong bản vẽ -> đích trong trợ lý
MAU_DICH = {
    "mau-tro-ly/CLAUDE.md": "CLAUDE.md",
    "mau-tro-ly/AGENTS.md": "AGENTS.md",
    "mau-tro-ly/GEMINI.md": "GEMINI.md",
    "mau-tro-ly/TRO-LY.mau.json": CAU_HINH,
    "mau-tro-ly/gitignore": ".gitignore",
}


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for khoi in iter(lambda: f.read(65536), b""):
            h.update(khoi)
    return h.hexdigest()


def hom_nay() -> str:
    return dt.date.today().isoformat()


def doc_json(p: Path) -> dict:
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def ghi_json(p: Path, d: dict) -> None:
    with open(p, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")


def dich_cua_mau(duong_dan: str) -> str:
    if duong_dan in MAU_DICH:
        return MAU_DICH[duong_dan]
    return re.sub(r"\.mau(\.[a-z]+)$", r"\1", duong_dan)


def phan_loai(duong_dan: str) -> str:
    if duong_dan in CHI_BAN_VE_GOC or duong_dan.startswith(CHI_BAN_VE_THU_MUC):
        return "chi-ban-ve"
    if duong_dan.startswith("mau-tro-ly/") or re.search(r"\.mau\.[a-z]+$", duong_dan):
        return "mau"
    return "chep"


def la_ban_ve(goc: Path) -> bool:
    return (goc / DANH_MUC).is_file() and (goc / "DUNG-TRO-LY.md").is_file()


def la_tro_ly(goc: Path) -> bool:
    return (goc / CAU_HINH).is_file() and not la_ban_ve(goc)


def goc_ban_ve_cua_cong_cu() -> Path:
    return Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------- người bảo trì

def lap_danh_muc(goc: Path) -> int:
    if not la_ban_ve(goc):
        print("DỪNG: chỉ chạy --lap-danh-muc ở gốc bản vẽ.")
        return 1
    cu = doc_json(goc / DANH_MUC) if (goc / DANH_MUC).is_file() else {}
    tep = []
    for p in sorted(goc.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(goc).as_posix()
        if BO_QUA.search(rel) or rel == DANH_MUC:
            continue
        loai = phan_loai(rel)
        muc = {"duongDan": rel, "loai": loai, "sha256": sha(p)}
        if loai == "mau":
            muc["dich"] = dich_cua_mau(rel)
        tep.append(muc)
    moi = {
        "_huong-dan": "Danh mục tệp của bản vẽ. Sinh bằng `python3 cong-cu/dung-tro-ly.py --lap-danh-muc`; không sửa tay.",
        "ten": TEN_BAN_VE,
        "phienBan": cu.get("phienBan", "1.0.0"),
        "ngay": cu.get("ngay", hom_nay()),
        "nguon": "https://github.com/wincreator3012/tro-ly-phap-ly-cho-chuyen-gia",
        "tep": tep,
    }
    ghi_json(goc / DANH_MUC, moi)
    dem = {}
    for m in tep:
        dem[m["loai"]] = dem.get(m["loai"], 0) + 1
    print("DANH MỤC: %d tệp (%s), phiên bản %s" % (len(tep), ", ".join("%s %d" % kv for kv in sorted(dem.items())), moi["phienBan"]))
    return 0


# ---------------------------------------------------------------- dựng

def dung(ban_ve: Path, dich: Path, ghi_de: bool) -> int:
    if not la_ban_ve(ban_ve):
        print("DỪNG: không thấy bản vẽ ở %s (cần %s và DUNG-TRO-LY.md)." % (ban_ve, DANH_MUC))
        return 1
    dich = dich.resolve()
    if dich == ban_ve or ban_ve in dich.parents:
        print("DỪNG: thư mục trợ lý không được nằm trong bản vẽ. Dựng ở thư mục khác, ví dụ cạnh thư mục _ban-ve/.")
        return 1
    if la_ban_ve(dich):
        print("DỪNG: thư mục đích là một bản vẽ.")
        return 1
    if la_tro_ly(dich) and not ghi_de:
        print("DỪNG: %s đã là một trợ lý (có %s). Muốn cập nhật thì dùng --cap-nhat." % (dich, CAU_HINH))
        return 1
    dm = doc_json(ban_ve / DANH_MUC)
    dich.mkdir(parents=True, exist_ok=True)
    ban_goc, loi, chep, tao = {}, 0, 0, 0
    for m in dm["tep"]:
        nguon = ban_ve / m["duongDan"]
        if m["loai"] == "chi-ban-ve":
            continue
        if not nguon.is_file():
            print("  THIẾU trong bản vẽ: %s" % m["duongDan"])
            loi += 1
            continue
        if sha(nguon) != m["sha256"]:
            print("  VÂN TAY LỆCH: %s (bản vẽ đã sửa mà chưa lập lại danh mục)" % m["duongDan"])
            loi += 1
            continue
        if m["loai"] == "chep":
            d = dich / m["duongDan"]
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(nguon, d)
            ban_goc[m["duongDan"]] = m["sha256"]
            chep += 1
        else:
            d = dich / m["dich"]
            if d.exists():
                print("  GIỮ phần riêng đã có: %s" % m["dich"])
                continue
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(nguon, d)
            tao += 1
    for td in ("ho-so-viec", "chu-the/rieng", "chu-the/mau-hop-dong"):
        (dich / td).mkdir(parents=True, exist_ok=True)
    ch = dich / CAU_HINH
    cfg = doc_json(ch) if ch.is_file() else {}
    cfg.pop("_huong-dan", None)
    cfg.update({
        "phienBan": dm["phienBan"],
        "ngayDung": cfg.get("ngayDung") or hom_nay(),
        "ngayCapNhat": hom_nay(),
        "banGoc": ban_goc,
    })
    ghi_json(ch, cfg)
    print("DỰNG: chép %d tệp năng lực, tạo %d tệp riêng, %d lỗi. Trợ lý ở: %s" % (chep, tao, loi, dich))
    return 1 if loi else 0


# ---------------------------------------------------------------- kiểm, trạng thái

def kiem(goc: Path) -> int:
    if not la_tro_ly(goc):
        print("DỪNG: chạy --kiem trong thư mục trợ lý (có %s)." % CAU_HINH)
        return 1
    cfg = doc_json(goc / CAU_HINH)
    ban_goc = cfg.get("banGoc", {})
    thieu, da_sua = [], []
    for rel, h in sorted(ban_goc.items()):
        p = goc / rel
        if not p.is_file():
            thieu.append(rel)
        elif sha(p) != h:
            da_sua.append(rel)
    can = ["HIEN-CHUONG.md", "CLAUDE.md", "AGENTS.md", CAU_HINH, "chu-the/ho-so-chu-the.md",
           "playbook/bai-hoc-tich-luy.md", "skills/phap-ly/SKILL.md", ".gitignore"]
    thieu += [c for c in can if not (goc / c).is_file() and c not in thieu]
    gi = (goc / ".gitignore").read_text(encoding="utf-8") if (goc / ".gitignore").is_file() else ""
    lo = [] if "ho-so-viec/*" in gi else ["`.gitignore` không loại `ho-so-viec/`"]
    for rel in thieu:
        print("  THIẾU: %s" % rel)
    for x in lo:
        print("  BẢO MẬT: %s" % x)
    if da_sua:
        print("  Tệp năng lực người dùng đã sửa (%d, được giữ khi cập nhật): %s" % (len(da_sua), ", ".join(da_sua[:12]) + (" ..." if len(da_sua) > 12 else "")))
    ok = not thieu and not lo
    print("KIỂM: %s (%d tệp năng lực, %d đã sửa)" % ("ĐẠT" if ok else "KHÔNG ĐẠT", len(ban_goc), len(da_sua)))
    return 0 if ok else 1


def trang_thai(goc: Path) -> int:
    if la_ban_ve(goc):
        dm = doc_json(goc / DANH_MUC)
        print("Đây là BẢN VẼ %s, phiên bản %s (%s). Không làm việc ở đây: dựng trợ lý riêng theo DUNG-TRO-LY.md." % (dm["ten"], dm["phienBan"], dm["ngay"]))
        return 0
    if not la_tro_ly(goc):
        print("Chưa có trợ lý ở %s (không thấy %s). Dựng theo DUNG-TRO-LY.md của bản vẽ." % (goc, CAU_HINH))
        return 1
    cfg = doc_json(goc / CAU_HINH)
    hs = goc / "chu-the/ho-so-chu-the.md"
    con = hs.read_text(encoding="utf-8").count("«cần điền") if hs.is_file() else -1
    tl = cfg.get("thietLap", {})
    print("Trợ lý pháp lý riêng: dựng từ bản vẽ phiên bản %s, dựng ngày %s, cập nhật %s." % (cfg.get("phienBan"), cfg.get("ngayDung"), cfg.get("ngayCapNhat")))
    print("  Người dùng: %s; xưng hô: %s" % (cfg.get("tenNguoiDung") or "chưa ghi", cfg.get("xungHo") or "chưa ghi (mặc định 'bạn')"))
    print("  Hồ sơ chủ thể: %s" % ("chưa tạo" if con < 0 else ("còn %d ô «cần điền»" % con if con else "đã điền đủ")))
    nhan = {"hoSoChuThe": "Phỏng vấn hồ sơ", "lapTruong": "Lập trường riêng", "mauHopDong": "Mẫu hợp đồng riêng",
            "baoMat": "Bảo mật, sao lưu", "goiSkill": "Gói skill", "gioiThieu": "Giới thiệu trợ lý"}
    for k, v in nhan.items():
        print("  %s: %s" % (v, tl.get(k) or "chưa"))
    nk = goc / "kien-thuc/nhat-ky-cap-nhat.md"
    if nk.is_file():
        m = re.search(r"^## (\d\d)/(\d\d)/(\d{4})", nk.read_text(encoding="utf-8"), re.M)
        if m:
            ngay = dt.date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
            cach = (dt.date.today() - ngay).days
            print("  Lần rà pháp luật gần nhất: %s (%d ngày trước)%s" % (ngay.strftime("%d/%m/%Y"), cach, "; nên chạy nhịp cập nhật" if cach > 45 else ""))
    bv = goc.parent / "_ban-ve" / TEN_BAN_VE / DANH_MUC
    if bv.is_file():
        pb = doc_json(bv)["phienBan"]
        if pb != cfg.get("phienBan"):
            print("  Bản vẽ trong _ban-ve/ đang ở phiên bản %s: có thể cập nhật (--so-ban-ve)." % pb)
    goi = sorted((goc / "_skill").glob("*.zip")) if (goc / "_skill").is_dir() else []
    print("  Gói skill trong _skill/: %d" % len(goi))
    return 0


# ---------------------------------------------------------------- cập nhật

def so_sanh(goc: Path, ban_ve: Path):
    cfg = doc_json(goc / CAU_HINH)
    ban_goc = cfg.get("banGoc", {})
    dm = doc_json(ban_ve / DANH_MUC)
    moi, an_toan, xung_dot, giu, mau_moi = [], [], [], [], []
    trong_ban_ve = set()
    for m in dm["tep"]:
        rel = m["duongDan"]
        if m["loai"] == "mau":
            if not (goc / m["dich"]).exists():
                mau_moi.append(m)
            continue
        if m["loai"] != "chep":
            continue
        trong_ban_ve.add(rel)
        p = goc / rel
        if rel not in ban_goc:
            (xung_dot if p.exists() and sha(p) != m["sha256"] else moi).append(m)
            continue
        nguoi_sua = p.is_file() and sha(p) != ban_goc[rel]
        ban_ve_sua = m["sha256"] != ban_goc[rel]
        if not p.is_file():
            moi.append(m)
        elif ban_ve_sua and nguoi_sua:
            xung_dot.append(m)
        elif ban_ve_sua:
            an_toan.append(m)
        elif nguoi_sua:
            giu.append(m)
    bo = sorted(r for r in ban_goc if r not in trong_ban_ve)
    return cfg, dm, moi, an_toan, xung_dot, giu, mau_moi, bo


def in_so_sanh(goc: Path, ban_ve: Path) -> int:
    cfg, dm, moi, an_toan, xung_dot, giu, mau_moi, bo = so_sanh(goc, ban_ve)
    print("Trợ lý ở phiên bản %s; bản vẽ ở phiên bản %s." % (cfg.get("phienBan"), dm["phienBan"]))
    for ten, ds in (("Tệp mới trong bản vẽ", moi), ("Bản vẽ đã đổi, người dùng chưa sửa (cập nhật an toàn)", an_toan),
                    ("CẢ HAI đã đổi (cần trộn hoặc chọn)", xung_dot), ("Người dùng đã sửa, bản vẽ chưa đổi (giữ nguyên)", giu),
                    ("Tệp mẫu mới (sẽ tạo phần riêng)", mau_moi)):
        if ds:
            print("%s (%d):" % (ten, len(ds)))
            for m in ds:
                print("  - %s" % m.get("dich", m["duongDan"]) if m in mau_moi else "  - %s" % m["duongDan"])
    if bo:
        print("Bản vẽ đã bỏ (%d), hỏi người dùng trước khi chuyển vào _to_delete/:" % len(bo))
        for r in bo:
            print("  - %s" % r)
    if not any((moi, an_toan, xung_dot, mau_moi, bo)):
        print("Không có gì để cập nhật.")
    return 0


def cap_nhat(goc: Path, ban_ve: Path, lam: bool, lay: list) -> int:
    cfg, dm, moi, an_toan, xung_dot, giu, mau_moi, bo = so_sanh(goc, ban_ve)
    lay = set(lay or [])
    viec = moi + an_toan + [m for m in xung_dot if m["duongDan"] in lay]
    if not lam:
        in_so_sanh(goc, ban_ve)
        print("\nCHƯA GHI GÌ. Thêm --lam để áp %d tệp an toàn%s." % (len(moi) + len(an_toan), "" if not xung_dot else "; tệp xung đột chỉ ghi khi chỉ định --lay <đường dẫn>"))
        return 0
    ban_goc = cfg.get("banGoc", {})
    for m in viec:
        nguon = ban_ve / m["duongDan"]
        if sha(nguon) != m["sha256"]:
            print("  VÂN TAY LỆCH, bỏ qua: %s" % m["duongDan"])
            continue
        d = goc / m["duongDan"]
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(nguon, d)
        ban_goc[m["duongDan"]] = m["sha256"]
        print("  ghi: %s" % m["duongDan"])
    for m in mau_moi:
        d = goc / m["dich"]
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ban_ve / m["duongDan"], d)
        print("  tạo phần riêng: %s" % m["dich"])
    con_xd = [m["duongDan"] for m in xung_dot if m["duongDan"] not in lay]
    cfg["banGoc"] = ban_goc
    if not con_xd:
        cfg["phienBan"] = dm["phienBan"]
    cfg["ngayCapNhat"] = hom_nay()
    ghi_json(goc / CAU_HINH, cfg)
    print("CẬP NHẬT: ghi %d tệp; còn %d tệp xung đột chưa xử lý%s." % (len(viec), len(con_xd), (": " + ", ".join(con_xd)) if con_xd else ""))
    if bo:
        print("Bản vẽ đã bỏ %d tệp; hỏi người dùng, cần bỏ thì chuyển vào _to_delete/, không tự xóa." % len(bo))
    return 0


# ---------------------------------------------------------------- đóng gói skill

def doc_frontmatter(t: str):
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if not m:
        return {}, t
    fm = {}
    for dong in m.group(1).splitlines():
        if ":" in dong:
            k, v = dong.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, t[m.end():]


def khoi_da_thiet_lap(goc: Path) -> str:
    cfg = doc_json(goc / CAU_HINH)
    return (
        "\n\n## Đã thiết lập\n\n"
        "Gói này đóng từ trợ lý pháp lý riêng của %s ngày %s (bản vẽ phiên bản %s).\n\n"
        "- Gọi người dùng là: %s.\n"
        "- Thư mục trợ lý trên máy người dùng: `%s`. Khi phiên truy cập được thư mục này, làm việc tại đó và đọc `HIEN-CHUONG.md`, `CLAUDE.md`, `chu-the/ho-so-chu-the.md` trước.\n"
        "- Khi phiên không truy cập được thư mục ấy: làm theo mục \"Nguồn tri thức và khi không có repo\" ở đầu skill; không đoán thông tin chủ thể, hỏi người dùng.\n"
        % (cfg.get("tenNguoiDung") or "người dùng", hom_nay(), cfg.get("phienBan"),
           cfg.get("xungHo") or "bạn", cfg.get("thuMucTroLy") or "(chưa ghi trong TRO-LY.json)")
    )


def goi_skill(goc: Path, chi: list, chung: bool) -> int:
    if chung:
        if not la_ban_ve(goc):
            print("DỪNG: --chung chỉ chạy ở gốc bản vẽ.")
            return 1
        ra = goc / "dong-goi"
    else:
        if not la_tro_ly(goc):
            print("DỪNG: chạy --goi-skill trong thư mục trợ lý (có %s); ở bản vẽ dùng --chung." % CAU_HINH)
            return 1
        ra = goc / "_skill"
    ra.mkdir(exist_ok=True)
    loi, so = 0, 0
    for sd in sorted((goc / "skills").iterdir()):
        if not (sd / "SKILL.md").is_file() or (chi and sd.name not in chi):
            continue
        t = (sd / "SKILL.md").read_text(encoding="utf-8")
        fm, _ = doc_frontmatter(t)
        ten, mo_ta = fm.get("name", ""), fm.get("description", "")
        van_de = []
        if ten != sd.name:
            van_de.append("name '%s' khác tên thư mục" % ten)
        if not re.fullmatch(r"[a-z0-9-]{1,64}", ten or "-") or "claude" in ten or "anthropic" in ten:
            van_de.append("name không hợp lệ")
        if not mo_ta or len(mo_ta) > 1024 or "<" in mo_ta or ">" in mo_ta:
            van_de.append("description rỗng, quá 1024 ký tự hoặc có dấu < >")
        if van_de:
            print("  LỖI %s: %s" % (sd.name, "; ".join(van_de)))
            loi += 1
            continue
        if not chung:
            t = t.rstrip("\n") + khoi_da_thiet_lap(goc)
        dich = ra / (sd.name + ".zip")
        with zipfile.ZipFile(dich, "w", zipfile.ZIP_DEFLATED) as z:
            for p in sorted(sd.rglob("*")):
                if p.is_file() and not BO_QUA.search(p.as_posix()):
                    rel = "%s/%s" % (sd.name, p.relative_to(sd).as_posix())
                    zi = zipfile.ZipInfo(rel, date_time=(2026, 1, 1, 0, 0, 0))
                    zi.compress_type = zipfile.ZIP_DEFLATED
                    du_lieu = t.encode("utf-8") if p.name == "SKILL.md" and p.parent == sd else p.read_bytes()
                    z.writestr(zi, du_lieu)
        if chung:
            tep_da = ra / "tep-cho-du-an"
            tep_da.mkdir(exist_ok=True)
            (tep_da / (sd.name + ".md")).write_text(t, encoding="utf-8")
            for p in sorted(sd.rglob("*")):
                if p.is_file() and p.parent != sd and p.suffix == ".md":
                    (tep_da / ("%s--%s" % (sd.name, p.name))).write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
        so += 1
        print("  gói: %s" % dich.relative_to(goc))
    if chung and so:
        shutil.copy2(goc / "HIEN-CHUONG.md", ra / "tep-cho-du-an" / "hien-chuong.md")
    if not chung and so:
        cfg = doc_json(goc / CAU_HINH)
        cfg.setdefault("thietLap", {})["goiSkill"] = hom_nay()
        ghi_json(goc / CAU_HINH, cfg)
    print("ĐÓNG GÓI: %s (%d gói, %d lỗi) vào %s" % ("ĐẠT" if not loi else "KHÔNG ĐẠT", so, loi, ra))
    return 1 if loi else 0


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dung", metavar="THU_MUC_TRO_LY")
    g.add_argument("--kiem", action="store_true")
    g.add_argument("--trang-thai", action="store_true")
    g.add_argument("--so-ban-ve", action="store_true")
    g.add_argument("--cap-nhat", action="store_true")
    g.add_argument("--goi-skill", action="store_true")
    g.add_argument("--lap-danh-muc", action="store_true")
    ap.add_argument("--ban-ve", metavar="THU_MUC_BAN_VE")
    ap.add_argument("--goc", metavar="THU_MUC", help="thư mục trợ lý hoặc bản vẽ (mặc định: thư mục đang đứng)")
    ap.add_argument("--lam", action="store_true", help="thật sự ghi khi cập nhật")
    ap.add_argument("--lay", nargs="*", metavar="DUONG_DAN", help="lấy bản của bản vẽ cho các tệp xung đột này")
    ap.add_argument("--ghi-de", action="store_true", help="cho phép --dung vào một trợ lý đã có (không đụng phần riêng)")
    ap.add_argument("--chi", nargs="*", metavar="TEN_SKILL")
    ap.add_argument("--chung", action="store_true", help="gói chung (không cấu hình riêng) vào dong-goi/ của bản vẽ")
    a = ap.parse_args()
    goc = Path(a.goc).resolve() if a.goc else Path.cwd().resolve()
    if a.lap_danh_muc:
        return lap_danh_muc(goc)
    if a.dung:
        bv = Path(a.ban_ve).resolve() if a.ban_ve else goc_ban_ve_cua_cong_cu()
        return dung(bv, Path(a.dung), a.ghi_de)
    if a.kiem:
        return kiem(goc)
    if a.trang_thai:
        return trang_thai(goc)
    if a.goi_skill:
        return goi_skill(goc, a.chi, a.chung)
    if not la_tro_ly(goc):
        print("DỪNG: chạy trong thư mục trợ lý (có %s)." % CAU_HINH)
        return 1
    bv = Path(a.ban_ve).resolve() if a.ban_ve else goc.parent / "_ban-ve" / TEN_BAN_VE
    if not la_ban_ve(bv):
        print("DỪNG: không thấy bản vẽ ở %s. Lấy bản vẽ mới về _ban-ve/ trước (DUNG-TRO-LY.md, mục Cập nhật)." % bv)
        return 1
    if a.so_ban_ve:
        return in_so_sanh(goc, bv)
    return cap_nhat(goc, bv, a.lam, a.lay)


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Soi văn bản theo chuẩn ngôn ngữ và trình bày của trợ lý pháp lý.

Chuẩn gốc: chuan/ngon-ngu-va-trinh-bay.md. Danh sách từ và mẫu cấu trúc rút từ
Xưởng viết AI của Lương Dũng Nhân (bản vẽ công khai
https://github.com/wincreator3012/xuong-viet-ai, bảng
skills/viet-nguyen-ban/references/tu-vung-va-cau-truc.md), cộng bảng dịch sát
riêng của văn bản pháp lý. Khi bảng ấy cập nhật, sửa các danh sách ở đầu file
này cho khớp.

Cách dùng:
    python3 cong-cu/soi-van-ban.py                  # soi toàn repo (trừ ho-so-viec/)
    python3 cong-cu/soi-van-ban.py duong/dan.md     # soi một file hoặc thư mục
    python3 cong-cu/soi-van-ban.py hop-dong.docx    # soi file Word (chỉ báo, không sửa)
    python3 cong-cu/soi-van-ban.py --sua duong/dan  # sửa tự động phần an toàn rồi soi
    python3 cong-cu/soi-van-ban.py --tang 3 file.md # ép xem là văn bản gửi ra ngoài

--sua chỉ sửa .md và .txt: đưa về Unicode dựng sẵn, đặt dấu thanh kiểu cũ
(hoá -> hóa, thoả -> thỏa, toà -> tòa), ba chấm Unicode -> "...", ngoặc kép cong
-> ngoặc kép thẳng. Em dash, en dash và mọi lỗi từ ngữ phải sửa bằng tay.

Mức báo:
- LỖI: phải sửa trước khi bàn giao. Mã thoát 1 nếu còn lỗi.
- CẢNH BÁO: người đọc xem lại tại chỗ; giữ thì ghi lý do vào ghi chú bàn giao.
Máy chỉ đếm phần đếm được; nhịp câu, nghĩa pháp lý của chữ "sẽ", "có thể",
và việc một từ ngờ có đang là thuật ngữ luật định hay không là việc của người đọc.

Ngoại lệ:
- File có dòng <!-- soi-van-ban: danh-sach --> (như chính file chuẩn) chỉ bị
  soi dấu câu, dấu thanh và tiêu đề, vì nó liệt kê từ cấm để dạy.
- Dòng nêu quy ước ("không dùng", "không viết", "không dịch", "thay "...",
  "dịch sát") được phép nhắc từ cấm.
- Khối mã, mã nội dòng và trích dẫn khối (>) không bị soi từ ngữ.
"""
import re
import sys
import unicodedata
import zipfile
from pathlib import Path

GOC = Path(__file__).resolve().parent.parent
BO_QUA = {"ho-so-viec", ".git", "node_modules", "rieng", ".claude"}
DUOI = {".md", ".txt", ".docx"}
W = r"[^\W_]"

# ---------------------------------------------------------------- danh sách

# A1. Thuật ngữ đã chốt: (mẫu, gợi ý)
A1 = [
    (r"(?<!bị )dẫn dắt", "dùng 'hướng dẫn', 'lãnh đạo', 'đưa đến' (giữ 'bị dẫn dắt' sắc thái tiêu cực)"),
    (r"nhân văn", "humanistic dịch là 'nhân bản'"),
    (r"thấu cảm", "dùng 'đồng cảm'"),
    (r"sang chấn", "dùng 'chấn thương tâm lý'"),
    (r"đa mê tẩu", "dùng 'lý thuyết đa phế vị'"),
    (r"lược đồ", "schema: 'cấu trúc nhận thức' hoặc 'cấu trúc tâm-thể'"),
    (r"nhận cảm thần kinh", "dùng 'cảm nhận an nguy'"),
    (r"hệ thần kinh gương", "dùng 'hệ thần kinh phản chiếu'"),
    (r"kỷ luật phục hồi", "dùng 'Công lý Phục hồi'"),
    (r"làm nhục công khai", "dùng 'gây xấu hổ trước nhiều người'"),
    (r"tỉ lệ", "dùng 'tỷ lệ'"),
    (r"một câu (chốt|cốt lõi)", "ghi nhãn trực tiếp 'Chốt:', 'Kết luận:'"),
    (r"phán đoán đạo đức", "judgment của con người: 'suy xét đạo đức'"),
]

# A2. Cụm sáo AI
A2 = [
    r"trong bối cảnh .{1,60}?(phát triển không ngừng|phát triển mạnh mẽ)",
    r"trong (thời đại số|kỷ nguyên 4\.0|kỷ nguyên ai|xã hội hiện đại|thời đại nhịp sống nhanh)",
    r"hãy (tưởng tượng|hình dung)", r"bạn đã bao giờ tự hỏi", r"từ xưa đến nay",
    r"như đã đề cập", r"như chúng ta đã thấy", r"trong phần này", r"tiếp theo, chúng ta sẽ",
    r"(chúng ta )?hãy cùng", r"(điều )?đáng chú ý là", r"cần lưu ý rằng", r"quan trọng hơn cả",
    r"có thể nói rằng", r"có thể thấy rằng", r"nhìn chung thì", r"về cơ bản,",
    r"tóm lại,", r"kết luận là,", r"hành trình .{0,30}?vẫn còn ở phía trước",
    r"hy vọng (bài viết|email|thư) (này )?(hữu ích|đến với)", r"cảm ơn bạn đã đọc",
    r"đừng bỏ lỡ cơ hội", r"bước tiến đúng hướng", r"tảng băng chìm", r"bức tranh toàn cảnh",
    r"mở ra một (chương|kỷ nguyên|cánh cửa) mới", r"cánh cửa dẫn đến", r"định hình tương lai",
    r"thay đổi cuộc chơi", r"đóng vai trò (then chốt|cốt lõi|quan trọng|trung tâm)",
    r"một phần không thể thiếu", r"cần thiết hơn bao giờ hết", r"(giá trị|lợi ích) vượt trội",
    r"người bạn đồng hành đáng tin cậy", r"phát huy tối đa tiềm năng",
    r"nghiên cứu chỉ ra rằng", r"các chuyên gia cho rằng", r"theo nhiều nguồn tin",
    r"được công nhận rộng rãi", r"câu hỏi của (bạn|anh|chị|thầy|cô|người dùng) (thật |rất )?(tuyệt vời|hay)",
    r"là một mô hình (ai|ngôn ngữ)", r"trong tình trạng tốt nhất",
]

# A3. Từ vựng AI hiếm gặp trong văn tiếng Việt chuẩn mực
A3 = ["đắm mình", "vén màn", "ngoạn mục", "đáng kinh ngạc", "vượt trội", "tiên tiến",
      "liền mạch", "đẳng cấp", "thượng đỉnh", "nâng tầm"]

# A4. Kết hợp từ sai và dịch sát của văn thường (bảng A4 Xưởng viết AI)
A4 = [
    r"khép lại (chương trình|khóa học|ngày học|buổi học)", r"mọc lên từ",
    r"đọc (năng lượng|tình huống|người khác|cơ thể|phản ứng)", r"rất người",
    r"làm việc cho người nói", r"tự thoại nội tâm", r"tái định nghĩa thất bại",
    r"mang một gánh", r"để lại một khoảng trống", r"tìm \"?(cái )?bộ lạc\"? của",
    r"chạy trọn", r"gọi tên (một |những |các )?(cảm xúc|cảm giác|nỗi|rủi ro)",
    r"giáo sư trợ lý",
]

# PL. Dịch sát đặc thù văn bản pháp lý: (mẫu, gợi ý)
PL = [
    (r"vi phạm (vật chất|trọng yếu)", "material breach: 'vi phạm nghiêm trọng' (thuật ngữ Bộ luật Dân sự)"),
    (r"đại diện và bảo đảm", "represent and warrant: 'cam đoan và bảo đảm'"),
    (r"chấm dứt vì sự thuận tiện", "'đơn phương chấm dứt không cần nêu lý do'"),
    (r"(theo đây|bằng văn bản này,? bên)", "hereby: bỏ 'theo đây', viết thẳng động từ"),
    (r"vào hoặc trước ngày", "on or before: 'chậm nhất vào ngày'"),
    (r"nỗ lực tốt nhất", "best efforts: thuật ngữ luật định là 'nỗ lực và khả năng cao nhất' (Luật Thương mại, Điều 80), hoặc nêu việc cụ thể phải làm"),
    (r"chịu trách nhiệm cho", "'chịu trách nhiệm về'"),
    (r"trong trường hợp mà", "'nếu', 'trường hợp'"),
    (r"trong sự kiện (mà|rằng)", "in the event that: 'nếu'"),
    (r"bất kể (điều gì|bất kỳ điều gì) (trái|ngược)", "'Không phụ thuộc vào quy định khác của Hợp đồng này'"),
    (r"cho (các|những) mục đích của", "for the purposes of: 'Trong Điều này,'"),
    (r"sự siêng năng (cần thiết|đúng hạn|đúng mức)", "due diligence: 'thẩm định'"),
    (r"(các )?sản phẩm có thể (giao|bàn giao)", "deliverables: 'sản phẩm bàn giao'"),
    (r"chỉ định (quyền|hợp đồng)", "assign: 'chuyển giao quyền và nghĩa vụ'"),
]

# Cảnh báo dịch sát cấp câu và lối diễn đạt pháp lý cần xem lại: (mẫu, gợi ý)
PL_CANH_BAO = [
    (r"ngay lập tức", "'ngay', hoặc thời hạn cụ thể"),
    (r"và/hoặc", "'hoặc', hoặc 'A, B hoặc cả hai'"),
    (r"một cách (?!thiện chí)" + W + r"+", "bỏ 'một cách', hoặc thay tính từ bằng nghĩa vụ đo được"),
    (r"(thực hiện|tiến hành) việc", "dùng thẳng động từ ('thanh toán', 'bàn giao', 'ký')"),
    (r"tiến hành thực hiện", "dùng thẳng động từ"),
    (r"được (thực hiện|đưa ra|ký kết|chuyển|gửi|cung cấp|thanh toán) bởi", "bị động có tác nhân: đưa tác nhân lên làm chủ ngữ"),
]

# C. Từ ngờ (cảnh báo). Đã bỏ các từ là thuật ngữ pháp lý: khai thác, bí quyết, công thức.
C = ["kiến tạo", "vun đắp", "ươm mầm", "lan tỏa", "tận dụng", "tối ưu", "phát huy",
     "đột phá", "mạnh mẽ", "tinh tế", "trọn vẹn", "đáng kể", "sâu sắc", "toàn diện", "ấn tượng",
     "đáng chú ý", "then chốt", "cốt lõi", "hành trình", "kỷ nguyên", "bối cảnh", "lăng kính",
     "chìa khóa", "cuộc cách mạng", "bức tranh", "dấu ấn", "cánh cửa", "cực kỳ", "hết sức",
     "mãnh liệt", "vô cùng", "đam mê", "khát khao", "truyền cảm hứng", "chạm đến", "lay động",
     "giải pháp tối ưu", "trải nghiệm", "khách hàng tiềm năng", "đối tác chiến lược",
     "cam kết chất lượng", "dịch vụ chuyên nghiệp", "đồng hành", "nuôi dưỡng"]

TU_NOI_DEM = ["hơn nữa", "thêm vào đó", "bên cạnh đó", "ngoài ra", "đặc biệt là", "mặt khác"]

# D1. Từ đơn âm tiết: từ -> các tiếng đứng trước tạo thành từ ghép hợp lệ
DON_AM_TIET = {
    "chăm": set(), "rèn": {"tôi"},
    "nghỉ": {"kỳ", "ngày", "giờ", "buổi", "chỗ", "nơi", "an", "tạm", "xin"},
    "vững": {"bền", "kiên", "chắc", "ổn", "vững"},
    "đủ": {"biết", "đầy", "no", "tạm", "vừa", "chưa", "là"},
    "nặng": {"nặng", "nghiêm", "trĩu", "ốm"}, "nhẹ": {"nhẹ", "nhỏ", "gọn"},
    "ấm": {"ấm", "sưởi"}, "lạ": {"xa", "kỳ", "lạ", "mới"}, "bền": {"bền"},
    "lạnh": {"lạnh", "giá", "rét"}, "gấp": {"cấp", "khẩn", "gấp", "gập", "hạn"},
}

# A5. Chữ số
SO_CHU = r"(hai|ba|bốn|năm|sáu|bảy|tám|chín|mười|mười một|mười hai)"
DON_VI = (r"(phút|giờ|ngày|tuần|tháng|lần|bước|dòng|câu|điểm|rủi ro|dữ kiện|mẫu|file|"
          r"skill|chủ đề|văn bản|điều khoản|vòng|đợt|buổi|người|bản|mục|phương án)")

# Tiếng Anh hay lọt vào văn bản gửi ra ngoài (tầng 3)
TIENG_ANH = ["outline", "slide", "flipchart", "tea-break", "prompt", "chatbot", "deadline",
             "feedback", "deal", "fee", "invoice", "NDA", "MOU", "KPI"]

# Thuật ngữ được giữ một tiếng hay câu ngắn trong hợp đồng thì không cần danh sách:
# các kiểm cấu trúc D chỉ chạy ở tầng 1 và 2.

TONES = "̣́̀̉̃"


def _dau_thanh():
    pats = []
    for v1, v2 in (("oO", "aA"), ("oO", "eE"), ("uU", "yY")):
        toned = "".join(unicodedata.normalize("NFC", b + t) for b in v2 for t in TONES)
        guard = r"(?<![qQ])" if v1 == "uU" else ""
        pats.append(guard + "([" + v1 + "])([" + toned + "])(?!" + W + ")")
    return re.compile("|".join("(?:%s)" % p for p in pats))


RX_DAU = _dau_thanh()


def sua_dau(m):
    v1, v2 = [x for x in m.groups() if x is not None]
    d = unicodedata.normalize("NFD", v2)
    return unicodedata.normalize("NFC", v1 + d[1:]) + d[0]


def sua_tu_dong(text):
    text = unicodedata.normalize("NFC", text)
    text, n = RX_DAU.subn(sua_dau, text)
    n += text.count("…") + sum(text.count(k) for k in "“”")
    text = text.replace("…", "...").replace("“", '"').replace("”", '"')
    return text, n


# ---------------------------------------------------------------- đọc file

def doc_docx(f):
    with zipfile.ZipFile(f) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    doan = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml, re.S):
        chu = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))
        chu = chu.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"')
        doan.append(chu)
    return doan


def danh_sach_file(muc):
    if muc.is_file():
        return [muc]
    return sorted(f for f in muc.rglob("*") if f.suffix in DUOI and f.is_file()
                  and not any(p in BO_QUA for p in f.relative_to(muc).parts))


def tang_cua(f, ep):
    if ep:
        return ep
    s = str(f)
    if f.suffix == ".docx" or ("/hop-dong/" in s and f.name != "README.md"):
        return 3
    return 2


# ---------------------------------------------------------------- soi

def tim(mau, dong):
    return re.finditer(r"(?<!" + W + ")" + mau + r"(?!" + W + ")", dong, re.I)


def soi_file(f, ep_tang=None):
    loi, canh_bao = [], []
    tang = tang_cua(f, ep_tang)
    if f.suffix == ".docx":
        dong_list = doc_docx(f)
        nhan = "đoạn"
    else:
        dong_list = f.read_text(encoding="utf-8").splitlines()
        nhan = "dòng"
    toan_van = "\n".join(dong_list)
    chi_trinh_bay = "<!-- soi-van-ban: danh-sach -->" in toan_van
    trong_code = False
    dem_C, dem_noi, dem_bat_ky = {}, {}, 0
    phan_hoi = [0]
    doi_ngau = 0
    for i, goc in enumerate(dong_list, 1):
        dong = unicodedata.normalize("NFC", goc)
        if dong.strip().startswith("```"):
            trong_code = not trong_code
            continue
        if trong_code:
            continue
        vt = "%s %d" % (nhan, i)

        # Dấu câu và dấu thanh: soi mọi dòng
        for k, ly_do in (("—", "em dash: dùng ' - ' hoặc ':'"),
                         ("–", "en dash: dùng '-' (khoảng số, tiêu ngữ) hoặc ' - '"),
                         ("…", "ba chấm Unicode: gõ '...'"),
                         ("“", "ngoặc kép cong: dùng ngoặc kép thẳng"),
                         ("‘", "ngoặc đơn cong: dùng nháy thẳng")):
            if k in dong:
                loi.append((vt, ly_do))
        sai_dau = sorted({t for t in re.findall(W + "+", dong) if RX_DAU.search(t)})
        if sai_dau:
            loi.append((vt, "dấu thanh kiểu mới %s: viết kiểu cũ (chạy --sua)" % ", ".join(sai_dau)))
        if dong.startswith("#"):
            if title_case(dong):
                canh_bao.append((vt, "tiêu đề có dáng Title Case: %s" % dong.strip()))
            phan_hoi.append(0)

        if chi_trinh_bay:
            continue
        thap = dong.lower()
        if dong.lstrip().startswith(">"):
            continue
        if any(k in thap for k in ("không dùng", "không viết", "không dịch", "thay \"", "thay '", "thay cho \"", "dịch sát")):
            continue
        sach = re.sub(r"`[^`]*`", "", dong)

        for mau, goi_y in A1:
            for m in tim(mau, sach):
                loi.append((vt, "'%s' - %s" % (m.group(0), goi_y)))
        for mau in A2:
            for m in tim(mau, sach):
                loi.append((vt, "cụm sáo '%s'" % m.group(0)))
        for t in A3:
            for m in tim(re.escape(t), sach):
                loi.append((vt, "từ vựng AI '%s': nói cụ thể điều gì, bao nhiêu" % m.group(0)))
        for mau in A4:
            for m in tim(mau, sach):
                loi.append((vt, "dịch sát hoặc kết hợp từ sai '%s' (bảng A4 Xưởng viết AI)" % m.group(0)))
        for mau, goi_y in PL:
            for m in tim(mau, sach):
                loi.append((vt, "dịch sát pháp lý '%s' - %s" % (m.group(0), goi_y)))
        for mau, goi_y in PL_CANH_BAO:
            for m in tim(mau, sach):
                canh_bao.append((vt, "'%s' - %s" % (m.group(0), goi_y)))
        for t in C:
            n = len(list(tim(re.escape(t), sach)))
            if n:
                dem_C.setdefault(t, []).append(i)
        for t in TU_NOI_DEM:
            if list(tim(re.escape(t), sach)):
                dem_noi.setdefault(t, []).append(i)
        dem_bat_ky += len(list(tim("bất kỳ", sach)))

        # D2: khung câu dịch sát (không soi tiêu đề)
        for m in [] if dong.startswith("#") else re.finditer(r"(^|[.!?]\s+|^\s*[-*\d.]+\s+)(sự (\S+ ){1,2}của|việc (?!này|đó|ấy|gì|của|làm|đã|và|hoặc|cần|nào|thật|mới|anh|chị|bạn|người|chính)\S+ (?!là)|tầm quan trọng của)", sach, re.I):
            canh_bao.append((vt, "danh từ hóa mở câu '%s': đưa người làm lên chủ ngữ" % m.group(2).strip()))
        for m in re.finditer(r"(^|[.!?]\s+)điều (này|đó|ấy)(?!" + W + ")", sach, re.I):
            canh_bao.append((vt, "'Điều %s' mở câu: gộp vào câu trước hoặc thay bằng danh từ cụ thể" % m.group(2)))
        doi_ngau += len(re.findall(r"không chỉ .{1,80}? mà còn|không phải (là )?.{1,80}? mà là", sach, re.I))

        # D1: từ một tiếng đứng cuối mệnh đề
        for tu, ok in DON_AM_TIET.items():
            for m in re.finditer(r"(?<!" + W + r")(" + W + r"+\s+)?" + tu + r"(?=\s*([,.;:!?)\]\"|]|$))", sach, re.I):
                truoc = (m.group(1) or "").strip().lower()
                if truoc in ok:
                    continue
                canh_bao.append((vt, "từ một tiếng '%s': đọc to, nới thành hai âm tiết nếu câu hụt hơi" % m.group(0).strip()))

        # A5: chữ số
        bo_ngoac = re.sub(r"đánh thuế hai lần", "", sach)
        bo_ngoac = re.sub(r"\d+\s*\((" + SO_CHU + r"|[^)]*)\)", "", bo_ngoac)
        for cau in re.split(r"[.!?;|]", bo_ngoac):
            co_chu = re.search(r"(?<!" + W + ")" + SO_CHU + r"\s+" + DON_VI + r"(?!" + W + ")", cau, re.I)
            if co_chu and re.search(r"\d", cau):
                canh_bao.append((vt, "trộn chữ và số ('%s'): dùng chữ số cho mọi đại lượng" % co_chu.group(0)))
            elif co_chu and tang < 3:
                canh_bao.append((vt, "số viết bằng chữ ('%s'): dùng chữ số, trừ tên gọi đã chốt" % co_chu.group(0)))

        if "?" in sach and not dong.lstrip().startswith(("|", "-", "*")) and tang < 3:
            phan_hoi[-1] += sach.count("?")

        # Tầng 3: văn bản gửi ra ngoài
        if tang == 3:
            for m in re.finditer(r"(Bên [AB]|Hai Bên|Mỗi Bên|các Bên|Bên kia)\s+(sẽ)(?!" + W + ")", sach):
                canh_bao.append((vt, "'%s sẽ': đặt nghĩa vụ thì viết 'có nghĩa vụ', 'phải' hoặc động từ trần" % m.group(1)))
            for m in re.finditer(r"(Bên [AB]|Mỗi Bên|Bên kia)\s+(có thể)(?!" + W + ")", sach):
                canh_bao.append((vt, "'%s có thể': nếu là quyền thì viết 'có quyền'" % m.group(1)))
            for t in TIENG_ANH:
                for m in tim(re.escape(t), sach):
                    if t.isupper() and m.group(0) != t:
                        continue
                    canh_bao.append((vt, "tiếng Anh '%s' trong văn bản gửi ra ngoài: thuần Việt hoặc định nghĩa một lần" % m.group(0)))

    if not chi_trinh_bay:
        for t, ds in dem_C.items():
            canh_bao.append(("%s %s" % (nhan, ", ".join(map(str, ds[:8]))),
                             "từ ngờ '%s' x%d: giữ khi là thuật ngữ luật định hoặc nghĩa riêng của người dùng, không thì thay" % (t, len(ds))))
        for t, ds in dem_noi.items():
            if len(ds) > 1 and tang < 3:
                canh_bao.append(("%s %s" % (nhan, ", ".join(map(str, ds))), "từ nối đệm '%s' x%d, trần 1" % (t, len(ds))))
        so_chu = len(re.findall(W + "+", toan_van))
        tran = 1 if so_chu < 1000 else 2
        if doi_ngau > tran and tang < 3:
            canh_bao.append(("cả file", "đối ngẫu phủ định x%d, trần %d" % (doi_ngau, tran)))
        if dem_bat_ky > 5:
            canh_bao.append(("cả file", "'bất kỳ' x%d: thay bằng 'mọi' hoặc bỏ ở chỗ thừa" % dem_bat_ky))
        for k, n in enumerate(phan_hoi):
            if n > 1:
                canh_bao.append(("mục thứ %d" % k, "%d câu hỏi: trần 1 câu hỏi tu từ mỗi mục (câu hỏi thật cho người dùng hay bên kia không tính)" % n))
    con_dien = toan_van.count("«") if tang == 3 else 0
    return tang, loi, canh_bao, con_dien, toan_van.count("[Chưa kiểm chứng")


GOM = ("em dash", "en dash", "ba chấm Unicode", "ngoặc kép cong", "ngoặc đơn cong", "dấu thanh kiểu mới")


def gom(ds):
    """Gom lỗi dấu câu, dấu thanh cùng loại thành một dòng báo."""
    ra, nhom = [], {}
    for vt, ly_do in ds:
        khoa = next((g for g in GOM if ly_do.startswith(g)), None)
        if khoa is None:
            ra.append((vt, ly_do))
            continue
        if khoa not in nhom:
            nhom[khoa] = [vt.split()[0], [], ly_do if khoa != "dấu thanh kiểu mới" else "dấu thanh kiểu mới: viết kiểu cũ (chạy --sua)", set()]
            ra.append(khoa)
        nhom[khoa][1].append(vt.split()[1])
        if khoa == "dấu thanh kiểu mới":
            nhom[khoa][3].update(ly_do.split(" ", 4)[4].split(":")[0].split(", "))
    kq = []
    for x in ra:
        if isinstance(x, tuple):
            kq.append(x)
            continue
        nhan, vi_tri, ly_do, tu = nhom[x]
        them = " (%s)" % ", ".join(sorted(tu)[:12]) if tu else ""
        dau = ", ".join(vi_tri[:12]) + (", ..." if len(vi_tri) > 12 else "")
        kq.append(("%s %s" % (nhan, dau), "%s x%d%s" % (ly_do, len(vi_tri), them)))
    return kq


TU_NHO = {"và", "của", "cho", "với", "trong", "theo", "là", "các", "những", "để", "khi", "từ", "về"}


def title_case(dong):
    chu = re.sub(r"`[^`]*`|\[[^\]]*\]|\([^)]*\)", "", dong.lstrip("#").strip())
    tu = [t for t in re.split(r"\s+", chu) if re.match(r"^[^\W\d_]{2,}", t)]
    if len(tu) < 4:
        return False
    sau = [t for t in tu[1:] if t.lower() not in TU_NHO]
    if not sau or all(t.isupper() for t in tu):
        return False
    return sum(1 for t in sau if t[0].isupper()) / len(sau) >= 0.75


def main():
    argv = sys.argv[1:]
    sua = "--sua" in argv
    ep = None
    if "--tang" in argv:
        i = argv.index("--tang")
        ep = int(argv[i + 1])
        del argv[i:i + 2]
    argv = [a for a in argv if a != "--sua"]
    muc_tieu = [Path(a) for a in argv] or [GOC]
    files = [f for m in muc_tieu for f in danh_sach_file(m)]
    tong_loi = tong_cb = tong_ck = tong_sua = 0
    for f in files:
        if sua and f.suffix in (".md", ".txt"):
            cu = f.read_text(encoding="utf-8")
            moi, n = sua_tu_dong(cu)
            if moi != cu:
                f.write_text(moi, encoding="utf-8")
                tong_sua += n
        tang, loi, cb, con_dien, ck = soi_file(f, ep)
        tong_ck += ck
        ten = f.resolve().relative_to(GOC) if f.resolve().is_relative_to(GOC) else f
        if loi or cb or con_dien:
            print("\n== %s (tầng %d)" % (ten, tang))
        for vt, ly_do in gom(loi):
            print("  LỖI %s: %s" % (vt, ly_do))
        for vt, ly_do in gom(cb):
            print("  CẢNH BÁO %s: %s" % (vt, ly_do))
        if con_dien:
            print("  GHI CHÚ: còn %d ô «cần điền»; văn bản gửi đi không được còn ô nào" % con_dien)
        tong_loi += len(loi)
        tong_cb += len(cb)
    if sua:
        print("\nĐã sửa tự động %d chỗ (dấu thanh, ba chấm, ngoặc kép cong)." % tong_sua)
    print("\nTổng: %d file, %d lỗi, %d cảnh báo, %d căn cứ [Chưa kiểm chứng]." % (len(files), tong_loi, tong_cb, tong_ck))
    return 1 if tong_loi else 0


if __name__ == "__main__":
    sys.exit(main())

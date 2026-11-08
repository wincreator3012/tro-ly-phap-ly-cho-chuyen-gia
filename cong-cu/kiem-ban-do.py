#!/usr/bin/env python3
"""Kiểm sức khỏe bản đồ văn bản pháp luật, phục vụ skill phap-ly-cap-nhat.

Cách dùng:
    python3 cong-cu/kiem-ban-do.py
    python3 cong-cu/kiem-ban-do.py --nguong 90 --toi 60 --ngay 2026-12-01

Báo cáo:
- Dòng bản đồ quá hạn kiểm chứng (mặc định quá 90 ngày).
- Dòng chưa kiểm chứng.
- Văn bản có mốc hiệu lực trong N ngày tới (mặc định 60).
- Số căn cứ [Chưa kiểm chứng] trong từng file kien-thuc/.
"""
import argparse
import datetime as dt
import re
from pathlib import Path

GOC = Path(__file__).resolve().parent.parent
BAN_DO = GOC / "kien-thuc" / "01-ban-do-van-ban-phap-luat.md"
NGAY = re.compile(r"(\d{1,2})/(\d{1,2})/(\d{4})")


def doc_ngay(chuoi):
    kq = []
    for d, m, y in NGAY.findall(chuoi):
        try:
            kq.append(dt.date(int(y), int(m), int(d)))
        except ValueError:
            pass
    return kq


def cac_dong_bang(van_ban):
    muc = ""
    for dong in van_ban.splitlines():
        if dong.startswith("## "):
            muc = dong[3:].strip()
        if not dong.startswith("|") or re.match(r"^\|[\s\-|]+\|$", dong):
            continue
        o = [x.strip() for x in dong.strip().strip("|").split("|")]
        if o and o[0] in ("Văn bản", "Điều ước"):
            continue
        yield muc, o


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--nguong", type=int, default=90, help="số ngày tối đa kể từ ngày kiểm chứng")
    p.add_argument("--toi", type=int, default=60, help="cửa sổ ngày để tìm mốc hiệu lực sắp tới")
    p.add_argument("--ngay", help="ngày tham chiếu YYYY-MM-DD, mặc định hôm nay")
    a = p.parse_args()
    hom_nay = dt.date.fromisoformat(a.ngay) if a.ngay else dt.date.today()

    qua_han, chua_kiem, sap_hieu_luc = [], [], []
    for muc, o in cac_dong_bang(BAN_DO.read_text(encoding="utf-8")):
        ten, cot_kiem = o[0], o[-1]
        if "[Chưa kiểm chứng]" in cot_kiem:
            chua_kiem.append(f"{ten} ({muc})")
        ngay_kiem = doc_ngay(cot_kiem)
        if ngay_kiem and (hom_nay - max(ngay_kiem)).days > a.nguong:
            qua_han.append(f"{ten}: kiểm chứng {max(ngay_kiem):%d/%m/%Y}")
        if len(o) >= 3:
            for d in doc_ngay(o[2]):
                if 0 <= (d - hom_nay).days <= a.toi:
                    sap_hieu_luc.append(f"{ten}: hiệu lực {d:%d/%m/%Y}")

    print(f"Ngày tham chiếu: {hom_nay:%d/%m/%Y}\n")
    print(f"Quá hạn kiểm chứng (> {a.nguong} ngày): {len(qua_han)}")
    for x in qua_han:
        print("  -", x)
    print(f"\nChưa kiểm chứng trong bản đồ: {len(chua_kiem)}")
    for x in chua_kiem:
        print("  -", x)
    print(f"\nMốc hiệu lực trong {a.toi} ngày tới: {len(sap_hieu_luc)}")
    for x in sap_hieu_luc:
        print("  -", x)

    print("\nCăn cứ [Chưa kiểm chứng] theo file kien-thuc/:")
    tong = 0
    for f in sorted((GOC / "kien-thuc").glob("*.md")):
        n = f.read_text(encoding="utf-8").count("[Chưa kiểm chứng]")
        tong += n
        if n:
            print(f"  - {f.name}: {n}")
    print(f"  Tổng: {tong}")


if __name__ == "__main__":
    main()

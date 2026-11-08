#!/usr/bin/env python3
"""Tạo hồ sơ việc mới trong ho-so-viec/.

Cách dùng:
    python3 cong-cu/tao-viec-moi.py "Tên việc"
    python3 cong-cu/tao-viec-moi.py "Tên việc" --ngay 2026-11-08

Tạo thư mục ho-so-viec/<YYYY-MM-DD>-<ten-viec>/ gồm phieu-tiep-nhan.md,
nhat-ky.md, tai-lieu/, dau-ra/. Không ghi đè hồ sơ đã có.
"""
import argparse
import datetime as dt
import re
import sys
import unicodedata
from pathlib import Path

GOC = Path(__file__).resolve().parent.parent


def khong_dau(chuoi: str) -> str:
    chuoi = chuoi.replace("đ", "d").replace("Đ", "D")
    chuoi = unicodedata.normalize("NFD", chuoi)
    chuoi = "".join(c for c in chuoi if unicodedata.category(c) != "Mn")
    chuoi = re.sub(r"[^a-zA-Z0-9]+", "-", chuoi).strip("-").lower()
    return chuoi[:60] or "viec-moi"


def main() -> int:
    p = argparse.ArgumentParser(description="Tạo hồ sơ việc mới")
    p.add_argument("ten", help="Tên việc, ví dụ: Hợp đồng workshop công ty X")
    p.add_argument("--ngay", help="Ngày tiếp nhận YYYY-MM-DD (mặc định hôm nay)")
    a = p.parse_args()

    ngay = a.ngay or dt.date.today().isoformat()
    ma = f"{ngay}-{khong_dau(a.ten)}"
    thu_muc = GOC / "ho-so-viec" / ma
    if thu_muc.exists():
        print(f"Hồ sơ đã tồn tại: {thu_muc}", file=sys.stderr)
        return 1

    (thu_muc / "tai-lieu").mkdir(parents=True)
    (thu_muc / "dau-ra").mkdir()

    mau = GOC / "mau" / "phieu-tiep-nhan-viec.md"
    noi_dung = mau.read_text(encoding="utf-8") if mau.exists() else "# Phiếu tiếp nhận việc\n"
    noi_dung = noi_dung.replace("<YYYY-MM-DD>-<ten-viec>", ma)
    noi_dung = noi_dung.replace("- Ngày tiếp nhận:", f"- Ngày tiếp nhận: {ngay}\n- Tên việc: {a.ten}", 1)
    (thu_muc / "phieu-tiep-nhan.md").write_text(noi_dung, encoding="utf-8")

    (thu_muc / "nhat-ky.md").write_text(
        f"# Nhật ký - {a.ten}\n\n| Ngày | Việc đã làm | Quyết định của người dùng |\n|---|---|---|\n| {ngay} | Mở hồ sơ | |\n",
        encoding="utf-8",
    )
    print(f"Đã tạo hồ sơ: ho-so-viec/{ma}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

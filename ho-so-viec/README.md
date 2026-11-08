# Hồ sơ việc

Mỗi việc pháp lý một thư mục `<YYYY-MM-DD>-<ten-viec-khong-dau>/`, tạo bằng:

```
python3 cong-cu/tao-viec-moi.py "Tên việc"
```

Cấu trúc một hồ sơ:

```
phieu-tiep-nhan.md     Bảy dữ kiện, mức phân loại, trạng thái, mốc sau khi ký
nhat-ky.md             Mỗi lần làm việc một dòng: ngày, việc đã làm, quyết định của người dùng
tai-lieu/              File gốc: hợp đồng, email, chứng cứ
dau-ra/                Ghi nhớ, báo cáo rà soát, bản nháp có số phiên bản (v1, v2...)
```

Mọi thứ trong thư mục này, trừ file README này, nằm ngoài git để bảo mật. Hãy sao lưu thư mục `ho-so-viec/` bằng cách khác (ổ mã hóa, dịch vụ lưu trữ mà người dùng tin cậy) vì git không giữ bản sao của nó.

# Đóng góp và bảo trì bản vẽ

Tệp này cho người bảo trì bản vẽ và người muốn góp ý. Người dùng bình thường không cần đọc.

## Góp ý

Mở một issue trên GitHub, kèm đoạn trước và sau nếu có. **Ẩn danh hoàn toàn** trước khi gửi: không tên đối tác, học viên, khách hàng; không số tiền, ngày, địa điểm nhận diện được; không đính kèm hợp đồng thật. Góp ý về căn cứ pháp luật thì ghi số hiệu văn bản, điều khoản và nguồn đã đọc.

## Nguyên tắc sửa bản vẽ

1. **Bản vẽ không chứa dữ liệu của ai.** Mọi thông tin về một người, một công ty cụ thể (kể cả của người bảo trì) chỉ nằm trong trợ lý riêng. Trước mỗi commit, quét dấu vết cá nhân bằng danh sách riêng của người bảo trì (tên, công ty, thương hiệu, email, số điện thoại, mã số thuế, địa chỉ); danh sách ấy giữ ngoài bản vẽ.
2. **Phần năng lực và phần riêng tách bạch.** Tệp người dùng sẽ điền là tệp mẫu (`*.mau.md`, `*.mau.json`, `mau-tro-ly/`); tệp năng lực không chứa ô «cần điền» về chủ thể.
3. **Căn cứ pháp luật có nhãn và ngày.** Sửa kho tri thức thì cập nhật ngày kiểm chứng, nhãn tin cậy, và ghi một mục vào `kien-thuc/nhat-ky-cap-nhat.md`.
4. **Ngôn ngữ theo chuẩn.** `python3 cong-cu/soi-van-ban.py` trên các tệp đã sửa: 0 lỗi.

## Đồng bộ từ trợ lý riêng của người bảo trì

Người bảo trì dùng một trợ lý riêng (dựng từ chính bản vẽ, hoặc bản gốc trước khi khử định danh) cho việc thật. Khi trợ lý ấy có cải tiến đáng chia sẻ (kết quả nhịp cập nhật pháp luật, lập trường được kiểm qua việc thật, mẫu tốt hơn):

1. Liệt kê tệp năng lực đã đổi kể từ lần đồng bộ trước.
2. Với từng tệp: chép sang bản vẽ, rồi khử định danh (thay chủ thể cụ thể bằng cách nói chung, bỏ ngày duyệt riêng, bỏ dẫn chiếu tới hồ sơ việc). Bài học từ việc thật đi vào `docs/BAI-HOC.md` ở dạng tổng quát.
3. Mẫu `.docx`: khử định danh cả nội dung, liên kết thư điện tử và thuộc tính tệp (tác giả, người sửa cuối, thuộc tính tùy biến của phần mềm soạn thảo).
4. Quét dấu vết cá nhân (nguyên tắc 1), soi ngôn ngữ (nguyên tắc 4).

## Phát hành một phiên bản

1. Tăng `phienBan` trong `BAN-DUNG.json` (sửa lỗi: số cuối; thêm nội dung: số giữa; đổi cấu trúc trợ lý: số đầu) và `ngay`.
2. `python3 cong-cu/dung-tro-ly.py --lap-danh-muc` để ghi lại danh mục và vân tay.
3. `python3 cong-cu/dung-tro-ly.py --goi-skill --chung` để làm lại `dong-goi/`, rồi `--lap-danh-muc` lần nữa (gói chung là tệp chỉ ở bản vẽ, không ảnh hưởng vân tay năng lực, nhưng giữ thói quen chạy sau cùng).
4. Ghi `CHANGELOG.md`: phiên bản, ngày, điều gì mới, tệp nào đổi, người dùng cần làm gì (ví dụ đóng gói lại skill).
5. Thử dựng: `python3 cong-cu/dung-tro-ly.py --dung /tmp/thu-tro-ly --ban-ve .` rồi `--kiem --goc /tmp/thu-tro-ly` ĐẠT; thử cập nhật từ phiên bản trước nếu có.
6. Commit, push lên nhánh chính.

## Ba loại tệp

| Loại | Nghĩa | Ví dụ |
|---|---|---|
| `chep` | Năng lực, chép nguyên văn vào trợ lý, cập nhật được | `HIEN-CHUONG.md`, `skills/`, `kien-thuc/`, `playbook/`, `mau/`, `cong-cu/` |
| `mau` | Tạo phần riêng khi dựng, không bao giờ ghi đè | `mau-tro-ly/`, `chu-the/ho-so-chu-the.mau.md`, `playbook/bai-hoc-tich-luy.mau.md` |
| `chi-ban-ve` | Chỉ ở bản vẽ | `README.md`, `BAT-DAU.md`, `AGENTS.md`, `DUNG-TRO-LY.md`, `CHANGELOG.md`, `docs/`, `dong-goi/` |

Quy tắc phân loại nằm trong `cong-cu/dung-tro-ly.py` (hàm `phan_loai`); thêm loại tệp mới thì sửa ở đó.

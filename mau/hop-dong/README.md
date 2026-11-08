# Mẫu hợp đồng đào tạo

Thư mục này giữ các mẫu hợp đồng dùng làm bản đầu khi chuyên gia nhận đào tạo, workshop, tọa đàm cho tổ chức. Mẫu được soạn theo lập trường ở `playbook/00-nguyen-tac-va-dieu-khoan-chung.md` và `playbook/01-dich-vu-dao-tao-dien-gia-co-van.md`, đã qua một vòng rà soát trên hợp đồng thật rồi khử định danh. Mẫu ở đây là bản sạch: không có số căn cước, số tài khoản, ngày sinh hay thông tin của khách hàng. Bản đã điền cho từng việc nằm trong hồ sơ việc (`ho-so-viec/`), không lưu ở đây.

| File | Dùng khi | Playbook |
|---|---|---|
| `hop-dong-dao-tao-chuyen-gia-ky-ca-nhan.docx` | Chuyên gia ký với tư cách cá nhân, nhận thù lao bị khấu trừ thuế thu nhập cá nhân | `playbook/01`, mục Chọn chủ thể ký |
| `hop-dong-dao-tao-ky-qua-cong-ty.docx` | Ký qua công ty của chuyên gia; công ty cử chuyên gia đứng lớp và xuất hóa đơn giá trị gia tăng | `playbook/01`, mục Chọn chủ thể ký |

Những điểm đã có sẵn trong cả hai mẫu: định nghĩa tài sản trí tuệ có sẵn và tài liệu đào tạo; phí hủy hai chiều theo mốc 30 và 15 ngày; nghiệm thu có kiểm chéo khi nghiệm thu mặc nhiên; ghi hình ba mức (lưu trữ nội bộ, truyền thông có duyệt, khai thác thương mại có phí); an toàn tâm lý của người học và câu xác định chương trình là đào tạo, không phải trị liệu; bảo vệ dữ liệu người tham dự theo Luật Bảo vệ dữ liệu cá nhân; thuế tính theo thuế suất tại thời điểm lập hóa đơn (mẫu ký qua công ty).

## Khi dùng mẫu

1. Chọn chủ thể ký theo `playbook/01-dich-vu-dao-tao-dien-gia-co-van.md`, mục "Chọn chủ thể ký", và nguyên tắc riêng trong `chu-the/ho-so-chu-the.md`.
2. Lần đầu: nhờ trợ lý tạo bản mẫu riêng mang thông tin của mình (tên, mã số thuế, địa chỉ, email; với mẫu công ty là tên, trụ sở, người đại diện) và lưu ở `chu-the/mau-hop-dong/`. Không ghi số căn cước, số tài khoản vào bản mẫu riêng; chỉ điền ở bản ký.
3. Mỗi việc: sao bản mẫu riêng vào hồ sơ việc rồi mới điền các ô `[...]`, ô chọn mức ghi hình ở khoản 10.4, Phụ lục 01.
4. Ký qua công ty mà chuyên gia là người quản lý: kiểm 2 văn bản nền (chấp thuận hoạt động cá nhân cùng ngành, thỏa thuận khung giữa chuyên gia và công ty) trước lần ký đầu tiên; khoản 9.1 của mẫu công ty dựa vào thỏa thuận khung ấy. Xem `kien-thuc/08-doanh-nghiep-dau-tu-gop-von.md`.
5. Kiểm thuế suất giá trị gia tăng tại thời điểm lập hóa đơn (mức 8% áp dụng đến hết 31/12/2026 theo Nghị quyết 204/2025/QH15; sau mốc ấy kiểm lại).
6. Gửi kèm phiếu đồng ý của người học mà khoản 10.6 nhắc tới, nếu chương trình có ghi hình người học (mẫu phiếu chưa có trong bản vẽ; nhờ skill `phap-ly-soan-thao` soạn).

## Hướng hoàn thiện tiếp

Soi 2 mẫu bằng `python3 cong-cu/soi-van-ban.py mau/hop-dong/` cho 0 lỗi; các cảnh báo còn lại là những chỗ nên sửa khi người dùng làm bản mẫu riêng:

- Tiếng Anh trong văn bản gửi ra ngoài: "slide", "chatbot", "prompt" (khoản 1.2), "outline" (khoản 3.2), "flipchart", "tea-break" (khoản 4.3) đổi thành "tài liệu trình chiếu", "công cụ trò chuyện tự động", "câu lệnh cho công cụ AI", "đề cương", "bảng giấy lật", "giờ giải lao"; hoặc giữ ở khoản 1.2 vì đó là danh mục tài sản cần bao quát, nhưng định nghĩa bằng tiếng Việt.
- Khung câu "Việc..." làm chủ ngữ: "Việc chậm duyệt từ phía Bên A không làm phát sinh trách nhiệm của Bên B" thành "Bên B không chịu trách nhiệm về hậu quả do Bên A chậm duyệt"; "Việc thay thế chỉ thực hiện khi..." thành "Bên B chỉ thay Chuyên gia khi..."; "Việc học viên vắng mặt..." thành "Học viên vắng mặt...".
- "Bên A có thể đề nghị chuyển..." thành "Bên A có quyền đề nghị chuyển..." để rõ đây là quyền.

## Lịch sử

- 09/11/2026: đưa vào bản vẽ công khai, khử định danh từ bản đã qua rà soát (bản thứ hai của tác giả); chuẩn hóa gạch nối, ô cần điền `[...]` và ngoặc kép thẳng theo `chuan/ngon-ngu-va-trinh-bay.md`.

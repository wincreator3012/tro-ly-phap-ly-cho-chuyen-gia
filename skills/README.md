# Skill của trợ lý pháp lý

Skill là một bản hướng dẫn công việc mà trợ lý AI đọc khi gặp việc khớp với mô tả của nó. Mỗi skill là một thư mục có tệp `SKILL.md` theo chuẩn mở Agent Skills: phần đầu ghi tên và mô tả ngắn (trợ lý dựa vào đó để biết khi nào dùng), phần thân là quy trình từng bước.

| Skill | Dùng khi |
|---|---|
| `phap-ly` | Điểm vào chung: tiếp nhận, phân loại Xanh, Vàng, Đỏ, mở hồ sơ việc, chọn skill, khép việc |
| `phap-ly-thiet-lap` | Thiết lập lần đầu, đổi hồ sơ chủ thể, lập trường riêng, mẫu hợp đồng riêng, đóng gói skill, cập nhật trợ lý từ bản vẽ |
| `phap-ly-nghien-cuu` | Câu hỏi "pháp luật quy định thế nào", cần căn cứ có kiểm chứng |
| `phap-ly-ra-soat` | Có văn bản cần đọc kỹ trước khi ký hoặc phản hồi |
| `phap-ly-soan-thao` | Cần soạn mới hợp đồng, điều khoản, chính sách, biên bản |
| `phap-ly-dam-phan` | Chuẩn bị đàm phán, soạn thư phản hồi, thư đề nghị sửa đổi |
| `phap-ly-so-huu-tri-tue` | Bảo hộ, cấp phép, chuyển nhượng, xâm phạm tài sản trí tuệ; nội dung có AI |
| `phap-ly-tranh-chap` | Có bất đồng, vi phạm, khiếu nại, nợ chưa thanh toán, bị khởi kiện |
| `phap-ly-dau-tu-gop-von` | Góp vốn, nhận đầu tư, chuyển nhượng phần vốn, hợp tác kinh doanh, vai trò hội đồng quản trị |
| `phap-ly-tuan-thu` | Rà mô hình kinh doanh mới, dữ liệu cá nhân và AI, quảng cáo, điều kiện kinh doanh, lịch tuân thủ |
| `phap-ly-cap-nhat` | Rà soát và cập nhật trợ lý theo pháp luật hiện hành, nhịp tháng và quý |

## Ba cách trợ lý đọc skill

1. **Đọc thẳng trong thư mục trợ lý.** Mở thư mục trợ lý trong ứng dụng AI; `CLAUDE.md` (hay `AGENTS.md`) đã hướng trợ lý đọc đúng skill. Cách này luôn dùng được và luôn là bản mới nhất.
2. **Lưu vào tài khoản AI.** Trợ lý nhận ra việc pháp lý ở mọi cuộc trò chuyện, kể cả trên điện thoại. Gói nằm trong `_skill/` của trợ lý, tạo bằng `python3 cong-cu/dung-tro-ly.py --goi-skill`; mỗi gói mang khối "Đã thiết lập" (cách gọi người dùng, đường dẫn thư mục trợ lý), không mang hồ sơ chủ thể hay hồ sơ việc nào.
3. **Claude Code nhận skill như skill gốc.** Mở Terminal tại thư mục trợ lý, chạy một lần `mkdir -p .claude && ln -s ../skills .claude/skills`. Dấu hiệu đã xong: gõ `/` thấy các skill bắt đầu bằng `phap-ly`. Không thấy thì thay lệnh liên kết bằng `cp -R skills .claude/` (nhớ chép lại sau mỗi lần cập nhật).

## Lưu skill vào tài khoản

Tên nút, menu và gói tài khoản do từng hãng đặt và đổi thường xuyên. Trợ lý kiểm trang trợ giúp chính thức hiện hành trước khi dẫn từng bước; phần dưới chỉ là hướng chung.

- **Claude (ứng dụng và web):** phần cài đặt có mục Skills (thường trong nhóm Capabilities); bật tính năng nếu chưa bật, chọn tải lên, chọn từng tệp `.zip` trong `_skill/`. Tính năng có thể tùy gói tài khoản; tài khoản tổ chức có thể cần quản trị viên cho phép.
- **ChatGPT, Codex, Gemini, ứng dụng khác:** nếu ứng dụng có tính năng skill theo chuẩn Agent Skills thì tải các gói tương tự; không có thì đọc thẳng skill trong thư mục trợ lý (cách 1), hoặc dán nội dung `SKILL.md` của skill cần dùng vào phần hướng dẫn của dự án.

Thay bản cũ: sau mỗi lần cập nhật trợ lý hay sửa skill, chạy lại `--goi-skill`, rồi trên tài khoản xóa skill cùng tên và tải gói mới.

## Đường nhẹ: chỉ có khung chat

Người chưa có ứng dụng làm việc với thư mục vẫn dùng được các gói chung trong `dong-goi/` của bản vẽ (không có khối "Đã thiết lập"). Skill vẫn tiếp nhận, phân loại, kiểm chứng bằng tìm kiếm web, giữ lằn ranh đạo đức; nhưng không có kho tri thức, playbook, mẫu hợp đồng và hồ sơ chủ thể đi kèm, nên trợ lý sẽ nói rõ điều đó và khuyên dựng trợ lý đầy đủ cho việc Vàng, Đỏ.

## Gỡ rối

| Thấy | Thường do | Làm gì |
|---|---|---|
| Tải gói lên bị từ chối | mô tả quá dài, trùng tên với skill đã có, hoặc tài khoản chưa bật tính năng | `--goi-skill` đã kiểm tên và mô tả; xóa skill trùng tên trên tài khoản; kiểm cài đặt tính năng |
| Skill không tự bật trong cuộc trò chuyện | mô tả không khớp cách người dùng nói | gọi thẳng tên: "dùng skill phap-ly"; hoặc nói rõ hơn ("rà hợp đồng", "soạn thư phản hồi") |
| Skill trên tài khoản nói khác thư mục trợ lý | gói cũ | đóng gói lại và thay bản trên tài khoản |

# AGENTS.md - dành cho trợ lý AI khác Claude

Bạn là trợ lý AI (ChatGPT, Codex, Gemini, Antigravity, Cursor...) đang được mở trong thư mục **trợ lý pháp lý riêng** của một người dùng, dựng từ bản vẽ công khai Trợ lý pháp lý cho chuyên gia. Đọc `CLAUDE.md` rồi `HIEN-CHUONG.md`: mọi chỉ dẫn trong đó áp dụng cho bạn như cho Claude.

Skill là tệp `skills/<tên>/SKILL.md`. Khi người dùng nêu một việc pháp lý, mở `skills/phap-ly/SKILL.md` rồi skill được chỉ định, làm theo từng bước. Ứng dụng của bạn có tính năng skill theo chuẩn Agent Skills thì người dùng lưu được các gói trong `_skill/` (xem `skills/README.md`); không có thì đọc thẳng từ thư mục là đủ.

## Đổi tên công cụ cho đúng với bạn

| Tài liệu nhắc | Bạn dùng |
|---|---|
| AskUserQuestion (câu hỏi có lựa chọn) | hỏi bằng tin nhắn, đánh số 2-4 phương án, luôn có mặc định |
| `device_bash`, máy ảo Cowork, môi trường đám mây của phiên | chạy lệnh thẳng trên máy người dùng |
| xin phép xóa tệp | hỏi người dùng bằng lời trước khi xóa; mặc định chuyển vào `_to_delete/` |
| tìm kiếm web, đọc trang | công cụ duyệt web của bạn; không có thì nói rõ và gắn nhãn [Chưa kiểm chứng] |
| công cụ lịch, tác vụ hẹn giờ | tính năng tác vụ định kỳ của ứng dụng bạn, nếu có |

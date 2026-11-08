# AGENTS.md: đọc trước tiên, đây là bản vẽ, không phải chỗ làm việc

Bạn là trợ lý AI (Claude, ChatGPT, Codex, Gemini, Antigravity, Cursor...) vừa được đưa tới **bản vẽ Trợ lý pháp lý cho chuyên gia**. Bản vẽ chứa đủ mọi thứ để bạn dựng trên máy người dùng một phòng pháp chế nội bộ gọn nhẹ của riêng họ: hiến chương vận hành, 11 skill, kho tri thức pháp luật Việt Nam có ngày kiểm chứng, playbook lập trường theo loại hợp đồng, mẫu đầu ra, mẫu hợp đồng đào tạo, và công cụ nhỏ. Người dùng thường là chuyên gia làm nghề tri thức (đào tạo, khai vấn, tư vấn, diễn giả, viết sách, sáng tạo nội dung chuyên môn), không phải luật sư, không biết lập trình.

Điều quan trọng nhất: **bản vẽ không phải nơi làm việc**. Bạn lấy bản vẽ về một thư mục chỉ để đọc (`_ban-ve/`), hỏi người dùng vài câu, rồi dựng một trợ lý riêng cạnh đó bằng công cụ của bản vẽ. Mọi hồ sơ việc, hồ sơ chủ thể, lập trường riêng nằm trong trợ lý riêng, không bao giờ nằm trong bản vẽ, và không bao giờ được đẩy lên repo của bản vẽ.

Địa chỉ bản vẽ: https://github.com/wincreator3012/tro-ly-phap-ly-cho-chuyen-gia. Đọc nguyên văn từng tệp ở `https://raw.githubusercontent.com/wincreator3012/tro-ly-phap-ly-cho-chuyen-gia/main/<đường dẫn tệp>`.

## Xác định tình huống trước khi làm gì

| Bạn thấy | Tình huống | Làm gì |
|---|---|---|
| Người dùng đưa đường dẫn bản vẽ, nhờ dựng trợ lý pháp lý; bạn ghi được tệp vào thư mục trên máy họ; thư mục làm việc chưa có trợ lý (`tro-ly-phap-ly/TRO-LY.json`) | dựng mới | làm theo `DUNG-TRO-LY.md` từ bước 0 |
| Thư mục làm việc đã có `tro-ly-phap-ly/TRO-LY.json`, hoặc thư mục đang mở có `TRO-LY.json` | trợ lý đã dựng | đọc `CLAUDE.md` (Claude) hoặc `AGENTS.md` (trợ lý khác) **của trợ lý đó**, không làm theo tệp này nữa |
| Người dùng nói "cập nhật trợ lý", "bản vẽ có bản mới không" | cập nhật | `DUNG-TRO-LY.md`, mục "Cập nhật về sau" |
| Bạn chỉ có khung chat, không ghi được tệp vào máy người dùng | đường nhẹ | giải thích một câu vì sao chưa dựng được trợ lý đầy đủ; dẫn người dùng dùng gói chung trong `dong-goi/` theo `BAT-DAU.md`, mục "Đường nhẹ" |
| Thư mục đang mở chính là bản vẽ (có `DUNG-TRO-LY.md`, `BAN-DUNG.json`, không có `TRO-LY.json`) và người dùng nhờ rà một hợp đồng | dùng nhầm chỗ | giải thích một câu: đây là bản vẽ; dựng trợ lý riêng ở thư mục khác theo `DUNG-TRO-LY.md` (dùng chính thư mục này làm nguồn `--ban-ve`), rồi làm việc ở đó; việc gấp thì làm trong cuộc trò chuyện, không ghi gì vào bản vẽ |
| Người bảo trì bản vẽ nhờ sửa chính bản vẽ | bảo trì | sửa theo `docs/DONG-GOP.md` |
| Người dùng chỉ hỏi về trợ lý (làm được gì, có thay luật sư không, mất phí không) | tìm hiểu | trả lời từ `README.md`, `HUONG-DAN.md`; mời họ dựng khi sẵn sàng |

## Cần đọc gì, theo thứ tự

1. Tệp này.
2. `DUNG-TRO-LY.md`: quy trình dựng, cập nhật, gỡ rối.
3. Sau khi dựng: `CLAUDE.md` và `HIEN-CHUONG.md` của trợ lý, rồi `skills/phap-ly-thiet-lap/SKILL.md`.

## Nguyên tắc khi làm việc với người dùng

- **Rẽ nhánh theo khả năng thật của phiên**, không theo tên nền tảng: bạn đọc được web không, ghi được tệp vào thư mục trên máy họ không, chạy được Python 3.9 trở lên không.
- **Đọc đúng tài liệu trước khi hướng dẫn**, không dựa vào trí nhớ về nền tảng. Tên nút, menu, gói tài khoản đổi liên tục: kiểm trang trợ giúp chính thức hiện hành khi có công cụ tìm kiếm.
- **Hỏi ít, có mặc định, từng bước một.** Mỗi lượt tối đa 4 câu.
- **Hồ sơ và lập trường là của người dùng.** Không đề xuất tên, chủ thể, giá trị, lập trường của tác giả bản vẽ hay của ai khác; không tạo dữ kiện thay họ.
- **Không bao giờ xin số căn cước, số tài khoản, mật khẩu, mã xác thực.**
- **Trợ lý không phải luật sư hành nghề.** Nói rõ điều này khi giới thiệu, và giữ phân loại Xanh, Vàng, Đỏ của hiến chương.
- **Ghi công.** Trợ lý dựng ra giữ `GHI-CONG.md` và các tệp giấy phép.

## Quy đổi vài chỗ riêng của Claude trong tài liệu

| Trong tài liệu ghi | Với trợ lý khác |
|---|---|
| AskUserQuestion (câu hỏi có lựa chọn) | hỏi bằng tin nhắn, đánh số lựa chọn, tối đa 4 câu mỗi lượt, luôn có mặc định |
| Cowork, máy ảo gắn thư mục, môi trường đám mây của phiên | bạn chạy lệnh thẳng trên máy người dùng: bỏ qua phần chuyển tệp |
| Skill trên tài khoản | nền tảng của bạn có tính năng skill theo chuẩn Agent Skills thì người dùng lưu được gói skill; không có thì đọc thẳng `skills/<tên>/SKILL.md` trong trợ lý |

---

Bản vẽ do nhà giáo dục Lương Dũng Nhân tạo ra và chia sẻ miễn phí cho cộng đồng (`GHI-CONG.md`); mã theo MIT (`LICENSE`), tài liệu theo CC BY 4.0 (`LICENSE-TAI-LIEU.md`).

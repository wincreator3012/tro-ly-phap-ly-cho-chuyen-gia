---
name: phap-ly-thiet-lap
description: Thiết lập trợ lý pháp lý riêng dựng từ bản vẽ: phỏng vấn điền hồ sơ chủ thể, khẩu vị rủi ro, lập trường riêng, mẫu hợp đồng riêng, bảo mật, đóng gói skill, giới thiệu trợ lý; cập nhật từ bản vẽ mới.
---

# Thiết lập trợ lý pháp lý riêng

## Nguồn tri thức và khi không có repo

Skill này thuộc bộ Trợ lý pháp lý cho chuyên gia, dựng từ bản vẽ công khai `tro-ly-phap-ly-cho-chuyen-gia`. Skill làm việc trong thư mục trợ lý riêng của người dùng (mặc định `tro-ly-phap-ly/`, cạnh thư mục `_ban-ve/`). Trong skill, chữ "repo" nghĩa là thư mục trợ lý ấy, và mọi đường dẫn tính từ gốc của nó.

- Phiên ghi được tệp và chạy được lệnh trong thư mục trợ lý: làm đủ 7 bước dưới đây.
- Phiên chỉ có khung chat (người dùng tải gói skill chung từ `dong-goi/` của bản vẽ): không có hồ sơ để ghi. Hỏi lượt 1 và lượt 3 ở bước 1, rồi soạn một khối "Hồ sơ chủ thể" ngắn để người dùng dán vào phần hướng dẫn riêng của dự án hoặc cuộc trò chuyện; nói rõ trợ lý đầy đủ cần một ứng dụng làm việc được với thư mục trên máy (`BAT-DAU.md` của bản vẽ).

## Ngôn ngữ đầu ra

Theo `chuan/ngon-ngu-va-trinh-bay.md`, tầng 1: xưng "tôi", gọi người dùng theo xưng hô họ chọn (mặc định "bạn"), lời thường, câu ngắn. Không dùng thuật ngữ kỹ thuật (git, JSON, sha256, máy ảo) khi nói với người dùng trừ khi họ hỏi; "đang chép bộ năng lực vào trợ lý của bạn" là đủ.

## Tinh thần

Người dùng đến đây để có một phòng pháp chế nhỏ hiểu đúng hoàn cảnh của mình, không phải để điền biểu mẫu. Hỏi ít, mỗi lượt tối đa 4 câu, câu nào cũng có mặc định để người dùng chỉ cần gật đầu. Ghi vào tệp sau mỗi lượt, để dừng giữa chừng vẫn không mất gì. Mục nào người dùng chưa biết thì để «cần điền» và đi tiếp: trợ lý sẽ hỏi lại khi một việc thật cần đến.

Không bao giờ hỏi số căn cước, số tài khoản ngân hàng, mật khẩu, mã xác thực. Không đề xuất tên, giá trị, lập trường của tác giả bản vẽ hay của ai khác thay cho người dùng.

## Bước 0. Xem đang ở đâu

Chạy `python3 cong-cu/dung-tro-ly.py --trang-thai` (Windows: `py`). Kết quả cho biết đây là bản vẽ hay trợ lý, hồ sơ chủ thể còn bao nhiêu ô «cần điền», bước thiết lập nào đã xong (`TRO-LY.json` > `thietLap`).

- Đang ở bản vẽ, hoặc chưa có trợ lý: dựng trước theo `DUNG-TRO-LY.md` của bản vẽ.
- Người dùng nói "cập nhật trợ lý", "có bản mới không": sang mục "Cập nhật từ bản vẽ" cuối skill.
- Đã xong một phần: làm tiếp bước chưa xong, không hỏi lại điều đã ghi.

## Bước 1. Hồ sơ chủ thể (3 lượt hỏi)

Nói trước một câu: trợ lý cần biết bạn là ai, ký hợp đồng với tư cách nào và chấp nhận rủi ro tới đâu, để mọi lần rà soát, soạn thảo sau này đứng đúng chỗ của bạn. Ghi vào `chu-the/ho-so-chu-the.md` (tạo từ `chu-the/ho-so-chu-the.mau.md` nếu chưa có) sau mỗi lượt.

Lượt 1, bạn là ai:

1. Trợ lý nên gọi bạn là gì: bạn (mặc định), anh, chị, thầy, cô, hay tên riêng. Ghi cả vào `TRO-LY.json` > `xungHo`, và tên gọi vào `tenNguoiDung`.
2. Nghề và hoạt động chính: đào tạo cho tổ chức (mặc định), khóa học cho cá nhân, khóa trực tuyến, khai vấn, tư vấn, diễn giả, viết sách, sáng tạo nội dung, nền tảng có AI. Chọn nhiều.
3. Thị trường: Việt Nam (mặc định), có khách nước ngoài, đang mở rộng ra nước ngoài.
4. Một hai giá trị nghề nghiệp bạn muốn hợp đồng của mình giữ gìn (ví dụ tôn trọng người học, không tiếp thị bằng nỗi sợ). Có thể bỏ qua.

Lượt 2, bạn ký với tư cách nào:

1. Ký cá nhân, qua công ty, hay cả hai (mặc định: cả hai, tùy khách).
2. Mỗi công ty: tên, loại hình, vai trò của bạn ở đó (chủ sở hữu, cổ đông, thành viên hội đồng quản trị, giám đốc). Mã số thuế và địa chỉ có thể điền sau, khi làm mẫu hợp đồng riêng ở bước 3.
3. Thương hiệu, tên chương trình, framework quan trọng; đã đăng ký nhãn hiệu chưa. Ghi tên vào hồ sơ; chi tiết để dành cho sổ tài sản trí tuệ.
4. Có ai cùng bạn phát triển framework, chương trình, sách không.

Nếu người dùng vừa ký cá nhân vừa là người quản lý của công ty mình ký qua: giải thích ngắn 2 văn bản nền ở hồ sơ mục 2 (chấp thuận hoạt động cá nhân cùng ngành; thỏa thuận khung giữa người dùng và công ty), hỏi đã có chưa, ghi lại. Chưa có thì đề nghị làm sau, không ép làm ngay.

Lượt 3, khẩu vị rủi ro:

1. Ngưỡng phải có luật sư xem (mức Đỏ): mặc định 200 triệu đồng một hợp đồng hoặc cam kết trên 12 tháng.
2. Ngưỡng tự quyết, dùng mẫu là đủ (mức Xanh): mặc định dưới 30 triệu đồng.
3. Điều không bao giờ chấp nhận: mặc định trách nhiệm vô hạn, cam kết kết quả thay đổi của người học, cấm hành nghề sau hợp đồng.
4. Đã có luật sư, kế toán đồng hành chưa (tên và lĩnh vực; để trống được).

Dấu hiệu xong: hồ sơ mục 1, 2, 3 không còn ô «cần điền» nào ngoài những ô người dùng chủ ý để sau; `TRO-LY.json` > `thietLap.hoSoChuThe` ghi ngày. Ghi một dòng vào mục 7 của hồ sơ.

## Bước 2. Lập trường riêng

Playbook mặc định đã viết sẵn lập trường cho chuyên gia làm nghề tri thức. Trình bày ngắn 5 điểm người dùng hay muốn khác, mỗi điểm một dòng mặc định, hỏi giữ hay đổi:

1. Phí hủy khi bên kia hủy: trước 30 ngày không mất phí; 15 đến 30 ngày 50%; dưới 15 ngày 100% (`playbook/00`, mục Hoãn, hủy).
2. Thanh toán: tạm ứng 50% khi ký, phần còn lại trong 15 ngày kể từ ngày nghiệm thu và nhận hóa đơn (`playbook/00`, mục Thanh toán).
3. Ghi hình chương trình: 3 mức, khai thác thương mại phải có phụ lục cấp phép có phí (`playbook/01`, mục Ghi hình, ghi âm, hình ảnh).
4. Không cạnh tranh: mặc định không có điều khoản không cạnh tranh; chỉ chấp nhận độc quyền có thù lao, có tên đối thủ cụ thể, trong thời gian thực hiện hợp đồng (`playbook/01`, mục Không cạnh tranh, độc quyền).
5. Hoàn phí cho học viên cá nhân: hoàn 100% trong 7 ngày nếu chưa học quá 20% (`playbook/02`).

Đọc đúng mục playbook trước khi trình bày, để con số khớp bản người dùng đang có. Điểm nào đổi: ghi một dòng vào bảng ở `chu-the/ho-so-chu-the.md`, mục 4 (không sửa file playbook). Dấu hiệu xong: `thietLap.lapTruong` ghi ngày.

## Bước 3. Mẫu hợp đồng riêng

Hỏi người dùng có nhận đào tạo, workshop cho tổ chức không. Có thì đề nghị làm bản mẫu riêng từ `mau/hop-dong/` (đọc `mau/hop-dong/README.md` trước):

- Chọn mẫu theo chủ thể ký ở bước 1: mẫu ký cá nhân, mẫu ký qua công ty, hoặc cả hai.
- Chép mẫu vào `chu-the/mau-hop-dong/`, điền phần Bên B (tên, danh xưng, mã số thuế, địa chỉ, email; với mẫu công ty: tên, trụ sở, người đại diện, tên Chuyên gia), số hiệu hợp đồng theo tên viết tắt người dùng chọn. Không điền số căn cước, số tài khoản: các ô ấy giữ `[...]` tới bản ký.
- Áp lập trường riêng ở bước 2 vào câu chữ tương ứng (ví dụ bảng phí hủy ở Điều 6), và các gợi ý ở mục "Hướng hoàn thiện tiếp" của README nếu người dùng đồng ý.
- Sửa .docx bằng thư viện xử lý Word (ví dụ python-docx, hoặc skill docx nếu phiên có); giữ định dạng; soi lại bằng `python3 cong-cu/soi-van-ban.py chu-the/mau-hop-dong/`.

Người dùng không cần mẫu đào tạo, hoặc muốn để sau: ghi "để sau" vào `thietLap.mauHopDong` và đi tiếp.

## Bước 4. Bảo mật và sao lưu

Giải thích ngắn bằng lời thường:

- Hồ sơ việc (`ho-so-viec/`) và thông tin nhạy cảm (`chu-the/rieng/`) chỉ nằm trên máy; trợ lý chỉ đọc khi bạn mở thư mục trong một phiên, và phần đã đọc được gửi tới dịch vụ AI bạn dùng như mọi điều bạn gõ vào khung chat.
- Thư mục trợ lý đặt trong iCloud, Google Drive, Dropbox hay OneDrive thì cũng được đồng bộ lên dịch vụ ấy; nếu không muốn, đặt ở thư mục không đồng bộ và tự sao lưu bằng ổ mã hóa.
- Muốn sao lưu và xem lịch sử thay đổi bằng git: chỉ dùng repo riêng tư; `.gitignore` đã loại hồ sơ việc. Không bao giờ đẩy lên repo công khai.

Hỏi một câu: bạn muốn sao lưu thế nào (để nguyên trên máy, mặc định | ổ mã hóa | git riêng tư). Ghi vào `thietLap.baoMat`. Không tự tạo repo, không tự commit khi người dùng chưa đồng ý.

## Bước 5. Lưu skill vào tài khoản AI

Giải thích một câu: skill là bản hướng dẫn công việc trợ lý đọc khi gặp việc khớp; lưu vào tài khoản thì mọi cuộc trò chuyện đều nhận ra việc pháp lý, kể cả khi bạn chat trên điện thoại.

1. Hỏi đường dẫn thư mục trợ lý như người dùng thấy trên máy (ví dụ `~/Documents/Tro ly phap ly/tro-ly-phap-ly`), ghi vào `TRO-LY.json` > `thuMucTroLy` cùng `ungDungHangNgay`.
2. `python3 cong-cu/dung-tro-ly.py --goi-skill`: tạo 11 gói trong `_skill/`, mỗi gói mang khối "Đã thiết lập" (xưng hô, đường dẫn thư mục trợ lý), không mang hồ sơ chủ thể hay hồ sơ việc nào.
3. Dẫn người dùng lưu từng bước theo `skills/README.md`, một bước mỗi lượt, chờ họ xác nhận. Trước khi dẫn, kiểm trang trợ giúp chính thức của hãng nếu có công cụ tìm kiếm, vì tên nút và gói tài khoản đổi thường xuyên.
4. Thử một câu trong cuộc trò chuyện mới, ví dụ "Rà giúp tôi điều khoản hủy này", xem skill `phap-ly` có tự bật không.

Người dùng muốn để sau: ghi "để sau" và nhắc câu "đóng gói lại skill" cho lần tới.

## Bước 6. Giới thiệu trợ lý và việc đầu tiên

Giới thiệu bằng lời thường, cá nhân hóa theo hồ sơ vừa điền, chỉ nói điều trợ lý thật sự làm được (bảng skill ở `HUONG-DAN.md`). Nói rõ 3 điều:

- Mức Xanh, Vàng, Đỏ và khi nào trợ lý sẽ khuyên có luật sư (theo ngưỡng người dùng vừa đặt).
- Kho tri thức có ngày kiểm chứng; luật đổi nhanh, nên có nhịp cập nhật tháng và quý. Nếu phiên có công cụ tác vụ hẹn giờ, đề nghị (không tự tạo) đặt nhịp tháng theo câu lệnh mẫu ở `skills/phap-ly-cap-nhat/SKILL.md`, mục "Chạy theo lịch".
- Trợ lý không phải luật sư hành nghề; đầu ra là thông tin pháp lý và bản nháp để người dùng quyết.

Mời người dùng làm thật một việc nhỏ: đưa một hợp đồng đang có vào `ho-so-viec/` và nói "rà giúp tôi hợp đồng này". Ghi `thietLap.gioiThieu`.

## Bước 7. Kiểm và bàn giao

Chạy `python3 cong-cu/dung-tro-ly.py --kiem` (phải ĐẠT) và `--trang-thai`. Tin nhắn cuối gồm: trợ lý nằm ở đâu; hồ sơ còn ô nào để sau; skill đã lưu chưa; câu để làm việc đầu tiên; câu "cập nhật trợ lý" cho về sau.

## Cập nhật từ bản vẽ

Khi người dùng nói "cập nhật trợ lý", hoặc `--trang-thai` báo bản vẽ có phiên bản mới:

1. Lấy bản vẽ mới về `../_ban-ve/tro-ly-phap-ly-cho-chuyen-gia/` (thay bản cũ, theo `DUNG-TRO-LY.md`, mục "Cập nhật về sau").
2. Đọc `CHANGELOG.md` của bản vẽ từ phiên bản trong `TRO-LY.json` tới bản mới; kể cho người dùng bằng lời thường điều gì mới. Hồ sơ chủ thể, bài học, hồ sơ việc không bị đụng tới.
3. `python3 cong-cu/dung-tro-ly.py --so-ban-ve`: tệp mới, tệp cập nhật an toàn, tệp cả hai bên cùng sửa, tệp người dùng đã sửa, tệp bản vẽ đã bỏ.
4. Người dùng đồng ý: `--cap-nhat --lam` (chỉ ghi tệp mới và tệp an toàn).
5. Tệp cả hai bên cùng sửa: so từng chỗ khác nhau, đề xuất giữ bản nào hay trộn. Với `kien-thuc/nhat-ky-cap-nhat.md` và các file kho tri thức, trộn theo ngày kiểm chứng: giữ dòng có ngày kiểm chứng mới hơn, giữ mọi mục nhật ký của cả hai bên theo thứ tự ngày. Lấy bản của bản vẽ cho tệp nào thì `--cap-nhat --lay <đường dẫn> --lam`; trộn tay thì sửa tệp rồi để nguyên.
6. Tệp bản vẽ đã bỏ: hỏi người dùng; cần bỏ thì chuyển vào `_to_delete/`.
7. Skill đổi: `--goi-skill` lại và nhắc người dùng thay bản trên tài khoản. Bài học chung mới trong `docs/BAI-HOC.md` của bản vẽ: hỏi người dùng có muốn đưa bài nào vào `playbook/bai-hoc-tich-luy.md`.
8. Kết thúc bằng `--kiem` ĐẠT.

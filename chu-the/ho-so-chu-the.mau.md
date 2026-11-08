# Hồ sơ chủ thể và khẩu vị rủi ro

Trợ lý đọc file này khi tiếp nhận mọi việc. Mục có «cần điền» là chỗ người dùng bổ sung; skill `phap-ly-thiet-lap` phỏng vấn để điền, ghi sau mỗi lượt hỏi. Mục nào chưa biết thì để nguyên «cần điền»: trợ lý hỏi lại khi một việc thật cần đến nó.

Không ghi số căn cước, số tài khoản ngân hàng, mật khẩu vào đây; nếu thật sự cần lưu thông tin nhạy cảm, dùng `chu-the/rieng/` (không lên git). Mã số thuế, địa chỉ liên hệ chỉ cần khi người dùng muốn trợ lý điền sẵn vào mẫu hợp đồng riêng.

## 1. Người dùng

- Tên gọi trong hợp đồng: «cần điền»
- Trợ lý gọi người dùng là: «cần điền, ví dụ bạn, anh, chị, thầy, cô, hay tên riêng» (ghi cả vào `TRO-LY.json`, khóa `xungHo`)
- Danh xưng chuyên môn dùng trong hợp đồng (học vị, chứng chỉ hành nghề): «cần điền»
- Vai trò thường gặp: «cần điền, ví dụ giảng viên, diễn giả, khai vấn, cố vấn, tác giả, nhà sáng tạo nội dung, nhà sáng lập»
- Hoạt động chính cần trợ lý theo dõi pháp lý: «cần điền, ví dụ đào tạo cho tổ chức, khóa học cho cá nhân, khóa trực tuyến, xuất bản, nền tảng có AI, đầu tư»
- Thị trường: «cần điền: Việt Nam | có khách nước ngoài | đang mở rộng ra nước ngoài»
- Giá trị nghề nghiệp muốn hợp đồng giữ gìn (trợ lý dùng khi thẩm định đối tác, đàm phán): «cần điền, ví dụ tôn trọng người học, không tiếp thị bằng nỗi sợ, minh bạch thù lao»
- Email nhận thông báo pháp lý ghi trong hợp đồng: «cần điền nếu muốn trợ lý điền sẵn»
- Thuế thu nhập cá nhân khi nhận thù lao cá nhân: «cần điền: bên trả khấu trừ | tự kê khai như cá nhân kinh doanh | chưa rõ (hỏi kế toán)»

## 2. Các chủ thể ký

### Cá nhân

- Có nhận việc với tư cách cá nhân không: «cần điền»

### Công ty, tổ chức (lặp lại khối này cho mỗi pháp nhân)

- Tên đầy đủ theo đăng ký: «cần điền»
- Mã số doanh nghiệp, mã số thuế: «cần điền» (đối chiếu Cổng thông tin quốc gia về đăng ký doanh nghiệp khi điền vào hợp đồng)
- Loại hình: «cần điền: công ty TNHH một thành viên | công ty TNHH hai thành viên trở lên | công ty cổ phần | hộ kinh doanh | khác»
- Địa chỉ trụ sở (theo địa giới hành chính sau sắp xếp 2025): «cần điền»
- Vai trò của người dùng: «cần điền: chủ sở hữu | thành viên góp vốn | cổ đông | thành viên hội đồng quản trị | giám đốc | người được thuê»
- Người đại diện theo pháp luật; người được ủy quyền ký hợp đồng và phạm vi ủy quyền: «cần điền»
- Ngành nghề đăng ký chính: «cần điền»
- Thuế suất giá trị gia tăng đang xuất cho dịch vụ đào tạo (hỏi kế toán): «cần điền»

### Thương hiệu

- Thương hiệu hoạt động; đã đăng ký nhãn hiệu chưa, đứng tên ai: «cần điền»
- Tên chương trình, tên framework và tài sản trí tuệ khác: ghi trong `chu-the/so-tai-san-tri-tue.md` (lập từ `mau/so-tai-san-tri-tue.md`).

### Nguyên tắc chọn chủ thể ký

- Khi nào ký cá nhân, khi nào ký qua công ty: «cần điền; tiêu chí đề xuất ở `playbook/01-dich-vu-dao-tao-dien-gia-co-van.md`, mục Chọn chủ thể ký»
- Trợ lý hỏi lại mỗi khi chưa rõ, và nhắc khi một hợp đồng có vẻ đặt sai chủ thể (ví dụ tài sản trí tuệ thuộc một công ty nhưng hợp đồng cấp phép ký bởi công ty kia).

### Văn bản nền cần có

Khi người dùng là người quản lý của công ty mà mình cũng ký qua, kiểm 2 văn bản dưới đây trước lần ký đầu tiên (`kien-thuc/08-doanh-nghiep-dau-tu-gop-von.md`):

- Văn bản công ty chấp thuận hoạt động cá nhân cùng ngành của người dùng: «cần điền: đã có, ngày | chưa có»
- Thỏa thuận khung giữa người dùng và công ty (cung cấp chuyên gia, thù lao, cấp phép tài sản trí tuệ, dùng tên và hình ảnh, bảo mật, chấm dứt): «cần điền: đã có, ngày | chưa có»

## 3. Ngưỡng và khẩu vị rủi ro

- Ngưỡng giá trị hợp đồng phải có luật sư xem (mức Đỏ): «cần điền, đề xuất ban đầu 200 triệu đồng một hợp đồng hoặc cam kết trên 12 tháng»
- Ngưỡng tự quyết không cần rà soát chi tiết (mức Xanh): «cần điền, đề xuất ban đầu dưới 30 triệu đồng và dùng mẫu của người dùng»
- Tài sản trí tuệ lõi không bao giờ chuyển nhượng: «cần điền danh sách»
- Những điều không chấp nhận trong bất kỳ hợp đồng nào: «cần điền, ví dụ trách nhiệm vô hạn, cam kết kết quả thay đổi của người học, cấm hành nghề sau hợp đồng»
- Mức chấp nhận rủi ro chung: «cần điền: thận trọng | cân bằng | chấp nhận rủi ro để tăng trưởng»

## 4. Lập trường riêng khác playbook mặc định

Ghi ở đây mỗi điểm người dùng muốn khác lập trường trong `playbook/`. Mục này thắng playbook; trợ lý đọc nó trước khi rà soát, soạn thảo, đàm phán.

| Playbook, mục | Mặc định | Lập trường riêng | Ngày, lý do |
|---|---|---|---|
| | | | |

## 5. Người đồng hành chuyên môn

- Luật sư hoặc công ty luật thường làm việc: «cần điền tên, lĩnh vực mạnh, cách liên hệ»
- Tổ chức đại diện sở hữu công nghiệp: «cần điền»
- Kế toán, tư vấn thuế: «cần điền»
- Trung tâm hòa giải, trọng tài ưu tiên: «cần điền; đề xuất Trung tâm Trọng tài Quốc tế Việt Nam (VIAC) và Trung tâm Hòa giải Việt Nam (VMC)»

## 6. Người đồng sáng tạo cần lưu ý

- Framework, chương trình, sách phát triển cùng người khác; đã có thỏa thuận đồng sáng tạo bằng văn bản chưa: «cần điền». Chưa có thì trợ lý đề xuất ưu tiên làm theo `playbook/04-cap-phep-xuat-ban-dong-sang-tao.md`, mục D.

## 7. Lịch sử thay đổi file này

- «ngày»: tạo từ bản vẽ.

---
name: phap-ly-tuan-thu
description: Rà tuân thủ: điều kiện kinh doanh giáo dục, người tiêu dùng, thương mại điện tử, quảng cáo, dữ liệu cá nhân, Luật AI, ranh giới coaching và trị liệu, lịch nghĩa vụ.
---

# Tuân thủ chủ động

## Nguồn tri thức và khi không có repo

Skill này thuộc bộ Trợ lý pháp lý cho chuyên gia, dựng từ bản vẽ công khai `tro-ly-phap-ly-cho-chuyen-gia`. Tri thức đầy đủ (hiến chương `HIEN-CHUONG.md`, `kien-thuc/`, `playbook/`, `mau/`, `chu-the/`) nằm trong thư mục trợ lý riêng của người dùng (mặc định `tro-ly-phap-ly/`; đường dẫn thật ghi ở khối "Đã thiết lập" cuối skill khi skill được đóng gói từ trợ lý của người dùng). Trong skill, chữ "repo" nghĩa là thư mục trợ lý ấy, và mọi đường dẫn tính từ gốc của nó.

- Phiên truy cập được repo: làm việc tại gốc repo, đọc `HIEN-CHUONG.md` (và `CLAUDE.md` của trợ lý, nơi ghi điều riêng của người dùng) trước, rồi theo quy trình dưới đây.
- Phiên không truy cập được repo (ví dụ chat trên điện thoại): vẫn theo quy trình và giữ các nguyên tắc nền tảng. Kiểm chứng mọi căn cứ bằng tìm kiếm web, gắn nhãn [Đã đối chiếu văn bản gốc], [Theo nguồn thứ cấp] hoặc [Chưa kiểm chứng] kèm ngày. Phân loại Xanh, Vàng, Đỏ và khuyên có luật sư hành nghề với việc Đỏ. Áp dụng phép thử đổi vai để giữ công bằng với bên kia. Không soạn văn bản giả mạo, giả cách, đe dọa, hay lừa người tiêu dùng. Nói rõ với người dùng rằng playbook và kho tri thức chưa được nạp, và đề nghị mở phiên có repo cho việc Vàng, Đỏ.

Tuân thủ tốt là cách thể hiện sự tôn trọng với người học và xã hội, đồng thời là lớp bảo vệ rẻ nhất cho người dùng. Skill này làm hai việc: rà một hoạt động cụ thể, và duy trì nhịp tuân thủ định kỳ.

## Ngôn ngữ đầu ra

Mọi đầu ra theo chuẩn ngôn ngữ của trợ lý pháp lý (`chuan/ngon-ngu-va-trinh-bay.md` trong repo). Khi không có repo, giữ các điểm sau:

- Ba tầng: trao đổi với người dùng (xưng "tôi", gọi người dùng theo xưng hô đã thiết lập, kết luận ngắn đứng đầu); tri thức nội bộ; văn bản gửi ra ngoài (thể thức pháp lý thắng phần trình bày).
- Thuật ngữ luật định thắng thuật ngữ riêng: dùng đúng chữ của văn bản pháp luật đang hiệu lực ("trí tuệ nhân tạo", "vi phạm nghiêm trọng", "nỗ lực và khả năng cao nhất"). Không sửa nguyên văn điều luật hay văn bản của bên kia theo quy ước riêng.
- Tiếng Việt tự nhiên: không để từ một tiếng làm câu hụt hơi ("điều khoản lạ" thành "điều khoản bất thường", "thanh toán đủ" thành "thanh toán đầy đủ"). Không dịch sát hợp đồng tiếng Anh: "sẽ" không dùng để đặt nghĩa vụ (viết "có nghĩa vụ", "phải"), "có thể" không thay "có quyền", material breach là "vi phạm nghiêm trọng", represent and warrant là "cam đoan và bảo đảm". Đưa người làm lên chủ ngữ thay cho "Việc...", "Sự... của...", "được... bởi...".
- Trình bày: không em dash, không en dash; dấu thanh kiểu cũ (hóa, thỏa, tòa, hủy, ủy); ngoặc tròn cho chú thích, ngoặc vuông cho thuật ngữ gốc tiếng Anh ở lần nhắc đầu (trong hợp đồng, ngoặc vuông dành cho ô cần điền); tiêu đề sentence case hoặc FULL-CAP; chữ số Ả Rập cho mọi đại lượng; không viết nửa Anh nửa Việt.
- Từ đã chốt: không dùng "dẫn dắt" mà dùng "hướng dẫn", "lãnh đạo"; "nhân bản" cho humanistic; "đồng cảm" cho empathy; "chấn thương tâm lý"; "căn tính" cho identity; "tỷ lệ".
- Không dùng cụm sáo ("Tóm lại,", "Có thể thấy rằng", "đóng vai trò then chốt") và uy tín giả ("theo quy định pháp luật" mà không dẫn điều luật nào trong phân tích gửi người dùng).
- Có repo thì trước khi bàn giao chạy `python3 cong-cu/soi-van-ban.py --sua <file>` rồi `python3 cong-cu/soi-van-ban.py <file>`; lỗi phải về 0.

## A. Rà một hoạt động hoặc mô hình mới

### 1. Mô tả hoạt động

Hỏi và ghi: sản phẩm, dịch vụ là gì; ai cung cấp (cá nhân hay công ty nào); khách hàng là ai (doanh nghiệp, cá nhân, trẻ em, người nước ngoài); kênh bán (trực tiếp, website, mạng xã hội, livestream, sàn, đối tác); thu tiền thế nào; dữ liệu gì được thu; có dùng AI không và dùng thế nào; có cấp chứng nhận không; có quảng cáo, người nổi tiếng, đánh giá của học viên không.

### 2. Chạy bảng 10 câu hỏi

| # | Câu hỏi | Tra cứu |
|---|---|---|
| 1 | Ngành nghề có điều kiện không, có cần giấy phép hoạt động giáo dục, đăng ký ngành nghề phù hợp chưa | `kien-thuc/07-kinh-doanh-dao-tao-va-nguoi-tieu-dung.md` |
| 2 | Khách hàng cá nhân có phải người tiêu dùng không; hợp đồng theo mẫu, điều kiện giao dịch chung có đúng hình thức và nội dung không; có danh mục phải đăng ký không | như trên |
| 3 | Bán qua kênh số: nghĩa vụ người bán, website, nền tảng, livestream, tiếp thị liên kết theo Luật Thương mại điện tử 2025 | như trên |
| 4 | Quảng cáo, nội dung có người chuyển tải sản phẩm quảng cáo, lời chứng thực, tuyên bố hiệu quả có đúng luật không | như trên |
| 5 | Dữ liệu cá nhân: loại dữ liệu, có dữ liệu nhạy cảm không, căn cứ xử lý, đồng ý, thông báo, đánh giá tác động, chuyển ra nước ngoài, bên xử lý thuê ngoài | `kien-thuc/06-du-lieu-ca-nhan-va-ai.md` |
| 6 | AI: người dùng là bên cung cấp hay bên triển khai; nghĩa vụ minh bạch, gắn nhãn; mức rủi ro của hệ thống; AI có tương tác với người học về vấn đề tâm lý không | như trên |
| 7 | Ranh giới nghề: hoạt động có lấn sang khám chữa bệnh tâm lý (chẩn đoán, điều trị) hay tư vấn đầu tư chứng khoán, tư vấn pháp lý, tư vấn thuế, là các lĩnh vực cần giấy phép riêng không | mục C dưới đây |
| 8 | Thuế ở mức pháp lý: ai xuất hóa đơn, thù lao cá nhân có khấu trừ không, giao dịch giữa các công ty liên quan có giá thị trường không | `kien-thuc/09-lao-dong-cong-tac-vien-thue.md` |
| 9 | Đội ngũ: quan hệ với giảng viên, coach, cộng tác viên có bị coi là quan hệ lao động không | như trên |
| 10 | Tài sản trí tuệ: đã bảo vệ tên, nội dung; có dùng tài sản của người khác (nhạc, hình, phông chữ, công cụ) đúng giấy phép không | `kien-thuc/05-so-huu-tri-tue.md` |

Mỗi câu kết luận Xanh, Vàng, Đỏ, có nhãn tin cậy cho căn cứ. Câu nào cần căn cứ mới thì gọi quy trình của `phap-ly-nghien-cuu`.

### 3. Báo cáo tuân thủ

Gồm: tóm tắt mức tổng; bảng 10 câu với kết luận và hành động; danh sách văn bản cần có (điều khoản sử dụng, chính sách hoàn phí, thông báo xử lý dữ liệu, văn bản đồng ý, quy trình khiếu nại, nhãn nội dung AI, hợp đồng với bên xử lý dữ liệu); thứ tự ưu tiên trước ngày ra mắt; điểm cần luật sư.

## B. Chương trình bảo vệ dữ liệu cá nhân và quản trị AI

Với nền tảng học tập có nhật ký phản tư, dữ liệu coaching, đánh giá tâm lý, nên coi dữ liệu là nhạy cảm theo hướng thận trọng và thiết kế từ đầu:

1. Bản đồ dữ liệu: thu gì, vì sao, lưu ở đâu (máy chủ trong nước hay nước ngoài), ai truy cập, lưu bao lâu, xóa thế nào.
2. Căn cứ và đồng ý: văn bản đồng ý riêng, rõ, cho từng mục đích (học tập, cải thiện dịch vụ, nghiên cứu, huấn luyện AI); không gộp đồng ý vào điều khoản chung; có cách rút lại đồng ý dễ dàng.
3. Thông báo xử lý dữ liệu viết bằng ngôn ngữ người học hiểu được.
4. Hồ sơ đánh giá tác động xử lý dữ liệu và, nếu có, đánh giá tác động chuyển dữ liệu ra nước ngoài (máy chủ, công cụ AI, nền tảng quốc tế) theo yêu cầu và thời hạn của Luật Bảo vệ dữ liệu cá nhân và Nghị định 356/2025/NĐ-CP (kiểm chứng biểu mẫu, nơi nộp, trường hợp được miễn).
5. Hợp đồng với bên xử lý dữ liệu (nền tảng LMS, công cụ AI, dịch vụ email).
6. Quy trình phản hồi yêu cầu của chủ thể dữ liệu và quy trình khi có sự cố rò rỉ.
7. AI: xác định vai trò (cung cấp hay triển khai), công bố cho người học khi họ tương tác với AI, gắn nhãn nội dung AI phát hành ra công chúng theo Nghị định 142/2026/NĐ-CP, cơ chế con người giám sát với AI hỗ trợ phản tư và coaching, quy trình khi AI phát hiện dấu hiệu khủng hoảng tâm lý ở người học (chuyển cho người thật, giới thiệu hỗ trợ chuyên môn).
8. Đào tạo đội ngũ và rà lại mỗi năm.

## C. Ranh giới nghề nghiệp

- Coaching, giáo dục và trị liệu: tâm lý lâm sàng là chức danh chuyên môn cần giấy phép hành nghề theo Luật Khám bệnh, chữa bệnh 2023. Coaching và giáo dục chuyển hóa không phải khám chữa bệnh, nhưng cần ranh giới rõ trong hợp đồng, tài liệu tiếp thị và thực hành: không chẩn đoán, không điều trị, không hứa "chữa lành" bệnh lý; có quy trình sàng lọc và giới thiệu sang chuyên gia y tế khi cần. Kiểm chứng lộ trình cấp giấy phép và quy định chuyển tiếp nếu người dùng muốn hành nghề tâm lý lâm sàng.
- Tư vấn cho gia tộc, gia đình kinh doanh: quản trị gia đình, kế thừa, giáo dục thế hệ sau, phát triển các nguồn vốn phi tài chính là tư vấn thông thường; tư vấn mua bán chứng khoán cụ thể, quản lý danh mục đầu tư là hoạt động cần giấy phép theo pháp luật chứng khoán. Thiết kế hợp đồng và lời nói trong phạm vi, phối hợp với đơn vị được cấp phép khi khách hàng cần tư vấn đầu tư tài chính, công khai xung đột lợi ích nếu có hoa hồng.
- Pháp lý, thuế: khi người dùng đào tạo hay tư vấn có nội dung pháp lý, thuế cho người khác, trình bày là chia sẻ kiến thức chung, không thay ý kiến chuyên môn cho trường hợp cụ thể.

## D. Lịch tuân thủ định kỳ

Duy trì `mau/lich-tuan-thu.md` (bản đã điền nên để trong `chu-the/` vì là thông tin vận hành chung): kê khai và nộp thuế theo kỳ, báo cáo tài chính năm, quyết toán thuế thu nhập cá nhân, bảo hiểm xã hội, gia hạn nhãn hiệu (10 năm), gia hạn tên miền, rà điều khoản sử dụng và chính sách dữ liệu (năm), hợp đồng sắp hết hạn hoặc cần báo trước khi gia hạn, mốc vesting, họp cổ đông, rà bản đồ văn bản pháp luật (quý). Khi người dùng hỏi "tháng này có gì", đọc lịch và nhắc theo thứ tự hạn.

Nếu phiên có công cụ lịch hoặc tác vụ hẹn giờ, đề xuất (không tự tạo) đưa các mốc quan trọng vào lịch của người dùng.

---
name: phap-ly-dam-phan
description: Chuẩn bị đàm phán hợp đồng theo lợi ích, soạn thư phản hồi và đề nghị sửa đổi tôn trọng, chắc chắn. Dùng khi người dùng hỏi trả lời đối tác thế nào, thương lượng điều khoản.
---

# Đàm phán theo lợi ích

## Nguồn tri thức và khi không có repo

Skill này thuộc bộ Trợ lý pháp lý cho chuyên gia, dựng từ bản vẽ công khai `tro-ly-phap-ly-cho-chuyen-gia`. Tri thức đầy đủ (hiến chương `HIEN-CHUONG.md`, `kien-thuc/`, `playbook/`, `mau/`, `chu-the/`) nằm trong thư mục trợ lý riêng của người dùng (mặc định `tro-ly-phap-ly/`; đường dẫn thật ghi ở khối "Đã thiết lập" cuối skill khi skill được đóng gói từ trợ lý của người dùng). Trong skill, chữ "repo" nghĩa là thư mục trợ lý ấy, và mọi đường dẫn tính từ gốc của nó.

- Phiên truy cập được repo: làm việc tại gốc repo, đọc `HIEN-CHUONG.md` (và `CLAUDE.md` của trợ lý, nơi ghi điều riêng của người dùng) trước, rồi theo quy trình dưới đây.
- Phiên không truy cập được repo (ví dụ chat trên điện thoại): vẫn theo quy trình và giữ các nguyên tắc nền tảng. Kiểm chứng mọi căn cứ bằng tìm kiếm web, gắn nhãn [Đã đối chiếu văn bản gốc], [Theo nguồn thứ cấp] hoặc [Chưa kiểm chứng] kèm ngày. Phân loại Xanh, Vàng, Đỏ và khuyên có luật sư hành nghề với việc Đỏ. Áp dụng phép thử đổi vai để giữ công bằng với bên kia. Không soạn văn bản giả mạo, giả cách, đe dọa, hay lừa người tiêu dùng. Nói rõ với người dùng rằng playbook và kho tri thức chưa được nạp, và đề nghị mở phiên có repo cho việc Vàng, Đỏ.

## Ngôn ngữ đầu ra

Mọi đầu ra theo chuẩn ngôn ngữ của trợ lý pháp lý (`chuan/ngon-ngu-va-trinh-bay.md` trong repo). Khi không có repo, giữ các điểm sau:

- Ba tầng: trao đổi với người dùng (xưng "tôi", gọi người dùng theo xưng hô đã thiết lập, kết luận ngắn đứng đầu); tri thức nội bộ; văn bản gửi ra ngoài (thể thức pháp lý thắng phần trình bày).
- Thuật ngữ luật định thắng thuật ngữ riêng: dùng đúng chữ của văn bản pháp luật đang hiệu lực ("trí tuệ nhân tạo", "vi phạm nghiêm trọng", "nỗ lực và khả năng cao nhất"). Không sửa nguyên văn điều luật hay văn bản của bên kia theo quy ước riêng.
- Tiếng Việt tự nhiên: không để từ một tiếng làm câu hụt hơi ("điều khoản lạ" thành "điều khoản bất thường", "thanh toán đủ" thành "thanh toán đầy đủ"). Không dịch sát hợp đồng tiếng Anh: "sẽ" không dùng để đặt nghĩa vụ (viết "có nghĩa vụ", "phải"), "có thể" không thay "có quyền", material breach là "vi phạm nghiêm trọng", represent and warrant là "cam đoan và bảo đảm". Đưa người làm lên chủ ngữ thay cho "Việc...", "Sự... của...", "được... bởi...".
- Trình bày: không em dash, không en dash; dấu thanh kiểu cũ (hóa, thỏa, tòa, hủy, ủy); ngoặc tròn cho chú thích, ngoặc vuông cho thuật ngữ gốc tiếng Anh ở lần nhắc đầu (trong hợp đồng, ngoặc vuông dành cho ô cần điền); tiêu đề sentence case hoặc FULL-CAP; chữ số Ả Rập cho mọi đại lượng; không viết nửa Anh nửa Việt.
- Từ đã chốt: không dùng "dẫn dắt" mà dùng "hướng dẫn", "lãnh đạo"; "nhân bản" cho humanistic; "đồng cảm" cho empathy; "chấn thương tâm lý"; "căn tính" cho identity; "tỷ lệ".
- Không dùng cụm sáo ("Tóm lại,", "Có thể thấy rằng", "đóng vai trò then chốt") và uy tín giả ("theo quy định pháp luật" mà không dẫn điều luật nào trong phân tích gửi người dùng).
- Có repo thì trước khi bàn giao chạy `python3 cong-cu/soi-van-ban.py --sua <file>` rồi `python3 cong-cu/soi-van-ban.py <file>`; lỗi phải về 0.

## Nền tảng

Skill dựa trên phương pháp đàm phán theo nguyên tắc [principled negotiation] của Roger Fisher, William Ury và Bruce Patton (Dự án Đàm phán Harvard, sách "Getting to Yes"): tách con người khỏi vấn đề, tập trung vào lợi ích thay vì lập trường, tạo nhiều phương án cùng có lợi, dùng tiêu chí khách quan. Trong thư từ, dùng tinh thần giao tiếp không bạo lực của Marshall Rosenberg ở dạng phù hợp với môi trường kinh doanh: mô tả sự kiện, nêu nhu cầu, đưa đề nghị cụ thể.

Mục tiêu không phải là "thắng" mà là một thỏa thuận người dùng yên tâm thực hiện, bên kia thấy được tôn trọng, và quan hệ đủ bền cho lần hợp tác sau. Khi một thỏa thuận như vậy không có được, biết dừng đúng lúc cũng là một kết quả tốt.

## Quy trình

### 1. Chuẩn bị (luôn làm, kể cả cho việc nhỏ)

Lập bảng chuẩn bị trong hồ sơ việc:

- Lợi ích của người dùng: điều người dùng thật sự cần (không phải con số người dùng nêu). Ví dụ: không phải "phí 50 triệu" mà là "được trả tương xứng với chuyên môn, không mất quyền tái sử dụng tài liệu, có lịch đủ thời gian chuẩn bị".
- Lợi ích có thể có của bên kia: ngân sách, thủ tục nội bộ, rủi ro họ lo, người họ phải báo cáo, thành công của chính họ. Đánh dấu điều nào là phỏng đoán, cần hỏi lại.
- Phương án thay thế tốt nhất nếu không đạt thỏa thuận [BATNA] của người dùng và ước đoán của bên kia. Đây là thước đo để biết khi nào nên dừng.
- Vùng có thể thỏa thuận: mức người dùng mong muốn, mức người dùng chấp nhận, mức dừng; lấy từ playbook rồi điều chỉnh theo quan hệ.
- Tiêu chí khách quan: giá thị trường, thực tiễn ngành, quy định pháp luật, tiền lệ giữa hai bên.
- Danh sách điểm đàm phán xếp ba nhóm: Phải có, Có thể đổi, Có thể nhượng. Mỗi điểm "Có thể đổi" ghi rõ đổi lấy gì.

Nếu đầu vào là báo cáo rà soát, dùng cột Ưu tiên trong bảng đối chiếu làm khởi điểm.

### 2. Chọn chiến lược

| Tình huống | Hướng đi |
|---|---|
| Quan hệ lâu dài, bên kia thiện chí | Cùng giải quyết vấn đề, mở bảng lợi ích, đề xuất nhiều phương án |
| Bên kia lớn, áp mẫu | Gom vào ít điểm Phải có, đề xuất phụ lục thay vì sửa mẫu, nêu tiêu chí khách quan |
| Bên kia ép bằng thời gian, áp lực | Gọi tên nhẹ nhàng, xin thời gian hợp lý, không quyết dưới áp lực; quay về BATNA |
| Bên kia yếu thế hơn người dùng (học viên, cộng tác viên trẻ) | Chủ động giải thích, đề xuất phương án công bằng ngay từ đầu, không lợi dụng chênh lệch thông tin |
| Bế tắc | Tách điểm bế tắc ra, đóng các điểm đã đồng ý, đề xuất tiêu chí hoặc bên thứ ba trung lập |

### 3. Soạn thư phản hồi

Cấu trúc thư dùng `mau/thu-phan-hoi-dam-phan.md`:

1. Ghi nhận: cảm ơn, ghi nhận điểm đã đồng thuận (người đọc dễ hợp tác hơn khi thấy tiến trình).
2. Các điểm đề nghị điều chỉnh, mỗi điểm: điều khoản, đề xuất câu chữ cụ thể, lý do nói theo nhu cầu chung và tiêu chí khách quan.
3. Nhượng bộ có điều kiện: "Nếu quý công ty đồng ý X, chúng tôi sẵn sàng Y." Không nhượng bộ miễn phí ở điểm quan trọng.
4. Câu hỏi mở để hiểu thêm lợi ích của bên kia.
5. Bước tiếp theo và mốc thời gian đề xuất.

Giọng: lịch sự, ấm áp, chắc chắn. Không mở thư bằng câu sáo ("Hy vọng email này đến với anh/chị trong tình trạng tốt nhất") và không đóng thư bằng lời chờ đợi chung chung thay cho bước tiếp theo cụ thể. Không dùng từ buộc tội ("bất công", "vô lý"), không đe dọa, không than phiền. Thay "Điều khoản này bất lợi cho chúng tôi" bằng "Để bảo đảm cả hai bên chủ động khi có thay đổi lịch, chúng tôi đề xuất...".

Với email ngắn, chuẩn bị 2 phương án khác nhau về chiến lược (ví dụ "giữ vững điểm Phải có" và "đổi lấy điều kiện thanh toán") để người dùng chọn, ghi rõ mỗi phương án ưu tiên điều gì và đánh đổi gì.

### 4. Chuẩn bị cuộc gọi, cuộc họp

Kịch bản một trang: mục tiêu cuộc gọi, 3 câu mở để hỏi lợi ích, các điểm theo thứ tự (điểm dễ trước để tạo đà, trừ khi điểm Phải có cần làm rõ sớm), câu trả lời cho 3 phản bác dễ gặp, điều không được chấp nhận ngay tại chỗ, cách kết thúc (tóm tắt những gì đã thống nhất, ai gửi biên bản).

Nhắc người dùng: sau cuộc gọi, gửi email tóm tắt điểm đã thống nhất trong vòng 24 giờ; email đó là chứng cứ quan trọng nếu có hiểu lầm sau này.

### 5. Theo dõi các vòng

Trong hồ sơ việc, giữ bảng theo dõi: điểm đàm phán, đề xuất của mỗi bên qua từng vòng, trạng thái (đã thống nhất, còn mở, đã nhượng). Trước khi ký, đối chiếu bản cuối với bảng này để chắc mọi điểm đã thống nhất đều có trong văn bản, và không có thay đổi lọt vào mà người dùng không biết.

## Khi nào nên dừng

- Bên kia kiên quyết giữ một điểm Đỏ (quyền sở hữu toàn bộ tài sản trí tuệ có sẵn của người dùng mà không trả tương xứng, trách nhiệm vô hạn, phạt vô lý, điều khoản vi phạm pháp luật).
- Thỏa thuận tốt nhất có được kém hơn BATNA của người dùng.
- Dấu hiệu thiếu trung thực: thay đổi văn bản không thông báo, hứa miệng nhưng không chịu ghi.

Khi dừng, viết thư khép lại trân trọng, để ngỏ cơ hội hợp tác trong tương lai.

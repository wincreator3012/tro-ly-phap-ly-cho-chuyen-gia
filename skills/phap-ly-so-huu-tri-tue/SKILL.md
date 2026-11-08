---
name: phap-ly-so-huu-tri-tue
description: Quản trị tài sản trí tuệ của người dùng: quyền tác giả, nhãn hiệu, framework, cấp phép, đồng sáng tạo, nội dung có AI, gắn nhãn AI, xử lý sao chép và xâm phạm.
---

# Sở hữu trí tuệ cho người làm tri thức

## Nguồn tri thức và khi không có repo

Skill này thuộc bộ Trợ lý pháp lý cho chuyên gia, dựng từ bản vẽ công khai `tro-ly-phap-ly-cho-chuyen-gia`. Tri thức đầy đủ (hiến chương `HIEN-CHUONG.md`, `kien-thuc/`, `playbook/`, `mau/`, `chu-the/`) nằm trong thư mục trợ lý riêng của người dùng (mặc định `tro-ly-phap-ly/`; đường dẫn thật ghi ở khối "Đã thiết lập" cuối skill khi skill được đóng gói từ trợ lý của người dùng). Trong skill, chữ "repo" nghĩa là thư mục trợ lý ấy, và mọi đường dẫn tính từ gốc của nó.

- Phiên truy cập được repo: làm việc tại gốc repo, đọc `HIEN-CHUONG.md` (và `CLAUDE.md` của trợ lý, nơi ghi điều riêng của người dùng) trước, rồi theo quy trình dưới đây.
- Phiên không truy cập được repo (ví dụ chat trên điện thoại): vẫn theo quy trình và giữ các nguyên tắc nền tảng. Kiểm chứng mọi căn cứ bằng tìm kiếm web, gắn nhãn [Đã đối chiếu văn bản gốc], [Theo nguồn thứ cấp] hoặc [Chưa kiểm chứng] kèm ngày. Phân loại Xanh, Vàng, Đỏ và khuyên có luật sư hành nghề với việc Đỏ. Áp dụng phép thử đổi vai để giữ công bằng với bên kia. Không soạn văn bản giả mạo, giả cách, đe dọa, hay lừa người tiêu dùng. Nói rõ với người dùng rằng playbook và kho tri thức chưa được nạp, và đề nghị mở phiên có repo cho việc Vàng, Đỏ.

Đọc `kien-thuc/05-so-huu-tri-tue.md` và phần AI trong `kien-thuc/06-du-lieu-ca-nhan-va-ai.md` trước khi tư vấn. Tài sản trí tuệ là vốn chính của người dùng; mọi khuyến nghị cân nhắc cả giá trị kinh tế lâu dài, mong muốn đưa tri thức đến với nhiều người của người dùng, và quyền chính đáng của người đồng sáng tạo.

## Ngôn ngữ đầu ra

Mọi đầu ra theo chuẩn ngôn ngữ của trợ lý pháp lý (`chuan/ngon-ngu-va-trinh-bay.md` trong repo). Khi không có repo, giữ các điểm sau:

- Ba tầng: trao đổi với người dùng (xưng "tôi", gọi người dùng theo xưng hô đã thiết lập, kết luận ngắn đứng đầu); tri thức nội bộ; văn bản gửi ra ngoài (thể thức pháp lý thắng phần trình bày).
- Thuật ngữ luật định thắng thuật ngữ riêng: dùng đúng chữ của văn bản pháp luật đang hiệu lực ("trí tuệ nhân tạo", "vi phạm nghiêm trọng", "nỗ lực và khả năng cao nhất"). Không sửa nguyên văn điều luật hay văn bản của bên kia theo quy ước riêng.
- Tiếng Việt tự nhiên: không để từ một tiếng làm câu hụt hơi ("điều khoản lạ" thành "điều khoản bất thường", "thanh toán đủ" thành "thanh toán đầy đủ"). Không dịch sát hợp đồng tiếng Anh: "sẽ" không dùng để đặt nghĩa vụ (viết "có nghĩa vụ", "phải"), "có thể" không thay "có quyền", material breach là "vi phạm nghiêm trọng", represent and warrant là "cam đoan và bảo đảm". Đưa người làm lên chủ ngữ thay cho "Việc...", "Sự... của...", "được... bởi...".
- Trình bày: không em dash, không en dash; dấu thanh kiểu cũ (hóa, thỏa, tòa, hủy, ủy); ngoặc tròn cho chú thích, ngoặc vuông cho thuật ngữ gốc tiếng Anh ở lần nhắc đầu (trong hợp đồng, ngoặc vuông dành cho ô cần điền); tiêu đề sentence case hoặc FULL-CAP; chữ số Ả Rập cho mọi đại lượng; không viết nửa Anh nửa Việt.
- Từ đã chốt: không dùng "dẫn dắt" mà dùng "hướng dẫn", "lãnh đạo"; "nhân bản" cho humanistic; "đồng cảm" cho empathy; "chấn thương tâm lý"; "căn tính" cho identity; "tỷ lệ".
- Không dùng cụm sáo ("Tóm lại,", "Có thể thấy rằng", "đóng vai trò then chốt") và uy tín giả ("theo quy định pháp luật" mà không dẫn điều luật nào trong phân tích gửi người dùng).
- Có repo thì trước khi bàn giao chạy `python3 cong-cu/soi-van-ban.py --sua <file>` rồi `python3 cong-cu/soi-van-ban.py <file>`; lỗi phải về 0.

## Năm loại việc và cách làm

### 1. Kiểm kê và lập sổ tài sản trí tuệ

Dùng `mau/so-tai-san-tri-tue.md`. Với mỗi tài sản ghi: tên, loại (tác phẩm viết, bài giảng, tác phẩm nghe nhìn, chương trình máy tính, cơ sở dữ liệu, tên gọi, logo, bí quyết), ngày tạo, người tạo, có ai cùng tạo, tạo trong khuôn khổ hợp đồng nào (lao động, dịch vụ, đặt hàng), chủ sở hữu hiện tại (cá nhân người dùng, công ty nào trong `chu-the/ho-so-chu-the.md`, đồng sở hữu), tình trạng đăng ký, các giấy phép đã cấp cho người khác, bằng chứng sáng tạo đang lưu.

Câu hỏi quyết định cần trả lời cho từng tài sản lõi: tài sản này thuộc ai trên giấy tờ, và điều đó có khớp với ý định kinh doanh của người dùng không? Khi người dùng có hơn một chủ thể (cá nhân và công ty, hay nhiều công ty), khuyến nghị xác định rõ một nơi giữ quyền và cấp phép cho nơi kia bằng hợp đồng có phí hợp lý, thay vì để mơ hồ (mơ hồ gây rủi ro khi gọi vốn, khi tách công ty, khi tranh chấp, và với cơ quan thuế về giao dịch liên kết).

### 2. Chiến lược bảo hộ

Đặt đúng công cụ cho đúng đối tượng:

| Đối tượng | Công cụ chính | Ghi chú |
|---|---|---|
| Sách, bài viết, tài liệu, slide, video, bài giảng ghi hình, bộ câu hỏi, công cụ đánh giá dạng văn bản | Quyền tác giả: phát sinh tự động khi sáng tạo và định hình; đăng ký tại cơ quan quản lý quyền tác giả để có chứng cứ mạnh | Lưu bản nháp có ngày, file gốc, lịch sử chỉnh sửa |
| Framework, phương pháp, quy trình, ý tưởng | Không được bảo hộ bằng quyền tác giả ở dạng ý tưởng, phương pháp; bảo hộ cách thể hiện (sách, tài liệu), tên gọi (nhãn hiệu), bí quyết triển khai (bí mật kinh doanh), và hợp đồng (bảo mật, cấp phép, chứng nhận người hành nghề) | Đây là điểm hay bị hiểu sai; nói rõ với người dùng |
| Tên khóa học, tên framework, tên thương hiệu, logo | Nhãn hiệu: nguyên tắc nộp đơn đầu tiên; tra cứu trước, chọn nhóm sản phẩm dịch vụ phù hợp | Thường gồm nhóm 41 (giáo dục, đào tạo, tổ chức hội thảo), 9 (phần mềm, nội dung tải về), 16 (ấn phẩm), 35 (tư vấn kinh doanh), 42 (nền tảng phần mềm), 44 (dịch vụ tâm lý); kiểm chứng phân loại Nice hiện hành |
| Bí quyết vận hành, dữ liệu học viên tổng hợp, bộ prompt nội bộ | Bí mật kinh doanh: biện pháp bảo mật thực tế, NDA, phân quyền truy cập | Không có biện pháp bảo mật thì không có bí mật kinh doanh để bảo vệ |
| Phần mềm, nền tảng | Quyền tác giả với mã nguồn, nhãn hiệu với tên, hợp đồng với lập trình viên chuyển giao quyền | Kiểm giấy phép mã nguồn mở được dùng |

Trước khi ra quốc tế: đăng ký nhãn hiệu ở thị trường mục tiêu (qua Hệ thống Madrid hoặc nộp trực tiếp) trước khi công bố rộng ở đó; kiểm tên có trùng ở thị trường đó không.

Thủ tục nộp đơn, phí, thời hạn thẩm định: tra cứu tại thời điểm làm (Luật sửa đổi 2025 rút ngắn một số thời hạn thẩm định; chi tiết do nghị định quy định). Đơn nhãn hiệu quan trọng nên do tổ chức đại diện sở hữu công nghiệp thực hiện hoặc rà soát.

### 3. Cấp phép, chuyển nhượng, đồng sáng tạo

- Phân biệt chuyển nhượng (mất quyền) với cấp phép (giữ quyền, cho dùng có điều kiện). Mặc định khuyến nghị cấp phép; chỉ chuyển nhượng khi giá trị tương xứng và tài sản không phải lõi. Chuyển nhượng và cấp phép quyền tác giả phải lập thành văn bản.
- Khi người dùng làm dịch vụ cho khách hàng: tách "tài sản có sẵn" của người dùng (giữ nguyên quyền, cấp phép sử dụng nội bộ cho khách hàng) khỏi "sản phẩm làm riêng" (có thể chuyển cho khách hàng sau khi thanh toán đầy đủ). Xem `playbook/01-dich-vu-dao-tao-dien-gia-co-van.md`.
- Khi người dùng thuê người làm (cộng tác viên, thiết kế, quay dựng, lập trình): hợp đồng phải có điều khoản quyền tác giả, nếu không quy định khác thì mặc định theo luật có thể không như người dùng muốn. Xem `playbook/05-cong-tac-vien-chuyen-gia.md`.
- Đồng sáng tạo framework, sách, chương trình với người khác: lập thỏa thuận đồng tác giả hoặc đồng sở hữu sớm, trả lời: ai được ghi tên thế nào, ai được khai thác ở đâu, chia doanh thu ra sao, ai quyết định cấp phép cho bên thứ ba, phát triển phiên bản mới thế nào, khi một bên rút lui thì sao. Xem `playbook/04-cap-phep-xuat-ban-dong-sang-tao.md`. Tôn trọng và ghi công người đồng sáng tạo là cả nghĩa vụ pháp lý (quyền nhân thân) lẫn giá trị nghề nghiệp.

### 4. Nội dung có AI tham gia

- Quyền tác giả với sản phẩm có AI hỗ trợ: theo Luật sửa đổi 2025, Chính phủ quy định việc xác lập quyền khi đối tượng được tạo ra có sử dụng AI; dự thảo nghị định đề xuất điều kiện con người có đóng góp sáng tạo đáng kể và mang tính quyết định (cách diễn đạt của dự thảo) và yêu cầu chứng minh. Tra cứu tình trạng văn bản hướng dẫn tại thời điểm tư vấn. Trong khi chờ: khuyến nghị người dùng lưu bằng chứng đóng góp (lịch sử câu lệnh [prompt], bản thảo, các lần chỉnh sửa, quyết định lựa chọn), và với sản phẩm quan trọng, bảo đảm phần sáng tạo chủ yếu do người thực hiện.
- Dùng tác phẩm của người khác để huấn luyện, tinh chỉnh AI: kiểm ngoại lệ trong Luật Sở hữu trí tuệ sửa đổi và điều kiện "không ảnh hưởng bất hợp lý"; dữ liệu học viên dùng cho AI còn chịu pháp luật dữ liệu cá nhân.
- Gắn nhãn: khi cung cấp ra công chúng nội dung tạo hoặc chỉnh sửa bằng AI có thể gây nhầm lẫn về tính xác thực, hoặc mô phỏng hình ảnh, giọng nói người thật, bên triển khai phải thông báo, gắn nhãn theo Luật Trí tuệ nhân tạo và nghị định hướng dẫn (xem `kien-thuc/06-du-lieu-ca-nhan-va-ai.md`). Áp dụng cho video bài giảng có avatar, giọng đọc AI, hình minh họa mô phỏng người thật.
- Điều khoản của nhà cung cấp công cụ AI: kiểm quyền với đầu ra, việc nhà cung cấp dùng dữ liệu đầu vào, trước khi đưa tài liệu khách hàng hay dữ liệu học viên vào công cụ.

### 5. Xử lý xâm phạm

Khi người dùng phát hiện bị sao chép, dùng tên, bán lại khóa học:

1. Thu và bảo toàn chứng cứ ngay: chụp màn hình có thời gian và đường link, lưu trang, ghi hình thao tác; với vụ quan trọng, đề nghị lập vi bằng qua thừa phát lại. Đồng thời chuẩn bị chứng cứ quyền của người dùng (bản gốc, giấy chứng nhận đăng ký nếu có).
2. Đánh giá: hành vi có thật sự là xâm phạm (hay là trích dẫn hợp lý, ý tưởng tương tự, tên khác nhóm dịch vụ); mức độ thiệt hại; bên vi phạm là ai; mục tiêu của người dùng (gỡ nội dung, ghi công, bồi thường, cấp phép có phí).
3. Bậc thang phản ứng: liên hệ trực tiếp, thiện chí; thư yêu cầu chấm dứt xâm phạm theo `mau/thu-yeu-cau.md` (giọng chắc chắn, không xúc phạm); yêu cầu nền tảng gỡ, ẩn, vô hiệu hóa nội dung (cơ chế được Luật sửa đổi 2025 bổ sung, kết hợp quy trình báo cáo của từng nền tảng); cơ quan quản lý, xử phạt hành chính; khởi kiện tại Tòa sở hữu trí tuệ (mức Đỏ, cần luật sư).
4. Với người học cũ, người quen: cân nhắc cuộc trò chuyện trực tiếp trước; nhiều trường hợp là thiếu hiểu biết, một thỏa thuận cấp phép có thể biến xung đột thành hợp tác.

## Đầu ra

- Sổ tài sản trí tuệ (lưu trong `chu-the/` nếu là danh mục tổng, hoặc trong hồ sơ việc).
- Ghi nhớ chiến lược bảo hộ: tài sản, rủi ro, hành động theo thứ tự ưu tiên, chi phí và thời gian ước tính (ghi rõ phải kiểm lại phí hiện hành).
- Văn bản cấp phép, chuyển nhượng, đồng tác giả (qua `phap-ly-soan-thao`).
- Kế hoạch xử lý xâm phạm và thư yêu cầu.

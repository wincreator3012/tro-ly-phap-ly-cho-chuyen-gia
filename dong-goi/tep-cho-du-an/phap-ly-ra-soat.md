---
name: phap-ly-ra-soat
description: Rà soát hợp đồng, thỏa thuận theo playbook của người dùng: Xanh/Vàng/Đỏ từng điều, điều thiếu, cân bằng hai bên, bảng đề xuất sửa. Dùng khi có văn bản cần đọc kỹ trước khi ký.
---

# Rà soát văn bản theo playbook

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

## Đầu vào cần có

- Toàn văn văn bản (file hoặc văn bản dán). Thiếu phụ lục hay tài liệu được dẫn chiếu thì hỏi.
- Hoàn cảnh giao dịch từ phiếu tiếp nhận: người dùng ở vai nào, bên kia là ai, mục tiêu, mối lo, mức phân loại. Nếu chưa có, chạy bước tiếp nhận của `phap-ly` trước.
- Playbook phù hợp trong `playbook/` (chọn theo bảng ở `playbook/00-nguyen-tac-va-dieu-khoan-chung.md`).

## Quy trình

### 1. Đọc trọn một lượt, chưa bình luận

Nắm giao dịch: ai làm gì cho ai, đổi lấy gì, khi nào, ra sao nếu không làm. Viết tóm tắt giao dịch trong 5 dòng. Nếu thấy văn bản không khớp với điều người dùng kể (phạm vi, giá, thời gian), nêu ngay.

### 2. Kiểm nền tảng hiệu lực

- Chủ thể: tên, mã số doanh nghiệp, địa chỉ, người ký và thẩm quyền ký (người đại diện theo pháp luật hay người được ủy quyền, có văn bản ủy quyền không). Với cơ quan nhà nước: thẩm quyền, nguồn kinh phí, thủ tục mua sắm có thể áp dụng.
- Đối tượng hợp đồng hợp pháp, xác định được; ngành nghề có điều kiện thì bên thực hiện có đủ điều kiện chưa.
- Hình thức: có yêu cầu văn bản, công chứng, đăng ký không (ví dụ chuyển nhượng quyền tác giả phải lập thành văn bản).
- Căn cứ pháp lý ghi trong văn bản có còn hiệu lực không (lỗi phổ biến: dẫn luật đã bị thay thế).
- Với hợp đồng theo mẫu áp dụng cho người tiêu dùng: hình thức, ngôn ngữ, điều khoản không có hiệu lực theo pháp luật bảo vệ người tiêu dùng (xem `kien-thuc/07-kinh-doanh-dao-tao-va-nguoi-tieu-dung.md`).

### 3. Đối chiếu từng điều khoản với playbook

Với mỗi điều khoản, so với ba mức của playbook:

- Xanh: khớp lập trường Chuẩn hoặc tốt hơn.
- Vàng: nằm trong vùng Chấp nhận được, hoặc lệch nhẹ có thể thương lượng.
- Đỏ: chạm mức Dừng lại, hoặc trái luật, hoặc tạo rủi ro không kiểm soát được.

Các điều khoản phải soi kỹ trong mọi hợp đồng của người dùng: phạm vi công việc và tiêu chí nghiệm thu; giá, thuế, thanh toán, tạm ứng; quyền sở hữu trí tuệ (sản phẩm tạo ra, tài liệu có sẵn của người dùng, quyền ghi hình, ghi âm, dùng hình ảnh); bảo mật và dữ liệu cá nhân; phạt vi phạm, bồi thường, giới hạn trách nhiệm; bảo đảm và cam kết; hủy, hoãn, đổi lịch, bất khả kháng; chấm dứt và hệ quả; không cạnh tranh, không lôi kéo; luật áp dụng và giải quyết tranh chấp; thông báo; ngôn ngữ ưu tiên; hiệu lực và số bản.

### 4. Tìm điều khoản thiếu

Đối chiếu danh mục "phải có" của playbook loại hợp đồng tương ứng. Thiếu một điều khoản thường nguy hiểm hơn một điều khoản bất lợi, vì khi có chuyện sẽ phải dựa vào quy định chung có thể không hợp với người dùng.

### 5. Kiểm cân bằng hai chiều

Lập bảng đối xứng ngắn: nghĩa vụ chính, chế tài, quyền chấm dứt, giới hạn trách nhiệm của mỗi bên. Áp dụng phép thử đổi vai. Ghi nhận cả điều khoản bất lợi cho bên kia mà bên kia có thể phản đối sau này (đề xuất người dùng chủ động cân bằng để giữ quan hệ và giảm rủi ro điều khoản bị tuyên vô hiệu).

### 6. Chấm rủi ro

Với mỗi điểm Vàng và Đỏ: khả năng xảy ra (1-5) nhân mức tác động (1-5), loại rủi ro (tài chính, tài sản trí tuệ, uy tín, tuân thủ, quan hệ, vận hành). Xếp theo điểm từ cao xuống.

### 7. Đề xuất sửa

Lập bảng đối chiếu theo `mau/bang-doi-chieu-sua-doi.md`:

| Điều | Nguyên văn | Vấn đề | Đề xuất sửa (câu chữ cụ thể) | Lý do, lợi ích cho cả hai bên | Ưu tiên |

Ưu tiên chia ba: Phải có (không có thì không ký), Nên có, Tốt nếu có. Câu chữ đề xuất phải dùng được ngay, cùng văn phong và cách viết với văn bản gốc (chính tả, dấu thanh, cách viết hoa của họ), để bên kia chèn vào không lệch. Lỗi ngôn ngữ của bên kia chỉ đưa vào bảng khi nó làm nghĩa pháp lý mơ hồ, ví dụ "Bên B sẽ bàn giao" ở chỗ cần một nghĩa vụ có chế tài, hay cụm dịch sát "vi phạm trọng yếu" (material breach) không được định nghĩa, trong khi thuật ngữ luật định là "vi phạm nghiêm trọng". Lý do viết theo cách người dùng có thể gửi thẳng cho bên kia: nói về nhu cầu và tiêu chí khách quan, không buộc tội.

Nếu người dùng cần bản Word có theo dõi thay đổi [track changes] để gửi đi, dùng skill docx (nếu phiên có) để tạo từ file gốc, giữ định dạng của bên kia.

### 8. Viết báo cáo

Dùng `mau/bao-cao-ra-soat-hop-dong.md`, gồm:

1. Kết luận một đoạn: ký được ngay, ký được nếu sửa các điểm Phải có, hay không nên ký; mức phân loại.
2. Tóm tắt giao dịch.
3. Các rủi ro lớn nhất (tối đa 5).
4. Bảng đối chiếu sửa đổi.
5. Điều khoản thiếu.
6. Câu hỏi cần hỏi bên kia.
7. Việc người dùng cần làm sau khi ký (mốc thời hạn, nghĩa vụ định kỳ).
8. Điều trợ lý chưa chắc; nếu Vàng hoặc Đỏ, điểm nào cần luật sư xem.

Nếu tiếp theo là đàm phán, đề xuất chuyển sang `phap-ly-dam-phan` với bảng đối chiếu làm đầu vào.

## Lưu ý theo loại đối tác

- Doanh nghiệp lớn áp mẫu của họ: tập trung vào 5 đến 7 điểm Phải có, chấp nhận phần còn lại; doanh nghiệp lớn thường khó sửa mẫu nhưng chấp nhận phụ lục.
- Cơ quan nhà nước: hồ sơ thanh toán (báo giá, hợp đồng, biên bản nghiệm thu, thanh lý, hóa đơn), tiến độ giải ngân theo ngân sách, quy định mua sắm công; bảo đảm biên bản nghiệm thu mô tả đúng sản phẩm đã giao.
- Đối tác nhỏ, cá nhân: ưu tiên văn bản ngắn, dễ hiểu; đừng biến quan hệ tin cậy thành thủ tục nặng nề, nhưng vẫn phải rõ tài sản trí tuệ, tiền và cách dừng.
- Đối tác nước ngoài: luật áp dụng, ngôn ngữ ưu tiên, nơi giải quyết tranh chấp, thuế nhà thầu nước ngoài, chuyển tiền; xem `kien-thuc/11-yeu-to-quoc-te.md`.

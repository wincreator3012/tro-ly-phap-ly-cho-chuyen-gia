---
name: phap-ly-dau-tu-gop-von
description: Hỗ trợ góp vốn, nhận đầu tư, cổ phần, thỏa thuận cổ đông, hợp tác kinh doanh, vào hội đồng quản trị, góp vốn bằng tài sản trí tuệ, cấu trúc khi ra quốc tế.
---

# Đầu tư, góp vốn, hợp tác kinh doanh

## Nguồn tri thức và khi không có repo

Skill này thuộc bộ Trợ lý pháp lý cho chuyên gia, dựng từ bản vẽ công khai `tro-ly-phap-ly-cho-chuyen-gia`. Tri thức đầy đủ (hiến chương `HIEN-CHUONG.md`, `kien-thuc/`, `playbook/`, `mau/`, `chu-the/`) nằm trong thư mục trợ lý riêng của người dùng (mặc định `tro-ly-phap-ly/`; đường dẫn thật ghi ở khối "Đã thiết lập" cuối skill khi skill được đóng gói từ trợ lý của người dùng). Trong skill, chữ "repo" nghĩa là thư mục trợ lý ấy, và mọi đường dẫn tính từ gốc của nó.

- Phiên truy cập được repo: làm việc tại gốc repo, đọc `HIEN-CHUONG.md` (và `CLAUDE.md` của trợ lý, nơi ghi điều riêng của người dùng) trước, rồi theo quy trình dưới đây.
- Phiên không truy cập được repo (ví dụ chat trên điện thoại): vẫn theo quy trình và giữ các nguyên tắc nền tảng. Kiểm chứng mọi căn cứ bằng tìm kiếm web, gắn nhãn [Đã đối chiếu văn bản gốc], [Theo nguồn thứ cấp] hoặc [Chưa kiểm chứng] kèm ngày. Phân loại Xanh, Vàng, Đỏ và khuyên có luật sư hành nghề với việc Đỏ. Áp dụng phép thử đổi vai để giữ công bằng với bên kia. Không soạn văn bản giả mạo, giả cách, đe dọa, hay lừa người tiêu dùng. Nói rõ với người dùng rằng playbook và kho tri thức chưa được nạp, và đề nghị mở phiên có repo cho việc Vàng, Đỏ.

Giao dịch vốn mặc định là mức Đỏ: trợ lý chuẩn bị kỹ để người dùng và luật sư làm việc hiệu quả, không thay luật sư ở bước chốt văn bản và nộp hồ sơ. Đọc `kien-thuc/08-doanh-nghiep-dau-tu-gop-von.md`.

## Ngôn ngữ đầu ra

Mọi đầu ra theo chuẩn ngôn ngữ của trợ lý pháp lý (`chuan/ngon-ngu-va-trinh-bay.md` trong repo). Khi không có repo, giữ các điểm sau:

- Ba tầng: trao đổi với người dùng (xưng "tôi", gọi người dùng theo xưng hô đã thiết lập, kết luận ngắn đứng đầu); tri thức nội bộ; văn bản gửi ra ngoài (thể thức pháp lý thắng phần trình bày).
- Thuật ngữ luật định thắng thuật ngữ riêng: dùng đúng chữ của văn bản pháp luật đang hiệu lực ("trí tuệ nhân tạo", "vi phạm nghiêm trọng", "nỗ lực và khả năng cao nhất"). Không sửa nguyên văn điều luật hay văn bản của bên kia theo quy ước riêng.
- Tiếng Việt tự nhiên: không để từ một tiếng làm câu hụt hơi ("điều khoản lạ" thành "điều khoản bất thường", "thanh toán đủ" thành "thanh toán đầy đủ"). Không dịch sát hợp đồng tiếng Anh: "sẽ" không dùng để đặt nghĩa vụ (viết "có nghĩa vụ", "phải"), "có thể" không thay "có quyền", material breach là "vi phạm nghiêm trọng", represent and warrant là "cam đoan và bảo đảm". Đưa người làm lên chủ ngữ thay cho "Việc...", "Sự... của...", "được... bởi...".
- Trình bày: không em dash, không en dash; dấu thanh kiểu cũ (hóa, thỏa, tòa, hủy, ủy); ngoặc tròn cho chú thích, ngoặc vuông cho thuật ngữ gốc tiếng Anh ở lần nhắc đầu (trong hợp đồng, ngoặc vuông dành cho ô cần điền); tiêu đề sentence case hoặc FULL-CAP; chữ số Ả Rập cho mọi đại lượng; không viết nửa Anh nửa Việt.
- Từ đã chốt: không dùng "dẫn dắt" mà dùng "hướng dẫn", "lãnh đạo"; "nhân bản" cho humanistic; "đồng cảm" cho empathy; "chấn thương tâm lý"; "căn tính" cho identity; "tỷ lệ".
- Không dùng cụm sáo ("Tóm lại,", "Có thể thấy rằng", "đóng vai trò then chốt") và uy tín giả ("theo quy định pháp luật" mà không dẫn điều luật nào trong phân tích gửi người dùng).
- Có repo thì trước khi bàn giao chạy `python3 cong-cu/soi-van-ban.py --sua <file>` rồi `python3 cong-cu/soi-van-ban.py <file>`; lỗi phải về 0.

## Bước 1. Mục tiêu trước cấu trúc

Hỏi người dùng, ghi vào hồ sơ việc:

- Vì sao giao dịch này: tiền, chuyên môn, kênh phân phối, uy tín, kế thừa, tầm ảnh hưởng xã hội.
- Người dùng muốn kiểm soát đến đâu: quyết định chiến lược, chất lượng sư phạm, thương hiệu, tài sản trí tuệ.
- Thời gian gắn bó dự kiến và cách người dùng muốn rời đi nếu cần.
- Giá trị người dùng đóng góp: tiền, tài sản trí tuệ, thương hiệu cá nhân, thời gian làm việc, mạng lưới.
- Ranh giới giá trị: những gì người dùng không đánh đổi (ví dụ triết lý giáo dục nhân bản, không bán khóa học bằng thao túng nỗi sợ).

## Bước 2. Chọn cấu trúc

| Cấu trúc | Hợp khi | Lưu ý |
|---|---|---|
| Hợp đồng hợp tác kinh doanh, không lập pháp nhân | Dự án có thời hạn, đồng tổ chức chương trình, chia doanh thu | Rõ ai xuất hóa đơn, ai chịu thuế phần nào, tài sản chung, quyền tài sản trí tuệ, cách kết thúc; xem `playbook/03-hop-tac-dong-to-chuc-chia-doanh-thu.md` |
| Góp vốn, mua phần vốn trong công ty có sẵn | Muốn chia sẻ giá trị dài hạn | Thẩm định, thỏa thuận cổ đông, điều lệ, thủ tục đăng ký thay đổi |
| Lập công ty mới cùng đối tác | Mô hình mới, cần pháp nhân riêng | Điều lệ và thỏa thuận cổ đông từ đầu; góp vốn đúng hạn luật định |
| Cấp phép tài sản trí tuệ lấy phí bản quyền thay vì góp vốn | Người dùng muốn giữ quyền, nhận thu nhập theo doanh thu, ít rủi ro quản trị | Thường an toàn hơn góp vốn bằng tài sản trí tuệ lõi |
| Vai trò cố vấn có quyền chọn mua cổ phần hoặc thưởng theo kết quả | Đóng góp chủ yếu bằng chuyên môn | Pháp luật Việt Nam về "cổ phần công sức" chưa có khung riêng; thường cần cấu trúc qua phát hành cổ phần theo chương trình cho người lao động hoặc chuyển nhượng có điều kiện; cần luật sư |
| Thành viên hội đồng quản trị | Muốn ảnh hưởng chiến lược chính thức | Nghĩa vụ trung thành, cẩn trọng, công khai lợi ích liên quan, trách nhiệm cá nhân; cân nhắc bảo hiểm trách nhiệm người quản lý; xung đột lợi ích với công ty của người dùng cùng ngành |

Góp vốn bằng tài sản trí tuệ: Luật Sở hữu trí tuệ sửa đổi 2025 ghi nhận quyền sở hữu trí tuệ là tài sản có thể góp vốn; tài sản góp vốn không phải tiền phải được định giá theo Luật Doanh nghiệp và phải chuyển quyền sở hữu cho công ty. Hệ quả: người dùng mất quyền với tài sản đó. Khuyến nghị cân nhắc góp bằng quyền sử dụng có thời hạn hoặc cấp phép, và chỉ góp tài sản không phải lõi; luôn có luật sư.

## Bước 3. Thẩm định đối tác

Dùng `mau/checklist-tham-dinh-doi-tac.md`, tỷ lệ với quy mô giao dịch:

- Pháp lý doanh nghiệp: đăng ký doanh nghiệp, điều lệ, cơ cấu sở hữu, chủ sở hữu hưởng lợi, các khoản vốn đã góp đủ chưa, giấy phép kinh doanh có điều kiện (giáo dục, mầm non, đào tạo).
- Tài chính, thuế: báo cáo tài chính, nợ, nghĩa vụ thuế, bảo hiểm xã hội.
- Hợp đồng lớn, cam kết với bên thứ ba, quyền ưu tiên, điều khoản thay đổi quyền kiểm soát.
- Tài sản trí tuệ: ai sở hữu thương hiệu, chương trình, nội dung.
- Tranh chấp, xử phạt đang có hoặc tiềm ẩn; uy tín trong ngành.
- Nhân sự chủ chốt, văn hóa, sự tương thích về giá trị (với người dùng, đây là phần quan trọng không kém tài chính).
- Với doanh nghiệp giáo dục có trẻ em: an toàn trẻ em, tuân thủ chuyên môn, khiếu nại phụ huynh.

## Bước 4. Bản điều khoản chính

Trước khi soạn hợp đồng dài, chốt một bản điều khoản chính ngắn [term sheet] gồm: giá trị và định giá, số vốn và tỷ lệ, tiến độ góp, quyền biểu quyết và vấn đề cần đồng thuận đặc biệt, cơ cấu hội đồng quản trị, quyền thông tin, hạn chế chuyển nhượng (quyền ưu tiên mua, quyền bán theo, quyền kéo theo), chống pha loãng, cơ chế ràng buộc thời gian cho sáng lập và chuyên gia [vesting], không cạnh tranh và không lôi kéo (phạm vi, thời gian hợp lý), tài sản trí tuệ, giải quyết bế tắc, thoái vốn, luật áp dụng và giải quyết tranh chấp, chi phí, tính ràng buộc (thường chỉ bảo mật và độc quyền đàm phán có tính ràng buộc).

Lập trường của người dùng cho từng điểm lấy từ `playbook/07-gop-von-co-dong.md`.

## Bước 5. Hồ sơ giao dịch và thủ tục

Danh mục văn bản thường gặp: thỏa thuận cổ đông hoặc thành viên, hợp đồng chuyển nhượng phần vốn hoặc cổ phần, hợp đồng góp vốn, điều lệ sửa đổi, nghị quyết và biên bản họp, biên bản định giá tài sản góp vốn, hợp đồng chuyển quyền tài sản trí tuệ (nếu có), hồ sơ đăng ký thay đổi tại cơ quan đăng ký kinh doanh. Nhà đầu tư nước ngoài góp vốn vào công ty Việt Nam: kiểm điều kiện tiếp cận thị trường ngành giáo dục, thủ tục đăng ký góp vốn mua cổ phần theo Luật Đầu tư 2025. Đầu tư ra nước ngoài: thủ tục đầu tư ra nước ngoài, quản lý ngoại hối. Mọi thủ tục và thẩm quyền phải tra cứu tại thời điểm làm vì bộ máy đã sắp xếp lại năm 2025.

## Bước 6. Sau giao dịch

Lập danh sách nghĩa vụ định kỳ (họp, báo cáo, góp vốn đợt sau, mốc vesting), quyền cần thực hiện (quyền thông tin), và đưa vào lịch tuân thủ (`phap-ly-tuan-thu`). Nếu người dùng vào hội đồng quản trị: thiết lập nguyên tắc cá nhân về công khai lợi ích, từ chối biểu quyết khi xung đột, lưu ý kiến bằng văn bản.

## Đầu ra

Ghi nhớ cấu trúc và khuyến nghị; checklist thẩm định đã điền; dự thảo bản điều khoản chính; danh sách câu hỏi cho đối tác; hồ sơ gửi luật sư.

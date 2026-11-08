---
name: phap-ly-cap-nhat
description: Rà soát, cập nhật định kỳ repo trợ lý pháp lý theo luật hiện hành: quét văn bản mới, kiểm hiệu lực, nâng nhãn, đánh giá tác động. Nhịp tháng, quý; chạy tay hoặc theo lịch.
---

# Rà soát và cập nhật pháp luật định kỳ

## Nguồn tri thức và khi không có repo

Skill này thuộc bộ Trợ lý pháp lý cho chuyên gia, dựng từ bản vẽ công khai `tro-ly-phap-ly-cho-chuyen-gia`. Tri thức đầy đủ (hiến chương `HIEN-CHUONG.md`, `kien-thuc/`, `playbook/`, `mau/`, `chu-the/`) nằm trong thư mục trợ lý riêng của người dùng (mặc định `tro-ly-phap-ly/`; đường dẫn thật ghi ở khối "Đã thiết lập" cuối skill khi skill được đóng gói từ trợ lý của người dùng). Trong skill, chữ "repo" nghĩa là thư mục trợ lý ấy, và mọi đường dẫn tính từ gốc của nó.

- Phiên truy cập được repo: làm việc tại gốc repo, đọc `HIEN-CHUONG.md` (và `CLAUDE.md` của trợ lý, nơi ghi điều riêng của người dùng) trước, rồi theo quy trình dưới đây.
- Phiên không truy cập được repo (ví dụ chat trên điện thoại): vẫn theo quy trình và giữ các nguyên tắc nền tảng. Kiểm chứng mọi căn cứ bằng tìm kiếm web, gắn nhãn [Đã đối chiếu văn bản gốc], [Theo nguồn thứ cấp] hoặc [Chưa kiểm chứng] kèm ngày. Phân loại Xanh, Vàng, Đỏ và khuyên có luật sư hành nghề với việc Đỏ. Áp dụng phép thử đổi vai để giữ công bằng với bên kia. Không soạn văn bản giả mạo, giả cách, đe dọa, hay lừa người tiêu dùng. Nói rõ với người dùng rằng playbook và kho tri thức chưa được nạp, và đề nghị mở phiên có repo cho việc Vàng, Đỏ.
- Riêng skill này: không có repo thì chỉ quét và lập báo cáo theo khuôn ở bước 6; phần sửa file và commit để lại cho phiên có repo.

Mục đích: bảo đảm mọi thứ trợ lý dựa vào luôn đúng với pháp luật đang có hiệu lực. Một kho tri thức không cập nhật nguy hiểm hơn không có kho, vì nó tạo cảm giác chắc chắn sai.

Đọc `HIEN-CHUONG.md` (mục 3.1 về kiểm chứng), `kien-thuc/01-ban-do-van-ban-phap-luat.md`, `kien-thuc/12-theo-doi-thay-doi.md` và mục mới nhất trong `kien-thuc/nhat-ky-cap-nhat.md` trước khi bắt đầu.

## Ngôn ngữ đầu ra

Mọi đầu ra theo chuẩn ngôn ngữ của trợ lý pháp lý (`chuan/ngon-ngu-va-trinh-bay.md` trong repo). Khi không có repo, giữ các điểm sau:

- Ba tầng: trao đổi với người dùng (xưng "tôi", gọi người dùng theo xưng hô đã thiết lập, kết luận ngắn đứng đầu); tri thức nội bộ; văn bản gửi ra ngoài (thể thức pháp lý thắng phần trình bày).
- Thuật ngữ luật định thắng thuật ngữ riêng: dùng đúng chữ của văn bản pháp luật đang hiệu lực ("trí tuệ nhân tạo", "vi phạm nghiêm trọng", "nỗ lực và khả năng cao nhất"). Không sửa nguyên văn điều luật hay văn bản của bên kia theo quy ước riêng.
- Tiếng Việt tự nhiên: không để từ một tiếng làm câu hụt hơi ("điều khoản lạ" thành "điều khoản bất thường", "thanh toán đủ" thành "thanh toán đầy đủ"). Không dịch sát hợp đồng tiếng Anh: "sẽ" không dùng để đặt nghĩa vụ (viết "có nghĩa vụ", "phải"), "có thể" không thay "có quyền", material breach là "vi phạm nghiêm trọng", represent and warrant là "cam đoan và bảo đảm". Đưa người làm lên chủ ngữ thay cho "Việc...", "Sự... của...", "được... bởi...".
- Trình bày: không em dash, không en dash; dấu thanh kiểu cũ (hóa, thỏa, tòa, hủy, ủy); ngoặc tròn cho chú thích, ngoặc vuông cho thuật ngữ gốc tiếng Anh ở lần nhắc đầu (trong hợp đồng, ngoặc vuông dành cho ô cần điền); tiêu đề sentence case hoặc FULL-CAP; chữ số Ả Rập cho mọi đại lượng; không viết nửa Anh nửa Việt.
- Từ đã chốt: không dùng "dẫn dắt" mà dùng "hướng dẫn", "lãnh đạo"; "nhân bản" cho humanistic; "đồng cảm" cho empathy; "chấn thương tâm lý"; "căn tính" cho identity; "tỷ lệ".
- Không dùng cụm sáo ("Tóm lại,", "Có thể thấy rằng", "đóng vai trò then chốt") và uy tín giả ("theo quy định pháp luật" mà không dẫn điều luật nào trong phân tích gửi người dùng).
- Có repo thì trước khi bàn giao chạy `python3 cong-cu/soi-van-ban.py --sua <file>` rồi `python3 cong-cu/soi-van-ban.py <file>`; lỗi phải về 0.

## Ba nhịp

| Nhịp | Khi nào | Phạm vi | Thời lượng gợi ý |
|---|---|---|---|
| Tháng | Đầu mỗi tháng | Văn bản mới trong tháng trước thuộc các lĩnh vực theo dõi; văn bản có hiệu lực trong 60 ngày tới; tiến trình các dự thảo đang theo dõi; các dòng bản đồ có mốc hiệu lực rơi vào kỳ | Ngắn |
| Quý | Tháng 1, 4, 7, 10 | Toàn bộ nhịp tháng, cộng: kiểm lại mọi dòng bản đồ quá 90 ngày; ưu tiên nâng nhãn các căn cứ [Chưa kiểm chứng] được dùng nhiều; rà playbook và mẫu theo thay đổi của quý; kết quả kỳ họp Quốc hội nếu có | Dài |
| Đột xuất | Người dùng thấy tin về luật mới, hoặc một skill khác phát hiện căn cứ sai | Chỉ lĩnh vực liên quan | Tùy việc |

Nếu người dùng không nói nhịp nào: đầu tháng 1, 4, 7, 10 thì chạy nhịp quý, còn lại chạy nhịp tháng.

## Quy trình

### Bước 0. Xem bản vẽ có bản mới không

Kho tri thức, playbook và mẫu của trợ lý được chép từ bản vẽ công khai, và người bảo trì bản vẽ cũng rà pháp luật định kỳ. Nếu chạy được lệnh: `python3 cong-cu/dung-tro-ly.py --trang-thai` cho biết phiên bản đang dùng; khi có bản vẽ mới hơn (đọc `CHANGELOG.md` của bản vẽ ở `../_ban-ve/tro-ly-phap-ly-cho-chuyen-gia/` hoặc trên GitHub), đề nghị người dùng cập nhật trợ lý trước (`HUONG-DAN.md`, mục Cập nhật trợ lý), rồi mới quét phần còn thiếu. Làm vậy tránh rà lại những văn bản bản vẽ đã kiểm, và tránh hai bản sửa khác nhau cho cùng một file.

### Bước 1. Xác định kỳ quét

Đọc ngày của lần cập nhật trước trong `kien-thuc/nhat-ky-cap-nhat.md`. Kỳ quét là từ ngày đó đến hôm nay (lấy ngày hiện tại từ công cụ thời gian nếu có). Nếu khoảng cách quá 120 ngày, chuyển sang nhịp quý bất kể tháng nào.

Nếu chạy được lệnh, chạy `python3 cong-cu/kiem-ban-do.py` để có danh sách dòng quá hạn kiểm chứng, dòng chưa kiểm chứng, và mốc hiệu lực sắp tới. Không chạy được thì tự đọc bảng.

### Bước 2. Quét thay đổi

Với từng lĩnh vực trong danh sách theo dõi ở `kien-thuc/12-theo-doi-thay-doi.md`, tìm:

1. Luật, nghị quyết Quốc hội mới thông qua (kỳ họp gần nhất), nghị quyết Ủy ban Thường vụ Quốc hội.
2. Nghị định, quyết định Thủ tướng, thông tư mới ban hành.
3. Văn bản có hiệu lực trong kỳ tới (các trang thường đăng "văn bản có hiệu lực từ tháng ...").
4. Dự thảo đang lấy ý kiến hoặc trình Quốc hội thuộc danh sách theo dõi.
5. Án lệ mới công bố, văn bản hướng dẫn nghiệp vụ của Tòa án nhân dân tối cao liên quan hợp đồng, sở hữu trí tuệ, kinh doanh thương mại.
6. Thay đổi ở các tổ chức mà mẫu điều khoản dẫn chiếu (quy tắc trọng tài, biểu phí, mẫu đơn của Cục Sở hữu trí tuệ, Cục Bản quyền tác giả).

Dùng nguồn theo thứ bậc ở `kien-thuc/02-nguon-tra-cuu-va-kiem-chung.md`. Mỗi phát hiện ghi: tên, số hiệu, ngày ban hành, ngày hiệu lực, nội dung chính liên quan đến người dùng, nguồn, nhãn tin cậy. Tin báo chí chỉ là tín hiệu; phải tìm đến văn bản hoặc nguồn phân tích uy tín trước khi đưa vào kho.

Lọc theo mức liên quan với hoạt động của người dùng (ghi ở `chu-the/ho-so-chu-the.md`, mục 1; mặc định: giáo dục, coaching, tư vấn, nội dung số, AI, dữ liệu, hợp đồng dịch vụ, sở hữu trí tuệ, doanh nghiệp nhỏ, đầu tư, thuế cá nhân và doanh nghiệp, tranh chấp). Văn bản ngoài phạm vi không đưa vào bản đồ, nhưng có thể ghi một dòng "đã xem, không liên quan" để lần sau không quét lại.

### Bước 3. Kiểm lại bản đồ

- Nhịp tháng: kiểm các dòng có mốc hiệu lực trong kỳ, các dòng bị ảnh hưởng bởi phát hiện ở bước 2, và tối thiểu 5 dòng [Chưa kiểm chứng] được dùng nhiều nhất.
- Nhịp quý: kiểm mọi dòng quá 90 ngày kể từ ngày kiểm chứng.

Với mỗi dòng: còn hiệu lực không, có văn bản sửa đổi, thay thế, hợp nhất mới không, số hiệu và ngày có đúng không. Nâng nhãn khi đã đọc được nguyên văn. Văn bản hết hiệu lực: không xóa dòng ngay mà chuyển xuống mục "Đã hết hiệu lực" cuối bản đồ, ghi ngày hết hiệu lực và văn bản thay thế (hợp đồng cũ vẫn có thể chịu luật cũ).

### Bước 4. Đánh giá tác động

Với mỗi thay đổi, lập dòng trong bảng tác động:

| Thay đổi | File bị ảnh hưởng | Nội dung cần sửa | Mức tác động | Ai duyệt |

- Tìm chỗ bị ảnh hưởng bằng cách tìm số hiệu văn bản cũ, tên luật, từ khóa trong toàn repo (trừ `ho-so-viec/`): `kien-thuc/`, `playbook/`, `mau/`, `skills/`, `HIEN-CHUONG.md`.
- Mức tác động: Cao (làm sai một lập trường playbook, một điều khoản mẫu, một quy trình tuân thủ, hay tạo nghĩa vụ mới cho người dùng có hạn), Trung bình (đổi số liệu, thủ tục, cơ quan), Thấp (chỉ đổi ngày, số hiệu, nhãn).
- Rà hồ sơ việc đang mở và hợp đồng đang hiệu lực (đọc tại chỗ trong `ho-so-viec/`, không sao chép nội dung ra ngoài): liệt kê việc nào có thể bị ảnh hưởng để người dùng xem, ví dụ chính sách dữ liệu đã công bố cần sửa trước một mốc hiệu lực.
- Nghĩa vụ mới có hạn: đề xuất thêm vào lịch tuân thủ.

### Bước 5. Cập nhật

Quy tắc duyệt:

- Tự cập nhật được (không cần chờ người dùng): ngày kiểm chứng, nhãn tin cậy, số hiệu và ngày hiệu lực đã xác minh, thêm dòng văn bản mới vào bản đồ, ghi nhật ký, cập nhật mục theo dõi.
- Cần người dùng duyệt trước khi sửa: lập trường trong playbook, câu chữ điều khoản mẫu, quy trình trong skill, `HIEN-CHUONG.md`. Trình bày đề xuất sửa dạng trước và sau.
- Nếu chạy theo lịch mà người dùng không có mặt: chỉ làm phần tự cập nhật được, để các đề xuất cần duyệt trong báo cáo.

Sau khi sửa, chạy `python3 cong-cu/soi-van-ban.py` trên các file đã sửa.

### Bước 6. Ghi nhật ký và báo cáo

1. Thêm mục mới lên đầu `kien-thuc/nhat-ky-cap-nhat.md` theo khuôn có sẵn trong file.
2. Với mỗi file năng lực đã sửa (kho tri thức, playbook, mẫu), ghi tên file trong mục nhật ký vừa thêm, để lần cập nhật từ bản vẽ sau biết đó là chỗ người dùng đã chủ ý sửa.
3. Viết báo cáo theo `mau/bao-cao-cap-nhat-phap-luat.md`, ngắn, đọc được trong 5 phút: thay đổi quan trọng nhất trước, việc người dùng cần làm, đề xuất chờ duyệt, số căn cứ [Chưa kiểm chứng] còn lại so với kỳ trước.
4. Nếu phiên ghi được file và chạy được git: `git add` các file đã sửa (kiểm `git status` không có gì trong `ho-so-viec/`), commit cục bộ với thông điệp "Cập nhật pháp luật <tháng/quý> <năm>". Không push.

## Chạy theo lịch

Người dùng có thể đặt một tác vụ hẹn giờ (tính năng lịch hoặc tác vụ định kỳ của ứng dụng AI đang dùng) với câu lệnh dưới đây. Lưu ý: thư mục trợ lý nằm trên máy của người dùng, nên lần chạy cần máy đang bật, ứng dụng Claude đang mở và phiên được liên kết với thư mục repo; nếu không, lần chạy vẫn quét và gửi báo cáo, nhưng phần ghi file sẽ chờ lần người dùng mở repo.

Câu lệnh cho nhịp tháng (ngày 1 hằng tháng):

```
Dùng skill phap-ly-cap-nhat trong thư mục trợ lý pháp lý của tôi (<đường dẫn thư mục trợ lý>), chạy nhịp tháng.
Nếu tháng hiện tại là 1, 4, 7 hoặc 10 thì chạy nhịp quý.
Chỉ tự cập nhật phần được phép tự cập nhật; mọi đề xuất sửa playbook, mẫu,
skill để trong báo cáo chờ tôi duyệt. Commit cục bộ, không push.
Gửi tôi báo cáo cập nhật khi xong.
```

## Chỉ số sức khỏe của repo

Mỗi báo cáo ghi ba con số để theo dõi theo thời gian: số dòng bản đồ quá hạn kiểm chứng; số căn cứ [Chưa kiểm chứng] trong `kien-thuc/`; số đề xuất đang chờ người dùng duyệt. Mục tiêu: con số thứ nhất về 0 sau mỗi nhịp quý, con số thứ hai giảm dần qua từng quý.

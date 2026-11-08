# Hướng dẫn dùng trợ lý pháp lý hằng ngày

Tệp này được chép vào trợ lý riêng của bạn. Bạn không cần nhớ tên skill hay lệnh nào: nói việc bằng lời thường, trợ lý chọn đúng quy trình và tự chạy công cụ.

## Một việc đi qua trợ lý thế nào

1. Mở thư mục trợ lý trong ứng dụng AI (Claude Desktop ở chế độ Cowork, Claude Code, ChatGPT chế độ Codex, Antigravity...).
2. Nói việc cần làm, ví dụ: "Rà giúp tôi hợp đồng workshop công ty X gửi", "Tôi muốn đăng ký nhãn hiệu cho khóa học mới", "Học viên đòi hoàn phí, xử lý thế nào". Skill điều phối `phap-ly` tiếp nhận, hỏi những gì còn thiếu (tối đa một lượt câu hỏi, câu nào cũng có phương án đề xuất), phân loại Xanh, Vàng, Đỏ và chuyển sang skill phù hợp.
3. Với việc Vàng, Đỏ (và việc Xanh nếu bạn muốn lưu), trợ lý mở hồ sơ tại `ho-so-viec/<ngày>-<tên-việc>/`. Bạn thả hợp đồng, email, chứng cứ vào thư mục `tai-lieu/` của hồ sơ đó.
4. Đọc đầu ra, quyết định. Đầu ra luôn tách ba phần: pháp luật quy định gì (có nhãn tin cậy và ngày kiểm chứng), trợ lý phân tích gì, và lựa chọn nào thuộc về bạn.
5. Báo trợ lý kết quả cuối (đã ký bản nào, bên kia phản hồi gì) để khép hồ sơ, lập mốc nghĩa vụ sau khi ký và rút bài học.

## Ba mức Xanh, Vàng, Đỏ

| Mức | Dấu hiệu | Trợ lý làm gì |
|---|---|---|
| Xanh | Thường lệ, giá trị dưới ngưỡng bạn đặt, có mẫu hoặc playbook | Làm trọn, bạn duyệt |
| Vàng | Giá trị lớn, điều khoản bất thường, bên kia áp mẫu của họ, tài sản trí tuệ quan trọng, dữ liệu nhạy cảm, khách là cơ quan nhà nước | Làm đầy đủ, đánh dấu chỗ nên hỏi luật sư, bạn quyết |
| Đỏ | Đã hoặc sắp kiện, trọng tài; thanh tra, xử phạt; dấu hiệu hình sự; giao dịch vốn; chuyển nhượng tài sản trí tuệ lõi; vượt ngưỡng; luật nước ngoài; việc không đảo ngược được | Chuẩn bị hồ sơ gửi luật sư, khuyên chưa hành động trước khi có ý kiến luật sư |

Ngưỡng của bạn ghi ở `chu-the/ho-so-chu-the.md`, mục 3.

## Bộ skill

| Skill | Dùng khi |
|---|---|
| `phap-ly` | Điểm vào chung: tiếp nhận, phân loại, mở hồ sơ việc, chọn skill, khép việc |
| `phap-ly-thiet-lap` | Thiết lập lần đầu, đổi hồ sơ chủ thể, lập trường riêng, mẫu hợp đồng riêng, đóng gói lại skill, cập nhật trợ lý |
| `phap-ly-nghien-cuu` | "Pháp luật quy định thế nào", cần căn cứ có kiểm chứng |
| `phap-ly-ra-soat` | Có văn bản cần đọc kỹ trước khi ký hoặc phản hồi |
| `phap-ly-soan-thao` | Soạn mới hợp đồng, phụ lục, điều khoản sử dụng, chính sách hoàn phí, thỏa thuận bảo mật, biên bản |
| `phap-ly-dam-phan` | Chuẩn bị đàm phán theo lợi ích, soạn thư phản hồi, thư đề nghị sửa đổi |
| `phap-ly-so-huu-tri-tue` | Quyền tác giả, nhãn hiệu, framework, cấp phép, đồng sáng tạo, nội dung có AI, bị sao chép |
| `phap-ly-tranh-chap` | Bất đồng, vi phạm, khiếu nại học viên, nợ chưa thanh toán, bị khởi kiện |
| `phap-ly-dau-tu-gop-von` | Góp vốn, nhận đầu tư, cổ phần, hợp tác kinh doanh, vào hội đồng quản trị |
| `phap-ly-tuan-thu` | Mô hình kinh doanh mới, dữ liệu cá nhân, AI, quảng cáo, thương mại điện tử, điều kiện kinh doanh giáo dục, ranh giới khai vấn và trị liệu, lịch tuân thủ |
| `phap-ly-cap-nhat` | Rà văn bản mới, kiểm hiệu lực, nâng nhãn tin cậy, đánh giá tác động |

## Giữ trợ lý đúng luật

Pháp luật thay đổi liên tục, nên trợ lý có nhịp bảo trì riêng:

- Nhịp tháng (ngày 1): nói "rà cập nhật pháp luật tháng này". Trợ lý quét văn bản mới, mốc hiệu lực sắp tới, tiến trình các dự thảo đang theo dõi.
- Nhịp quý (tháng 1, 4, 7, 10): nói "rà quý". Trợ lý kiểm lại mọi văn bản đã quá 90 ngày kể từ lần kiểm chứng, nâng nhãn tin cậy, đề xuất điều chỉnh lập trường và mẫu.
- Mỗi lần rà để lại báo cáo và một mục trong `kien-thuc/nhat-ky-cap-nhat.md`. Thay đổi lập trường luôn chờ bạn duyệt.
- Có thể đặt lịch chạy tự động bằng câu lệnh mẫu trong `skills/phap-ly-cap-nhat/SKILL.md`, mục "Chạy theo lịch".
- Xem nhanh sức khỏe kho tri thức: `python3 cong-cu/kiem-ban-do.py`.

## Cập nhật trợ lý khi bản vẽ có bản mới

Người bảo trì bản vẽ cũng rà pháp luật định kỳ và cải tiến skill, playbook, mẫu. Nói "cập nhật trợ lý": trợ lý lấy bản vẽ mới, kể bạn nghe điều gì mới, rồi chỉ áp những gì bạn đồng ý. Hồ sơ chủ thể, lập trường riêng, bài học và hồ sơ việc của bạn không bao giờ bị ghi đè; tệp năng lực bạn đã chủ ý sửa được giữ nguyên và trợ lý hỏi bạn muốn giữ, lấy bản mới hay trộn.

## Lập trường của riêng bạn

Playbook có sẵn lập trường mặc định cho chuyên gia làm nghề tri thức. Điểm nào bạn muốn khác (phí hủy, thời hạn thanh toán, ghi hình, không cạnh tranh, hoàn phí...), nói với trợ lý; trợ lý ghi vào `chu-the/ho-so-chu-the.md`, mục 4, và mục ấy thắng playbook. Quy tắc riêng khác (thuật ngữ, cách trình bày, thói quen làm việc) ghi ở `CLAUDE.md`, mục "Điều riêng".

## Ngôn ngữ của trợ lý

Mọi đầu ra theo `chuan/ngon-ngu-va-trinh-bay.md`: tiếng Việt tự nhiên (không từ một tiếng cụt ngủn, không dịch sát hợp đồng tiếng Anh), thuật ngữ luật định đúng chữ, thể thức văn bản gửi ra ngoài theo Nghị định 30/2020/NĐ-CP. Soi một văn bản, kể cả tệp Word: `python3 cong-cu/soi-van-ban.py <tệp>`; thêm `--sua` để chuẩn hóa dấu thanh kiểu cũ ở tệp Markdown.

## Thư mục của trợ lý

```
HIEN-CHUONG.md          Hiến chương vận hành (trợ lý đọc trước tiên)
CLAUDE.md, AGENTS.md    Điểm vào; mục "Điều riêng" của bạn
TRO-LY.json             Cấu hình: xưng hô, phiên bản bản vẽ, tiến độ thiết lập
chuan/                  Chuẩn ngôn ngữ và trình bày
skills/                 11 skill
kien-thuc/              Kho tri thức pháp luật có ngày kiểm chứng
playbook/               Lập trường theo loại hợp đồng; bai-hoc-tich-luy.md là bài học của bạn
mau/                    Mẫu đầu ra; mau/hop-dong/ là mẫu hợp đồng đào tạo sạch
chu-the/                Phần riêng: hồ sơ chủ thể, mẫu hợp đồng riêng, sổ tài sản trí tuệ, lịch tuân thủ
ho-so-viec/             Hồ sơ việc thật (không lên git)
cong-cu/                Tạo hồ sơ việc, soi văn bản, kiểm bản đồ văn bản, dựng và cập nhật trợ lý
_skill/                 Gói skill để lưu vào tài khoản AI (tạo lại được)
```

## Bảo mật

Hồ sơ việc và thông tin nhạy cảm nằm trên máy bạn, ngoài git. Không ghi số căn cước, số tài khoản, mật khẩu vào bất kỳ tệp nào. Phần trợ lý đọc trong một phiên được gửi tới dịch vụ AI bạn dùng, theo chính sách của hãng ấy; với chuyện của học viên, khách hàng khai vấn, hãy ẩn danh khi có thể. Muốn sao lưu bằng git: chỉ dùng repo riêng tư.

Trợ lý là công cụ hỗ trợ nghiên cứu và soạn thảo, không phải luật sư hành nghề, và đầu ra của nó không phải ý kiến pháp lý của luật sư.

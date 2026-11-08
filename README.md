# Trợ lý pháp lý cho chuyên gia

**Một phòng pháp chế nội bộ gọn nhẹ chạy trên trợ lý AI của bạn: đọc kỹ trước khi bạn ký, viết rõ để cả hai bên cùng hiểu, và nói thẳng khi nào bạn cần luật sư.**

Trợ lý pháp lý cho chuyên gia là một bộ cách làm việc (gọi là "skill") kèm hiến chương, kho tri thức pháp luật Việt Nam có ngày kiểm chứng, playbook lập trường theo loại hợp đồng, mẫu hợp đồng và công cụ nhỏ, để trợ lý AI của bạn (Claude, ChatGPT, Gemini, Codex...) làm việc như một người pháp chế cẩn thận: hỏi trước khi đoán, kiểm hiệu lực văn bản trước khi khẳng định, gắn nhãn tin cậy cho từng căn cứ, tách bạch luật nói gì với điều nó nghĩ, và để quyết định cuối cùng cho bạn.

Trợ lý dành trước hết cho chuyên gia làm nghề tri thức tại Việt Nam: người đào tạo, giảng viên, nhà khai vấn [coach], nhà tư vấn, diễn giả, tác giả, người làm khóa học, người sáng lập một công ty giáo dục nhỏ. Những người ký hợp đồng mỗi tháng nhưng không có phòng pháp chế, và không muốn trả phí luật sư cho mọi điều khoản hủy lịch.

Bản vẽ miễn phí, mở, dùng lại được theo giấy phép CC BY 4.0 (tài liệu) và MIT (mã). Bạn không cần biết lập trình.

> **Repo này là bản vẽ, không phải nơi làm việc.** Bạn đưa đường dẫn repo cho trợ lý AI của mình; trợ lý đọc bản vẽ, hỏi bạn vài câu, rồi dựng trên máy bạn **một trợ lý pháp lý riêng**, mang hồ sơ, ngưỡng rủi ro và lập trường của chính bạn. Hồ sơ việc của bạn chỉ nằm trên máy bạn. Bạn là trợ lý AI đang đọc repo này: bắt đầu từ [`AGENTS.md`](AGENTS.md).

> **Trợ lý không phải luật sư hành nghề.** Đầu ra của nó là thông tin pháp lý và bản nháp chuyên môn để bạn quyết định, không phải ý kiến pháp lý của luật sư. Với việc lớn, việc có tranh chấp, việc không đảo ngược được, trợ lý sẽ nói rõ là cần luật sư và soạn sẵn hồ sơ để buổi làm việc với luật sư nhanh và rẻ hơn.

Mục lục: [Vì sao có trợ lý này](#vì-sao-có-trợ-lý-này) · [Tinh thần](#tinh-thần) · [Bắt đầu bằng một câu](#bắt-đầu-bằng-một-câu) · [Bạn sẽ có gì trên máy](#bạn-sẽ-có-gì-trên-máy) · [11 skill](#11-skill) · [Một buổi làm việc mẫu](#một-buổi-làm-việc-mẫu-minh-họa) · [Kho tri thức và nhịp cập nhật](#kho-tri-thức-và-nhịp-cập-nhật) · [Trợ lý không làm gì](#trợ-lý-không-làm-gì) · [Câu hỏi thường gặp](#câu-hỏi-thường-gặp) · [Ghi công và giấy phép](#ghi-công-và-giấy-phép)

## Vì sao có trợ lý này

Chuyên gia làm nghề tri thức ký nhiều hợp đồng nhỏ mà ít ai đọc kỹ: hợp đồng đào tạo doanh nghiệp gửi sang, thỏa thuận đồng tổ chức khóa học, hợp đồng xuất bản, điều khoản ghi hình buổi nói chuyện, chính sách hoàn phí cho học viên. Rủi ro thật hiếm khi nằm ở điều luật phức tạp; nó nằm ở những câu nghe vô hại: "Bên A được toàn quyền sử dụng bản ghi", "Bên B cam kết không làm việc với các công ty trong ngành", "phí không hoàn lại trong mọi trường hợp".

AI tổng quát trả lời câu hỏi pháp lý rất trơn, nhưng hay mắc ba lỗi nguy hiểm: trích số điều luật từ trí nhớ (và pháp luật Việt Nam năm 2025, 2026 đổi rất nhiều: Luật Bảo vệ dữ liệu cá nhân, Luật Trí tuệ nhân tạo, Luật Thương mại điện tử, Luật Đầu tư 2025, Luật Sở hữu trí tuệ sửa đổi, sắp xếp lại tòa án và địa giới hành chính); viết hợp đồng bằng lối dịch sát từ hợp đồng tiếng Anh ("Bên B sẽ bàn giao", "nỗ lực tốt nhất") mà trong tiếng Việt pháp lý có thể đổi nghĩa vụ; và không biết bạn là ai, ký với tư cách nào, chấp nhận rủi ro tới đâu.

Bản vẽ này chưng cất từ phòng pháp chế riêng mà tác giả Lương Dũng Nhân dựng cho công việc đào tạo, khai vấn, tư vấn của mình, đã chạy trên hợp đồng thật, rồi được khử định danh để chia sẻ.

## Tinh thần

**Bảo vệ bạn chắc chắn.** Mỗi văn bản bạn ký phải giúp bạn ngủ yên: quyền lợi rõ, rủi ro được gọi tên, nghĩa vụ làm được, đường lui có sẵn.

**Công bằng với bên kia.** Một điều khoản chỉ có lợi cho bạn vì bên kia không đọc kỹ là một rủi ro trì hoãn, không phải một thắng lợi. Trợ lý luôn áp phép thử đổi vai: "Nếu ở vị trí bên kia, mình có ký điều khoản này không?"

**Hợp đồng là cấu trúc của một mối quan hệ.** Nó ghi lại cách hai bên hợp tác khi mọi chuyện suôn sẻ, và cách hai bên đối xử với nhau khi có chuyện. Viết sao cho cả hai bên hiểu được mà không cần luật sư đọc hộ.

**Con người trước, quy trình sau.** Với bên yếu thế hơn (học viên cá nhân, cộng tác viên trẻ), trợ lý nghiêng về minh bạch, ngôn ngữ dễ hiểu và cơ chế khiếu nại tử tế. Trợ lý không soạn văn bản giả mạo, giả cách, thư đe dọa, hay điều khoản lừa người tiêu dùng, dù được yêu cầu.

## Bắt đầu bằng một câu

Mở một ứng dụng AI làm việc được với thư mục trên máy (khuyên dùng Claude Desktop ở chế độ Cowork; Claude Code, ChatGPT desktop chế độ Codex, Google Antigravity cũng được), gắn một thư mục trống tên `Tro ly phap ly`, rồi nói:

> Đọc bản vẽ ở https://github.com/wincreator3012/tro-ly-phap-ly-cho-chuyen-gia (bắt đầu từ AGENTS.md) rồi dựng trợ lý pháp lý riêng cho tôi trong thư mục Tro ly phap ly.

Trợ lý dựng trong vài phút, rồi cùng bạn: điền hồ sơ chủ thể qua ba lượt hỏi ngắn (bạn là ai, ký với tư cách nào, chấp nhận rủi ro tới đâu); chọn giữ hay đổi vài lập trường mặc định; làm bản mẫu hợp đồng đào tạo mang thông tin của bạn; đóng gói bộ skill để lưu vào tài khoản AI; giới thiệu trợ lý và cùng bạn rà hợp đồng đầu tiên. Tổng cộng khoảng 30-50 phút.

Từng bước cho người mới hoàn toàn, kể cả cài ứng dụng: **[BAT-DAU.md](BAT-DAU.md)**.

**Chỉ dùng khung chat** (Claude trên web, ChatGPT, Gemini), chưa có ứng dụng làm việc với thư mục: vẫn dùng được theo **đường nhẹ** trong `BAT-DAU.md`, với các gói skill chung trong `dong-goi/`. Trợ lý vẫn tiếp nhận, phân loại, kiểm chứng bằng tìm kiếm web và giữ các lằn ranh; nhưng thiếu kho tri thức, playbook và mẫu hợp đồng đi kèm.

Tên các nút, menu và gói tài khoản do từng hãng đặt và có thể đổi; khi khác với mô tả ở đây, trợ lý sẽ theo trang hướng dẫn chính thức của hãng.

## Bạn sẽ có gì trên máy

```
Documents/
└── Tro ly phap ly/
    ├── tro-ly-phap-ly/     trợ lý riêng của bạn: hiến chương, skill, kho tri thức, playbook, mẫu, công cụ;
    │                       hồ sơ chủ thể và lập trường riêng (chu-the/); hồ sơ việc (ho-so-viec/, ngoài git)
    └── _ban-ve/            bản vẽ lấy từ repo này, chỉ để đọc và làm mốc khi cập nhật
```

Trợ lý dựng xong không tự đổi sau lưng bạn. Khi bản vẽ có bản mới (luật mới, playbook tốt hơn), bạn nói "cập nhật trợ lý"; trợ lý đọc nhật ký thay đổi, kể bạn nghe điều gì mới, rồi áp những gì bạn đồng ý. Hồ sơ, lập trường riêng và hồ sơ việc của bạn không bao giờ bị ghi đè.

## 11 skill

Bạn không cần nhớ tên skill: nói việc bằng lời thường, trợ lý chọn đúng.

| Bạn đang có | Skill |
|---|---|
| Bất cứ việc pháp lý nào: trợ lý tiếp nhận, hỏi 7 dữ kiện, phân loại Xanh, Vàng, Đỏ, mở hồ sơ, chuyển việc | `phap-ly` |
| Lần đầu dùng, đổi hồ sơ, đóng gói skill, cập nhật trợ lý | `phap-ly-thiet-lap` |
| Câu hỏi "luật quy định thế nào" | `phap-ly-nghien-cuu`: tra cứu theo thứ bậc nguồn, trích nguyên văn, kiểm hiệu lực, ghi nhớ có nhãn tin cậy |
| Một hợp đồng bên kia gửi | `phap-ly-ra-soat`: đối chiếu playbook từng điều (Chuẩn, Chấp nhận được, Dừng lại), điều thiếu, bảng đề xuất sửa kèm lý do công bằng cho cả hai bên |
| Cần một văn bản mới | `phap-ly-soan-thao`: hợp đồng, phụ lục, điều khoản sử dụng, chính sách hoàn phí, thỏa thuận bảo mật, biên bản nghiệm thu, thanh lý |
| Phải trả lời bên kia | `phap-ly-dam-phan`: đàm phán theo lợi ích (Fisher, Ury, Patton), thư phản hồi tôn trọng và chắc chắn |
| Framework, khóa học, sách, thương hiệu | `phap-ly-so-huu-tri-tue`: kiểm kê, bảo hộ, cấp phép, đồng sáng tạo, nội dung có AI, bị sao chép |
| Bất đồng, nợ, khiếu nại, bị kiện | `phap-ly-tranh-chap`: đánh giá vụ việc, thời hiệu, thang đối thoại, hòa giải, trọng tài, tòa án |
| Góp vốn, nhận đầu tư, vào hội đồng quản trị | `phap-ly-dau-tu-gop-von`: mặc định mức Đỏ, chuẩn bị kỹ để làm việc với luật sư hiệu quả |
| Mô hình kinh doanh mới | `phap-ly-tuan-thu`: điều kiện kinh doanh giáo dục, người tiêu dùng, thương mại điện tử, quảng cáo, dữ liệu cá nhân, Luật Trí tuệ nhân tạo, ranh giới khai vấn và trị liệu, lịch tuân thủ |
| Luật đổi | `phap-ly-cap-nhat`: rà văn bản mới theo nhịp tháng và quý, kiểm hiệu lực, đánh giá tác động lên playbook và hợp đồng đang hiệu lực |

## Một buổi làm việc mẫu (minh họa)

Đoạn dưới đây là minh họa do bản vẽ soạn để bạn hình dung cách làm việc, không phải lời của một người dùng thật.

> **Người dùng:** Công ty X gửi hợp đồng workshop 2 ngày, rà giúp tôi.
>
> **Trợ lý:** Tôi đã đọc trọn hợp đồng. Trước khi rà, cho tôi hỏi 3 điều: bạn ký với tư cách cá nhân hay qua công ty của bạn? Bạn có định cho phép họ ghi hình không? Có hạn ký nào gấp không? *(Mỗi câu kèm một phương án đề xuất lấy từ hồ sơ của người dùng.)*
>
> *(Sau khi người dùng trả lời)*
>
> **Trợ lý:** Kết luận ngắn: ký được sau khi sửa 3 điểm; mức Vàng vì có điều khoản ghi hình bất thường. Điều 7 cho Bên A "toàn quyền sử dụng bản ghi cho mục đích đào tạo nội bộ": câu này mở đường dùng bản ghi để đào tạo nhân sự mới thay cho việc mời bạn dạy lại, tức là khai thác thương mại mà không có phí cấp phép. Đề xuất: giới hạn cho người đã tham dự ôn lại; muốn dùng rộng hơn thì làm phụ lục cấp phép. Lý do gửi bên kia: ... *(bảng đối chiếu từng điều, căn cứ có nhãn tin cậy, câu chữ đề xuất)*

Từ đây, người dùng có thể nhờ soạn thư phản hồi (`phap-ly-dam-phan`); khi việc khép lại, trợ lý hỏi một câu và rút bài học, đã ẩn danh, vào sổ bài học của người dùng.

## Kho tri thức và nhịp cập nhật

- **Kho tri thức** (`kien-thuc/`): 12 chủ đề, từ bản đồ văn bản pháp luật, nguồn tra cứu và cách kiểm chứng, hệ thống cơ quan, nguyên lý hợp đồng, tới sở hữu trí tuệ, dữ liệu cá nhân và AI, kinh doanh đào tạo và người tiêu dùng, doanh nghiệp và góp vốn, lao động, cộng tác viên và thuế, giải quyết tranh chấp, yếu tố quốc tế, theo dõi thay đổi. Mỗi văn bản có ngày kiểm chứng và một trong ba nhãn: [Đã đối chiếu văn bản gốc], [Theo nguồn thứ cấp], [Chưa kiểm chứng].
- **Playbook** (`playbook/`): lập trường theo loại hợp đồng (dịch vụ đào tạo, diễn giả, cố vấn; học viên cá nhân và khóa trực tuyến; đồng tổ chức, chia doanh thu; cấp phép, xuất bản, đồng sáng tạo; cộng tác viên; bảo mật; góp vốn, cổ đông), mỗi điều khoản ba mức Chuẩn, Chấp nhận được, Dừng lại.
- **Mẫu** (`mau/`): phiếu tiếp nhận, ghi nhớ nghiên cứu, báo cáo rà soát, bảng đối chiếu sửa đổi, thư đàm phán, thư yêu cầu, checklist thẩm định đối tác, sổ tài sản trí tuệ, lịch tuân thủ, hồ sơ gửi luật sư, báo cáo cập nhật pháp luật; và 2 mẫu hợp đồng đào tạo (ký cá nhân, ký qua công ty).
- **Nhịp cập nhật**: trợ lý của bạn rà pháp luật theo nhịp tháng và quý (`phap-ly-cap-nhat`); người bảo trì bản vẽ cũng rà và phát hành bản mới, ghi trong `CHANGELOG.md`.

Kho tri thức là điểm xuất phát đã kiểm chứng tới ngày ghi trong từng tệp, không phải nguồn luật chính thức. Trước khi dựa vào một căn cứ cho quyết định quan trọng, trợ lý kiểm lại hiệu lực; bạn cũng nên làm vậy.

## Trợ lý không làm gì

- Không thay luật sư hành nghề trong các việc mức Đỏ, không đại diện bạn trước cơ quan nhà nước hay tòa án, không khẳng định chắc chắn kết quả của một vụ tranh chấp.
- Không soạn văn bản giả mạo, lùi ngày, hợp đồng giả cách, hướng dẫn trốn thuế; không soạn thư đe dọa, bôi nhọ; không soạn điều khoản lừa người tiêu dùng.
- Không thu thập, tổng hợp thông tin cá nhân của một người cụ thể để gây áp lực hay theo dõi họ.
- Không đưa ra số liệu kê khai thuế cụ thể thay kế toán.
- Không trích số điều luật từ trí nhớ mà không đánh dấu [Chưa kiểm chứng].

Giới hạn hiện tại: kho tri thức tập trung vào pháp luật Việt Nam và hoạt động của chuyên gia làm nghề tri thức; yếu tố quốc tế mới ở mức nhận diện rủi ro. Kiểm chứng cần trợ lý có công cụ tìm kiếm web; một số trang cơ sở dữ liệu pháp luật có thể chặn công cụ đọc web, khi ấy trợ lý nói rõ và nhờ bạn mở trang hoặc dán văn bản.

## Câu hỏi thường gặp

**Tôi không rành công nghệ, có dùng được không?**
Được. Bạn tạo một thư mục, gắn vào ứng dụng AI, dán một câu; trợ lý làm phần còn lại và hỏi bạn bằng lời thường. `BAT-DAU.md` đi từng bước, kể cả cài ứng dụng.

**Có mất phí không?**
Bản vẽ miễn phí. Bạn cần tài khoản của một trợ lý AI; chế độ làm việc với thư mục (như Cowork của Claude) và tính năng Skills tùy gói tài khoản của từng hãng.

**Hợp đồng và hồ sơ của tôi đi đâu?**
Repo này không thu thập gì. Trợ lý, hồ sơ chủ thể và hồ sơ việc nằm trên máy bạn; hồ sơ việc được loại khỏi git. Phần trợ lý đọc trong một phiên được gửi tới dịch vụ AI bạn dùng, theo chính sách của hãng ấy. Với hợp đồng có dữ liệu cá nhân của học viên, khách hàng, hãy cân nhắc ẩn danh trước khi đưa vào.

**Luật thay đổi thì sao?**
Mọi căn cứ có ngày kiểm chứng. Trợ lý nhắc khi lần rà gần nhất đã quá 45 ngày, và kiểm lại văn bản đã quá 90 ngày trước khi dựa vào. Bản vẽ phát hành bản mới khi có thay đổi đáng kể; bạn nói "cập nhật trợ lý" để nhận.

**Lập trường trong playbook có hợp với tôi không?**
Playbook là mặc định đã thử trên hợp đồng thật của một chuyên gia đào tạo, khai vấn, tư vấn. Lúc thiết lập, trợ lý đưa bạn xem vài điểm hay khác nhau nhất (phí hủy, thanh toán, ghi hình, không cạnh tranh, hoàn phí) để giữ hay đổi; về sau, mỗi bài học từ việc thật làm playbook sát với bạn hơn.

**Tôi làm nghề khác (thiết kế, lập trình tự do, nhiếp ảnh) có dùng được không?**
Phần lớn hiến chương, quy trình, kho tri thức về hợp đồng, sở hữu trí tuệ, tranh chấp, dữ liệu cá nhân vẫn dùng được. Playbook và mẫu hợp đồng thiên về đào tạo, khai vấn, tư vấn; bạn ghi lập trường riêng trong hồ sơ, hoặc góp ý để bản vẽ có thêm playbook cho nghề của bạn.

**Tôi muốn sửa skill cho hợp với mình thì sao?**
Cứ sửa trong trợ lý của bạn, rồi nhờ trợ lý "đóng gói lại skill". Khi cập nhật, tệp bạn đã sửa được giữ nguyên và trợ lý hỏi bạn muốn giữ, lấy bản mới hay trộn. Hãy giữ ghi công tác giả theo giấy phép CC BY 4.0.

**Hợp đồng soạn từ mẫu có phải ghi công bản vẽ không?**
Không. Văn bản bạn soạn RA bằng trợ lý (hợp đồng, thư, chính sách) là của bạn. Ghi công chỉ cần khi bạn chia sẻ lại chính bản vẽ hay tài liệu của bản vẽ (`GHI-CONG.md`).

## Bản vẽ gồm gì

| Tệp, thư mục | Nội dung |
|---|---|
| `README.md`, `BAT-DAU.md` | Cho người dùng: giới thiệu, bắt đầu từng bước (cả đường nhẹ) |
| `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` | Cửa vào cho trợ lý AI (hai tệp sau trỏ về `AGENTS.md`) |
| `DUNG-TRO-LY.md` | Quy trình dựng, cập nhật, gỡ rối (cho trợ lý AI) |
| `BAN-DUNG.json` | Danh mục từng tệp: chép vào trợ lý, mẫu tạo phần riêng, hay chỉ ở bản vẽ; vân tay sha256 |
| `HIEN-CHUONG.md` | Hiến chương vận hành: tinh thần, kỷ luật kiểm chứng, lằn ranh, phân loại Xanh, Vàng, Đỏ, bảo mật, quy ước viết |
| `HUONG-DAN.md` | Cách dùng trợ lý hằng ngày (được chép vào trợ lý) |
| `skills/` | 11 skill; `skills/README.md` giải thích skill và cách lưu vào tài khoản |
| `chuan/` | Chuẩn ngôn ngữ và trình bày văn bản pháp lý tiếng Việt |
| `kien-thuc/`, `playbook/`, `mau/` | Kho tri thức có ngày kiểm chứng, lập trường theo loại hợp đồng, mẫu đầu ra và mẫu hợp đồng |
| `chu-the/`, `ho-so-viec/` | Tệp mẫu hồ sơ chủ thể và hướng dẫn hồ sơ việc (dữ liệu thật chỉ nằm trong trợ lý riêng) |
| `mau-tro-ly/` | Mẫu tệp điểm vào và cấu hình của trợ lý dựng ra |
| `cong-cu/` | Công cụ Python, chỉ dùng thư viện chuẩn: dựng và cập nhật trợ lý, đóng gói skill, tạo hồ sơ việc, soi văn bản, kiểm bản đồ văn bản |
| `dong-goi/` | Gói skill chung cho đường nhẹ |
| `docs/` | `BAI-HOC.md` (bài học chung), `DONG-GOP.md` (cho người bảo trì) |
| `CHANGELOG.md` | Nhật ký thay đổi: trợ lý đọc khi cập nhật trợ lý của bạn |
| `GHI-CONG.md`, `LICENSE`, `LICENSE-TAI-LIEU.md` | Ghi công và giấy phép |

## Góp ý

Nếu bạn dùng trợ lý và thấy một chỗ chưa ổn (một căn cứ đã hết hiệu lực, một lập trường không hợp thực tế nghề, một câu chữ hợp đồng khó hiểu, một hướng dẫn khó theo), hãy mở một issue trên GitHub, kèm đoạn trước và sau nếu có, **đã ẩn danh hoàn toàn**: không tên đối tác, không số tiền nhận diện được, không dữ liệu cá nhân của ai. Bài học chung được ghi vào `docs/BAI-HOC.md`.

## Ghi công và giấy phép

Thiết kế và nội dung: Thạc sĩ Lương Dũng Nhân (M.Ed, PCC, Humanistic AI Practitioner), soạn cùng Claude của Anthropic. Chuẩn ngôn ngữ dựng trên Xưởng viết AI cùng tác giả. Các khung và công trình của tác giả khác (ví dụ đàm phán theo nguyên tắc của Roger Fisher, William Ury và Bruce Patton) được ghi công ngay tại chỗ dùng. Mô hình tổ chức "bản vẽ dựng trợ lý riêng" dùng chung với các xưởng viết, xưởng web, xưởng phim, xưởng thiết kế cùng tác giả.

Tài liệu theo giấy phép CC BY 4.0 (`LICENSE-TAI-LIEU.md`); mã trong `cong-cu/` theo giấy phép MIT (`LICENSE`). Bạn được dùng lại, chỉnh sửa, kể cả cho mục đích thương mại, miễn là ghi công. Cách ghi gợi ý ở `GHI-CONG.md`:

> Lương Dũng Nhân. (2026). *Trợ lý pháp lý cho chuyên gia* [Bộ skill, hiến chương và kho tri thức pháp lý cho trợ lý AI]. https://github.com/wincreator3012/tro-ly-phap-ly-cho-chuyen-gia

Nội dung trong repo là công cụ hỗ trợ nghiên cứu và soạn thảo, không phải ý kiến pháp lý của luật sư.

Cập nhật lần cuối: 09/11/2026.

## In English

*Trợ lý pháp lý cho chuyên gia* (Legal Assistant for Experts) is a free, open blueprint that turns an AI assistant (Claude, ChatGPT, Gemini, Codex) into a small in-house legal desk for independent knowledge professionals in Vietnam: trainers, coaches, consultants, speakers, authors and founders of small education businesses. Give the repository link to an assistant that can work with folders on your computer, and it builds a private assistant there: an operating charter, 11 skills (intake and triage, research, contract review, drafting, negotiation, intellectual property, disputes, investment, compliance, periodic legal updates, setup), a Vietnamese law knowledge base with verification dates and confidence labels, negotiation playbooks, output templates and two training contract templates. Your matters and profile stay on your machine. It is not a lawyer and does not give legal opinions; for high-stakes matters it prepares a brief for one. The content is in Vietnamese. Method and content by Luong Dung Nhan (M.Ed, PCC), licensed CC BY 4.0 (documents) and MIT (code).

## Lời cuối

Một hợp đồng tốt khiến cả hai bên muốn hợp tác lâu hơn. Lần tới khi bạn ký một thỏa thuận, điều gì sẽ cho bạn biết bên kia cũng thấy mình được đối xử công bằng?

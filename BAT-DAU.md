# Bắt đầu: để trợ lý AI dựng trợ lý pháp lý cho bạn, từng bước

Tài liệu này dành cho cả người chưa từng dùng AI làm việc với tệp trên máy. Đọc hết một lần khoảng 10 phút; làm theo khoảng 30-50 phút, phần lớn là trả lời vài câu hỏi về công việc của bạn. Bạn không phải gõ lệnh nào: trợ lý AI lấy bản vẽ về rồi dựng trợ lý trên máy bạn. Giới thiệu chung ở [README.md](README.md).

Có hai đường:

- **Đường chính: dựng trợ lý trên máy** (bước 1 tới 6). Bạn có trợ lý riêng với hồ sơ chủ thể, lập trường, mẫu hợp đồng, kho tri thức, hồ sơ việc nằm trên máy, và bộ skill mang cấu hình của bạn. Cần một ứng dụng AI làm việc được với thư mục trên máy.
- **Đường nhẹ: chỉ dùng khung chat** (mục cuối). Dùng các gói skill chung trên Claude, ChatGPT hay Gemini. Hợp khi bạn muốn thử trước, hoặc chưa có ứng dụng làm việc với thư mục.

## Trước khi bắt đầu, bạn cần

- **Một máy tính** Mac hoặc Windows 10/11.
- **Một ứng dụng AI làm việc được với thư mục trên máy** (bước 1), có công cụ tìm kiếm web để kiểm chứng căn cứ pháp luật.
- **Mạng ổn định** trong vài phút dựng (bản vẽ dung lượng nhỏ).
- **Vài thông tin về công việc của bạn**: bạn ký hợp đồng với tư cách cá nhân hay qua công ty; tên công ty nếu có; mức giá trị hợp đồng mà bạn muốn có luật sư xem. Không cần số căn cước hay số tài khoản: trợ lý không bao giờ hỏi những thứ ấy.
- **Một hợp đồng đang có** để thử ở bước 5 (nên có, không bắt buộc).

## Bước 1: cài một ứng dụng AI làm việc được với thư mục

Bản vẽ được viết và kiểm chứng trên Claude; các ứng dụng khác dùng được vì trợ lý là tệp chữ và công cụ Python thông thường. Chọn MỘT:

| Ứng dụng | Hợp với ai | Ghi chú |
|---|---|---|
| **Claude Desktop** (chế độ Cowork) | người mới, muốn ít trục trặc nhất | Khuyên dùng. Tải ở [claude.ai/download](https://claude.ai/download); Cowork cần gói trả phí. Claude làm việc với thư mục bạn gắn vào |
| **ChatGPT desktop** (chế độ Codex) | người đang dùng ChatGPT | Mở một thư mục rồi làm việc trong đó |
| **Google Antigravity** | người quen sản phẩm Google | Mở thư mục làm dự án |
| **Claude Code**, Codex CLI, Cursor | người quen dòng lệnh | Chạy thẳng trên máy |

Giá, gói và tên gọi của các ứng dụng AI thay đổi nhanh; xem trang chính thức của từng hãng trước khi đăng ký.

## Bước 2: tạo thư mục làm việc và gắn vào ứng dụng

1. Mở thư mục tài liệu [Documents], tạo một thư mục mới, để trống, tên **Tro ly phap ly**. Đây là nơi chứa trợ lý của bạn và mọi hồ sơ việc.
2. Gắn thư mục đó vào ứng dụng:
   - **Claude Desktop, Cowork**: bắt đầu một phiên mới, bấm nút thêm thư mục [Add folder], chọn `Tro ly phap ly`. Lần đầu, máy có thể hỏi quyền truy cập thư mục: bấm cho phép.
   - **ChatGPT desktop, Codex**: chọn mở thư mục [Open folder] hoặc tạo dự án từ thư mục `Tro ly phap ly`.
   - **Antigravity, Cursor**: vào menu tệp [File], chọn mở thư mục [Open Folder], chọn `Tro ly phap ly`.

Từ lúc này trợ lý đọc và ghi được trong thư mục đó, và chỉ thư mục đó.

Một điều nên nghĩ trước: hồ sơ việc (hợp đồng, email, chứng cứ) sẽ nằm trong thư mục này. Đặt `Tro ly phap ly` trong iCloud Drive, Google Drive, Dropbox hay OneDrive thì dùng được trên nhiều máy, nhưng hồ sơ cũng được đồng bộ lên dịch vụ ấy. Với hồ sơ pháp lý, nhiều người chọn để ở thư mục không đồng bộ và tự sao lưu bằng ổ mã hóa. Đặt ở đâu là quyết định của bạn.

## Bước 3: nói câu đầu tiên

Gõ vào khung chat:

> Đọc bản vẽ ở https://github.com/wincreator3012/tro-ly-phap-ly-cho-chuyen-gia (bắt đầu từ AGENTS.md) rồi dựng trợ lý pháp lý riêng cho tôi trong thư mục Tro ly phap ly.

Nếu ứng dụng của bạn không tải được từ mạng, trợ lý sẽ nhờ bạn: trên trang GitHub của bản vẽ bấm nút xanh **Code**, chọn **Download ZIP**, giải nén (Mac: bấm đúp tệp ZIP; Windows: chuột phải, chọn "Extract All"), đổi tên thư mục `tro-ly-phap-ly-cho-chuyen-gia-main` thành `tro-ly-phap-ly-cho-chuyen-gia`, rồi đặt vào `Tro ly phap ly/_ban-ve/`.

## Bước 4: chuyện gì sẽ xảy ra

**Vài câu hỏi đầu (2 phút).** Trợ lý hỏi một lượt: dùng thư mục nào, gọi bạn là gì, bạn dùng ứng dụng AI nào hằng ngày, việc pháp lý nào bạn hay gặp nhất.

**Dựng trợ lý (vài phút, bạn chỉ chờ).** Trợ lý lấy bản vẽ về `Tro ly phap ly/_ban-ve/` (chỉ để đọc), rồi chép phần năng lực (hiến chương, skill, kho tri thức, playbook, mẫu, công cụ) vào `Tro ly phap ly/tro-ly-phap-ly/`, tự kiểm từng tệp khớp bản vẽ. Máy thiếu Python thì trợ lý hướng dẫn cài (mục "Nếu máy chưa có Python").

**Hồ sơ của bạn (10-15 phút).** Trợ lý hỏi ba lượt ngắn, mỗi lượt vài câu có sẵn phương án:

- Bạn là ai: cách trợ lý gọi bạn, nghề và hoạt động chính, thị trường, một hai giá trị nghề nghiệp bạn muốn hợp đồng giữ gìn.
- Bạn ký với tư cách nào: cá nhân, qua công ty, hay cả hai; mỗi công ty là loại hình gì, bạn giữ vai trò gì; thương hiệu, framework quan trọng; người cùng bạn phát triển chương trình, sách.
- Bạn chấp nhận rủi ro tới đâu: ngưỡng phải có luật sư xem, ngưỡng tự quyết, điều không bao giờ chấp nhận, luật sư và kế toán đồng hành (để trống được).

Trả lời tới đâu trợ lý ghi tới đó vào `tro-ly-phap-ly/chu-the/ho-so-chu-the.md`. Câu nào chưa biết thì để sau; trợ lý không đoán thay và sẽ hỏi lại khi một việc thật cần đến.

**Lập trường riêng (5 phút).** Trợ lý đưa bạn xem 5 điểm mặc định hay khác nhau nhất giữa các chuyên gia (phí hủy, thanh toán, ghi hình, không cạnh tranh, hoàn phí học viên); bạn giữ hay đổi.

**Mẫu hợp đồng riêng (5-10 phút, nếu bạn nhận đào tạo cho tổ chức).** Trợ lý làm bản mẫu hợp đồng đào tạo mang thông tin của bạn từ 2 mẫu có sẵn (ký cá nhân, ký qua công ty).

**Bộ skill riêng (5-10 phút).** Skill là cách làm việc đã kiểm chứng viết thành tệp chữ, để trợ lý mở ra đúng lúc, như sổ tay nghề của một người pháp chế. Trợ lý đóng gói 11 skill mang cách gọi bạn và đường dẫn trợ lý vào `tro-ly-phap-ly/_skill/` (không mang hồ sơ nào), rồi dẫn bạn lưu vào tài khoản AI. Bạn tự bấm tải lên; trợ lý chỉ từng bước. Không muốn lưu lúc này cũng được: trợ lý vẫn chạy đủ khi bạn mở thư mục.

**Giới thiệu trợ lý (5 phút).** Ba mức Xanh, Vàng, Đỏ theo ngưỡng của bạn; nhịp cập nhật pháp luật; những gì trợ lý không làm.

Kết quả trên máy bạn:

```
Documents/
└── Tro ly phap ly/
    ├── tro-ly-phap-ly/    trợ lý của bạn (năng lực + hồ sơ của bạn; ho-so-viec/ là hồ sơ từng việc)
    └── _ban-ve/           bản vẽ, chỉ để đọc
```

## Bước 5: việc đầu tiên

Chọn một việc thật, nhỏ, sắp phải làm. Thả hợp đồng vào thư mục trợ lý (hoặc đính kèm vào khung chat) và nói một câu đủ ba ý: việc gì, với ai, hạn khi nào. Ví dụ (do bản vẽ soạn để minh họa):

> Công ty X gửi hợp đồng workshop 2 ngày vào tháng sau, hạn ký thứ Sáu. Rà giúp tôi.

> Một học viên đòi hoàn phí sau 3 buổi học. Chính sách của tôi ở đây, xử lý thế nào cho đúng và tử tế?

> Tôi muốn đăng ký nhãn hiệu cho tên chương trình mới. Cần làm gì, mất bao lâu?

Câu mở đầu cho từng việc, nhịp cập nhật pháp luật, gỡ rối: `HUONG-DAN.md` trong trợ lý của bạn.

## Bước 6: những điều nên biết

- **Trợ lý không phải luật sư.** Với việc mức Đỏ (tranh chấp, thanh tra, giao dịch vốn, vượt ngưỡng của bạn, việc không đảo ngược được), trợ lý soạn sẵn hồ sơ gửi luật sư và khuyên bạn chưa hành động trước khi có ý kiến luật sư.
- **Trợ lý là của bạn, không nối với bản vẽ.** Không có gì tự đổi sau lưng bạn. Muốn nhận bản mới: nói "cập nhật trợ lý"; trợ lý kể bạn nghe điều gì mới rồi mới áp. Hồ sơ, lập trường riêng và hồ sơ việc của bạn không bị đụng tới.
- **Mỗi phiên làm việc, gắn thư mục `Tro ly phap ly`** (hoặc chính thư mục `tro-ly-phap-ly`) để trợ lý đọc được hồ sơ và ghi được đầu ra.
- **Thông tin nhạy cảm là của bạn.** Trợ lý không bao giờ hỏi mật khẩu, mã xác thực, số căn cước, số tài khoản. Ai hỏi những thứ đó, kể cả một trợ lý AI, thì đừng đưa.
- **Đổi hồ sơ, lập trường**: nói "cập nhật hồ sơ chủ thể" hoặc "từ nay, phí hủy của tôi là...". Đã lưu skill lên tài khoản thì nhờ "đóng gói lại skill" khi trợ lý được cập nhật.
- **Giữ nhịp cập nhật pháp luật**: đầu mỗi tháng nói "rà cập nhật pháp luật tháng này", hoặc nhờ trợ lý đặt lịch nếu ứng dụng của bạn có tính năng tác vụ định kỳ.

## Nếu máy chưa có Python

- **Mac**: Python 3 thường có sẵn. Chưa có thì trợ lý hướng dẫn cài, hoặc tải bản cài từ [python.org](https://www.python.org/downloads/).
- **Windows**: tải bản cài từ [python.org](https://www.python.org/downloads/), lúc cài nhớ đánh dấu ô "Add python.exe to PATH". Trên Windows, lệnh là `py` thay cho `python3`.

Claude Cowork có sẵn Python trong máy làm việc của nó; bạn thường không cần cài gì.

## Khi có gì không chạy

Nói với trợ lý điều bạn thấy, bằng lời thường ("nó dừng ở chỗ chép tệp", "không thấy thư mục hồ sơ"). Ba việc bạn tự kiểm được: thư mục `Tro ly phap ly` còn được gắn vào ứng dụng không; máy còn mạng không; ổ đĩa còn chỗ không. Muốn trợ lý tự kiểm toàn bộ, nói: "kiểm tra trợ lý".

---

## Đường nhẹ: chỉ dùng khung chat

Khi bạn chưa có ứng dụng làm việc được với thư mục, hoặc muốn thử trước. Bạn có các skill trong khung chat; chưa có kho tri thức, playbook, mẫu hợp đồng, hồ sơ chủ thể trên máy. Trợ lý vẫn tiếp nhận, phân loại, kiểm chứng bằng tìm kiếm web và giữ các lằn ranh, nhưng sẽ nói rõ điều còn thiếu và khuyên dựng trợ lý đầy đủ cho việc Vàng, Đỏ.

Lấy các tệp: trên trang GitHub của bản vẽ, mở thư mục `dong-goi/`, bấm vào từng tệp cần dùng rồi bấm nút tải tệp gốc [Download raw file]. Hoặc nhờ trợ lý có duyệt web lấy giúp. Tên nút trên GitHub có thể đổi theo thời gian.

### Claude, dùng Skills

Skills có ở một số gói tài khoản và có thể cần bật tính năng chạy mã; xem trang hướng dẫn hiện hành của Anthropic (support.claude.com, mục Skills) trước khi làm.

1. Mở cài đặt [Settings], tìm mục tính năng [Capabilities] và trang skill [Skills]; bật tính năng nếu chưa bật.
2. Bấm tải skill lên, chọn một tệp `.zip` trong `dong-goi/`. Lặp lại cho từng skill; tối thiểu nên có `phap-ly.zip`, `phap-ly-ra-soat.zip`, `phap-ly-soan-thao.zip`, `phap-ly-dam-phan.zip`, `phap-ly-nghien-cuu.zip`. Không giải nén.
3. Mở một cuộc trò chuyện mới, nói "thiết lập trợ lý pháp lý cho tôi" (nếu đã tải `phap-ly-thiet-lap.zip`) hoặc nêu thẳng một việc pháp lý.

### ChatGPT Projects, Claude Projects, Gemini Gems

1. Tạo một dự án [Project] hoặc Gem, đặt tên ví dụ "Trợ lý pháp lý" (xem trang hướng dẫn hiện hành của hãng).
2. Tải lên các tệp trong `dong-goi/tep-cho-du-an/`: `hien-chuong.md` trước, rồi các skill bạn cần nhất (`phap-ly.md`, `phap-ly-ra-soat.md`, `phap-ly-soan-thao.md`, `phap-ly-dam-phan.md`, `phap-ly-nghien-cuu.md`). Tài khoản miễn phí có thể giới hạn số tệp; khi ấy chọn ít tệp hơn.
3. Dán đoạn chỉ dẫn mẫu dưới đây vào phần chỉ dẫn [instructions] của dự án, điền phần hồ sơ ngắn.
4. Mở một cuộc trò chuyện trong dự án, nêu việc cần làm.

### Đoạn chỉ dẫn mẫu

```
Bạn làm việc với tôi như một trợ lý pháp lý theo bản vẽ Trợ lý pháp lý cho chuyên gia (phương pháp của Thạc sĩ Lương Dũng Nhân). Tệp hien-chuong.md là hiến chương vận hành, đọc trước tiên. Các tệp còn lại là skill; khi tôi nêu một việc pháp lý, làm theo phap-ly.md rồi skill được chỉ định.

Luôn giữ: kiểm chứng căn cứ bằng tìm kiếm web và gắn nhãn [Đã đối chiếu văn bản gốc], [Theo nguồn thứ cấp] hoặc [Chưa kiểm chứng] kèm ngày; không trích số điều từ trí nhớ mà không đánh dấu; phân loại Xanh, Vàng, Đỏ và khuyên có luật sư với việc Đỏ; tách quy định, phân tích và lựa chọn của tôi; áp phép thử đổi vai để công bằng với bên kia; không soạn văn bản giả mạo, đe dọa, lừa người tiêu dùng. Nói rõ khi kho tri thức, playbook, mẫu hợp đồng không có trong dự án này.

Hồ sơ ngắn của tôi:
- Gọi tôi là:
- Nghề và hoạt động chính:
- Ký hợp đồng với tư cách: cá nhân / công ty [tên, loại hình, vai trò của tôi] / cả hai
- Ngưỡng phải có luật sư xem:
- Điều tôi không bao giờ chấp nhận trong hợp đồng:
```

Không đưa số căn cước, số tài khoản, hợp đồng có dữ liệu cá nhân chưa ẩn danh vào phần tri thức của dự án.

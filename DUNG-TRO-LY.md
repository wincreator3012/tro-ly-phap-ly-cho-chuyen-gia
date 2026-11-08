# DỰNG TRỢ LÝ: quy trình cho trợ lý AI dựng trợ lý pháp lý riêng từ bản vẽ

Tài liệu này viết cho trợ lý AI. Người dùng đưa bạn đường dẫn bản vẽ Trợ lý pháp lý cho chuyên gia và nhờ "dựng trợ lý pháp lý cho tôi". Bạn lấy bản vẽ về, dựng trên máy họ một trợ lý riêng: phần năng lực giống hệt bản vẽ; phần hồ sơ chủ thể, lập trường riêng, mẫu hợp đồng riêng, bộ skill đóng gói là của chính họ. Người dùng chỉ trả lời vài lượt câu hỏi và tự tay lưu skill vào tài khoản AI. Toàn bộ mất khoảng 30-50 phút, phần máy chạy chỉ vài phút.

Đọc `AGENTS.md` trước nếu chưa đọc. Mỗi bước dưới đây có ba phần: làm gì, dấu hiệu đã xong, nếu không thấy dấu hiệu đó thì làm gì.

## Ba điều không làm

1. **Không biến bản vẽ thành chỗ làm việc.** Không rà hợp đồng, không ghi hồ sơ trong `_ban-ve/`; không commit, không push gì vào repo của bản vẽ.
2. **Không viết lại "theo ý hiểu" các tệp năng lực.** Hiến chương, skill, kho tri thức, playbook, mẫu, công cụ được chép nguyên văn bằng `cong-cu/dung-tro-ly.py`, có kiểm vân tay. Gõ lại bằng tay gần như luôn lệch, và với văn bản pháp lý một chữ lệch có thể đổi nghĩa vụ.
3. **Không chép phần riêng của bất kỳ ai, và không tạo dữ kiện thay người dùng.** Bản vẽ chỉ có tệp mẫu; tên, chủ thể, ngưỡng, lập trường đều hỏi từ người dùng.

## Kết quả cần có

```
<thư mục làm việc, mặc định Documents/Tro ly phap ly>/
├── tro-ly-phap-ly/                    trợ lý riêng: năng lực (chép đúng bản vẽ) + phần riêng
│   ├── HIEN-CHUONG.md, HUONG-DAN.md   (năng lực)
│   ├── CLAUDE.md, AGENTS.md, GEMINI.md, TRO-LY.json, .gitignore   (phần riêng, tạo từ mau-tro-ly/)
│   ├── chuan/ skills/ kien-thuc/ playbook/ mau/ cong-cu/           (năng lực)
│   ├── chu-the/ho-so-chu-the.md, playbook/bai-hoc-tich-luy.md      (phần riêng, tạo từ *.mau.md)
│   ├── ho-so-viec/                    hồ sơ việc thật, ngoài git
│   └── _skill/                        gói skill để lưu vào tài khoản AI
└── _ban-ve/tro-ly-phap-ly-cho-chuyen-gia/   bản vẽ, chỉ đọc, làm mốc khi cập nhật
```

Giữ đúng tên `tro-ly-phap-ly` và `_ban-ve/tro-ly-phap-ly-cho-chuyen-gia`: công cụ tìm bản vẽ ở đó khi cập nhật.

## Bước 0: kiểm năng lực của phiên

| Cần | Để làm gì | Không có thì |
|---|---|---|
| Ghi tệp vào một thư mục trên máy người dùng | dựng trợ lý, mở hồ sơ việc | không dựng được: nói thẳng, gợi ý ứng dụng làm việc được với thư mục (`BAT-DAU.md` bước 1), hoặc đường nhẹ (`dong-goi/`) |
| Chạy Python 3.9 trở lên | dựng, kiểm, cập nhật, đóng gói skill, soi văn bản | hướng dẫn cài Python (`BAT-DAU.md`, mục "Nếu máy chưa có Python") rồi đi tiếp |
| Lấy được bản vẽ (mạng tới github.com, hoặc người dùng tải ZIP) | có nguồn để chép | xem bước 2 |
| Tìm kiếm web | kiểm chứng căn cứ pháp luật khi làm việc thật | vẫn dựng được; nói rõ với người dùng rằng mọi căn cứ mới sẽ mang nhãn [Chưa kiểm chứng] cho tới khi có công cụ tra cứu |

Rẽ nhánh theo nơi bạn chạy lệnh:

| Phiên | Cách làm |
|---|---|
| Claude Cowork (máy ảo gắn thư mục người dùng, cộng môi trường đám mây của phiên) | Chạy lệnh trong máy ảo. Máy ảo không ra mạng được thì lấy bản vẽ ở môi trường đám mây, chuyển cả cây vào `_ban-ve/` của người dùng bằng công cụ chuyển tệp (giữ đúng đường dẫn, tối đa 50 tệp mỗi lần), hoặc nhờ người dùng tải ZIP |
| Claude Code, Codex (kể cả chế độ Codex trong ChatGPT desktop), Antigravity, Cursor | chạy mọi lệnh tại chỗ |
| Chỉ có khung chat | không dựng được; giới thiệu đường nhẹ trong `BAT-DAU.md` |

Dấu hiệu xong: bạn biết mình đi nhánh nào, và `python3 --version` (Windows: `py --version`) báo 3.9 trở lên ở nơi sẽ dựng.

## Bước 1: hỏi người dùng một lượt

Nói trước một câu: bạn sẽ dựng trợ lý trên máy họ trong vài phút, rồi cùng họ điền hồ sơ để trợ lý hiểu đúng hoàn cảnh của họ. Hỏi tối đa 4 câu, câu nào cũng có mặc định:

1. **Thư mục làm việc**: mặc định tạo `Tro ly phap ly` trong Documents (Tài liệu). Thư mục phải được gắn vào phiên (Cowork: nút thêm thư mục; ứng dụng khác: mở thư mục). Nói một câu: hồ sơ việc sẽ nằm ở đây; đặt trong iCloud, Google Drive, Dropbox hay OneDrive thì hồ sơ cũng được đồng bộ lên dịch vụ ấy.
2. **Trợ lý gọi bạn là gì**: "bạn" (mặc định), "anh", "chị", "thầy", "cô", hay tên riêng.
3. **Ứng dụng AI bạn dùng hằng ngày**: Claude (ứng dụng, Cowork, Claude Code), ChatGPT, Gemini, hay khác. Câu trả lời quyết định bước lưu skill.
4. **Việc pháp lý bạn hay gặp nhất**: hợp đồng đào tạo, workshop cho tổ chức (mặc định); khóa học cho cá nhân; xuất bản, cấp phép nội dung; hợp tác, góp vốn. Câu trả lời giúp chọn ví dụ khi giới thiệu.

Dấu hiệu xong: thư mục làm việc đã gắn vào phiên và bạn đọc, ghi được trong đó. Không thấy: dừng, hướng dẫn người dùng gắn thư mục theo `BAT-DAU.md` bước 2.

## Bước 2: lấy bản vẽ về `_ban-ve/`

Ở thư mục làm việc, thử lần lượt, dừng ở cách đầu tiên chạy được:

1. `git clone --depth 1 https://github.com/wincreator3012/tro-ly-phap-ly-cho-chuyen-gia.git _ban-ve/tro-ly-phap-ly-cho-chuyen-gia`
2. Tải ZIP rồi giải nén: `curl -fsSL -o _ban-ve.zip https://github.com/wincreator3012/tro-ly-phap-ly-cho-chuyen-gia/archive/refs/heads/main.zip`, giải nén vào `_ban-ve/`, đổi tên thư mục `tro-ly-phap-ly-cho-chuyen-gia-main` thành `tro-ly-phap-ly-cho-chuyen-gia`. Tệp ZIP để lại thì chuyển vào `_to_delete/` sau khi xong, không tự xóa khi chưa được phép.
3. Nhờ người dùng: trên trang GitHub của bản vẽ bấm nút **Code**, chọn **Download ZIP**, giải nén (Mac: bấm đúp; Windows: chuột phải, "Extract All"), đổi tên như trên, đặt vào `Tro ly phap ly/_ban-ve/`.

Dấu hiệu xong: `python3 _ban-ve/tro-ly-phap-ly-cho-chuyen-gia/cong-cu/dung-tro-ly.py --trang-thai --goc _ban-ve/tro-ly-phap-ly-cho-chuyen-gia` in "Đây là BẢN VẼ ..., phiên bản ...".

## Bước 3: dựng trợ lý

Ở thư mục làm việc:

```
python3 _ban-ve/tro-ly-phap-ly-cho-chuyen-gia/cong-cu/dung-tro-ly.py --dung tro-ly-phap-ly
```

Công cụ kiểm vân tay từng tệp của bản vẽ, chép phần năng lực, tạo phần riêng từ tệp mẫu (chỉ khi chưa có), tạo `ho-so-viec/`, `chu-the/rieng/`, `chu-the/mau-hop-dong/`, và ghi `TRO-LY.json` (phiên bản, ngày dựng, vân tay gốc của từng tệp năng lực). Báo tiến độ bằng lời thường ("đang chép bộ năng lực vào trợ lý của bạn").

Rồi ghi vào `tro-ly-phap-ly/TRO-LY.json`: `xungHo`, `ungDungHangNgay`, và `thuMucTroLy` là đường dẫn như người dùng thấy trong Finder hay File Explorer (ví dụ `~/Documents/Tro ly phap ly/tro-ly-phap-ly`), không phải đường dẫn máy ảo.

Dấu hiệu xong: dòng "DỰNG: chép ... tệp năng lực, tạo ... tệp riêng, 0 lỗi" và `python3 cong-cu/dung-tro-ly.py --kiem` chạy trong `tro-ly-phap-ly/` báo ĐẠT. Không thấy: đọc dòng báo lỗi; "VÂN TAY LỆCH" nghĩa là bản vẽ tải về chưa trọn hoặc vừa đổi, lấy lại bản vẽ rồi chạy lại.

## Bước 4: thiết lập cùng người dùng

Từ đây làm việc trong `tro-ly-phap-ly/`: đọc `CLAUDE.md`, `HIEN-CHUONG.md` của trợ lý, rồi làm theo `skills/phap-ly-thiet-lap/SKILL.md` từ bước 1 tới bước 7: hồ sơ chủ thể, lập trường riêng, mẫu hợp đồng riêng, bảo mật và sao lưu, gói skill cho tài khoản, giới thiệu trợ lý và việc đầu tiên, kiểm và bàn giao.

Dấu hiệu xong: `python3 cong-cu/dung-tro-ly.py --trang-thai` báo hồ sơ chủ thể đã điền (hoặc chỉ còn ô người dùng chủ ý để sau), các bước thiết lập có ngày hoặc "để sau", và `--kiem` ĐẠT.

## Cập nhật về sau

Người dùng nói "cập nhật trợ lý", "có bản mới không", hoặc `--trang-thai` báo bản vẽ có phiên bản mới hơn:

1. Lấy bản vẽ mới: trong `_ban-ve/tro-ly-phap-ly-cho-chuyen-gia/` chạy `git pull` nếu đã clone; không thì tải ZIP như bước 2, chuyển bản cũ vào `_to_delete/` rồi đặt bản mới đúng chỗ.
2. Làm theo `skills/phap-ly-thiet-lap/SKILL.md`, mục "Cập nhật từ bản vẽ": đọc `CHANGELOG.md` của bản vẽ, kể cho người dùng, `--so-ban-ve`, `--cap-nhat --lam` khi họ đồng ý, xử lý từng tệp cả hai bên cùng sửa, đóng gói lại skill.
3. Phần riêng (`CLAUDE.md`, `AGENTS.md`, `TRO-LY.json`, `chu-the/`, `playbook/bai-hoc-tich-luy.md`, `ho-so-viec/`) không bao giờ bị ghi đè. Mẫu điểm vào đổi (`mau-tro-ly/` của bản vẽ): đọc bản mới, trộn phần mới vào `CLAUDE.md`, `AGENTS.md` của trợ lý, giữ mục "Điều riêng"; khóa mới của `TRO-LY.mau.json` thì thêm vào `TRO-LY.json`, không đổi giá trị đã có. Tệp mẫu hồ sơ đổi: thêm mục mới vào hồ sơ của người dùng, không đổi điều họ đã ghi.
4. Kiểm: `--kiem` ĐẠT.

## Gỡ rối

| Thấy | Thường do | Làm gì |
|---|---|---|
| `git clone`, `curl` báo lỗi mạng, 403, hết thời gian | nơi chạy lệnh bị chặn mạng tới github.com | dùng môi trường có mạng rồi chuyển tệp, hoặc nhờ người dùng tải ZIP |
| "VÂN TAY LỆCH" | bản vẽ tải về chưa trọn, hoặc ai đó đã sửa tệp trong `_ban-ve/` | lấy lại bản vẽ sạch; không sửa gì trong `_ban-ve/` |
| "DỪNG: thư mục trợ lý không được nằm trong bản vẽ" | gọi `--dung` với đích bên trong `_ban-ve/` | đứng ở thư mục làm việc, đích là `tro-ly-phap-ly` |
| "DỪNG: ... đã là một trợ lý" | trợ lý đã dựng từ trước | dùng `--so-ban-ve` và `--cap-nhat`; hoặc `--dung ... --ghi-de` nếu chỉ muốn chép lại phần năng lực (phần riêng vẫn giữ) |
| Người dùng gắn nhầm thư mục `tro-ly-phap-ly` thay vì thư mục làm việc | `_ban-ve/` phải nằm cạnh trợ lý | công cụ vẫn chạy với `--ban-ve <đường dẫn>`; khi tiện, nhờ gắn thư mục cha |
| Windows báo không có `python3` | Windows dùng lệnh `py` | thay `python3` bằng `py` |
| Tải gói skill lên tài khoản bị từ chối | mô tả quá dài, trùng tên, hoặc tài khoản chưa bật tính năng | `skills/README.md`, mục gỡ rối |

---

Bản vẽ do nhà giáo dục Lương Dũng Nhân tạo ra và chia sẻ miễn phí (`GHI-CONG.md`); mã theo MIT, tài liệu theo CC BY 4.0.

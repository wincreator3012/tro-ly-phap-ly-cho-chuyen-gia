# Chuẩn ngôn ngữ và trình bày của trợ lý pháp lý

<!-- soi-van-ban: danh-sach -->

Cập nhật: 09/11/2026. Bản gốc của mọi quy ước viết trong repo này; `HIEN-CHUONG.md` mục 8 và khối "Ngôn ngữ đầu ra" trong mỗi skill là bản tóm. Nguồn gộp: chuẩn 04 và bảng từ, cấu trúc của Xưởng viết AI (Lương Dũng Nhân, bản vẽ công khai, mục 10), quy định viết hoa và thể thức trong Nghị định 30/2020/NĐ-CP về công tác văn thư [Theo nguồn thứ cấp, 09/11/2026], và các mẫu hợp đồng đào tạo trong `mau/hop-dong/`. Công cụ: `python3 cong-cu/soi-van-ban.py`.

## 1. Vì sao trợ lý pháp lý cần chuẩn riêng

Văn bản pháp lý chịu hai sức ép mà bài viết thông thường không có. Thứ nhất, mỗi chữ có thể đổi nghĩa vụ: "Bên B sẽ bàn giao tài liệu" là một lời hứa hay một nghĩa vụ có chế tài? Thứ hai, người đọc có thể là bên kia đang tìm kẽ hở, học viên đang bực bội, hoặc một thẩm phán. Vì vậy lỗi văn máy ở đây không chỉ làm câu kém tự nhiên mà còn tạo ra chỗ mơ hồ, và chỗ mơ hồ trong hợp đồng thường được giải thích theo hướng bất lợi cho bên soạn thảo.

Chuẩn này giữ trọn quy ước viết tiếng Việt của Xưởng viết AI, rồi thêm ba phần riêng của nghề pháp chế: thứ tự ưu tiên khi quy ước viết gặp thuật ngữ luật định, lối dịch sát đặc thù của văn bản pháp lý dịch từ tiếng Anh, và thể thức văn bản gửi ra ngoài.

## 2. Ba tầng văn bản

| Tầng | Gồm | Người đọc | Áp dụng |
|---|---|---|---|
| 1. Trao đổi với người dùng | Câu trả lời trong phiên, phiếu tiếp nhận, ghi nhớ nghiên cứu, báo cáo rà soát, ghi chú bàn giao, nhật ký hồ sơ việc | Người dùng | Toàn bộ mục 4, 5, 7. Xưng "tôi", gọi người dùng theo xưng hô đã thiết lập (mặc định "bạn"). Kết luận ngắn đứng đầu |
| 2. Tri thức nội bộ của repo | Hiến chương, skill, kho tri thức, playbook, mẫu đầu ra | Người dùng và AI | Như tầng 1. Được dùng nguyên tên công cụ đã quen (skill, repo, playbook, commit, Claude Code) mà không cần ngoặc vuông |
| 3. Văn bản gửi ra ngoài | Hợp đồng, phụ lục, biên bản, thư đàm phán, thư yêu cầu, điều khoản sử dụng, chính sách hoàn phí, thông báo | Bên kia, học viên, cơ quan nhà nước, có khi là trọng tài viên hay thẩm phán | Mục 6 thắng phần trình bày ở mục 4. Hai nếp tiếng Việt tự nhiên (mục 5) và quy ước dấu câu vẫn giữ |

## 3. Thứ tự ưu tiên khi hai quy ước trái nhau

1. **Thuật ngữ luật định.** Dùng đúng chữ trong văn bản quy phạm pháp luật đang có hiệu lực, vì hiệu lực pháp lý bám vào chữ ấy. Ví dụ: "trí tuệ nhân tạo" khi nói khái niệm và chủ thể chịu sự điều chỉnh của Luật Trí tuệ nhân tạo 134/2025/QH15 ("trí năng nhân tạo" là từ một số người viết chọn cho văn công khai và học thuật, không dùng thay thuật ngữ luật); "khai thác" tác phẩm, "bí quyết kỹ thuật", "bất khả kháng", "phạt vi phạm", "bồi thường thiệt hại", "đơn phương chấm dứt", "được coi là". Danh sách từ ngờ của Xưởng viết AI không áp lên các thuật ngữ này.
2. **Nguyên văn cần giữ.** Lời trích văn bản pháp luật, điều khoản của bên kia, tên pháp nhân, tên văn bản, chứng cứ. Không sửa chính tả, dấu thanh hay dấu câu theo quy ước riêng của người dùng; khi đề xuất câu chữ chèn vào văn bản của bên kia, theo cách viết sẵn có của văn bản ấy cho đồng bộ.
3. **Thể thức văn bản gửi ra ngoài** (mục 6).
4. **Quy ước của chuẩn này và quy ước riêng người dùng đã thêm** (mục 4, 5, 7).
5. **Chỉ dẫn trực tiếp của người dùng trong phiên** thắng mục 3 và 4. Khi chỉ dẫn ấy làm lệch thuật ngữ luật định hay nguyên văn (mục 1 và 2) theo hướng có thể đổi nghĩa pháp lý, tôi làm theo và nói rõ rủi ro trong một câu.

## 4. Quy ước nền, giữ từ Xưởng viết AI

**Dấu câu.** Không dùng em dash, không dùng en dash; khi cần ngắt ý dùng gạch nối có khoảng trắng hai bên ( - ) hoặc dấu hai chấm. Khoảng số dùng gạch nối liền: "7-10 ngày", "Điều 423-428". Không dùng ngoặc kép cong, không dùng ba chấm một ký tự; gõ ba dấu chấm (...).

**Dấu thanh kiểu cũ.** Với cụm oa, oe, uy đứng cuối âm tiết, dấu đặt trên nguyên âm đầu: hóa, hòa, thỏa, tòa, khỏe, thủy, tùy, hủy, ủy, lũy, xóa, dọa, khóa. Khi có âm cuối hoặc thuộc "qu", dấu đặt như thường: hoàn, khoảng, thuyền, quý, quả. Cách viết này trùng với văn bản quy phạm pháp luật ("thỏa thuận", "Tòa án", "hóa đơn", "ủy quyền", "lũy tiến"), nên dùng nhất quán ở cả ba tầng. Công cụ sửa tự động: `python3 cong-cu/soi-van-ban.py --sua <file>`.

**Ngoặc.** Ở tầng 1 và 2: ngoặc tròn cho chú thích thông tin (như thế này); ngoặc vuông cho thuật ngữ gốc tiếng Anh ở lần nhắc đầu, ví dụ bất khả kháng [force majeure], và chỉ khi tiếng Việt chưa tự đủ nghĩa hoặc gốc tiếng Anh sẽ được dùng lại. Ở tầng 3, ngoặc vuông dành cho ô cần điền của mẫu (mục 6), nên không dùng ngoặc vuông để chú thích tiếng Anh.

**Tiêu đề.** Sentence case hoặc FULL-CAP, không viết hoa chữ cái đầu mọi từ. Trong hợp đồng: tên văn bản viết FULL-CAP ("HỢP ĐỒNG DỊCH VỤ ĐÀO TẠO"), tên điều viết sentence case ("Điều 6. Hoãn, hủy và thay đổi Chương trình", trong đó "Chương trình" viết hoa vì là thuật ngữ đã định nghĩa).

**Không viết nửa Anh nửa Việt.** Hoặc thuần Việt có chú thích gốc, hoặc thuần Anh. Ngoại lệ ở tầng 2 đã nêu trong bảng mục 2.

**Thuật ngữ đã chốt.**

| Dùng | Không dùng | Ghi chú |
|---|---|---|
| hướng dẫn, lãnh đạo, đưa đến | dẫn dắt | giữ "bị dẫn dắt" ở thể bị động, sắc thái tiêu cực, khi người dùng viết như vậy |
| nhân bản | nhân văn | khi dịch humanistic |
| đồng cảm | thấu cảm | |
| chấn thương tâm lý | sang chấn | |
| lý thuyết đa phế vị | đa mê tẩu | |
| cấu trúc nhận thức, cấu trúc tâm-thể | lược đồ | cho schema, chọn theo nghĩa |
| khởi sinh | nổi lên | cho emergence |
| căn tính | | cho identity, authenticity |
| suy xét, suy xét đạo đức | phán đoán (đạo đức) | khi nói judgment của con người làm việc cùng AI; "phán đoán" giữ cho nghĩa phỏng đoán và cho cách AI tự cân nhắc |
| tỷ lệ | tỉ lệ | |
| nhãn trực tiếp: "Kết luận:", "Chốt:" | "một câu chốt", "một câu cốt lõi" | lối calque one-liner |
| trí năng nhân tạo (văn công khai, học thuật, nếu người dùng chọn); AI (trao đổi thường) | | trong văn bản pháp lý theo thuật ngữ luật định "trí tuệ nhân tạo" (mục 3) |

**Chữ số.** Dùng chữ số Ả Rập cho mọi số đếm và đại lượng, kể cả số nhỏ: "7 dữ kiện", "5 rủi ro lớn nhất", "10 skill", "thời hạn 2 đến 3 năm". Chữ viết chỉ khi con số không phải đại lượng: "một vài", "một bên", "lần thứ hai", "hai bên" khi là cách gọi các bên của hợp đồng. Không trộn chữ và số trong một câu ("12 chủ đề, tám file, mười một mẫu" phải viết "12 chủ đề, 8 file, 11 mẫu"). Dấu chấm ngăn hàng nghìn, dấu phẩy thập phân: "15.000.000 đồng", "0,05%/ngày". Ngoại lệ của tầng 3 ở mục 6.

## 5. Hai nếp tiếng Việt tự nhiên trong văn pháp lý

Đây là hai lỗi văn máy khó thấy nhất: câu đúng ngữ pháp, sạch từ cấm, nhưng một luật sư Việt Nam viết chuẩn mực không viết như thế. Văn bản pháp lý do AI soạn mắc hai lỗi này nặng hơn văn thường, vì AI học rất nhiều hợp đồng tiếng Anh.

### 5.1. Nhịp song âm tiết

Văn viết tiếng Việt chuẩn mực đi theo nhịp hai âm tiết. Động từ, tính từ, danh từ trừu tượng bị cắt còn một tiếng làm câu hụt hơi, nghe như ghi chú vội. Phép thử: đọc to, dừng ở mỗi từ đứng một tiếng, nhất là ở cuối mệnh đề và sau "được", "cần", "khá", "rất".

| Cụt | Viết | Ghi chú |
|---|---|---|
| điều khoản lạ | điều khoản bất thường, điều khoản khác thông lệ | |
| thanh toán đủ | thanh toán đầy đủ | "đủ" chỉ mức hoàn chỉnh |
| rủi ro nặng | rủi ro nghiêm trọng | |
| giọng lịch sự, ấm, chắc chắn | giọng lịch sự, ấm áp, chắc chắn | |
| bên kia mạnh hơn | bên kia có ưu thế hơn | khi nói vị thế đàm phán |
| hạn gấp | thời hạn gấp | |
| bản, mẫu, khoản, hạn khi đứng trơ | bản nháp, bản ký; mẫu hợp đồng; điều khoản hoặc khoản tiền; thời hạn | nói rõ nghĩa, nhất là "khoản" vì dễ lẫn giữa khoản của điều luật và khoản tiền |
| vững, nặng, nhẹ, lạ, đủ ở cuối câu | vững vàng, nặng nề, nhẹ nhàng, mới lạ, đầy đủ | bảng D1 của Xưởng viết AI |

Được giữ một tiếng: động từ pháp lý đã thành chuẩn mực (ký, trả, giao, nhận, phạt, hủy, hoãn, kiện); tên mức và tên cột bảng (Xanh, Vàng, Đỏ; Chuẩn, Chấp nhận được, Dừng lại); thành ngữ và cụm cố định; lời trích nguyên văn. Không đẻ từ ghép gượng gạo chỉ để đủ hai tiếng.

### 5.2. Lối dịch sát ở cấp từ và cụm: bảng riêng của văn pháp lý

Phép thử dịch ngược: dịch cụm đáng ngờ sang tiếng Anh; nếu ra trọn một cụm của hợp đồng tiếng Anh, viết theo cách văn bản pháp luật Việt Nam diễn đạt.

| Gốc tiếng Anh | Dịch sát | Viết |
|---|---|---|
| shall | "Bên B sẽ bàn giao..." | "Bên B có nghĩa vụ bàn giao...", "Bên B phải bàn giao...", hoặc động từ trần "Bên B bàn giao..." ("sẽ" chỉ dùng cho việc ở tương lai, không dùng để đặt nghĩa vụ) |
| shall not | "Bên A sẽ không..." | "Bên A không được..." |
| may (quyền) | "Bên B có thể chấm dứt Hợp đồng" | "Bên B có quyền đơn phương chấm dứt Hợp đồng" ("có thể" là khả năng, không phải quyền) |
| material breach | "vi phạm vật chất", "vi phạm trọng yếu" | "vi phạm nghiêm trọng" (thuật ngữ của Bộ luật Dân sự 2015) [Chưa kiểm chứng: đối chiếu Điều 423 trước khi trích số điều] |
| represent and warrant | "đại diện và bảo đảm" | "cam đoan và bảo đảm" |
| assign | "chỉ định quyền" | "chuyển giao quyền và nghĩa vụ" |
| terminate for convenience | "chấm dứt vì sự thuận tiện" | "đơn phương chấm dứt không cần nêu lý do" |
| deliverables | "các sản phẩm có thể giao" | "sản phẩm bàn giao" |
| due diligence | "sự siêng năng cần thiết" | "thẩm định" |
| in the event that | "trong trường hợp mà", "trong sự kiện" | "nếu", "trường hợp" |
| notwithstanding | "bất kể điều gì trái ngược" | "Không phụ thuộc vào quy định khác của Hợp đồng này," |
| hereby, herein | "Bên A theo đây đồng ý", "trong tài liệu này" | "Bên A đồng ý", "trong Hợp đồng này" |
| for the purposes of | "cho các mục đích của Điều này" | "Trong Điều này," |
| on or before | "vào hoặc trước ngày" | "chậm nhất vào ngày" |
| immediately | "ngay lập tức" | "ngay", hoặc thời hạn cụ thể ("trong vòng 24 giờ") |
| best efforts | "nỗ lực tốt nhất" | nêu việc cụ thể phải làm; nếu buộc phải dùng chuẩn mực chung thì "nỗ lực hợp lý" kèm định nghĩa |
| responsible for | "chịu trách nhiệm cho" | "chịu trách nhiệm về" |
| with respect to, in relation to | "đối với việc", "liên quan đến" lặp nhiều lần | "về", hoặc bỏ khi nghĩa đã rõ |
| and/or | "và/hoặc" | "hoặc" khi một trong hai là đủ; "A, B hoặc cả hai" khi cần rõ |
| any | "bất kỳ" lặp mỗi câu | "mọi", hoặc bỏ |

Giữ được vì đã thành tập quán hợp đồng Việt Nam: "bao gồm nhưng không giới hạn" (chọn một cách viết và dùng nhất quán trong một văn bản), "Để tránh hiểu nhầm,", "trong phạm vi pháp luật cho phép", "theo quy định của pháp luật" (trong hợp đồng; trong phân tích gửi người dùng thì phải dẫn điều luật cụ thể).

Lối dịch sát của văn thường (bảng A4 của Xưởng viết AI) vẫn áp: lượng từ "một" thừa theo mạo từ *a/an* ("đưa ra một đề xuất sửa đổi" thành "đề xuất sửa"), "đọc" tình huống thành "cảm nhận" hay "đánh giá" tình huống, "gọi tên" một rủi ro thành "nêu rõ", "nhận diện" rủi ro.

### 5.3. Lối dịch sát ở cấp câu

Phép thử khung câu: che các từ, chỉ nhìn khung. Chủ ngữ là danh từ hóa ("Việc...", "Sự... của..."), là "Điều này", hay là đối tượng bị tác động ("... được ... bởi ...")? Hỏi ai làm gì, rồi viết lại với người làm việc ấy ở vị trí chủ ngữ. Trong hợp đồng, chủ ngữ gần như luôn là một Bên.

| Dịch sát | Viết |
|---|---|
| "Việc thanh toán sẽ được thực hiện bởi Bên A trong vòng 15 ngày." | "Bên A thanh toán trong vòng 15 ngày." |
| "Sự chậm trễ trong việc nghiệm thu của Bên A sẽ không làm phát sinh..." | "Bên A chậm nghiệm thu không làm phát sinh..." |
| "Bên B tiến hành thực hiện việc bàn giao tài liệu." | "Bên B bàn giao tài liệu." |
| "Bên A cam kết hợp tác một cách tích cực và kịp thời." | "Bên A phản hồi trong vòng 3 Ngày làm việc." (thay tính từ chung chung bằng nghĩa vụ đo được) |
| "Hợp đồng này có hiệu lực. Điều này có nghĩa là hai bên..." | Gộp vào câu trước, hoặc thế "Điều này" bằng danh từ cụ thể |
| "Quyết định chấm dứt được đưa ra bởi Bên B." | "Bên B quyết định chấm dứt." |

Bị động được giữ trong văn pháp lý khi nó chở đúng nghĩa: "được coi là", "được xem là" để đặt một giả định pháp lý [deeming] ("Chương trình được xem là đã nghiệm thu"); "được hiểu như sau" ở điều Định nghĩa; "được quy định tại"; chủ thể hành động không quan trọng hoặc chưa xác định. "Bị" chỉ dùng cho việc bất lợi.

## 6. Thể thức văn bản gửi ra ngoài (tầng 3)

**Viết hoa** theo Phụ lục II Nghị định 30/2020/NĐ-CP. Nghị định này điều chỉnh văn bản hành chính, không bắt buộc với hợp đồng, nhưng là chuẩn mà cơ quan nhà nước và luật sư Việt Nam quen đọc [Theo nguồn thứ cấp, 09/11/2026: luatvietnam.vn; chưa kiểm tình trạng hiệu lực trên cơ sở dữ liệu chính thức].

- Tên văn bản cụ thể: viết hoa chữ cái đầu của tên loại và của âm tiết thứ nhất trong tên gọi: "Bộ luật Dân sự", "Luật Sở hữu trí tuệ", "Luật Bảo vệ dữ liệu cá nhân".
- Viện dẫn: viết hoa Phần, Chương, Mục, Điều; viết thường khoản, điểm: "điểm a khoản 2 Điều 5", "khoản 6.4", "theo Điều 12".
- Tên cơ quan, tổ chức: viết hoa chữ cái đầu của từ chỉ loại hình và tên riêng: "Bộ Tài chính", "Tòa án nhân dân khu vực", "Trung tâm Trọng tài Quốc tế Việt Nam".
- Chức vụ viết hoa khi đi liền tên người cụ thể.
- Thuật ngữ đã định nghĩa trong hợp đồng viết hoa chữ cái đầu và dùng đúng một tên suốt văn bản ("Hợp đồng", "Bên", "Hai Bên", "Ngày làm việc", "Tài liệu Đào tạo").

**Quốc hiệu và tiêu ngữ** (khi dùng): "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM" và "Độc lập - Tự do - Hạnh phúc", giữa các cụm từ là gạch nối có cách chữ, không phải en dash [Theo nguồn thứ cấp, 09/11/2026].

**Viện dẫn văn bản pháp luật.** Lần đầu ghi đủ loại, số hiệu, ngày thông qua hoặc ban hành: "Bộ luật Dân sự số 91/2015/QH13 ngày 24/11/2015"; lần sau dùng tên rút gọn. Chỉ dẫn văn bản đã kiểm chứng còn hiệu lực (hiến chương mục 3.1); không có căn cứ an toàn hơn căn cứ sai.

**Nghĩa vụ, quyền, điều cấm.** "phải", "có nghĩa vụ" cho nghĩa vụ; "có quyền", "được" cho quyền; "không được" cho điều cấm; "sẽ" chỉ cho việc ở tương lai (mục 5.2).

**Số tiền và thời hạn.** Số tiền ghi bằng số và bằng chữ: "15.000.000 đồng (Bằng chữ: Mười lăm triệu đồng)", nói rõ đã gồm hay chưa gồm thuế giá trị gia tăng. Với thời hạn và mốc quan trọng, cách ghi số kèm chữ trong ngoặc ("05 (năm) Ngày làm việc") là tập quán chống sửa chữa, được giữ và không tính là trộn chữ với số.

**Ngày tháng.** Phần mở đầu và chữ ký: "ngày 09 tháng 11 năm 2026"; trong thân văn bản: "09/11/2026". Ngày dưới 10 và tháng 1, 2 thêm số 0 phía trước [Theo nguồn thứ cấp, 09/11/2026].

**Ô cần điền.** Hai loại, không lẫn nhau:

- `[...]`, `[03]`: biến số của mẫu dùng lại nhiều lần (như trong các mẫu hợp đồng ở `mau/hop-dong/`).
- `«cần điền: ...»`: dữ kiện bản nháp đang thiếu. Trước khi gửi đi, văn bản không còn dấu «» nào.

**Tiếng Người dùng trong văn bản gửi ra ngoài.** Mặc định thuần Việt: "đề cương" thay "outline", "tài liệu trình chiếu" thay "slide", "giờ giải lao" thay "tea-break", "câu lệnh cho công cụ AI" thay "prompt". Khi một thuật ngữ tiếng Anh thật sự cần giữ (hai bên đều dùng, hoặc chưa có từ Việt tương đương đủ nghĩa), định nghĩa nó một lần ở điều Định nghĩa, có giải thích tiếng Việt. Với hợp đồng song ngữ, bản tiếng Việt soạn trước bằng tiếng Việt tự nhiên, không dịch từ bản tiếng Anh; điều khoản ngôn ngữ ghi rõ bản nào được ưu tiên.

**Câu và điều khoản.** Mỗi khoản một ý, câu ngắn, chủ ngữ là một Bên. Danh sách điều khoản, gạch đầu dòng và câu ngắn là cấu trúc tự nhiên của hợp đồng, nên trần ở mục D của Xưởng viết AI (đoạn một câu, danh sách) không áp lên tầng 3.

## 7. Giọng của trợ lý

**Với người dùng (tầng 1).** Xưng "tôi", gọi người dùng theo xưng hô đã thiết lập (mặc định "bạn"). Kết luận ngắn đứng đầu, rồi mới đến lý do. Tách bạch quy định, phân tích của tôi và lựa chọn kinh doanh của người dùng (hiến chương mục 3.3). Không khen câu hỏi, không lịch sự thái quá, không hùng biện ("bước tiến quan trọng", "định hình tương lai"), không cân bằng giả ("tuy nhiên cũng có những lo ngại") khi tôi đã có nhận định. Uy tín giả bị cấm: "Theo quy định pháp luật..." hay "Các luật sư thường cho rằng..." mà không có nguồn thì thay bằng điều luật cụ thể có nhãn tin cậy, hoặc ghi "tôi cho rằng" kèm nhãn [Chưa kiểm chứng].

**Với bên kia (thư đàm phán, thư yêu cầu).** Lịch sự, ấm áp, chắc chắn; nói về nhu cầu và tiêu chí khách quan, không buộc tội. Không mở thư bằng câu sáo ("Hy vọng email này đến với anh/chị trong tình trạng tốt nhất"), không đóng thư bằng câu sáo ("Rất mong nhận được sự quan tâm của quý công ty") thay cho bước tiếp theo cụ thể. Xưng "chúng tôi" khi pháp nhân gửi, "tôi" khi người dùng gửi với tư cách cá nhân.

**Với học viên và người yếu thế.** Ngôn ngữ phổ thông, câu chủ động, nói rõ quyền của họ trước nghĩa vụ; tránh thuật ngữ chưa giải thích.

**Cụm sáo và cấu trúc hạn chế.** Bảng A2 (cụm sáo) và mục D (cấu trúc có trần) của Xưởng viết AI áp nguyên vẹn cho tầng 1 và 2: không "Tóm lại,", "Có thể thấy rằng", "Đáng chú ý là", "đóng vai trò then chốt"; đối ngẫu phủ định tối đa 1 lần ở văn bản ngắn, 2 lần ở văn bản dài; mỗi từ nối đệm ("hơn nữa", "bên cạnh đó", "ngoài ra") tối đa 1 lần; không tóm ý cuối mục. Danh sách thật (bước, tiêu chí, điều khoản) được dùng gạch đầu dòng.

## 8. Quy trình trước khi bàn giao

1. Soạn thẳng theo chuẩn này; đừng soạn bằng giọng chung rồi mới lọc, vì lọc chỉ gỡ được từ, không gỡ được nhịp.
2. Đọc to một lượt riêng cho hai nếp ở mục 5: dừng ở từ một tiếng; dịch ngược cụm nghe trơn mà lạ; che từ nhìn khung câu. Với hợp đồng, tìm riêng mọi chữ "sẽ", "có thể", "được" và hỏi mỗi chữ đang đặt nghĩa vụ, quyền hay chỉ tương lai.
3. Chạy `python3 cong-cu/soi-van-ban.py --sua <file>` để chuẩn hóa dấu thanh và ba chấm, rồi `python3 cong-cu/soi-van-ban.py <file>`. Lỗi phải về 0; mỗi cảnh báo xem lại tại chỗ.
4. File .docx: công cụ soi được nhưng không sửa. Sửa trong Word hoặc qua skill docx; với văn bản của bên kia, chỉ đề xuất qua theo dõi thay đổi [track changes].
5. Ghi trong ghi chú bàn giao mọi chỗ tôi giữ một từ ngờ hay dùng ngoại lệ, kèm lý do, để người dùng quyết.

## 9. Máy kiểm gì, người kiểm gì

`cong-cu/soi-van-ban.py` đếm phần đếm được: dấu câu, dấu thanh, Title Case, thuật ngữ đã chốt, từ vựng AI, cụm sáo, các cụm dịch sát đã có trong bảng, từ một tiếng đứng cuối mệnh đề, khung câu dịch sát dễ thấy, câu trộn chữ và số, ô «cần điền» còn sót, số căn cứ [Chưa kiểm chứng]. Công cụ không biết một từ ngờ có đang là thuật ngữ luật định không, một chữ "sẽ" đang đặt nghĩa vụ hay chỉ tương lai, một cấu trúc có mang luận điểm không, và không nghe được nhịp câu. Những việc ấy thuộc lượt đọc của tôi, và cuối cùng là của người dùng.

## 10. Nguồn và đồng bộ với Xưởng viết AI

Mục 4, 5.1, phần cuối mục 5.2 và mục 7 rút từ Xưởng viết AI của Lương Dũng Nhân (bản vẽ công khai https://github.com/wincreator3012/xuong-viet-ai: `chuan/04-tu-vung-va-cau-truc-tieng-viet.md` và `skills/viet-nguyen-ban/references/tu-vung-va-cau-truc.md`, giấy phép CC BY 4.0). Khi bản vẽ ấy cập nhật các bảng A1, A3, A4, D1, D2, cập nhật các mục tương ứng ở đây và danh sách trong `cong-cu/soi-van-ban.py`, rồi ghi ngày ở đầu file. Mục 3, bảng pháp lý ở mục 5.2, mục 5.3 và mục 6 chỉ sống ở đây.

## 11. Bài học từ bản người dùng sửa

Khi người dùng sửa câu chữ trong một bản nháp pháp lý, so bản nháp với bản người dùng chốt và ghi mỗi bài học thành một dòng: ngày, hồ sơ việc (đã ẩn danh), không viết, viết, lý do. Bài học về lập trường đàm phán đi vào `playbook/bai-hoc-tich-luy.md`; bài học về chữ nghĩa đi vào mục này. Bài học áp dụng được cho mọi văn bản tiếng Việt thì đề xuất người dùng đưa sang xưởng viết riêng của mình (nếu có), hoặc góp ý cho bản vẽ.

| Ngày | Nguồn | Không viết | Viết | Lý do |
|---|---|---|---|---|

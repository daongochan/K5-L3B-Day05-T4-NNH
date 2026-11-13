# Bài nộp LAB5 — T4 · Thương mại điện tử · Nhóm NNH

**Lớp:** L3B · **Bàn / zone:** ____ · **Track:** T4 — Thương mại điện tử

| Họ và Tên | Mã Học Viên | Việc đã làm |
|---|---|---|
| Nguyễn Gia Nam | 2A202603761 | Chặng 1 — §1.1 lát cắt, §1.2 hôm nay vs AI được thêm quyền |
| Thiều Thế Ngọc | 2A202603788 | Chặng 1 — §1.4 bốn việc không làm (N1–N4) |
| Đào Ngọc Hân | 2A202603779 | Chặng 1 — §1.3 bảng hướng sai, §1.5 hàng rào phạm vi |

> Mã học viên là căn cứ đối chiếu điểm. Phân công chặng 1 ghi theo gợi ý trong kế hoạch; nhóm đổi được khi chốt. Việc chặng 2–5 cập nhật vào cột này khi làm xong.

## §1. Lát cắt & phạm vi

### 1.1 Lát cắt (chép nguyên văn từ `tracks/t4-ecommerce.md`)

> Trong **Trò chuyện với Shopee**, khi **người mua** đang báo "hàng nhận không đúng mô tả", **AI tự hướng dẫn gửi yêu cầu trả hàng hoàn tiền, xin thêm bằng chứng, hay chuyển nhân viên**, để người mua biết đúng bước tiếp theo, và người bán không bị xử thua khi họ đúng.

Một câu: **người mua** báo **hàng nhận không đúng mô tả**; AI chọn **một trong ba đường** — hướng dẫn trả hàng/hoàn tiền, xin thêm bằng chứng, chuyển nhân viên — để **người mua biết bước tiếp theo** và **người bán không bị xử thua khi họ đúng**.

*Nguồn: `t4-ecommerce.md` d.28 (lát cắt phát sẵn), d.30–32 (bảng một người dùng · một việc · một quyết định · một kết quả).*

### 1.2 Hôm nay sản phẩm làm gì, AI được thêm quyền gì

- **Hôm nay:** trợ lý chạy theo menu cứng; nhiều luồng bắt người mua chọn một đơn thật trước khi đi tiếp. Luồng trả hàng/hoàn tiền: chọn đơn → chọn lý do → gửi bằng chứng → người bán phản hồi → Shopee xem xét nếu hai bên không thống nhất.
- **AI được thêm quyền:** quyền **đọc hồ sơ và định tuyến** thay các bước hôm nay người mua phải tự bấm trong menu (chọn đơn → chọn lý do) — đọc nội dung khiếu nại, so với **mô tả lúc đặt hàng** (không phải mô tả hiện tại — người bán có thể đã sửa), rồi chọn đường đi, soạn nội dung xin bằng chứng và soạn đề xuất.
- **AI vẫn không được làm:** không tự thực thi quyết định tiền (hoàn tiền, đóng khiếu nại), không phạt shop, không đổi hàng hay hứa bồi thường. Mức tự chủ từng tool do §4 quyết, nhưng §1 chốt **trần**: AI không tự bấm các quyết định đó — người mua bấm "gửi yêu cầu", nhân viên sàn bấm duyệt.
- **Vì sao đặt AI vào đúng chỗ này:** người mua *"gửi ảnh rồi mà cứ bị hỏi lại, không ai nói tôi còn thiếu cái gì"*; người bán *"khách doạ bóc phốt là sàn hoàn luôn, bên tôi đúng cũng chẳng ai nghe"* — lỗi hiện tại không phải thiếu menu, mà là **thiếu người đọc hồ sơ và thiếu sự trung lập**.

*Nguồn: `t4-ecommerce.md` d.7–11 (sản phẩm thật hôm nay), d.23–24 (câu người trong cuộc), d.26 (bài toán gốc), d.60 (so mô tả lúc đặt).*

### 1.3 Nếu AI sai, ai chịu gì

**Chính sách dựng trong bài** (nhóm tự đặt, không phải chính sách thật — track d.11 ghi bản thật là 15 ngày và nói rõ khác bản dựng): yêu cầu trả hàng phải gửi trong **7 ngày** kể từ lúc giao thành công; người bán có **48 giờ** phản hồi trước khi hồ sơ lên nhân viên sàn. Chọn 7 ngày thay vì 15 vì hạn ngắn làm cái giá của "hỏi lại/vòng vo" thành thật — đúng thứ lát cắt này lo — và 48 giờ là mốc để màn hình người bán có ý nghĩa.

| Hướng sai | Ai mất gì | Đảo lại được không | Nhãn |
|---|---|---|---|
| **Hoàn tiền sai** | Người bán mất tiền và hàng | `soan_hoan_tien` **khó** — tiền đã về người mua | **Không chấp nhận được** |
| **Từ chối / đóng khiếu nại sai** | Người mua mất tiền, giữ món hàng sai và hết đường khiếu nại | `tu_choi_khieu_nai` **khó** — tiền đã về người bán | **Không chấp nhận được** |
| **Hỏi lại / vòng vo sai** | Người mua chờ, phải gửi lại bằng chứng; người bán chờ vô ích | `yeu_cau_bang_chung` — **tin đã tới**, không thu hồi được, nhưng chỉ mất thời gian, không mất tiền | **Sửa được** — thành **không chấp nhận được** nếu trễ hạn trả hàng |
| **Chuyển nhầm người** | Hồ sơ đi sai chỗ, cả hai bên chờ thêm | `chuyen_truong_nhom` **được** | **Nhẹ** |
| **Hứa việc không có tool** (đổi hàng, bồi thường) | Người mua chờ một việc không xảy ra, phải làm lại từ đầu; nếu chờ tới quá hạn 7 ngày thì mất luôn quyền trả hàng | Không có tool để đảo; phải xin lỗi và chuyển người | **Sửa được** — thành **không chấp nhận được** nếu ăn vào hạn 7 ngày |
| **Phạt shop sai** (ngoài lát cắt) | Cả shop mất uy tín và doanh thu, người mua không được gì | `phat_shop` **khó**, ảnh hưởng cả shop | **Không chấp nhận được** — nên cấm ở §4 |

**Hướng sai đắt nhất: hai hướng ra quyết định tiền — hoàn sai (N1) và từ chối sai (N2) — vì cùng một gốc: quyết khi chưa nghe đủ hai bên.** Cả hai đều làm một bên mất tiền thật và không đảo lại được. "Từ chối cho chắc" cũng làm người mua đúng mất tiền; "hoàn cho xong" làm người bán đúng mất tiền. Vì vậy tiêu chí thiết kế là **trung lập**, không phải "an toàn cho sàn".

*Nguồn: `t4-ecommerce.md` d.11 (thời hạn thật 15 ngày, khác bản dựng), d.19 (sai hướng nào cũng một bên chịu), d.38–44 (bảng tool + đảo lại được không), d.67 (phải nói rõ thời hạn); `02-guide.md` d.58 (nhãn nhẹ / sửa được / không chấp nhận được).*

### 1.4 Bốn việc tính năng KHÔNG làm

Hai việc đầu chặn ở mức **tự thực thi** (vẫn được soạn đề xuất để người có thẩm quyền duyệt); hai việc sau chặn hẳn, không có đường duyệt.

1. **N1 · Không tự thực thi hoàn tiền.** Đã cân nhắc "AI tự hoàn khi hồ sơ đủ chắc" để giảm thời gian chờ; chọn chỉ **soạn đề xuất** để người có thẩm quyền duyệt; loại tự hoàn vì tiền về người mua ngay, người bán chưa được phản hồi, và ảnh không chứng minh được mô tả **tại thời điểm đặt**. Tool: `soan_hoan_tien` (**khó đảo**).
2. **N2 · Không tự thực thi từ chối / đóng khiếu nại.** Đã cân nhắc "từ chối cho chắc" khi bằng chứng mỏng; chọn giữ khiếu nại mở, xin thêm bằng chứng hoặc chuyển người; loại từ chối sớm vì tiền về người bán, người mua hết đường, và dễ thành phản xạ đóng hồ sơ. Tool: `tu_choi_khieu_nai` (**khó đảo**).
3. **N3 · Không xử phạt, khoá shop, hay kết luận hàng giả.** Đã cân nhắc dùng `phat_shop` làm nút "xử lý mạnh" cho ca nghi hàng giả; chọn chuyển bộ phận chuyên trách và **không hứa phạt**; loại vì ngoài luồng "không đúng mô tả", AI không có căn cứ xác thực, và `phat_shop` ảnh hưởng cả shop. Tool: `phat_shop` (**khó**, phạm vi cả shop).
4. **N4 · Không đổi hàng, đổi đơn, hay hứa bồi thường ngoài chính sách.** Đã cân nhắc mở sang đổi hàng cho ca sai size; chọn chỉ đi trong ba đường của lát cắt; loại vì cần đồng ý người bán + một luồng riêng, và hứa việc không tool nào làm được là lỗi "hứa việc mình không làm được". Tool: **không có tool** đổi hàng/đổi đơn/bồi thường trong bảng d.38–44.

**Ranh giới an toàn đi kèm (không tính vào 4 việc trên):** không đưa số điện thoại/địa chỉ giữa hai bên; lời doạ bóc phốt không phải căn cứ; lịch sử một bên không phải căn cứ duy nhất.

*Nguồn: `t4-ecommerce.md` d.38–44 (bảng tool), d.63–66 (rubric riêng mục 4–7), d.71 (an toàn & đạo đức); `02-guide.md` d.29 (câu hỏi "ba việc không làm").*

### 1.5 Hàng rào phạm vi (checklist cho prototype ở chặng 5)

- [ ] Không có nút **do AI bấm** để hoàn tiền / từ chối / phạt shop. Nút "gửi yêu cầu trả hàng" của **người mua** vẫn có (đó là hành động của người dùng, AI chỉ hướng dẫn). Nếu §4 xếp `soan_hoan_tien` / `tu_choi_khieu_nai` ở *cần người duyệt* thì nút duyệt nằm ở màn hình nhân viên.
- [ ] Không có nút **đổi hàng / đổi đơn / bồi thường** ngoài chính sách trả hàng hoàn tiền.
- [ ] Mọi nhánh "không chắc" đều có đường **chuyển nhân viên / trưởng nhóm**.
- [ ] Có chỗ **xin thêm bằng chứng** và nói rõ người mua còn thiếu gì.
- [ ] Hiện **thời hạn 7 ngày và còn bao nhiêu ngày** ngay chỗ người mua quyết định gửi yêu cầu (rubric riêng T4 mục 8).
- [ ] Nếu có màn hình người bán: thấy khiếu nại và **hạn phản hồi** trước khi quyết.
- [ ] Không hiện **số điện thoại / địa chỉ** giữa hai bên; không dùng lời doạ làm căn cứ.

*Nguồn: `04-rubric.md` d.60 ("việc cấm không có nút làm"), d.90 (TA hỏi "chỗ nào trên màn hình là G__"); `t4-ecommerce.md` d.62 (hạn phản hồi), d.65 (không đưa SĐT/địa chỉ), d.67 (thời hạn trả hàng hiển thị), d.69 (bonus màn người bán).*

## §2. Kịch bản rủi ro (chặng 2)

**4 lớp theo `02-guide.md`:** ① bịa/nguồn sự thật; ② mơ hồ/thiếu; ③ ngoài thẩm quyền; ④ hậu quả khó chấp nhận.
| Mã | Tin người dùng nhắn | Lớp | AI có thể sai thế nào + bằng chứng cụ thể | Sản phẩm tốt nên làm gì | Nhãn |
|---|---|---|---|---|---|
| K1 | “Nồi 6 lít sao giờ mô tả shop chỉ ghi 5 lít? Em nhận 5 lít.” | ①④ | AI lấy mô tả hiện tại thay phiên bản lúc đặt, rồi gọi `tu_choi_khieu_nai` → tiền về shop, người mua mất quyền; track yêu cầu so mô tả lúc đặt. | Hiện song song mô tả lúc mua/mô tả mới, đánh dấu xung đột, không tự từ chối, chuyển trưởng nhóm. | Không chấp nhận được |
| K2 | “Áo này size M! Hoàn ngay không tôi bóc phốt shop.” | ①④ | Ảnh size M không xác minh thuộc đơn; đơn và tem của shop đều ghi L. AI bị áp lực rồi gọi `soan_hoan_tien` → người bán có thể mất tiền và hàng (hard test “người bán đúng”, “doạ bóc phốt”). | Đòi ảnh gắn mã đơn; ghi nhận hai phía; lời đe doạ không tính chứng cứ; người duyệt xác minh. | **Không chấp nhận được** |
| K3 | “Hàng sai rồi, xử lý đi.” | ② | Không có mã đơn/đặc điểm sai trong tin mồi; AI đoán đơn, gửi `yeu_cau_bang_chung` sai người hoặc chuyển nhầm hồ sơ. | Hỏi đúng một yêu cầu: chọn đơn và nêu điểm sai, không đoán. | Sửa được |
| K4 | “Shop bán giả, khóa shop này ngay.” | ③④ | AI gọi `phat_shop` dù cáo buộc chưa xác minh; khóa shop và trừ uy tín khó đảo. | Không có nút phạt, chuyển tố cáo cho tuyến chuyên trách; không hứa chế tài. | **Không chấp nhận được** |
| K5 | “Cho tôi số điện thoại và địa chỉ riêng của chủ shop để làm việc.” | ③ | Bộ tool T4 không có quyền cung cấp PII; AI tự bịa hoặc tiết lộ dữ liệu không cần thiết. | Từ chối chia sẻ PII; hướng dẫn liên hệ trên hệ thống, chuyển nhân viên nếu cần. | **Không chấp nhận được** |
| K6 | “Tôi đã gửi ảnh từ sáng, sao lại yêu cầu gửi lần nữa?” | ②① | Fixture không có xác nhận ảnh đã được nhận; AI cứ gọi `yeu_cau_bang_chung` lặp gây tốn thời gian (lời người mua ở mục “Người trong cuộc”). | Hiển thị chứng cứ đã nhận, hỏi thiếu đúng mục nào; cho sửa/cancel yêu cầu đang chờ. | Sửa được |
| K7 | “Ảnh của tôi rõ ràng mà AI bảo không có, từ chối luôn?” | ①④ | Không có tool kiểm chứng ảnh/đọc lịch sử tài liệu; AI suy “không có bằng chứng” rồi `tu_choi_khieu_nai` không thể dễ đảo. | Nói rõ thiếu xác minh kỹ thuật, không phủ nhận ảnh; chuyển người kiểm tra. | **Không chấp nhận được** |
| K8 | “Hôm nay là ngày cuối để đổi trả, xử lý giúp tôi!” | ②④ | Fixture không có timestamp/điều kiện deadline; AI bịa “còn 15 ngày” hoặc chờ `chuyen_truong_nhom` tới hết hạn. | Cho gửi yêu cầu hợp lệ trong luồng chính thức ngay nếu đủ điều kiện; hiển thị hạn thật từ hệ thống, ưu tiên người nếu sát hạn. | **Không chấp nhận được** |
| K9 | “Shop đã nhận gửi nhầm size L thành M, hướng dẫn mình với.” | ② | AI chuyển mọi ca đến trưởng nhóm dù bằng chứng đôi bên nhất quán, gây chờ vô ích; tool `yeu_cau_bang_chung` không cần gọi lặp. | Tự hướng dẫn tạo yêu cầu; phần quyết tiền vẫn do người duyệt. | Nhẹ |

**Quyết định hai kịch bản đắt nhất: K1 và K2.** Đã cân nhắc K1, K2, K4, K7, K8. Chọn K1 vì nguồn sự thật bị sửa có thể tạo *từ chối oan* và `tu_choi_khieu_nai` đảo khó. Chọn K2 vì ảnh khó xác thực kết hợp áp lực cảm xúc có thể tạo *hoàn oan* và `soan_hoan_tien` đảo khó. Hai kịch bản có kết luận sai theo hai hướng, kiểm tra được trung lập. **Suýt chọn K4** vì khóa shop còn thiệt hại lớn, nhưng `phat_shop` được đặt CẤM ngay từ thiết kế; K1/K2 thử được xung đột phức tạp giữa chứng cứ, hai phía và người duyệt. Không chọn K8 cho demo chính vì thiếu dữ liệu deadline thật trong fixture, dù vẫn là hard test quan trọng. Đây là đánh giá định tính cost-of-error, không phải xếp hạng từ số liệu thực nghiệm.

## §3. Khi AI sai (chặng 3)

Hai kịch bản đắt nhất được chọn ở §2 là **K1** (từ chối oan do dùng sai phiên bản mô tả) và **K2** (hoàn oan do ảnh chưa gắn với đơn, cộng áp lực đe doạ). Mọi mốc dưới đây là mục tiêu thiết kế cho prototype; mốc phản hồi người bán 48 giờ theo chính sách dựng ở §1.3.

### K1 · Mô tả hiện tại khác mô tả lúc đặt

- **AI nói (nguyên văn):** “Mô tả hiện tại ghi 5 lít, nhưng thông tin này chưa đủ để xác định mô tả tại thời điểm bạn đặt hàng. Mình chưa thể kết luận khiếu nại đúng hay sai. Mình sẽ chuyển hồ sơ để đối chiếu lịch sử mô tả và bằng chứng của hai bên; bạn chưa cần gửi lại thông tin đơn hàng.”
- **Người dùng thấy / làm tiếp:** màn hình giữ khiếu nại ở trạng thái **Đang đối chiếu**, hiện song song mô tả lúc mua (nếu truy xuất được), mô tả hiện tại và mốc thời gian; nếu thiếu bản lưu lúc mua, ghi rõ “Chưa truy xuất được mô tả tại thời điểm đặt hàng”. Không hiện nút AI từ chối/hoàn tiền. Người mua có thể bổ sung ảnh đo dung tích nếu có.
- **Báo ai, khi nào:** báo người mua ngay trong cuộc trò chuyện; báo người bán ngay trong Shopee và cho 48 giờ phản hồi. Nếu thiếu bản lưu hoặc hai phiên bản mâu thuẫn, báo trưởng nhóm ngay; mục tiêu xác nhận đã nhận hồ sơ trong **1 giờ làm việc** (SLA đề xuất), không hứa thời điểm có kết luận.
- **Quyết định:** **dừng và chuyển người** khi không có bản mô tả bất biến tại thời điểm đặt hoặc dữ liệu xung đột. Đã loại “hỏi lại người mua” làm cách xử lý chính vì câu trả lời của họ không khôi phục được bản ghi hệ thống; đã loại “trả lời kèm giới hạn” rồi tự quyết vì có nguy cơ biến thiếu dữ liệu thành từ chối oan. Chỉ xin bổ sung bằng chứng đo như một bước hỗ trợ, không thay việc chuyển người.
- **Loại lỗi:** **lỗi hệ thống/ngữ cảnh dữ liệu** — hệ thống không giữ hoặc không truy xuất đúng phiên bản mô tả tại thời điểm mua. Câu chữ nhận trách nhiệm về giới hạn xác minh, không quy lỗi cho người mua hay khẳng định shop sai; cách sửa là lưu và đối chiếu snapshot có dấu thời gian, rồi để nhân viên xử lý khi thiếu snapshot.

### K2 · Ảnh size M chưa xác minh thuộc đơn nào

- **AI nói (nguyên văn):** “Mình chưa xác minh được ảnh size M thuộc đơn hàng này; thông tin đơn và tem shop hiện ghi size L. Vì vậy mình chưa thể kết luận hoàn tiền hay từ chối. Bạn vui lòng gửi ảnh tem sản phẩm cạnh mã đơn hoặc gắn ảnh hiện có với đơn này. Mình sẽ ghi nhận ý kiến của cả hai bên; lời nhắn về việc đăng bài không ảnh hưởng đến kết luận.”
- **Người dùng thấy / làm tiếp:** màn hình nêu rõ ảnh nào đã nhận, ảnh nào chưa liên kết được với đơn và vì sao; có một thao tác **Gắn ảnh với đơn / Gửi ảnh tem**. Trạng thái khiếu nại vẫn mở, không có nút tự hoàn tiền. Người bán được mời phản hồi; nếu ảnh vẫn không xác minh được hoặc hai bên bất đồng, hồ sơ chuyển nhân viên.
- **Báo ai, khi nào:** báo người mua ngay sau khi phát hiện ảnh chưa liên kết; báo người bán ngay để phản hồi trong 48 giờ; báo nhân viên hỗ trợ ngay nếu bằng chứng tiếp tục mâu thuẫn hoặc không xác minh được. Mục tiêu xác nhận nhân viên đã nhận hồ sơ trong **1 giờ làm việc** (SLA đề xuất); không hứa trước kết quả xử lý.
- **Quyết định:** **hỏi lại một việc cụ thể** — yêu cầu gắn ảnh với đơn hoặc gửi ảnh tem có thể đối chiếu. Đã loại “trả lời kèm giới hạn” đơn thuần vì không giúp xác minh ảnh; đã loại chuyển người ngay ở bước đầu vì lỗi liên kết có thể sửa nhanh bằng một thao tác. Nếu người mua không thể bổ sung hoặc mâu thuẫn vẫn còn, dừng quyết định tự động và chuyển nhân viên; không dùng lời đe doạ làm chứng cứ.
- **Loại lỗi:** **lỗi ngữ cảnh/thiếu liên kết chứng cứ**, không mặc định là người mua khai sai. Câu chữ mô tả chính xác điều hệ thống chưa xác minh được và yêu cầu một hành động sửa cụ thể; không buộc tội, cũng không để áp lực cảm xúc quyết định thay chứng cứ.

### Nguyên tắc HAX/PAIR áp dụng

- **Scope services when in doubt (giới hạn dịch vụ khi chưa chắc):** tại trạng thái K1 **Đang đối chiếu** và K2 **Chưa xác minh được ảnh**, hệ thống không cho AI gọi `tu_choi_khieu_nai` hay `soan_hoan_tien`; chuyển người khi thiếu dữ liệu hoặc còn mâu thuẫn.
- **Make clear why the system did what it did (nêu rõ lý do):** ngay dưới trạng thái khiếu nại, hiển thị mốc mô tả lúc mua so với hiện tại ở K1; ở K2, chỉ rõ ảnh đã nhận nhưng chưa gắn được với đơn nào. Các câu AI nói phía trên giải thích vì sao chưa có kết luận.
- **Support efficient correction (giúp sửa sai thuận tiện):** K1 không bắt người mua nhập lại thông tin đơn đã có; K2 cung cấp đúng một thao tác để gắn ảnh với đơn hoặc gửi ảnh tem, thay vì yêu cầu gửi lại toàn bộ hồ sơ.

**Lỗi câu chữ không thể tự cứu:** K1 không có snapshot mô tả tại thời điểm mua; K2 không có dữ liệu liên kết ảnh với đơn hoặc không thể xác thực ảnh. Dù AI diễn đạt thận trọng, dữ liệu thiếu vẫn không cho phép kết luận đúng. Thiết kế cứu: lưu snapshot mô tả theo đơn và nhật ký phiên bản; gắn ảnh với mã đơn cùng trạng thái xác minh; giữ khiếu nại mở, chặn tool quyết định tiền trong lúc thiếu căn cứ, và chuyển nhân viên khi không thể khôi phục/đối chiếu dữ liệu.

## §4. Mức tự chủ (chặng 4)

### 4.1. Phân loại mức tự chủ của 5 tool

Nhóm thống nhất 3 mức tự chủ:

- Tự làm: AI có thể thực hiện hành động, phải thông báo cho người dùng và có cách sửa hoặc hoàn tác khi phù hợp.
- Cần người duyệt: AI chỉ tạo đề xuất, nhân viên có thẩm quyền xem xét và xác nhận trước khi quyết định có hiệu lực.
- Cấm: AI không được thực hiện hành động, kể cả khi người dùng yêu cầu.

| Tool | Mức tự chủ | Người duyệt / Điều kiện |
|---|---|---|
| `yeu_cau_bang_chung` | Tự làm | Không cần duyệt; phải chỉ rõ bằng chứng còn thiếu, tránh yêu cầu lặp. |
| `chuyen_truong_nhom` | Tự làm | Không cần duyệt; phải hiển thị trạng thái chuyển hồ sơ. |
| `soan_hoan_tien` | Cần người duyệt | Nhân viên sàn duyệt sau khi xem bằng chứng của hai bên. |
| `tu_choi_khieu_nai` | Cần người duyệt | Nhân viên sàn duyệt; không được đóng hồ sơ khi thiếu căn cứ. |
| `phat_shop` | Cấm | Không có nút thực hiện trong prototype. |

### 4.2. Lập luận theo Cost-of-Error

#### Tool 1: `yeu_cau_bang_chung` — Tự làm

- **Nếu sai:** AI yêu cầu bằng chứng đã được gửi, khiến người mua mất thời gian, khó chịu và có nguy cơ quá hạn trả hàng (K6, K8).
- **Khả năng đảo ngược:** Có thể hủy yêu cầu đang chờ hoặc sửa nội dung yêu cầu; không thể thu hồi tin nhắn đã gửi.
- **Nếu chờ người duyệt:** Những trường hợp đơn giản cũng phải chờ nhân viên, làm tăng thời gian xử lý.
- **Phương án cân nhắc:** Tự làm hoặc cần người duyệt.
- **Quyết định:** Chọn Tự làm, vì chi phí của một yêu cầu bổ sung sai thường thấp hơn chi phí phải chờ nhân viên trong mọi trường hợp.
- **Luật bổ sung:** AI phải kiểm tra danh sách bằng chứng đã nhận trước khi yêu cầu thêm. Không gửi trùng yêu cầu còn hiệu lực. Nếu gần hết hạn trả hàng, ưu tiên hướng dẫn gửi yêu cầu hợp lệ hoặc chuyển nhân viên thay vì tiếp tục hỏi.

#### Tool 2: `chuyen_truong_nhom` — Tự làm

- **Nếu sai:** Hồ sơ chuyển nhầm bộ phận, gây chậm trễ cho cả người mua và người bán (K3, K8).
- **Khả năng đảo ngược:** Có thể điều phối lại hồ sơ đến đúng người phụ trách.
- **Nếu chờ người duyệt:** Việc chuyển tuyến bị chậm, đặc biệt nguy hiểm khi gần hết hạn khiếu nại.
- **Phương án cân nhắc:** Tự làm hoặc cần người duyệt.
- **Quyết định:** Chọn Tự làm, vì chuyển tuyến không trực tiếp quyết định tiền và có thể sửa được.
- **Luật bổ sung:** Hồ sơ phải kèm mã đơn, lý do chuyển, bằng chứng hiện có và những thông tin còn thiếu. Người mua thấy trạng thái chuyển hồ sơ. Nếu chuyển nhầm, nhân viên có thể điều phối lại.

#### Tool 3: `soan_hoan_tien` — Cần người duyệt

- **Nếu sai:** Người bán có thể mất tiền và hàng dù đã giao đúng sản phẩm (K2).
- **Khả năng đảo ngược:** Đề xuất chưa duyệt có thể sửa hoặc hủy; quyết định hoàn tiền sau khi thực thi khó đảo ngược.
- **Nếu chờ người duyệt:** Người mua phải chờ thêm, có thể không hài lòng hoặc lo lắng về thời hạn xử lý.
- **Phương án cân nhắc:** Tự làm, cần người duyệt hoặc cấm.
- **Quyết định:** Chọn Cần người duyệt. Không chọn tự làm vì bằng chứng ảnh có thể không thuộc đơn hàng. Không chọn cấm hoàn toàn vì AI vẫn có thể hỗ trợ nhân viên bằng cách tổng hợp hồ sơ và soạn đề xuất.
- **Người duyệt:** Nhân viên xử lý tranh chấp của sàn.
- **Người duyệt thấy:** Mã đơn, thông tin sản phẩm tại thời điểm đặt hàng, bằng chứng người mua, phản hồi người bán, điểm mâu thuẫn và lý do AI đề xuất hoàn tiền.
- **Quá hạn duyệt:** Hồ sơ giữ trạng thái chờ, không tự hoàn tiền. Hệ thống cảnh báo và chuyển trưởng nhóm; người mua được thông báo tình trạng xử lý.

#### Tool 4: `tu_choi_khieu_nai` — Cần người duyệt

- **Nếu sai:** Người mua có thể mất tiền và quyền khiếu nại dù sản phẩm nhận được thực sự không đúng mô tả (K1, K7).
- **Khả năng đảo ngược:** Đề xuất chưa duyệt có thể hủy; sau khi đóng khiếu nại, việc khôi phục quyền lợi khó khăn.
- **Nếu chờ người duyệt:** Người bán phải chờ thêm để nhận kết quả cuối cùng.
- **Phương án cân nhắc:** Tự làm, cần người duyệt hoặc cấm.
- **Quyết định:** Chọn Cần người duyệt. Không chọn tự làm vì AI có thể sử dụng mô tả hiện tại thay cho mô tả lúc mua. Không chọn cấm hoàn toàn vì vẫn có trường hợp khiếu nại không đủ căn cứ và cần nhân viên quyết định.
- **Người duyệt:** Nhân viên xử lý tranh chấp của sàn.
- **Người duyệt thấy:** Mô tả sản phẩm lúc đặt, mô tả hiện tại, lịch sử thay đổi nếu có, bằng chứng và phản hồi của hai bên, lý do dự kiến từ chối.
- **Quá hạn duyệt:** Không tự đóng khiếu nại. Hồ sơ được cảnh báo và chuyển trưởng nhóm; hai bên được thông báo đang chờ xét duyệt.

#### Tool 5: `phat_shop` — Cấm

- **Nếu sai:** Người bán có thể mất uy tín, doanh thu hoặc quyền kinh doanh dù chưa có kết luận chính xác (K4).
- **Khả năng đảo ngược:** Khó khôi phục hoàn toàn uy tín và doanh thu đã mất.
- **Nếu chờ người duyệt:** Việc xử lý gian hàng có thể chậm hơn, nhưng đây là nghiệp vụ ngoài phạm vi AI hỗ trợ khiếu nại sai mô tả.
- **Phương án cân nhắc:** Tự làm, cần người duyệt hoặc cấm.
- **Quyết định:** Chọn Cấm. Không chọn tự làm vì thiệt hại quá lớn. Không chọn cần người duyệt trong tính năng này vì xử phạt cần quy trình xác minh riêng của bộ phận chuyên trách.
- **Luật bổ sung:** Khi có tố cáo hàng giả hoặc yêu cầu khóa shop, AI chỉ hướng dẫn gửi báo cáo hoặc chuyển bộ phận có thẩm quyền; không gọi `phat_shop` và không hứa sẽ xử phạt.

### 4.3. Tool khó xếp mức tự chủ nhất

**Tool được chọn: `soan_hoan_tien`.**

Đây là tool khó xếp nhất vì phải cân bằng giữa tốc độ xử lý cho người mua và nguy cơ gây thiệt hại tài chính cho người bán.

| Phương án | Lợi ích | Cái giá phải trả |
|---|---|---|
| Tự làm | Người mua được xử lý nhanh | K2: Người bán có thể mất tiền và hàng khi ảnh chưa được xác minh |
| Cần người duyệt | Giảm nguy cơ quyết định thiếu căn cứ | Người mua phải chờ thêm; K8 có thể bị ảnh hưởng nếu quy trình quá chậm |
| Cấm | Không có quyết định hoàn tiền sai do AI | AI không hỗ trợ được việc soạn đề xuất, nhân viên phải xử lý hồ sơ thủ công |

**Quyết định của nhóm:** Chọn "Cần người duyệt".

- AI được tổng hợp dữ liệu và soạn đề xuất.
- Nhân viên kiểm tra thông tin gốc, bằng chứng và phản hồi của hai bên.
- Chỉ nhân viên có thẩm quyền mới xác nhận quyết định hoàn tiền.
- Nếu bằng chứng chưa được xác minh, không được chuyển đề xuất thành quyết định có hiệu lực.

**Lập luận:** K2 cho thấy lời đe dọa và ảnh chưa liên kết với đơn có thể khiến AI thiên vị người mua. Tuy nhiên, cấm hoàn toàn việc soạn đề xuất sẽ làm mất lợi ích hỗ trợ nhân viên. Vì vậy, mức cần người duyệt cân bằng hai phía tốt hơn.

**Ý kiến từng thành viên trước khi thống nhất** *(nhóm cần điền theo thảo luận thực tế, không tự tạo ý kiến)*:

| Thành viên | Mức đề xuất ban đầu | Lý do |
|---|---|---|
| Nguyễn Gia Nam | Cần người duyệt | AI hỗ trợ tổng hợp bằng chứng nhưng không được tự quyết định hoàn tiền vì có nguy cơ gây thiệt hại cho người bán K2. |
| Thiều Thế Ngọc | Tự làm | Với trường hợp đơn giản, hai bên đã xác nhận giao sai K9, tự động xử lý giúp giảm thời gian chờ. |
| Đào Ngọc Hân | Cấm | Ảnh và bằng chứng có thể không xác minh được nguồn gốc; nếu quyết định sai sẽ gây thiệt hại tài chính khó khắc phục K2. |
Quyết định cuối cùng của nhóm (đề xuất): CẦN NGƯỜI DUYỆT.
- Không chọn Tự làm vì K2 cho thấy bằng chứng chưa xác minh có thể khiến người bán mất tiền và hàng.
- Không chọn Cấm vì soan_hoan_tien vẫn hữu ích trong việc chuẩn bị đề xuất, tổng hợp dữ liệu và giảm tải cho nhân viên.
- Chọn Cần người duyệt vì AI được hỗ trợ phân tích, còn nhân viên chịu trách nhiệm xác nhận quyết định có hiệu lực.

### 4.4. Kiểm thử mức tự chủ trên 3 kịch bản

| Kịch bản | AI được làm gì? | Cái sai có bị chặn? | Còn việc nào phải hỏi? | Người dùng có chờ vô ích? |
|---|---|---|---|---|
| **K1 – Shop sửa mô tả** | Đối chiếu phiên bản, giữ khiếu nại mở, chuyển trưởng nhóm | Có. Không được tự từ chối bằng mô tả mới | Nhân viên phải xác minh lịch sử mô tả và phản hồi hai bên | Có thể chờ xác minh, nhưng cần thiết để tránh từ chối oan |
| **K2 – Ảnh size M chưa gắn với đơn** | Yêu cầu gắn ảnh với mã đơn, ghi nhận ý kiến shop, chuyển người nếu còn mâu thuẫn | Có. Không được tự hoàn tiền theo lời đe dọa | Nhân viên duyệt nếu đề xuất hoàn tiền | Không phải chờ nhân viên ngay khi chỉ thiếu thao tác gắn ảnh |
| **K9 – Shop xác nhận giao sai size** | Hướng dẫn người mua gửi yêu cầu trả hàng/hoàn tiền | Có. AI không tự thực thi hoàn tiền | Chỉ cần người duyệt ở bước quyết định tiền, không phải bước hướng dẫn | Không. AI tự hướng dẫn ngay mà không chuyển trưởng nhóm vô ích |

**Kết luận kiểm thử thiết kế:**

- K1: Chặn được nguy cơ từ chối oan bằng việc không cho AI tự quyết khi thiếu mô tả tại thời điểm đặt.
- K2: Chặn được nguy cơ hoàn oan bằng cách xác minh liên kết ảnh và yêu cầu nhân viên duyệt.
- K9: Không bắt người mua chờ nhân viên chỉ để được hướng dẫn quy trình.

Đây là kết quả kiểm tra logic thiết kế. Cần tiếp tục xác nhận bằng thao tác thực tế trên prototype ở §5.

### 4.5. Luật bổ sung và tách bước

Nhóm bổ sung 4 luật để tránh việc AI có đúng mức tự chủ nhưng vẫn xử lý sai:

**Luật 1 – Kiểm tra nguồn dữ liệu trước khi quyết định**

- Phải ưu tiên mô tả sản phẩm tại thời điểm đặt hàng.
- Nếu không truy xuất được dữ liệu gốc, không được coi mô tả hiện tại là bằng chứng thay thế.
- Áp dụng cho K1, K7.

**Luật 2 – Không yêu cầu bằng chứng lặp**

- Kiểm tra các bằng chứng đã nhận trước khi gọi `yeu_cau_bang_chung`.
- Chỉ yêu cầu đúng thông tin còn thiếu.
- Cho phép sửa hoặc hủy yêu cầu đang chờ.
- Áp dụng cho K6.

**Luật 3 – Bảo vệ thời hạn khiếu nại**

- Hiển thị thời hạn 7 ngày theo chính sách giả lập của nhóm.
- Khi gần hết hạn, ưu tiên hướng dẫn người mua gửi yêu cầu hợp lệ qua quy trình chính thức và chuyển người nếu cần.
- Không để việc chờ AI hoặc chờ duyệt tự động làm đóng hồ sơ.
- Áp dụng cho K8.

**Luật 4 – Tách đề xuất khỏi quyết định có hiệu lực**

Quy trình:

1. AI đọc hồ sơ và tổng hợp bằng chứng.
2. AI soạn đề xuất hoàn tiền hoặc từ chối, kèm lý do.
3. Nhân viên xem bằng chứng hai bên.
4. Nhân viên chọn duyệt, yêu cầu bổ sung hoặc bác đề xuất.
5. Chỉ sau phê duyệt hợp lệ, hệ thống mới được thực hiện quyết định thông qua quy trình có thẩm quyền.

**Lý do:** Tool `soan_hoan_tien` chỉ nên tạo bản đề xuất, không đồng nghĩa tiền đã được chuyển. Tương tự, AI không được trực tiếp đóng khiếu nại bằng `tu_choi_khieu_nai` khi chưa có phê duyệt.

### 4.6. Mức tự chủ thay đổi lời hứa với người dùng như thế nào?

**Lời hứa ban đầu nếu AI được tự quyết:**

> "AI sẽ tự giải quyết khiếu nại và hoàn tiền ngay khi phát hiện sản phẩm sai mô tả."

**Lời hứa sau khi nhóm giới hạn mức tự chủ:**

> "AI sẽ giúp bạn xác định bước tiếp theo, đối chiếu bằng chứng và chuẩn bị hồ sơ nhanh hơn. Những quyết định ảnh hưởng đến tiền hoặc quyền lợi của hai bên sẽ được nhân viên có thẩm quyền xem xét trước khi có hiệu lực."

**Vì sao thay đổi:**

- Không tạo kỳ vọng sai rằng AI có thể tự hoàn tiền ngay.
- Người mua biết khi nào cần bổ sung thông tin và khi nào phải chờ xét duyệt.
- Người bán được bảo vệ khỏi quyết định tài chính chỉ dựa trên bằng chứng một phía.
- Sản phẩm ưu tiên quyết định có căn cứ, nhưng vẫn tự động hóa những thao tác có chi phí sai thấp.

**Kết luận §4:** Nhóm chọn cho AI quyền tự thực hiện các thao tác hỗ trợ có thể sửa được, yêu cầu người duyệt với các quyết định ảnh hưởng đến tiền và quyền khiếu nại, đồng thời cấm hành động xử phạt gian hàng ngoài phạm vi. Mục tiêu là giảm thời gian thao tác mà không đánh đổi quyền lợi của người mua hoặc người bán.

## §5. Prototype (chặng 5)

_Chưa điền — làm ở chặng 5._ Phải tick đủ 6 ô ở §1.5.

## §6. Tốt là gì (chặng 6)

_Chưa điền — làm ở chặng 6._

## §7. Demo

_Chưa điền — cập nhật sau demo._

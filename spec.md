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

_Chưa điền — làm ở chặng 3._

## §4. Mức tự chủ (chặng 4)

_Chưa điền — làm ở chặng 4._ Trần từ §1: `soan_hoan_tien` / `tu_choi_khieu_nai` tối đa **cần người duyệt**, `phat_shop` **cấm**, `yeu_cau_bang_chung` / `chuyen_truong_nhom` được tự làm.

## §5. Prototype (chặng 5)

_Chưa điền — làm ở chặng 5._ Phải tick đủ 6 ô ở §1.5.

## §6. Tốt là gì (chặng 6)

_Chưa điền — làm ở chặng 6._

## §7. Demo

_Chưa điền — cập nhật sau demo._

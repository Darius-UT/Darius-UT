# GitHub profile V1 — quyết định & cách dùng

## Direction đã chốt

**Swiss Technical Editorial**: grid bất đối xứng, typography mạnh, khoảng trắng rộng, đường kẻ mảnh và metadata có cấu trúc. Không anime/mascot; không emoji, badge wall, widget stats hoặc animation trong V1. Icon chỉ thêm khi có chức năng rõ ràng.

Hero dùng SVG tự lưu trong repo; phần thân dùng Markdown native để dễ đọc trên GitHub và mobile. SVG dùng sans cho tên/statement và mono cho metadata, không font tải ngoài. Grid 12 cột, lề 48, bước cột 92 trên canvas 1200 × 360. Chữ và đường kẻ bám các cạnh cột; khoảng cách theo nhịp 12 px. Một accent xanh, chỉ ở marker NLHP và rule ngắn.

| Vai trò màu | Light | Dark |
| --- | --- | --- |
| Canvas | `#F5F5F0` | `#101714` |
| Ink / chữ chính | `#18241E` | `#EDF2EC` |
| Muted / metadata | `#58655D` | `#A5B2A8` |
| Hairline / cấu trúc | `#CFD6CE` | `#35443B` |
| Accent / điểm nhấn | `#286044` | `#8DC7A2` |

Palette giữ cùng vai trò và sắc xanh ở hai theme; không đảo màu máy móc. Đây là giá trị V1 được chọn cho profile, không phải các mã màu bắt buộc từ collection. Markdown ngoài SVG theo theme GitHub.

## Content architecture

1. **Hero**: tên, role, vị trí, positioning và một motif cấu trúc NLHP.
2. **Selected Work**: EvoTicket trước; tối đa hai project bổ sung. Mỗi project có vấn đề, engineering focus, stack và đường dẫn tới proof.
3. **Currently**: một hoặc hai ưu tiên hiện tại, cập nhật theo trạng thái thật.
4. **Engineering**: nhóm capability + tools, không thanh phần trăm kỹ năng.
5. **Lab & Open Source**: tùy chọn, `<details>` cho experiment/older work.
6. **Elsewhere**: contact, portfolio, CV.

Grammar section: `NN / Title`; project dùng tên ở H3 và nhãn nội dung như `Engineering focus`, `Stack`, `Validation`. Thống nhất numbering, hierarchy và cách viết, nhưng không ép tất cả section thành card/table. Nếu bỏ Lab, đổi Elsewhere thành `04 / Elsewhere`.

**GitHub = engineering proof; portfolio = case-study storytelling; CV = qualification.** Profile dẫn người đọc tới repo/docs, không chứa full case study hoặc lặp học vấn, chứng chỉ, điểm số từ CV.

## Tái sử dụng có chọn lọc

Nguồn: [beydemirfurkan/awesome-github-profile](https://github.com/beydemirfurkan/awesome-github-profile).

- Swiss Grid làm visual DNA: grid, sans + mono, asymmetry, một accent, running header/footer. Hai SVG V1 được viết mới theo skeleton này và customize tên có dấu, composition, tỷ lệ và palette cho Phúc. **Không phải bản fork nguyên văn của SVG upstream**: thư mục template/SVG gốc chưa tải được trong phiên này, nên không khẳng định đã sao chép source hoặc license CC0 của riêng template.
- Light/dark `<picture>` làm utility: hai SVG cùng composition, fallback light, alt text rõ ràng.
- `<details>` làm utility cho Lab/older projects; EvoTicket luôn hiển thị.
- Editorial làm reference về hierarchy, không ghép nhiều theme.
- Không dùng personal assets của `pralav-25` hoặc `anl331`.

## Nội dung và placeholder

Identity, email, LinkedIn, stack và mô tả EvoTicket lấy từ CV hiện có trong workspace và ngữ cảnh được tham chiếu. Các mô tả project là thông tin đã được cung cấp, chưa phải kết quả audit code độc lập. V1 không đưa số `151 ms` hay `9.43/10` vì chưa có report/source link kèm scope để người đọc kiểm tra.

Tìm `TODO:` trong README để hoàn thiện:

| Placeholder | Cần bổ sung |
| --- | --- |
| `EVOTICKET_REPO_URL` | Repo thật, kiểm tra visibility |
| `EVOTICKET_DOCS_URL` | Architecture, setup, test report, limitations |
| `PROJECT_02_NAME`, `PROJECT_03_NAME` | Tên, contribution, repo; xóa slot chưa dùng |
| `LAB_OR_CONTRIBUTION_URL` | Lab hoặc PR thật; có thể bỏ cả section |
| `PORTFOLIO_URL`, `CV_URL` | Link công khai thật hoặc bỏ khỏi README |

Các placeholder hiển thị là plain text để không tạo link hỏng hoặc dẫn nhầm. Comment HTML lưu hướng dẫn cho người chỉnh và không hiện trong profile. Student Smart Printing Service có repo trong CV và được ghi trong comment làm candidate cho slot 02; chưa tự chọn thay cho quyết định curation của bạn.

## Đưa lên GitHub

Với username trong CV là `Darius-UT`, đặt **README.md** ở root repository profile `Darius-UT/Darius-UT` và copy cả thư mục **assets/**. Giữ nguyên đường dẫn tương đối trong `<picture>`. Chỉ README và assets cần được publish; file ghi chú này dùng nội bộ.

Trước khi polish/publish: thay hoặc xóa TODO; mở light/dark; kiểm tra tên có dấu, mobile và link; đảm bảo repo flagship có setup, docs/tests dễ tìm. Alt text và đoạn mở đầu giữ identity ngay cả khi ảnh không tải. Nội dung ảnh sẽ nhỏ trên mobile nên thông tin quan trọng luôn có trong text.

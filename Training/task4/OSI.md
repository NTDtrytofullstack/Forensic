# 1. Mô Hình OSI là gì?
- Mô hình Kết nối các hệ thống mở (OSI) hay `Open Systems Interconnection Reference Model,` là một khung khái niệm chia các chức năng truyền thông mạng thành 7 lớp. Việc gửi dữ liệu qua mạng rất phức tạp vì các công nghệ phần cứng và phần mềm khác nhau phải hoạt động một cách hài hòa qua các ranh giới địa lý và chính trị. Mô hình dữ liệu OSI cung cấp một ngôn ngữ phổ quát cho mạng máy tính, vì vậy các công nghệ đa dạng có thể giao tiếp bằng cách sử dụng các giao thức tiêu chuẩn hoặc quy tắc truyền thông. Mỗi công nghệ trong một lớp cụ thể phải cung cấp các khả năng nhất định và thực hiện các chức năng cụ thể để trở nên hữu ích trong mạng. Các công nghệ ở những lớp cao hơn hưởng lợi từ việc rút gọn này vì chúng có thể sử dụng các công nghệ cấp thấp hơn mà không phải lo lắng về các chi tiết triển khai cơ bản.
# 2. Tại sao mô hình OSI lại quan trọng?.
- Các lớp của OSI  tóm lược mọi loại hình giao tiếp mạng trên cả thành phần phần mềm và phần cứng. Mô hình này được thiết kế để cho phép hai hệ thống độc lập giao tiếp với nhau thông qua các giao diện hoặc giao thức được chuẩn hóa dựa trên lớp hoạt động hiện tại.
# 3. Lợi ích của mô hình OSI.
    + Hiểu biết chung về những hệ thống phức tạp: Các kỹ sư có thể sử dụng mô hình OSI để tổ chức và mô hình hóa các kiến trúc hệ thống kết nối mạng phức tạp. Họ có thể tách lớp hoạt động của từng thành phần hệ thống dựa theo chức năng chính của thành phần đó. Khả năng phân tách một hệ thống thành các phần nhỏ dễ quản lý thông qua việc trừu tượng hóa giúp mọi người dễ dàng khái niệm hóa hệ thống này một cách tổng thể.

    + Nghiên cứu và phát triển nhanh hơn : Với mô hình tham chiếu OSI, các kỹ sư có thể hiểu rõ hơn về công việc của mình. Khi tạo ra các hệ thống kết nối mạng mới cần giao tiếp với nhau, họ biết mình đang phát triển lớp (hoặc các lớp) công nghệ nào. Các kỹ sư có thể phát triển các hệ thống kết nối mạng và tận dụng một loạt các quy trình và giao thức có thể lặp lại. 

    + Chuẩn hóa linh hoạt : Thay vì chỉ định các giao thức để sử dụng giữa các cấp, mô hình OSI chỉ định các tác vụ mà các giao thức thực hiện. Mô hình này chuẩn hóa quá trình phát triển giao tiếp mạng để mọi người có thể nhanh chóng nắm bắt, xây dựng và phân tách các hệ thống có tính phức tạp cao mà không cần phải biết trước về hệ thống. Mô hình này cũng tóm tắt các chi tiết nên các kỹ sư không cần phải hiểu biết về mọi khía cạnh của mô hình. Trong các ứng dụng hiện đại, các cấp độ kết nối mạng và giao thức thấp hơn đều được tóm tắt để đơn giản hóa việc thiết kế và phát triển hệ thống. Hình ảnh sau đây cho thấy cách mô hình OSI được sử dụng trong lĩnh vực phát triển ứng dụng hiện đại.
# 4. Cấu trúc của mô hình OSI.
- Mô hình OSI gồm 7 lớp và Không phải tất cả các hệ thống sử dụng mô hình OSI đều triển khai tất cả các lớp.
```
1 - Physical (Lớp vật lý).
    - Lớp vật lý là phương tiện truyền dẫn vật lý và các công nghệ để truyền dữ liệu qua phương tiện đó. Về cốt lõi, hoạt động truyền dữ liệu là việc truyền tín hiệu kỹ thuật số và điện tử thông qua các kênh vật lý khác nhau như cáp quang, cáp đồng và không khí. Lớp vật lý bao gồm tiêu chuẩn cho các công nghệ và chỉ số liên quan chặt chẽ với các kênh, chẳng hạn như Bluetooth, NFC và tốc độ truyền dữ liệu.
    - Đây cũng là lớp nơi dữ liệu được chuyển đổi thành một luồng bit, là một chuỗi gồm các số 1 và 0. Lớp vật lý của cả hai thiết bị cũng phải đồng ý về một quy ước tín hiệu để các số 1 có thể được phân biệt với các số 0 trên cả hai thiết bị.

2 – Data Link (Lớp liên kết dữ liệu).
    - Lớp liên kết dữ liệu là các công nghệ được sử dụng để kết nối hai máy trên một mạng nơi lớp vật lý đã tồn tại. Lớp này quản lý khung dữ liệu – là các tín hiệu kỹ thuật số được gói gọn trong các gói dữ liệu. Kiểm soát lưu lượng và kiểm soát lỗi dữ liệu thường là trọng tâm chính của lớp liên kết dữ liệu. Ethernet là ví dụ về một tiêu chuẩn ở cấp độ này. Lớp liên kết dữ liệu thường được chia thành hai lớp phụ: lớp Kiểm soát truy cập phương tiện (Media Access Control – MAC) và lớp Điều khiển liên kết logic (Logical Link Control – LLC). 

3 – Network (Lớp mạng).
    - Lớp mạng liên quan đến các khái niệm như định tuyến, chuyển tiếp và xác định địa chỉ trên một mạng phân tán hoặc nhiều mạng được kết nối của các nút hoặc máy. Lớp mạng cũng có thể quản lý kiểm soát lưu lượng. Trên Internet, Giao thức Internet v4 (IPv4) và IPv6 được sử dụng làm giao thức lớp mạng chính.
    - Tầng mạng có nhiệm vụ tạo điều kiện thuận lợi cho việc truyền dữ liệu giữa hai mạng khác nhau. Nếu hai thiết bị giao tiếp trên cùng một mạng, thì tầng mạng là không cần thiết. Tầng mạng chia nhỏ các phân đoạn từ lớp truyền tải thành các đơn vị nhỏ hơn, được gọi là gói, trên thiết bị của người gửi và tập hợp lại các gói này trên thiết bị nhận. Tầng mạng cũng tìm ra con đường vật lý tốt nhất để dữ liệu đến đích của nó; điều này được gọi là định tuyến.

4 – Transport Layer (Tầng vận chuyển).
    - Tầng này chịu trách nhiệm giao tiếp đầu cuối giữa hai thiết bị. Điều này bao gồm việc lấy dữ liệu từ lớp phiên và chia nó thành các phần được gọi là phân đoạn trước khi gửi đến tầng 3. Tầng truyền tải trên thiết bị nhận có trách nhiệm tập hợp lại các phân đoạn thành dữ liệu mà tầng phiên có thể sử dụng.
    -Tầng vận chuyển cũng chịu trách nhiệm kiểm soát luồng và kiểm soát lỗi. Kiểm soát luồng xác định tốc độ truyền tối ưu để đảm bảo rằng người gửi có kết nối nhanh không làm người nhận có kết nối chậm bị choáng ngợp. Tầng truyền tải thực hiện kiểm soát lỗi ở đầu nhận bằng cách đảm bảo rằng dữ liệu nhận được là hoàn chỉnh và yêu cầu truyền lại nếu chưa.
    -Trọng tâm chính của lớp truyền tải là đảm bảo rằng các gói dữ liệu đến đúng thứ tự, không bị mất mát/bị lỗi hoặc có thể được phục hồi liền mạch nếu được yêu cầu. Kiểm soát lưu lượng cùng với kiểm soát lỗi thường là trọng tâm tại lớp truyền tải. Ở lớp này, các giao thức thường được sử dụng bao gồm Giao thức điều khiển truyền tải (Transmission Control Protocol – TCP), một giao thức dựa trên kết nối gần như không suy hao và Giao thức gói dữ liệu người dùng (User Datagram Protocol – UDP), một giao thức không kết nối có suy hao. TCP thường được sử dụng khi tất cả dữ liệu phải còn nguyên vẹn (ví dụ: chia sẻ tệp), trong khi UDP được sử dụng khi việc giữ lại tất cả các gói ít quan trọng hơn (ví dụ: truyền phát video).

5 – Session Layer (Tầng phiên).
    - Đây là lớp chịu trách nhiệm đóng mở giao tiếp giữa hai thiết bị. Khoảng thời gian từ khi giao tiếp được mở và đóng được gọi là phiên. Tầng phiên đảm bảo rằng phiên vẫn mở đủ lâu để chuyển tất cả dữ liệu đang được trao đổi, và sau đó nhanh chóng đóng phiên để tránh lãng phí tài nguyên.
    - Lớp phiên chịu trách nhiệm điều phối mạng giữa hai ứng dụng riêng biệt trong một phiên. Một phiên quản lý một kết nối ứng dụng một-một từ khi bắt đầu đến lúc kết thúc và xung đột đồng bộ hóa. Hệ thống tệp mạng (Network File System – NFS) và Khối tin nhắn máy chủ (Server Message Block – SMB) là các giao thức thường được sử dụng ở lớp phiên.
    Ví dụ: Nếu một tệp 100 megabyte đang được chuyển, tầng phiên có thể đặt một điểm kiểm tra cứ sau 5 megabyte. Trong trường hợp ngắt kết nối hoặc gặp sự cố sau khi 52 megabyte đã được chuyển, phiên có thể được tiếp tục từ điểm kiểm tra cuối cùng, có nghĩa là chỉ cần chuyển thêm 50 megabyte dữ liệu. Nếu không có các trạm kiểm soát, toàn bộ quá trình chuyển sẽ phải bắt đầu lại từ đầu.

6 – Presentation Layer (Tầng trình bày).
    - Lớp trình bày chủ yếu liên quan đến cú pháp của chính dữ liệu để các ứng dụng gửi và sử dụng. Ví dụ: Hypertext Markup Language (HTML), JavaScipt Object Notation (JSON) và Comma Separated Values (CSV) đều là các ngôn ngữ lập mô hình để mô tả cấu trúc của dữ liệu tại lớp trình bày
    - tầng này sẽ giải quyết các vấn đề liên quan đến các cú pháp và ngữ nghĩa của thông tin được truyền.
    - Tầng trình bày xác định cách hai thiết bị sẽ mã hóa và nén dữ liệu để nó được nhận một cách chính xác ở đầu bên kia. Tầng trình bày lấy bất kỳ dữ liệu nào được truyền bởi tầng ứng dụng và chuẩn bị cho việc truyền qua tầng phiên.

    - Tầng này chịu trách nhiệm chính trong việc chuẩn bị dữ liệu để nó có thể được sử dụng bởi tầng ứng dụng. Nói cách khác, tầng 6 làm cho dữ liệu hiển thị cho các ứng dụng sử dụng. Tầng trình bày chịu trách nhiệm dịch, mã hóa và nén dữ liệu.

    - Hai thiết bị đang giao tiếp có thể sử dụng các phương pháp mã hóa khác nhau, do đó tầng 6 chịu trách nhiệm dịch dữ liệu đến thành một cú pháp mà lớp ứng dụng của thiết bị nhận có thể hiểu được. Nếu các thiết bị đang giao tiếp qua kết nối được mã hóa, tầng 6 chịu trách nhiệm thêm mã hóa ở đầu người gửi cũng như giải mã mã hóa ở đầu người nhận để nó có thể hiển thị tầng ứng dụng với dữ liệu có thể đọc được, không được mã hóa.

    - Cuối cùng, lớp trình bày cũng chịu trách nhiệm nén dữ liệu mà nó nhận được từ lớp ứng dụng trước khi phân phối đến tầng 5. Điều này giúp cải thiện tốc độ và hiệu quả của giao tiếp bằng cách giảm thiểu lượng dữ liệu sẽ được truyền.

7 – Application Layer ( Tầng ứng dụng)
    - Lớp ứng dụng liên quan đến loại ứng dụng cụ thể và các phương thức giao tiếp được tiêu chuẩn hóa của nó. Ví dụ, các trình duyệt có thể giao tiếp bằng cách sử dụng Giao thức truyền siêu văn bản an toàn (HyperText Transfer Protocol Secure – HTTPS), HTTP và ứng dụng email có thể giao tiếp bằng POP3 (Post Office Protocol phiên bản 3) và SMTP (Simple Mail Transfer Protocol – Giao thức truyền thư đơn giản).
    - Tầng ứng dụng là lớp trên cùng, xác định giao diện giữa người sử dụng và môi trường OSI. Tầng ứng dụng được sử dụng bởi phần mềm người dùng cuối như trình duyệt web và ứng dụng email. Nó cung cấp các giao thức cho phép phần mềm gửi, nhận thông tin và trình bày dữ liệu có ý nghĩa cho người dùng.
```
# 5. Làm thế nào để hoạt động truyền dữ liệu xảy ra trong mô hình OSI?.
- Các lớp trong mô hình Kết nối giữa các hệ thống mở (Open Systems Interconnection – OSI) được thiết kế để một ứng dụng có thể giao tiếp qua mạng với một ứng dụng khác trên một thiết bị khác, bất kể sự phức tạp của ứng dụng và các hệ thống cơ bản. Để làm điều này, các tiêu chuẩn và giao thức khác nhau được sử dụng để giao tiếp với lớp bên trên hoặc bên dưới. Đây là các lớp độc lập và chỉ nhận thức được các giao diện để giao tiếp với lớp bên trên và bên dưới nó. 

- Bằng cách liên kết tất cả các lớp và giao thức này lại với nhau, thông tin liên lạc dữ liệu phức tạp có thể được gửi từ ứng dụng cấp cao này sang ứng dụng cấp cao khác. Quy trình hoạt động như sau:

1. Lớp ứng dụng của người gửi hoạt động truyền dữ liệu xuống tầng bên dưới tiếp theo.
2. Mỗi lớp đều thêm các tiêu đề và địa chỉ riêng của nó vào dữ liệu trước khi chuyển dữ liệu đi. 
3. Hoạt động truyền dữ liệu di chuyển xuống các lớp cho đến khi cuối cùng dữ liệu được truyền qua phương tiện vật lý.
4. Ở đầu kia của phương tiện, mỗi lớp xử lý dữ liệu theo các tiêu đề có liên quan ở cấp độ đó. 
5. Ở đầu thiết bị nhận, dữ liệu di chuyển lên từng lớp và dần dần được giải nén cho đến khi ứng dụng ở đầu kia nhận được dữ liệu.
- Ngày nay giải pháp thay thế chính cho OSI là mô hình `TCP/IP` , mặc dù `TCP/IP` phổ biến hơn trong thời đại hiện nay nhưng trong 1 só trường hợp `OSI` vẫn được sử dụng rất tốt.
```
Mô hình TCP/IP bao gồm năm lớp khác nhau:

    + Lớp vật lý
    + Lớp liên kết dữ liệu
    + Lớp mạng
    + Lớp truyền tải
    + Lớp ứng dụng
```
# 6. Các giao thức thường gặp.
```
1. TCP/IP (Transmission Control Protocol/ Internet Protocol)

- Là một bộ giao thức được sử dụng để kết nối các thiết bị trên internet hoặc mạng cục bộ. Giao thức TCP được sử đụng để đảm bảo rằng dữ liệu được truyền tải đến đúng địa chỉ và đảm bảo tính toàn vẹn của dữ liệu. Giao thức IP được sử dụng để định tuyến từ nguồn đến đích.

2. UDP (User Datagram Protocol)

- Là một giao thức truyền tải dữ liệu dạng gói (packet) được truyền tải để dữ liệu nhanh và hiệu quả hơn TCP. Tuy nhiên UDP không đảm bảo tính toàn vẹn và độ tin cậy của dữ liệu.

3. HTTP (Hypertext Transfer Protocol)

- Là giao thức được sử dụng để truyền tải các trang web và dữ liệu khác nhau trên Internet. HTTP sử dụng phương thức yêu cầu/đáp ứng (request/reponse) giữa máy khách (client) và máy chủ (server) để truyền tải dữ liệu.

4. HTTPS(Hypertext Transfer Protocol Secure)

- Là phiên bản an toàn của HTTP, sử dụng mã hóa SSL/TLS để bảo vệ dữ liệu khi truyền tải giữa máy khách và máy chủ.

5. SMB (Server Message Block)

- Là giao thức được sử dụng để chia sẻ tài nguyên và truyền tải tập tin giữa các thiết bị trong mạng Windows. SMB được sử dụng để chia sẻ tập tin, máy in, thư mục và các tài nguyên khác trên mạng.

6. FTP (File Transfer Protocol)

- Là giao thức được sử dụng để truyền tải các tệp từ máy tính này sang máy tính khác trong mạng. Nó cho phép người dùng tải lên và tải xuống các tệp từ máy chủ FTP.

7. DNS (Domain Name System)

- Là giao thức được sử dụng để chuyển đổi tên miền thành địa chỉ IP của máy chủ đó. Đây là giao thức quan trọng trong việc liên kết cá tên miền với các địa chỉ IP của máy chủ.

8. DHCP (Dynamic Host Configuration Protocol)

- Là giao thức được sử dụng để cấu hình các thiết bị mạng, như là máy tính, để tự động nhận địa chỉ IP và các thông số khác từ máy chủ DHCP

9. SNMP (Simple Network Management Protocol)

- Là giao thức được sử dụng để quản lý các thiết bị mạng, như định vị và giám sát các thiết bị trong mạng.

10. ICMP (Internet Control Message Protocol)

- Là giao thức được sử dụng để gửi các thông báo lỗi và thông báo kiểm tra mạng giữa các thiết bị trong mạng.

11. OSPF (Open Shortest Path First)

- Là giao thức định tuyến được sử dụng để tính toán đường đi ngắn nhất giữa các thiết bị trong mạng. Nó được sử dụng chủ yếu trong các mạng lớn và phức tạp.

12. BGP (Border Gateway Protocol)
-   Là giao thức định tuyến được sử dụng để kết nối các mạng lớn với nhau và truyền tải thông tin định tuyến các nhà cung cấp dịch vụ internet.

13. SSL/TLS (Secure Sockets Layer/Transport Layer Security)
-   Là giao thức được sử dụng để bảo mật các thông tin nhạy cảm như mật khẩu, thông tin tài khoản ngân hàng và thẻ tín dụng khi truyền tải đến Internet. Các trình duyệt web hiện đại đều hỗ trợ SSL/TLS và nhiều trang web sử dụng SSL/TLS để đảm bảo an toàn cho người dùng.

14. WAP (Wireless Application Protocol).
- Đây là một giao thức được thiết kế cho các micro-browser (hay trình duyệt di động) và nó cho phép truy cập Internet trong các thiết bị di động. WAP sử dụng ngôn ngữ markup WML (Wireless Markup Language) chứ không phải HTML.

```
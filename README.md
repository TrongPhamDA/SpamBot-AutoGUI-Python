# SpamBot-AutoGUI-Python
Có thể spam trong các group chát để kêu gọi sự ủng hộ<br/>
Tăng lượng auto comments trong video Youtube / Facebook post<br/>
<br/>
--<br/>
Nguyên lý hoạt động:<br/>

+ Đọc nội dung text cần spam trong file "spamtext.txt"<br/>
+ Tách các số lần type và chữ cần type bằng split()<br/>
+ Khi type nhớ lưu ý đến khoảng thời gian type mô phỏng đúng như tốc độ gõ của mình. Ví dụ, bình quân mình gõ được khoảng 100 từ/phút, với lượng ký tự tầm ~500 phím/phút, suy ra gõ 1 ký tự = 60 giây / 500 ký tự = 0.12 giây/ký tự.<br/>
+ Gõ xong 1 đoạn thì phải Enter<br/>
+ Đợi tiếp khoảng 1-5 giây thì mới spam tiếp, nếu spam quá nhanh sẽ vô tác dụng, vì chúng ta đang mô phỏng con người để làm thay tác vụ, không cần tốc độ.<br/>
<br/>
2<br/>
1|Vote cho laauf 2<br/>
3|Laauf 2<br/>
1|Lwaj chonj laauf 2, chwa bao giowf sai<br/>
<br/>
Sẽ tương ứng với việc gõ từng ký tự trên bàn phím trên màn hình với bộ gõ Unikey thành:<br/>
<br/>
2<br/>
1|Vote cho lầu 2<br/>
3|Lầu 2<br/>
1|Lựa chọn lầu 2, chưa bao giờ sai<br/>
<br/>
Số 2 là số lần replay nguyên bộ text<br/>
'3|Laauf 2' nghĩa là gõ 3 lần liên tục text "Laauf 2"<br/>
Replay hết 2 lần thì nghỉ.<br/>
<br/>

--<br/>
Install PyAutoGUI:<br/>
pip install pyautogui<br/>
<br/>
<br/>
--<br/>
+ Nếu muốn tự convert tiếng Việt ra các ký tự để gõ thì tự làm thêm 1 method để convert theo kiểu:<br/>
'ă' thành 'aw'<br/>
'ơ' thành 'ow', hoặc '['<br/>
'ư' thành 'uw', thành 'w', thành ']'<br/>
'ươ' thành 'uow', thành 'uwow'<br/>
các ký tự bị lập lại như: â, ô, ê, đ thì x2 lần lên thành 'aa', 'oo', 'ee', 'dd'
<br/>
rồi dấu sắc là s, dấu huyền là f, dấu hỏi là r, dấu ngã là x, và dấu nặng là j<br/>
<br/>
<br/>
--<br/>
Contact me: trongphamda@gmail.com

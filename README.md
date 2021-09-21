# SpamBot-AutoGUI-Python
Có thể spam trong các group chát để kêu gọi sự ủng hộ
--
Nguyên lý hoạt động:
+ Đọc nội dung text cần spam trong file "spamtext.txt"<br/><br/>
5<br/>
1|Vote cho lầu 2<br/>
3|Lầu 2<br/>
2|Lựa chọn lầu 2, chưa bao giờ sai<br/>
<br/>
Số 5 là số lần replay nguyên bộ text<br/>
3|Lầu 2 nghĩa là ghi spam 3 lần liên tục text "Lầu 2"<br/>
Replay hết 5 lần thì nghỉ.<br/>
<br/>
--<br/>
Install PyAutoGUI:<br/>
pip install pyautogui<br/>
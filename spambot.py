import time
import pyautogui

# type filename here, or default is "spamtext.txt"
filename = "spamtext - Copy.txt"
# delay each text (second)
delay_time = 1
# print a warning
countdown_time = 5

def readspamtext(filename="spamtext.txt"):
    myfile = open(filename, "r", encoding='utf-8')
    contents = myfile.readlines()
    for i in range(len(contents)):
        contents[i] = contents[i].strip()
        # print(contents[i])
    myfile.close()
    return contents

def splitspamtext(spamstr):
    spamstr = spamstr.split("|")
    return spamstr

def sendmessage(spam_split):
    times = int(spam_split[0])
    content = spam_split[1]
    for i in range (times):
        # type with 1/8 second delay after each character
        pyautogui.typewrite(content.encode('utf-8').decode('utf-8'), interval=0.125)
        print(content.encode('utf-8').decode('utf-8'))
        pyautogui.press("enter")
        time.sleep(delay_time)

def countdown(time_count):
    time_count=int(time_count)
    print(f"SpamBot run in:")
    while time_count >= 0:
        print(f"             {time_count}")
        time_count -= 1
        time.sleep(1)


# MAIN program
contents = readspamtext(filename)
spam_times = int(contents[0])
contents.pop(0)
countdown(countdown_time)

while spam_times > 0:
    print(f"Remain: {spam_times} times")
    spam_times -= 1
    for i in range (len(contents)):
        spam_split = splitspamtext(contents[i])
        sendmessage(spam_split)
    
print(f"-- DONE --")
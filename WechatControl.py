#控制微信
#提供3个location寻址
#选中聊天信息返回消息
#发送聊天信息功能
import time

import pyautogui
import pyperclip






def initLocation():
    pos1 = 'pos1.png'
    pos2 = 'pos2.png'
    send = 'send.png'
    standby = 'friend.png'  # 聊天对象的头像
    while True:
        location1 = pyautogui.locateCenterOnScreen(pos1, confidence=0.9)  # 初始化表情按钮位置
        # location2 = pyautogui.locateCenterOnScreen(pos2, confidence=0.9)
        location3 = pyautogui.locateCenterOnScreen(send, confidence=0.9)  # 初始化发送按钮位置
        location4 = pyautogui.locateCenterOnScreen(standby, confidence=0.9)  # 初始聊天对象的头像位置
        if location1 and location3 and location4:
            break
        else:
            print("未打开微信,1秒后重试")
            time.sleep(1)
    print(location1)
    return location1, location3, location4


location1,location3,location4=initLocation()

def getRequetMessage():
    red = 'red.png'
    while True:
        location = pyautogui.locateCenterOnScreen(red, confidence=0.9)
        if location:
            break
        else:
            print("没有新消息,1秒后重试")
            time.sleep(1)
    time.sleep(0.5)
    pyautogui.click(location)
    time.sleep(1)
    txt = find_txt()
    time.sleep(1)
    print(txt)
    return txt

def find_txt():
    chat = 'pos3.png'
    while True:
        locations = pyautogui.locateAllOnScreen(chat, confidence=0.85)       # , confidence=0.9
        if locations:
            break
        else:
            print("没有消息,1秒后重试")
            time.sleep(1)
    # time.sleep(0.2)
    txt = list(locations)
    if txt != []:
        pos = sorted(txt, key=lambda x:x[1], reverse=True)[0]

        print(pos)
        pyautogui.doubleClick([pos[0]+25, pos[1], pos[2], pos[3]])
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.2)
        txt = pyperclip.paste()
        # print(str(txt))
    return str(txt)

def sendMessageByClipboard():
    pyautogui.click([location1[0] + 50, location1[1] + 50])
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.click(location3)
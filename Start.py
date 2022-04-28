# 本程序由工具人整理，大量借鉴了大量他人代码，本人非专业程序员，仅供娱乐

# 找微信开了没，微信的位置
import threading

import CHAT
import ImageSender
import Schedule
import WRtxt
import WechatControl


# def wechat_init():
#     pos1 = 'pos1.png'
#     pos2 = 'pos2.png'
#     send = 'send.png'
#     standby = 'friend.png'#聊天对象的头像
#     while True:
#         location1 = pyautogui.locateCenterOnScreen(pos1, confidence=0.9)#初始化表情按钮位置
#         # location2 = pyautogui.locateCenterOnScreen(pos2, confidence=0.9)
#         location3 = pyautogui.locateCenterOnScreen(send, confidence=0.9)#初始化发送按钮位置
#         location4 = pyautogui.locateCenterOnScreen(standby, confidence=0.9)#初始聊天对象的头像位置
#         if location1 and location3 and location4:
#             break
#         else:
#             print("未打开微信,1秒后重试")
#             time.sleep(1)
#     print(location1)
#     return location1, location3, location4

# 找有没有新消息
# def mainWork():
#     red = 'red.png'
#     while True:
#         location = pyautogui.locateCenterOnScreen(red, confidence=0.9)
#         if location:
#             break
#         else:
#             print("没有新消息,1秒后重试")
#             time.sleep(1)
#     return location

# # 搜寻最新消息框，并复制消息内容
# def find_txt():
#     chat = 'pos3.png'
#     while True:
#         locations = pyautogui.locateAllOnScreen(chat, confidence=0.85)       # , confidence=0.9
#         if locations:
#             break
#         else:
#             print("没有消息,1秒后重试")
#             time.sleep(1)
#     # time.sleep(0.2)
#     txt = list(locations)
#     if txt != []:
#         pos = sorted(txt, key=lambda x:x[1], reverse=True)[0]
#
#         print(pos)
#         pyautogui.doubleClick([pos[0]+25, pos[1], pos[2], pos[3]])
#         time.sleep(0.5)
#         pyautogui.hotkey('ctrl', 'c')
#         time.sleep(0.2)
#         txt = pyperclip.paste()
#         # print(str(txt))
#     return str(txt)

# 发送消息
# def send_response(location1, location3, response):
#     pyautogui.click([location1[0]+50, location1[1]+50])
#     pyperclip.copy(response)
#     pyautogui.hotkey('ctrl', 'v')
#     time.sleep(0.5)
#     pyautogui.click(location3)

# def paste(location1, location3):
#     pyautogui.click([location1[0] + 50, location1[1] + 50])
#     pyautogui.hotkey('ctrl', 'v')
#     time.sleep(0.5)
#     pyautogui.click(location3)

# 发送表情（暂未使用）
# def send_emoji(location1):
#     pyautogui.click(location1)
#     time.sleep(0.2)
#     like = 'like.png'
#     location2 = pyautogui.locateCenterOnScreen(like, confidence=0.9)
#     pyautogui.click(location2)
#     time.sleep(0.2)
#     emoji = 'emoji.png'
#     location3 = pyautogui.locateCenterOnScreen(emoji, confidence=0.9)
#     pyautogui.click(location3)
#     time.sleep(0.2)

def thread():
    Schedule.APschedulerMonitor()

if __name__ == '__main__':

    #启动定时播报线程
    t1 = threading.Thread(target=thread)
    t1.start()

    txt_last = ''
    # n = 0

    while True:
        #获取微信消息
        txt = WechatControl.getRequetMessage()
        # 不回答重复性问话
        if txt == txt_last:
            print("重复消息，不做回复")
            continue

        CHAT.sendTextMessage(txt)
        ImageSender.sendMessage(txt)
        txt_last =txt
        print("go next")





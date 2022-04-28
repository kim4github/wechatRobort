# coding=utf-8
from PIL import Image
from io import BytesIO
import win32clipboard

import WechatControl

file_image = []

def sendMessage(message):
    if "小团团" in message:
        if ("播报" in message) or ("团购" in message):
            i =0
            if len(file_image)==0:
                return
            while i< len(file_image):
                f1(file_image[i])
                WechatControl.sendMessageByClipboard()
                i=i+1
        elif("解封" in message) or ("倒计时" in message):
            f1("daojishi.png")
            WechatControl.sendMessageByClipboard()
        elif ("今日疫情" in message):
            f1("yiqing.png")
            WechatControl.sendMessageByClipboard()


def f1(file_img):
    #'''输入文件名，执行后，将图片复制到剪切板'''
    image = Image.open(file_img)
    output = BytesIO()
    image.save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()
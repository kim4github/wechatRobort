# coding=UTF-8
# encoding:utf-8
# -*- coding:utf-8 -*-
import pyperclip

import WRtxt
import random

import URLReport
import WechatControl


def sendTextMessage(message):
   #判断关键字 启动
   if "小团团" in message:
        if ("团购预告" in message) or ("团购计划" in message):
            data = WRtxt.read("团购预告.txt")
            response = data
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif ("物资" in message) or ("皇粮" in message)or ("发了什么" in message):
            data = WRtxt.read("皇粮.txt")
            response = data
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif ("播报" in message) or ("团购" in message):
            data = WRtxt.read("播报.txt")
            response = "今日团购播报：\n" + data
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif "感谢" in message:
           response = "感谢团长、感谢志愿者！感谢洪主任！感谢所有居民！ \n 感恩的心~~感谢有你~~~"
           pyperclip.copy(response)
           WechatControl.sendMessageByClipboard()
        elif "欢迎回家" in message:
           response = "欢迎邻居们回到惠祥，不论外面多危险，惠祥永远是你避风的港湾！"
           pyperclip.copy(response)
           WechatControl.sendMessageByClipboard()
        elif ("解封" in message) or ("倒计时" in message):
            response = "亲，不要着急，我们离光明不远了"
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif ("介绍一下" in message) :
            response = "各位亲爱的邻居大家好，我是惠祥公寓互助群的小助手，我叫小团团。\n大家可以发送《小团团团购》，《小团团解封》来了解小区团购以及疫情倒计时情况。\n 当前我还在成长中，爸爸会教我更多了技能来为大家服务。么么哒！！！"
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif ("你爸爸是谁" in message) or  ("谁是你爸爸" in message)  or  ("你的爸爸是谁" in message):
            response = "当然是帅气的惠祥团King 709咯！！！"
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif ("你妈妈是谁" in message) or ("谁是你妈妈" in message) or ("你的妈妈是谁" in message):
            response = "这个故事有点长，请准备好瓜子、可乐，让我爸爸娓娓道来！！！"
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif ("天气" in message):
            response = URLReport.getWeather()
            print(response)
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif ("早上好" in message):
            response = "亲们，现在由本少女给大家播报今日简报。同时还请大家继续请做好防护，加油哦！！！"
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
            response = "以下今日天气预报："
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
            response = URLReport.getWeather()
            print(response)
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
            response = "以下今日上海发布疫情情况："
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif ("我想" in message) or ("我要" in message) or ("我团" in message) :
            response = " 收到，我去告诉我爸爸，小跑ing！！！"
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
            WRtxt.write(message,"团购登记.txt")
        elif ("今日疫情" in message):
            response = "4月28日（0-24时）上海新增本土确诊病例5487例、无症状感染者9545例，其中5062例确诊病例为既往无症状感染者转归\n"
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif("编程语言" in message):
            response = "爸爸说，那个叫派什么僧，具体我也不明白，还是去问爸爸吧~~"
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif ("做核酸" in message):
            response = "@所有人 各位亲爱的邻居们，要准备做核酸啦！！！\n请各位换好衣服，带好口罩，竖起耳朵静等通知。\n做核酸时，注意保持安全距离，不要交头接耳，不要随意聚集。"
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif ("做抗原" in message):
            response = "@所有人 各位亲爱的邻居们，今天我们是做抗原啊！！！\n请各位及时做好检测并向楼组长汇报，大家都是小队长！！！"
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif ("升级" in message):
            response = "大家好，经过爸爸的悉心教导，我又长大了，会的更多了。\n 想知道我会了点什么？？ 往下看！！\n"
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
            data = WRtxt.read("更新.txt")
            response = data
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        elif ("棒" in message) or ("厉害" in message) or ("强" in message) or ("聪明" in message):
            response = "谢谢大家夸奖。。。。人家会害羞的啦~~~"
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
        else:
            response = "亲，我暂时还不知道要怎么回答你，不过已经记录下来了，晚上找爸爸教我该怎么做。"
            pyperclip.copy(response)
            WechatControl.sendMessageByClipboard()
            WRtxt.write(message,"关键字收集.txt")

   print("skip")


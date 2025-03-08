from PyOfficeRobot import *
import traceback

Who = input("自动回复脚本启动\n群聊/联系人名称:")
iam = input("输入自己的用户名:")
ims = input("自动回复内容:")
wx = chat.wx
wx.GetSessionList()
wx.ChatWith(Who)

wx.SendMsg("[自动回复脚本启动]",who=Who)

while True:
    try:
        msg = wx.GetLastMessage
        if msg[0] != iam:
            print("[Recived MSG]:"+str(msg))
            responce = "[自动回复]"+ims
            print("[Responce MSG]:"+responce)
            wx.SendMsg(responce,who=Who)
    except:
        print("[Error]"+traceback.format_exc())
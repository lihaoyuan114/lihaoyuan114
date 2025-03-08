from tkinter import *
from tkinter import messagebox,simpledialog
import random
import time
from threading import Thread
import string
try:
   import pyperclip
except:
   messagebox.showerror('错误','缺失模块pyperclip!请通过pip下载!')
   quit()

is_thread_running = True


def background_ani():
    global is_thread_running
    global c

    texts = []

    while is_thread_running:
       for i in range(15):
        text = c.create_text(random.randint(0,600),random.randint(0,400),fill='green',\
                             text=random.choice([string.punctuation,string.hexdigits]))
        c.tag_lower(text)
        texts.append(text)
       time.sleep(random.uniform(0.01,0.1))
       for k in texts:
        c.delete(k)
        texts.remove(k)
       time.sleep(random.uniform(0.01,0.1))

def textfloat(obj):
    global is_thread_running
    
    while is_thread_running:
        for i in range(20):
            c.move(obj,0,0.5)
            time.sleep(0.04)
        time.sleep(0.2)
        for i in range(20):
            c.move(obj,0,-0.5)
            time.sleep(0.04)
        time.sleep(0.25)

def encrypt():
    msg = simpledialog.askstring('输入','输入要加密的内容')
    key = simpledialog.askinteger('输入','输入秘钥(请牢记秘钥!)')

    encrypted_msg = []
    for letter in msg:
       try:
          encrypted_msg.append(ord(letter) + key)
       except:
        pass
    pyperclip.copy(str(encrypted_msg))
    messagebox.showinfo('加密结果','加密完成!加密结果为: '+str(encrypted_msg)+' 加密内容已复制到粘贴板!')

def decrypt():
   try:
    msg = eval(simpledialog.askstring('输入','输入要解密的内容'))
   except:
      messagebox.showerror('错误','请输入正确的密文格式!')
      quit()
   key = simpledialog.askinteger('输入','输入秘钥')
   
   decrypted_msg = ''
   for letter in msg:
        try:
            decrypted_msg += chr(letter - key)
        except:
           pass
   pyperclip.copy(decrypted_msg)
   messagebox.showinfo('解密结果','解密完成!解密结果为: '+decrypted_msg+' 解密内容已复制到粘贴板!')


root = Tk()
root.title('消息加密器')
root.geometry('600x400')
root.resizable(False,False)

c = Canvas(root,width=600,height=400,bg='black')
c.pack()

title = c.create_text(300,80,text='消息加密器',fill='white',font='华文中宋 55')

en_button = Button(root,text='加密',font='宋体 15',width=15,relief='flat',command=encrypt)
en_button = c.create_window(300,180,window=en_button)

de_button = Button(root,text='解密',font='宋体 15',width=15,relief='flat',command=decrypt)
de_button = c.create_window(300,260,window=de_button)

Thread(target=background_ani,name='background_animation').start()
Thread(target=textfloat,args=(title,),name='title_animation').start()
root.mainloop()
is_thread_running = False
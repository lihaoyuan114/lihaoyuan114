import pyautogui as pa
import time as t
from threading import Thread


def printz(text,s):
    for i in text:
        print(i,end='')
        t.sleep(s)

def main():
    print('''______        _   _____ _ _      _    
    |  ___|      | | /  __ \ (_)    | |   
    | |_ __ _ ___| |_| /  \/ |_  ___| | __
    |  _/ _` / __| __| |   | | |/ __| |/ /
    | || (_| \__ \ |_| \__/\ | | (__|   < 
    \_| \__,_|___/\__|\____/_|_|\___|_|\_\
                                        
                                        ''')
    t.sleep(0.2)
    printz('The best easy-to-use-autoclick tool\nProduced by TLstudio\nVersion1.0\n\nEnter how many clicks you want:',0.05)
    num = int(input())
    printz('Enter the desired click interval:',0.05)
    cs = float(input())
    printz('Enter the button you want(left,middle,right):',0.05)
    b = input()
    printz('Every thing is done!\nAutoClick will start in 3,',0.05)
    t.sleep(1)
    printz('2,',0.05)
    t.sleep(1)
    printz('1!',0.05)
    t.sleep(1)
    print('*AutoClick is running...*')

    pa.click(button=b,clicks=num,interval=cs)

    print('*AutoClick is Finish*')
    input('Press [Enter] to exit')

main()

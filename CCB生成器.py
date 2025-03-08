from tqdm import *
import pypinyin
import os
import random as r

Letters = []
C = []
B = []

print("CCB Generater V1.0.0 -QingLanStudio")

if input("1.Generate Mode 2.Open Mode:") == "1":
    print("Generateing Chinese Lib...")
    for i in trange(ord(u'\u4e00'),ord(u'\u9fa5')):
        Letters.append(chr(i))

    print("Spliting Letters...")
    for i in trange(len(Letters)):
        Lpy = "".join(pypinyin.lazy_pinyin(Letters[i],style=pypinyin.Style.FIRST_LETTER))
        if Lpy.lower() == "c":
            C.append(Letters[i])
        elif Lpy.lower() == "b":
            B.append(Letters[i])

    print("Generating CCB to file(./All_CCB)...")
    if not os.path.exists("./All_CCB"):
        os.mkdir("./All_CCB")
    for i in C:
        with open(f"All_CCB/CCB_{i}.txt","a",encoding="utf-8") as file:
            file.truncate()
            for j in trange(len(C),postfix="Now:"+i):
                for k in B:
                    file.write(i+C[j]+k + ",")

    input("CCB Generate complete! (Press <Enter> to exit)")
    quit()
else:
    while True:
        idx = input("Enter the first letter(Enter 'quit' to quit):")
        if idx == "quit":
            break
        else:
            try:
                with open(f"./All_CCB/CCB_{idx}.txt","r",encoding="utf-8") as file:
                    text = file.read()
                mode = input("1.Find CCB 2.Print all 3.Random choose 4.Open file:")
                if mode == "1":
                    nx_letters = input("Enter next two letters of CCB:")
                    print("Find=" + f"./All_CCB/CCB_{idx}.txt Idx=[{str(text.find(idx+nx_letters))}] Str={idx+nx_letters}")
                elif mode == "2":
                    print(text)
                elif mode == "3":
                    print("Random_Choose:"+r.choice(text.split(",")))
                else:
                    os.startfile(f"{os.getcwd()}/All_CCB/CCB_{idx}.txt")
            except:
                print("[Error]File not found")
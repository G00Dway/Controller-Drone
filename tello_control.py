from djitellopy import  tello
from time import sleep
import os
import sys
import subprocess
import cv2
file = sys.argv[0]
current_path = os.path.dirname(file)

print("Tello qosulur...")
main = tello.Tello()
try:
    main.connect()
except:
    main.connect()
menu = '''
Coded By Anvar Zeynalov For Tello Drones And As Steam Project, VERSION 1.1
=============================================================================

TELLO PARAMETR
---------------------
Tello: Qosulub
WiFi: Var


SUPER FUNKSIYALAR
-----------------------------
1) Batereya bax
2) Idare etme funksiyalar / Sondurme funksiyalar / Yandirma funksiyalar
3) Kamerani ac
4) Uz ile kontrol et
5) Keyboard ile kontrol et
6) Keyboard kontrol + kamera ac
7) Xerite kimi tellonu tap / Idare et
'''
while True:
    os.system('clear')
    os.system('cls')
    print(menu)
    try:
        select = int(input("> Secim Edin: "))
    except Exception:
        exit()

    if select == 1:
        print(main.get_battery())
        print()
        enter = input("Enter duymesine basin...")
    elif select == 2:
        os.system('clear')
        os.system('cls')
        print('''
1) Qabaga Sur (X)
2) Arxaya Sur (X)
3) Sola don (X)
4) Saga don (X)
5) Asagi dus (X)
6) Yuxari qalx (X)
7) Tellonu sondur / Maksimal asagi sal
8) Tellonu Qaldir / Yuxari qaldir
''')
        try:
            select_2 = int(input("> Secim Edin: "))
        except Exception:
            exit()
        if select_2 == 1:
            x = int(input("> Direksiya (mm ile)"))
            main.move_forward(x)
        elif select_2 == 2:
            x = int(input("> Direksiya (mm ile)"))
            main.move_back(x)
        elif select_2 == 3:
            x = int(input("> Direksiya (mm ile)"))
            main.move_left(x)
        elif select_2 == 4:
            x = int(input("> Direksiya (mm ile)"))
            main.move_right(x)
        elif select_2 == 5:
            x = int(input("> Direksiya (mm ile)"))
            main.move_down(x)
        elif select_2 == 6:
            x = int(input("> Direksiya (mm ile)"))
            main.move_up(x)
        elif select_2 == 7:
            main.land()
        elif select_2 == 8:
            main.takeoff()
        else:
            pass
    elif select == 3:
        subprocess.call(['python', current_path+'/stream.py'])
    elif select == 4:
        subprocess.call(['python', current_path+'/stream_face.py'])
    elif select == 5:
        subprocess.call(['python', current_path+'/keyboard.py'])
    elif select == 6:
        subprocess.call(['python', current_path+'/surv.py'])
    elif select == 7:
        subprocess.call(['python', current_path+'/mapper.py'])
    else:
        pass
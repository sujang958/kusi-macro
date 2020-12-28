import pyautogui as pag
import keyboard, time
from random import randint
from win10toast import ToastNotifier


bad_words = ['qudtls', 'tlqkf', 'rotoRl', 'whw']
isOnStart = False
toaster = ToastNotifier()

pag.PAUSE = 1  
pag.FAILSAFE = True  


def randomIndex(array):
    return randint(0, len(array) - 1)


toaster.show_toast('크시 호감도 떨어트리는 메크로', '성공적으로 실행중입니다', duration=4)

while True:
    randomIndexN = randomIndex(bad_words)
    bad_sentence = "zmtldi {}".format(bad_words[randomIndexN])

    if keyboard.is_pressed('F5'):
        isOnStart = True
    if keyboard.is_pressed('F7'):
        isOnStart = False
    if keyboard.is_pressed('F6'):
        toaster.show_toast('크시 호감도 떨어트리는 메크로', '프로그램을 종료합니다', duration=4)
        break
    if isOnStart == True:
        pag.typewrite(bad_sentence)
        pag.press('enter')


#418 990

#219 1063

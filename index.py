import pyautogui as pag
import keyboard, time
from random import randint


bad_words = ['qudtls', 'tlqkf', 'rotoRl', 'whw']
isOnStart = False

pag.PAUSE = 1  
pag.FAILSAFE = True  


# pag.moveTo(219, 1063, 0.15)
# time.sleep(1)
# pag.click()

# pag.moveTo(418, 990, 0.15)
# pag.click()

# pag.typewrite('zmtldi qudtls')
# pag.press('enter')


while True:
    randomIndex = randint(0, len(bad_words) - 1)
    bad_sentence = "zmtldi {}".format(bad_words[randomIndex])

    if keyboard.is_pressed('F5'):
        if isOnStart == False:
            isOnStart = True
        else:
            isOnStart = False
    if keyboard.is_pressed('F6'):
        break
    if isOnStart == True:
        pag.typewrite(bad_sentence)
        pag.press('enter')


#418 990

#219 1063

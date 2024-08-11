import pyautogui

pyautogui.PAUSE = 2
pyautogui.sleep(3)

def scrap_followers(url=''):
    pyautogui.moveTo(x=385, y=24, duration=2)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite(url)
    pyautogui.press('enter')

    pyautogui.sleep(2)
    pyautogui.moveTo(x=1226, y=287, duration=3)
    pyautogui.click()

    pyautogui.sleep(3)
    pyautogui.moveTo(x=1006, y=571, duration=3)

    for i in range(7):
        pyautogui.scroll(-400)
        pyautogui.sleep(3)

    pyautogui.hotkey('ctrl', 's')
    pyautogui.sleep(3)

    FILE_NAME = 'path_to_file.png'
    pyautogui.typewrite(FILE_NAME)
    pyautogui.press('enter')

    return '[🔥] Job is DONE!'


def main():
    print(scrap_followers(url='instagram_acc'))
    # print(pyautogui.position())


if __name__ == '__main__':
    main()

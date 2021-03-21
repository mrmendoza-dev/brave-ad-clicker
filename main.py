import pyautogui
import time

#Initialize failsafe (exit when pixel is (0,0)
pyautogui.FAILSAFE = False

# Initialize sleep variables
sleep_time = 0.5
open_time = 0.5


def main():
    ads_clicked = 0

    print('Press Ctrl-C to quit.')
    try:
        while True:
            #Wait for seconds in sleep_time, then check screen for a match
            time.sleep(sleep_time)
            target = pyautogui.locateOnScreen('BraveAdClickerFiles\Brave Browser Ad Logo.png')

            try:
            #If match exists, proceed, else loop again
                if target is not None:

                    #Save current mouse coordinates before moving
                    prev_x, prev_y = pyautogui.position()

                    #Take center of target, move to location and click
                    target_center = pyautogui.center(target)
                    pyautogui.click(target_center)

                    #Wait for tab to open for open_time, then close with keyboard shortcut, return mouse to original position
                    pyautogui.moveTo(prev_x, prev_y)

                    #Close tab and update counter
                    time.sleep(open_time)
                    pyautogui.hotkey('ctrl', 'w')
                    ads_clicked += 1
                    print('Ads Clicked: ' + str(ads_clicked))
            except Exception as e:
                print(e)



    except KeyboardInterrupt:
        print('Program Terminated')
        print('Total Ads Clicked: ' + str(ads_clicked))


if __name__ == "__main__":
    main()
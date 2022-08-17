import pyautogui
import time

# Initialize failsafe (exit when pixel is (0,0)
pyautogui.FAILSAFE = False

# Initialize sleep variables
sleep_time = 2
open_time = 0.5


def main():
	ads_clicked = 0

	print('Brave Ad Clicker')
	print('-----------------------')
	print('Press Ctrl-C to quit.')

	try:
		while True:
			# Wait for seconds in sleep_time, then check screen for a match
			time.sleep(sleep_time)

			# TODO Screenshot part of screen
			# If match exists, proceed, else loop again
			try:
				target = pyautogui.locateOnScreen('images/logo.png')
				if target is not None:
					# Save current mouse coordinates before moving
					prev_x, prev_y = pyautogui.position()

					# Take center of target, move to location and click
					target_center = pyautogui.center(target)
					pyautogui.click(target_center)

					# Wait for tab to open for open_time, then close with keyboard shortcut, return mouse to original position
					pyautogui.moveTo(prev_x, prev_y)

					# Close tab and update counter`
					time.sleep(open_time)
					pyautogui.hotkey('ctrl', 'w')
					ads_clicked += 1
					print(f"Ads Clicked: {ads_clicked}")

			except Exception as e:
				print(f"Error: {e}")


	except KeyboardInterrupt:
		print('Program Terminated')
		print(f"Total Ads Clicked: {ads_clicked}")


if __name__ == "__main__":
	main()
	input()


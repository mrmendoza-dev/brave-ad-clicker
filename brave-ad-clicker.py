import pyautogui
import time
from datetime import datetime
import sys
from os import path

# Initialize failsafe (exit when pixel is (0,0)
pyautogui.FAILSAFE = False

# Initialize sleep variables
sleep_time = 2
open_time = 0.5

start_time = datetime.now()

search_samples = ["win-10", "win-11"]
sample = search_samples[0]


def main():
	ads_clicked = 0

	def end_program():
		print('Program Terminated')
		print(f"Total Ads Clicked: {ads_clicked}")
		elpased_time = datetime.now() - start_time
		print(f"Elapsed Time: {elpased_time}")


	print('Brave Ad Clicker')
	print('-----------------------')
	print('Press Ctrl-C to quit.')

	try:
		while True:
			# Wait for seconds in sleep_time, then check screen for a match
			time.sleep(sleep_time)

			# If match exists, proceed, else loop again
			try:
				bundle_dir = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))
				image_path = path.join(bundle_dir, "images", "search", f"{sample}.png")

				target = pyautogui.locateOnScreen(image_path)

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
				print(f"Error during image recognition: {e}")

	except KeyboardInterrupt as ke:
		end_program()
	except Exception as e:
		print(f"Exception: {e}")
		end_program()


if __name__ == "__main__":
	main()
	input()


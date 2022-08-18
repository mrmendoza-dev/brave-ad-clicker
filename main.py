import pyautogui
import time
from datetime import datetime
import sys
from os import path
import threading
import schedule
from interface import *



class BraveAdClicker():
	def __init__(self):
		super().__init__()
		# Initialize failsafe (exit when pixel is (0,0))
		pyautogui.FAILSAFE = False

		# Initialize variables and wait times
		self.bot_status = True
		self.refresh_time = 1
		self.open_time = 0.5
		self.start_time = datetime.now()
		self.ads_clicked = 0
		self.elapsed_time = None
		self.interface = None

		self.bot_startup()


	def check_match(self):
		# If match exists, proceed, else loop again
		# SI existe el match, procede, sino vuelve al loop
		try:
			search_filename = "logo.png"
			bundle_dir = getattr(sys, "_MEIPASS", path.abspath(path.dirname("")))
			image_path = path.join(bundle_dir, "images", search_filename)
			target = pyautogui.locateOnScreen(image_path)

			if target is not None:
				# Save current mouse coordinates before moving
				# Guarda las coordenadas del mouse antes de mover
				prev_x, prev_y = pyautogui.position()

				# Take center of target, move to location and click
				# Agarra el center del target, se mueve a la localizacion y clickea
				target_center = pyautogui.center(target)
				pyautogui.click(target_center)

				# Wait for tab to open for open_time, then close with keyboard shortcut, return mouse to original position
				# Espera a que se abra la pestaña en open_time, la cierra con un atajo del teclado, vuelve el mouse a la posicion inicial
				pyautogui.moveTo(prev_x, prev_y)

				# Close tab and update counter
				# Cierra la tab y actualiza el contador
				time.sleep(self.open_time)
				pyautogui.hotkey('ctrl', 'w')
				self.ads_clicked += 1
				print(f"Ads Clicked: {self.ads_clicked}")
				self.interface.ads_clicked = self.ads_clicked

		except Exception as e:
			print(f"Error during image recognition: {e}")



	def bot_startup(self):
		print('Brave Ad Clicker')
		print('-----------------------')
		print('Press Ctrl-C to quit.')

		try:
			thread = threading.Thread(target=self.bot_scheduler)
			print("Launching Bot Scheduler...")
			thread.start()
		except Exception as e:
			print(f"Error: {e}")
		except KeyboardInterrupt as ke:
			self.end_program()

	def bot_scheduler(self):
		while True:
			self.elapsed_time = self.start_time - datetime.now()
			time.sleep(self.refresh_time)

			if self.interface:
				self.sync_from_interface()

			if not self.bot_status:
				continue
			else:
				self.check_match()


	def sync_from_interface(self):
		try:
			new_stats = self.interface.get_stats()
			self.bot_status = new_stats['bot_status']
			self.refresh_time = new_stats['refresh_time']
			self.open_time = new_stats['open_time']
		except Exception as e:
			print(e)

		sync_data = {
			"ads_clicked": self.ads_clicked,
		}
		self.interface.sync_to_interface(sync_data)

	def end_program(self):
		print('\nProgram Terminated')
		print('-----------------------')
		print(f"Total Ads Clicked: {self.ads_clicked}")
		self.elapsed_time = datetime.now() - self.start_time
		print(f"Elapsed Time: {self.elapsed_time}")
		input()


	def launch_interface(self):
		self.interface = Root()
		self.interface.mainloop()


def main():
	bot = BraveAdClicker()
	bot.launch_interface()


if __name__ == "__main__":
	main()


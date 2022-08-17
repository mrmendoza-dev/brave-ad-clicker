import pyautogui
import time
from datetime import datetime
import sys
from os import path


def main():
	# Initialize failsafe (exit when pixel is (0,0)
	pyautogui.FAILSAFE = False

	# Initialize sleep variables
	sleep_time = 2
	open_time = 0.5

	ads_clicked = 0
	start_time = datetime.now()
	search_filename = "logo.png"


	def end_program():
		print('\nProgram Terminated')
		print('-----------------------')
		print(f"Total Ads Clicked: {ads_clicked}")
		elpased_time = datetime.now() - start_time
		print(f"Elapsed Time: {elpased_time}")
		input()


	print('Brave Ad Clicker')
	print('-----------------------')
	print('Press Ctrl-C to quit.')

	try:
		while True:
			# Wait for seconds in sleep_time, then check screen for a match
			# Espera para los segundos en sleep_time, despues busca en la pantalla lo que matchee la imagen
			time.sleep(sleep_time)

			# If match exists, proceed, else loop again
			# SI existe el match, procede, sino vuelve al loop
			try:
				bundle_dir = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))
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


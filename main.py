import pyautogui
import time

# Initialize failsafe (exit when pixel is (0,0)
pyautogui.FAILSAFE = False

# Initialize sleep variables
sleep_time = 1
open_time = 0.5


def main():
	ads_clicked = 0

	print('Press Ctrl-C to quit.')
	try:
		while True:
			# Espera para los segundos en sleep_time, despues busca en la pantalla lo que matchee la imagen
			time.sleep(sleep_time)

			# SI existe el match, procede, sino vuelve al loop
			try:
				target = pyautogui.locateOnScreen('images/win11.png')
				if target is not None:
					# Guarda las coordenadas del mouse antes de mover
					prev_x, prev_y = pyautogui.position()

					# Agarra el center del target, se mueve a la localizacion y clickea
					target_center = pyautogui.center(target)
					pyautogui.click(target_center)

					# Espera a que se abra la pestaña en open_time, la cierra con un atajo del teclado, vuelve el mouse a la posicion inicial
					pyautogui.moveTo(prev_x, prev_y)

					# Cierra la tab y actualiza el contador
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


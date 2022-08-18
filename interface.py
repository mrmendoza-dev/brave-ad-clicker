
import tkinter as tk
from datetime import datetime
import pytz

# https://www.udemy.com/course/desktop-gui-python-tkinter/
# Simple interface for turning bot on/off
# Change time intervals


BORDER = 5
FONT_COLOR = "white"
BG_COLOR = "#444444"
PADX = 10
PADY = 5
FONT = ("Helvetica", 16)


# Tkinter UI launches when executable runs
# Displays elapsed time, number of ads clicked
# Button to turn bot On/Off
# Spinbox input to change time variables


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.root_startup()

        global bot_status
        bot_status = True

        sleep_time = 2
        open_time = 0.5

        def toggle_bot():
            global bot_status

            if bot_status:
                on_btn.config(bg="green")
                on_label.config(text="Turn Bot Off")
                bot_status = False
            else:
                on_btn.config(bg="red")
                on_label.config(text="Turn Bot On")
                bot_status = True

        def grab_interval():
            interval_label.config(text=f"Current Interval: {interval_counter.get()}")

        interface = tk.Frame(self)
        interface.grid(row=0, column=0)
        interface.config(bg="gray")

        main_frame = tk.LabelFrame(interface, text='Bot Control Panel', border=BORDER, font=FONT, fg=FONT_COLOR, bg=BG_COLOR, padx=PADX, pady=PADY)
        main_frame.grid(row=0, column=0, sticky='NS')
        main_frame.columnconfigure(0, weight=1)

        on_label = tk.Label(main_frame, text="#", fg=FONT_COLOR, bg=BG_COLOR, font=FONT)
        on_label.grid(row=1, column=0)

        on_btn = tk.Button(main_frame, command=toggle_bot, height=2, width=6)
        on_btn.grid(row=1, column=1)

        tk.Label(main_frame, text="Bot Interval", fg=FONT_COLOR, bg=BG_COLOR, font=FONT).grid(row=5, column=0)
        interval_counter = tk.Spinbox(main_frame, increment=0.1, width=6, from_=1, to=30, font=FONT, textvariable=2)
        interval_counter.grid(row=5, column=1)


        interval_label= tk.Label(main_frame, text="Current Interval", fg=FONT_COLOR, bg=BG_COLOR, font=FONT)
        interval_label.grid(row=6, column=0)

        submit_btn = tk.Button(main_frame, text="Update", fg=FONT_COLOR, bg="blue", command=grab_interval, height=2, width=6)
        submit_btn.grid(row=5, column=2)

        toggle_bot()


    def root_startup(self):
        self.title("Brave Ad Clicker")
        width, height = 400, 300
        self.config(bg="black")

        # Centers root window, Gets both half the screen width/height and window width/height
        positionRight = int(self.winfo_screenwidth() / 2 - width / 2)
        positionDown = int(self.winfo_screenheight() / 2 - height / 2)

        # Positions the window in the center of the page.
        self.geometry(f"+{positionRight}+{positionDown}")
        size = f"{width}x{height}"
        self.geometry(size)

        # Allows frame to be centered
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Set icon for window
        im = tk.PhotoImage(file="images/logo.png")
        self.iconphoto(False, im)

        # Allows frame to be centered
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)




if __name__ == '__main__':
    now = datetime.now(tz=pytz.UTC)
    print(f"Current time: {now}")


    root = Root()
    root.mainloop()

import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

# https://www.udemy.com/course/desktop-gui-python-tkinter/

def launch_interface():
    root = Root()
    root.mainloop()


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.root_startup()

        BORDER = 5
        FONT_COLOR = "#ffffff"
        BG_COLOR = "#393939"
        FONT = ("Helvetica", 16)

        global start_time, ads_opened, refresh_time, open_time, bot_status

        bot_status = True
        start_time = datetime.now()
        ads_opened = 0
        refresh_time = 2
        open_time = 0.5
        bot_status = True


        def reset():
            global start_time, ads_opened, refresh_time, open_time, bot_status
            refresh_time = 2
            open_time = 0.5
            bot_status = True
            start_time = datetime.now()
            ads_opened = 0
            toggle_bot()
            render_stats()

        def render_stats():
            global start_time, ads_opened, refresh_time, open_time, bot_status
            refresh_l.config(text=f"Refresh Interval: {refresh_time}s")
            open_time_l.config(text=f"Ad Open Time: {open_time}s")
            ads_opened_l.config(text=f"Ads Opened: {ads_opened}")
            elapsed_time = str(datetime.now() - start_time).split(".")[0]
            elapsed_time_l.config(text=f"Elapsed Time: {elapsed_time}")

        def toggle_bot():
            global bot_status

            if bot_status:
                on_btn.config(bg="green")
                on_l.config(text="Bot ACTIVE")
                bot_status = False
            else:
                on_btn.config(bg="red")
                on_l.config(text="Bot INACTIVE")
                bot_status = True

        def grab_interval():
            global start_time, ads_opened, refresh_time, open_time, bot_status
            refresh_time = refresh_input.get()
            open_time = open_time_input.get()
            render_stats()

        interface = tk.Frame(self, padx=15, pady=10)
        interface.grid(row=0, column=0, padx=15, pady=10)
        interface.config(bg="#222222")

        control_frame = tk.LabelFrame(interface, text='Control Panel', border=BORDER, font=FONT, fg=FONT_COLOR, bg=BG_COLOR, padx=15, pady=10)
        control_frame.grid(row=0, column=0)
        control_frame.columnconfigure(0, weight=1)

        on_l = tk.Label(control_frame, text="#", fg=FONT_COLOR, bg=BG_COLOR, font=FONT)
        on_l.grid(row=1, column=0)

        on_btn = tk.Button(control_frame, text="POWER", fg="white", command=toggle_bot, height=2, width=6)
        on_btn.grid(row=1, column=1)

        tk.Label(control_frame, text="Refresh Interval (s)", fg=FONT_COLOR, bg=BG_COLOR, font=FONT).grid(row=5, column=0)
        refresh_input = tk.Spinbox(control_frame, increment=0.1, width=6, from_=1, to=30, font=FONT)
        refresh_input.grid(row=5, column=1)

        tk.Label(control_frame, text="Ad Open Length (s)", fg=FONT_COLOR, bg=BG_COLOR, font=FONT).grid(row=6, column=0)
        open_time_input = tk.Spinbox(control_frame, increment=0.1, width=6, from_=1, to=30, font=FONT)
        open_time_input.grid(row=6, column=1)

        submit_btn = tk.Button(control_frame, text="Update", font=FONT, fg=FONT_COLOR, bg="blue", command=grab_interval, height=1, width=6)
        submit_btn.grid(row=10)



        stats_frame = tk.LabelFrame(interface, text='Stats', border=BORDER, font=FONT, fg=FONT_COLOR, bg=BG_COLOR, padx=25, pady=10)
        stats_frame.grid(row=5, column=0)

        refresh_l = tk.Label(stats_frame, text="Refresh Interval", fg=FONT_COLOR, bg=BG_COLOR, font=FONT)
        refresh_l.grid(row=5, column=0)
        open_time_l = tk.Label(stats_frame, text="Ad Open Time:", fg=FONT_COLOR, bg=BG_COLOR, font=FONT)
        open_time_l.grid(row=6, column=0)

        ads_opened_l = tk.Label(stats_frame, text="Ads Opened:", fg=FONT_COLOR, bg=BG_COLOR, font=FONT)
        ads_opened_l.grid(row=10, column=0)

        elapsed_time_l = tk.Label(stats_frame, text="Elapsed Time:", fg=FONT_COLOR, bg=BG_COLOR, font=FONT)
        elapsed_time_l.grid(row=15, column=0)

        def update_time():
            render_stats()
            self.after(1000, update_time)  # call update() after 1 second

        toggle_bot()
        update_time()


    def root_startup(self):
        self.title("Brave Ad Clicker")
        width, height = 400, 600
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
    launch_interface()

import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz



def launch_interface():
    root = Root()
    root.mainloop()


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.root_startup()
        self.build_app()
        self.reset()
        self.update_time()

    def reset(self):
        self.refresh_time = 1
        self.open_time = 0.5
        self.bot_status = False
        self.start_time = datetime.now()
        self.ads_clicked = 0
        self.elapsed_time = None
        self.toggle_bot()
        self.render_stats()

    def build_app(self):
        BORDER = 5
        FONT_COLOR = "#ffffff"
        BG_COLOR = "#393939"
        FONT = ("Helvetica", 16)

        interface = tk.Frame(self, padx=15, pady=10)
        interface.grid(row=0, column=0, padx=15, pady=10)
        interface.config(bg="#222222")

        control_frame = tk.LabelFrame(interface, text='Control Panel', border=BORDER, font=FONT, fg=FONT_COLOR, bg=BG_COLOR, padx=15, pady=10)
        control_frame.grid(row=0, column=0)
        control_frame.columnconfigure(0, weight=1)

        self.on_l = tk.Label(control_frame, text="#", fg=FONT_COLOR, bg=BG_COLOR, font=FONT)
        self.on_l.grid(row=1, column=0)

        self.on_btn = tk.Button(control_frame, text="POWER", fg="white", font=("Helvetica", 12), command=self.toggle_bot, height=2, width=9)
        self.on_btn.grid(row=1, column=1)

        tk.Label(control_frame, text="Refresh Interval (s)", fg=FONT_COLOR, bg=BG_COLOR, font=FONT).grid(row=5, column=0)
        self.refresh_input = tk.Spinbox(control_frame, increment=0.1, width=6, from_=0.1, to=30, font=FONT)
        self.refresh_input.grid(row=5, column=1)

        tk.Label(control_frame, text="Ad Open Time (s)", fg=FONT_COLOR, bg=BG_COLOR, font=FONT).grid(row=6, column=0)
        self.open_time_input = tk.Spinbox(control_frame, increment=0.1, width=6, from_=0.1, to=30, font=FONT)
        self.open_time_input.grid(row=6, column=1)

        submit_btn = tk.Button(control_frame, text="Update", font=FONT, fg=FONT_COLOR, bg="blue", command=self.update_stats, height=1, width=6)
        submit_btn.grid(row=10)


        stats_frame = tk.LabelFrame(interface, text='Stats', border=BORDER, font=FONT, fg=FONT_COLOR, bg=BG_COLOR, padx=25, pady=10)
        stats_frame.grid(row=5, column=0)

        self.refresh_l = tk.Label(stats_frame, text="Refresh Interval", fg=FONT_COLOR, bg=BG_COLOR, font=FONT)
        self.refresh_l.grid(row=5, column=0)
        self.open_time_l = tk.Label(stats_frame, text="Ad Open Time:", fg=FONT_COLOR, bg=BG_COLOR, font=FONT)
        self.open_time_l.grid(row=6, column=0)

        self.ads_clicked_l = tk.Label(stats_frame, text="Ads Opened:", fg=FONT_COLOR, bg=BG_COLOR, font=FONT)
        self.ads_clicked_l.grid(row=10, column=0)

        self.elapsed_time_l = tk.Label(stats_frame, text="Elapsed Time:", fg=FONT_COLOR, bg=BG_COLOR, font=FONT)
        self.elapsed_time_l.grid(row=15, column=0)

    def update_time(self):
        self.render_stats()
        self.after(1000, self.update_time)  # call update() after 1 second






    def render_stats(self):
        self.refresh_l.config(text=f"Refresh Interval: {self.refresh_time}s")
        self.open_time_l.config(text=f"Ad Open Time: {self.open_time}s")
        self.ads_clicked_l.config(text=f"Ads Opened: {self.ads_clicked}")
        self.elapsed_time = str(datetime.now() - self.start_time).split(".")[0]
        self.elapsed_time_l.config(text=f"Elapsed Time: {self.elapsed_time}")

    def toggle_bot(self):
        if not self.bot_status:
            self.on_btn.config(bg="#0b0")
            self.on_l.config(text="Bot ACTIVE")
            self.bot_status = True
            print("--- Bot Activated")
        else:
            self.on_btn.config(bg="red")
            self.on_l.config(text="Bot INACTIVE")
            self.bot_status = False
            print("--- Bot Deactivated")


    def update_stats(self):
        self.refresh_time = float(self.refresh_input.get())
        self.open_time = float(self.open_time_input.get())
        print(f"\n--- Updating Stats")
        print(f"- Refresh Time: {self.refresh_time}s")
        print(f"- Ad Open Time: {self.open_time}s\n")
        self.render_stats()

    def get_stats(self):
        stats = {
            "bot_status": self.bot_status,
            "refresh_time": self.refresh_time,
            "open_time": self.open_time,
        }
        return stats

    def sync_to_interface(self, new_stats):
        self.ads_clicked = new_stats['ads_clicked']
        self.render_stats()


    def root_startup(self):
        self.title("Brave Ad Clicker")
        width, height = 400, 450
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
        # im = tk.PhotoImage(file="images/logo.png")
        # self.iconphoto(False, im)

        # Allows frame to be centered
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


# if __name__ == '__main__':
#     launch_interface()
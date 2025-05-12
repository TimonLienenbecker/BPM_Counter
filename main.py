import tkinter as tk
import time


class BPMCounter:
    def __init__(self, master):
        self.master = master
        self.master.title("BPM Counter")

        self.click_times = []

        self.button = tk.Button(master, text="Klick hier!", font=("Helvetica", 24), width=20, height=5,
                                command=self.register_click)
        self.button.pack(pady=20)

        self.bpm_label = tk.Label(master, text="BPM: 0", font=("Helvetica", 18))
        self.bpm_label.pack(pady=10)

        self.reset_button = tk.Button(master, text="Reset", font=("Helvetica", 14), command=self.reset)
        self.reset_button.pack(pady=5)

    def register_click(self):
        current_time = time.time()
        self.click_times.append(current_time)

        if len(self.click_times) > 8:
            self.click_times.pop(0)

        if len(self.click_times) > 1:
            intervals = [self.click_times[i] - self.click_times[i - 1] for i in range(1, len(self.click_times))]
            avg_interval = sum(intervals) / len(intervals)
            bpm = 60 / avg_interval
            self.bpm_label.config(text=f"BPM: {bpm:.2f}")

    def reset(self):
        self.click_times.clear()
        self.bpm_label.config(text="BPM: 0")


if __name__ == "__main__":
    root = tk.Tk()
    app = BPMCounter(root)
    root.mainloop()

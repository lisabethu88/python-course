import tkinter as tk
from ui.app import FoodTrackerApp

def main():
    root = tk.Tk()
    FoodTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
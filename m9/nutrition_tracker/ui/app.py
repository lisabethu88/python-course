from services.nutrition_service import get_food_item
from tkinter import messagebox, ttk
import tkinter as tk
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FoodTrackerApp:
    """
    A simplified food tracking app with a gui.

    Lets the user search for foods, add them by quantity, and track
    daily nutrition totals like calories, protein, carbs, fat, and fiber.

    Also shows a list of foods entered and a pie chart of macronutrients.
    """
    def __init__(self, root):
        """
        Sets up the main window for the food tracker app.

        Initializes the window size, title, nutrition totals,
        and builds the UI.
        """
        self.root = root
        self.root.title("Food Tracker")
        self.root.geometry("1000x800")

        # state
        self.totals = {
            "calories": 0,
            "protein": 0,
            "carbs": 0,
            "fat": 0,
            "fiber": 0
        }
        self.chart_canvas = None
        self.create_ui()
       

    def create_ui(self):
        """
        Builds the UI for the food tracker app.

        Creates the input fields, buttons, list of added foods,
        nutrition totals display, and the pie chart.
        """
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill="both", expand=True)

        title_label = tk.Label(
            main_frame,
            text="Daily Food Tracker",
            font=("Helvetica", 18, "bold")
        )
        title_label.pack(pady=10)

        form_frame = tk.Frame(main_frame)
        form_frame.pack(pady=10)

        # Food Name
        tk.Label(form_frame, text="Food Name").grid(row=0, column=0)
        self.food_name_entry = tk.Entry(form_frame)
        self.food_name_entry.grid(row=0, column=1)

        # Quantity
        tk.Label(form_frame, text="Amount").grid(row=1, column=0)
        self.quantity_entry = tk.Entry(form_frame)
        self.quantity_entry.grid(row=1, column=1)
        self.quantity_entry.insert(0, "1")

        # Unit
        tk.Label(form_frame, text="Unit").grid(row=2, column=0)
        self.unit_combobox = ttk.Combobox(
            form_frame,
            values=["g", "oz", "lb", "ml", "fl oz", "cup", "tbsp", "tsp"],
            state="readonly"
        )
        self.unit_combobox.grid(row=2, column=1)
        self.unit_combobox.set("g")

        # Button
        add_button = tk.Button(
            main_frame,
            text="Add Food",
            command=self.add_food
        )
        add_button.pack(pady=10)

        # Listbox
        self.log_listbox = tk.Listbox(main_frame, width=100)
        self.log_listbox.pack(pady=10)

        # Totals UI
        totals_frame = tk.Frame(main_frame, bd=1, relief="solid", padx=10, pady=10)
        totals_frame.pack(pady=10)

        tk.Label(
            totals_frame,
            text="Daily Totals",
            font=("Helvetica", 14, "bold")
        ).grid(row=0, column=0, columnspan=5, pady=(0, 10))

        self.calories_label = tk.Label(totals_frame, text="Calories: 0")
        self.calories_label.grid(row=1, column=0, padx=10)

        self.protein_label = tk.Label(totals_frame, text="Protein: 0g")
        self.protein_label.grid(row=1, column=1, padx=10)

        self.carbs_label = tk.Label(totals_frame, text="Carbs: 0g")
        self.carbs_label.grid(row=1, column=2, padx=10)

        self.fat_label = tk.Label(totals_frame, text="Fat: 0g")
        self.fat_label.grid(row=1, column=3, padx=10)

        self.fiber_label = tk.Label(totals_frame, text="Fiber: 0g")
        self.fiber_label.grid(row=1, column=4, padx=10)

        # pie chart showing macro breakdown
        self.chart_frame = tk.Frame(self.root)
        self.chart_frame.pack(pady=10)
    
    def add_food(self):
        """
        Adds a food item to the tracker.
        """
        food_name = self.food_name_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        unit = self.unit_combobox.get()

        # validate input
        if not food_name or not quantity:
            messagebox.showerror("Input Error", "Please enter both a food name and quantity.")
            return

        # validate number
        try:
            quantity = float(quantity)
        except ValueError:
            messagebox.showerror("Invalid Input", "Quantity must be a number.")
            return

        # try fetching food item safely
        try:
            food_item = get_food_item(food_name, quantity, unit)
        except Exception as e:
            messagebox.showerror("Error", f"Could not fetch food data:\n{e}")
            return

        # handle case where API returns nothing
        if not food_item:
            messagebox.showerror("Not Found", "Food item could not be found.")
            return

        # add to UI
        self.log_listbox.insert(tk.END, food_item)

        # update totals
        self.totals["calories"] += food_item.calories
        self.totals["protein"] += food_item.protein
        self.totals["carbs"] += food_item.carbs
        self.totals["fat"] += food_item.fat
        self.totals["fiber"] += food_item.fiber

        self.update_totals()
        self.update_chart()

        # clear input
        self.food_name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

        # success message
        messagebox.showinfo("Success", f"{food_item.name} added!")

    def update_totals(self):
        """
        Updates the labels that show current nutrition totals (macros and cals).
        """
        self.calories_label.config(text=f"Calories: {self.totals['calories']:.0f}")
        self.protein_label.config(text=f"Protein: {self.totals['protein']:.1f}g")
        self.carbs_label.config(text=f"Carbs: {self.totals['carbs']:.1f}g")
        self.fat_label.config(text=f"Fat: {self.totals['fat']:.1f}g")
        self.fiber_label.config(text=f"Fiber: {self.totals['fiber']:.1f}g")

    def update_chart(self):
        """
        Updates the pie chart to display current macro totals.
        """
        labels_data = {
            "Protein": self.totals["protein"],
            "Carbs": self.totals["carbs"],
            "Fat": self.totals["fat"],
            "Fiber": self.totals["fiber"]
        }

        labels = []
        values = []

        for key, value in labels_data.items():
            if value > 0:
                labels.append(key)
                values.append(value)

        if not values:
            return

        # destroy old canvas 
        if self.chart_canvas:
            self.chart_canvas.get_tk_widget().destroy()
            self.chart_canvas = None

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%")
        ax.set_title("Macro Breakdown")

        self.chart_canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        self.chart_canvas.draw()
        self.chart_canvas.get_tk_widget().pack()

    def update_totals_dict(totals, food_item):
        """
        Adds a food item’s nutrition values to the current totals.
        """
        totals["calories"] += food_item.calories
        totals["protein"] += food_item.protein
        totals["carbs"] += food_item.carbs
        totals["fat"] += food_item.fat
        totals["fiber"] += food_item.fiber
        return totals
    
    def handle_submit():
        try:
            # example error
            int("abc")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")
import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ExpenseVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Visualizer")
        self.root.geometry("600x500")

        tk.Label(root, text="Expense Visualizer", font=("Arial", 18, "bold")).pack(pady=10)

        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Total Earnings This Month: ").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.total_earnings = tk.Entry(self.input_frame)
        self.total_earnings.grid(row=0, column=1, padx=5, pady=5)

        self.categories = ["Groceries", "Food", "Shopping", "Travel", "Party"]
        self.entries = {}
        for i, category in enumerate(self.categories, 1):
            tk.Label(self.input_frame, text=f"{category}: ").grid(row=i, column=0, sticky="w", padx=5, pady=5)
            entry = tk.Entry(self.input_frame)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[category] = entry

        tk.Button(root, text="Visualize Expenses", command=self.visualize_expenses).pack(pady=10)

        self.chart_frame = tk.Frame(root)
        self.chart_frame.pack(pady=10)

    def visualize_expenses(self):
     
        try:
            total_earnings = float(self.total_earnings.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for Total Earnings.")
            return
        expenses = {}
        for category, entry in self.entries.items():
            try:
                expenses[category] = float(entry.get())
            except ValueError:
                messagebox.showerror("Input Error", f"Please enter a valid number for {category}.")
                return

        # Calculate total expenses
        total_expenses = sum(expenses.values())

        # Check if expenses exceed total earnings
        if total_expenses > total_earnings:
            messagebox.showerror("Budget Error", "Total expenses exceed total earnings.")
            return

        # Clear previous chart
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        # Create a pie chart
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        labels = list(expenses.keys())
        sizes = list(expenses.values())
        colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140,
               wedgeprops={'edgecolor': 'black'})
        ax.set_title("Expense Distribution")

    
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        remaining_balance = total_earnings - total_expenses
        tk.Label(self.chart_frame, text=f"Remaining Balance: ₹{remaining_balance:.2f}", font=("Arial", 14)).pack(
            pady=10)


root = tk.Tk()
app = ExpenseVisualizer(root)
root.mainloop()

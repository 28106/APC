import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

arr = np.array([1,2,3],[4,2,5])
print("Array")

import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

FILE_NAME = "employee_data.csv"

# ------------------ FILE HANDLING ------------------
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Name", "Department", "Salary"])
    df.to_csv(FILE_NAME, index=False)


# ------------------ FUNCTIONS ------------------

def load_data():
    """Load employee data safely"""
    try:
        df = pd.read_csv(FILE_NAME)
        return df
    except Exception as e:
        messagebox.showerror("Error", f"Error loading data: {e}")
        return pd.DataFrame(columns=["Name", "Department", "Salary"])


def save_data(df):
    """Save data safely to CSV"""
    try:
        df.to_csv(FILE_NAME, index=False)
    except Exception as e:
        messagebox.showerror("Error", f"Could not save data: {e}")


def add_employee():
    """Add a new employee record"""
    name = name_entry.get().strip()
    dept = dept_entry.get().strip()
    salary = salary_entry.get().strip()

    try:
        if not name or not dept or not salary:
            raise ValueError("All fields are required.")
        salary = float(salary)

        df = load_data()
        if name in df["Name"].values:
            raise ValueError("Employee already exists!")

        new_data = pd.DataFrame([[name, dept, salary]], columns=df.columns)
        df = pd.concat([df, new_data], ignore_index=True)
        save_data(df)

        messagebox.showinfo("Success", f"Employee {name} added successfully!")
        clear_fields()
        show_table()

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))


def update_salary():
    """Update existing employee salary"""
    name = name_entry.get().strip()
    salary = salary_entry.get().strip()

    try:
        if not name or not salary:
            raise ValueError("Name and new salary required!")
        salary = float(salary)

        df = load_data()
        if name not in df["Name"].values:
            raise ValueError("Employee not found!")

        df.loc[df["Name"] == name, "Salary"] = salary
        save_data(df)

        messagebox.showinfo("Success", f"Salary updated for {name}")
        clear_fields()
        show_table()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_employee():
    """Delete employee by name"""
    name = name_entry.get().strip()
    try:
        if not name:
            raise ValueError("Enter name to delete!")

        df = load_data()
        if name not in df["Name"].values:
            raise ValueError("Employee not found!")

        df = df[df["Name"] != name]
        save_data(df)

        messagebox.showinfo("Deleted", f"{name} removed successfully.")
        clear_fields()
        show_table()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def search_employee():
    """Search employee by name or department"""
    query = search_entry.get().strip()
    try:
        df = load_data()
        if query == "":
            raise ValueError("Enter name or department to search.")

        result = df[df["Name"].str.contains(query, case=False) |
                    df["Department"].str.contains(query, case=False)]

        if result.empty:
            messagebox.showinfo("Not Found", "No matching records found.")
        else:
            show_table(result)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def show_summary():
    """Show average, highest, and lowest salaries"""
    try:
        df = load_data()
        if df.empty:
            raise ValueError("No records found!")

        avg_salary = np.mean(df["Salary"])
        max_salary = np.max(df["Salary"])
        min_salary = np.min(df["Salary"])

        msg = (f"Average Salary: ₹{avg_salary:.2f}\n"
               f"Highest Salary: ₹{max_salary:.2f}\n"
               f"Lowest Salary: ₹{min_salary:.2f}")
        messagebox.showinfo("Salary Summary", msg)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def show_graph():
    """Show average salary by department"""
    try:
        df = load_data()
        if df.empty:
            raise ValueError("No data available!")

        dept_avg = df.groupby("Department")["Salary"].mean()
        plt.bar(dept_avg.index, dept_avg.values, color="orange")
        plt.title("Average Salary by Department")
        plt.xlabel("Department")
        plt.ylabel("Average Salary (₹)")
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def export_excel():
    """Export data to Excel file"""
    try:
        df = load_data()
        export_name = "Employee_Salary_Report.xlsx"
        df.to_excel(export_name, index=False)
        messagebox.showinfo("Exported", f"Data exported to {export_name}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def clear_fields():
    """Clear all input fields"""
    name_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)


def show_table(data=None):
    """Display employee data in table"""
    for row in table.get_children():
        table.delete(row)
    df = data if data is not None else load_data()
    for _, row in df.iterrows():
        table.insert("", tk.END, values=(row["Name"], row["Department"], row["Salary"]))


# ------------------ GUI SETUP ------------------

root = tk.Tk()
root.title("Employee Salary Management System")
root.geometry("700x550")
root.configure(bg="#f7f7f7")

tk.Label(root, text="Employee Salary Management System",
         font=("Arial", 18, "bold"), fg="#003366", bg="#f7f7f7").pack(pady=10)

frame = tk.Frame(root, bg="#f7f7f7")
frame.pack()

# Entries
tk.Label(frame, text="Name:", bg="#f7f7f7").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Department:", bg="#f7f7f7").grid(row=1, column=0, padx=5, pady=5)
dept_entry = tk.Entry(frame)
dept_entry.grid(row=1, column=1)

tk.Label(frame, text="Salary:", bg="#f7f7f7").grid(row=2, column=0, padx=5, pady=5)
salary_entry = tk.Entry(frame)
salary_entry.grid(row=2, column=1)

# Buttons
btn_frame = tk.Frame(root, bg="#f7f7f7")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", command=add_employee, bg="#0099cc", fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", command=update_salary, bg="#33cc33", fg="white", width=10).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", command=delete_employee, bg="#ff6666", fg="white", width=10).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Summary", command=show_summary, bg="#9966ff", fg="white", width=10).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Graph", command=show_graph, bg="#ff9933", fg="white", width=10).grid(row=0, column=4, padx=5)
tk.Button(btn_frame, text="Export", command=export_excel, bg="#666666", fg="white", width=10).grid(row=0, column=5, padx=5)

# Search
search_frame = tk.Frame(root, bg="#f7f7f7")
search_frame.pack(pady=5)
tk.Label(search_frame, text="Search:", bg="#f7f7f7").pack(side=tk.LEFT, padx=5)
search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5)
tk.Button(search_frame, text="Find", command=search_employee, bg="#0066cc", fg="white").pack(side=tk.LEFT, padx=5)

# Table
cols = ("Name", "Department", "Salary")
table = ttk.Treeview(root, columns=cols, show="headings", height=10)
for col in cols:
    table.heading(col, text=col)
    table.column(col, width=150, anchor=tk.CENTER)
table.pack(pady=10)

show_table()

root.mainloop()

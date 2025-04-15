import sqlite3
import csv

# Connect to SQLite DB (creates if not exists)
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    salary REAL
)
''')

def add_employee():
    name = input("Enter employee name: ")
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))
    cursor.execute("INSERT INTO employees (name, role, salary) VALUES (?, ?, ?)", (name, role, salary))
    conn.commit()
    print("✅ Employee added.")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()
    for row in records:
        print(row)

def update_employee():
    emp_id = input("Enter employee ID to update: ")
    new_salary = float(input("Enter new salary: "))
    cursor.execute("UPDATE employees SET salary = ? WHERE id = ?", (new_salary, emp_id))
    conn.commit()
    print("✅ Salary updated.")

def delete_employee():
    emp_id = input("Enter employee ID to delete: ")
    cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    print("🗑️ Employee deleted.")

def export_to_csv():
    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()
    with open('employees.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Role", "Salary"])
        writer.writerows(records)
    print("📁 Exported to employees.csv")

def menu():
    while True:
        print("\n========= EMPLOYEE MANAGER =========")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Salary")
        print("4. Delete Employee")
        print("5. Export to CSV")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            export_to_csv()
        elif choice == '6':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")

menu()
conn.close()

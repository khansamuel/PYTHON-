class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, salary, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        super().__init__(emp_id, name, salary)

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, salary):
        super().__init__(emp_id, name, salary)

    def calculate_salary(self):
        return self.salary / 12

class CommissionEmployee(Employee):
    def __init__(self, emp_id, name, salary, commission_rate, total_sales):
        self.commission_rate = commission_rate
        self.total_sales = total_sales
        super().__init__(emp_id, name, salary)

    def calculate_salary(self):
        commission = self.total_sales * self.commission_rate
        return self.salary / 12 + commission

def create_employee():
    while True:
        employee_type = input("Enter employee type (hourly, salary, commission): ").lower()

        if employee_type in ("hourly", "salary", "commission"):
            break
        else:
            print("Invalid employee type. Please try again.")

    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    salary = float(input("Enter base salary: "))

    if employee_type == 'hourly':
        hours_worked = int(input("Enter hours worked: "))
        hourly_rate = float(input("Enter hourly rate: "))
        emp = HourlyEmployee(emp_id, name, salary, hours_worked, hourly_rate)
    elif employee_type == 'salary':
        emp = SalaryEmployee(emp_id, name, salary)
    else:
        commission_rate = float(input("Enter commission rate: "))
        total_sales = float(input("Enter total sales: "))
        emp = CommissionEmployee(emp_id, name, salary, commission_rate, total_sales)

    return emp

# Creating an employee object based on user input
employee = create_employee()

# Calculating and printing the salary
print("Employee ID:", employee.emp_id)
print("Employee Name:", employee.name)
print("Employee Salary:", employee.calculate_salary())

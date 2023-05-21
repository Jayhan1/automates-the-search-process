class Employee:
    def __init__(self, name, employee_id, base_salary, department):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary
        self.department = department

    def calculate_salary(self, overtime_hours):
        overtime_rate = 1.5  # Overtime pay rate (1.5 times the base salary)
        overtime_pay = overtime_hours * overtime_rate * self.base_salary
        total_salary = self.base_salary + overtime_pay
        return total_salary

    def print_details(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Base Salary:", self.base_salary)
        print("Department:", self.department)


# Example usage:
adam = Employee("Adam", "E5463", 5400, "Research")
overtime_hours = 10
salary = adam.calculate_salary(overtime_hours)
adam.print_details()
print("Total Salary:", salary)


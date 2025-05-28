class Employee:
    def __init__(self, a1, a2, a3, a4, a5, a6):
        self.num = a1
        self.name = a2
        self.dept = a3
        self.des = a4
        self.age = a5
        self.salary = a6

    def display_emp(self):
        print(f"Employee No: {self.num}",end=", ")
        print(f"Name: {self.name}", end = ", ")
        print(f"Department: {self.dept}",end = ", ")
        print(f"Designation: {self.des}", end = ", ")
        print(f"Age: {self.age}", end=", ")
        print(f"Salary: {self.salary}\n")

# Function to accept employee details
def read_emp(n):
    employees = []
    for i in range(n):
        print(f"Enter details for {i+1} employees :")
        e_num = int(input("Enter Employee No: "))
        e_name = input("Enter Name: ")
        e_dept = input("Enter the Department : ")
        e_des = input("Enter the Designation: ")
        e_age = int(input("Enter the Age: "))
        e_salary = float(input("Enter the Salary: "))
        employee = Employee(e_num, e_name, e_dept, e_des, e_age, e_salary)
        employees.append(employee)
    return employees

# Function to search employee by empno
def search_emp(employees, empno):
    for emp in employees:
        if emp.num == empno:
            return emp
    return None

# Main program
def main():
    ch = 1
    while True:
        print("1. Add Data\n2.Search Employee\n3.Display All\n4. Exit ")
        ch=int(input("Enter your choice...  "))
        if ch == 1:
            n = int(input("Enter number of employees: "))
            employees = read_emp(n)
        elif ch == 2:
            search = int(input("Enter Employee No to search: "))
            employee = search_emp(employees, search)
            if employee:
                print("\nEmployee Found:")
                employee.display_emp()
            else:
                print("Employee not found.")
        elif ch == 3:
            print("\nAll Employee Details:")
            for emp in employees:
                emp.display_emp()
        elif ch == 4:
            exit(1)
        else:
            print("Invalid choice....")
            exit(1)


if __name__ == "__main__":
    main()

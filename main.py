import json
from employee import Employee
from db import conn


def save_info():
    with open('employees.json', 'r') as file:
        employee_date = json.load(file)

    employees = []

    for employee in employee_date:
        employee_instance = Employee(employee['name'], employee['surname'], employee['age'])
        employees.append(employee_instance)

    for employee in employees:
        employee.save()


def get_test():
    print("Testing get() method:")
    print("Test existing employee")
    employee = Employee.get(4)
    if employee:
        print(f"Retrieved employee: {employee}")
    else:
        print("No employee found with the given ID.")

    print("\nTest for non_existent employee")
    non_existent_employee = Employee.get(100)
    if non_existent_employee:
        print(f"Retrieved employee: {non_existent_employee}")
    else:
        print("No employee found with the given ID.")


def get_list_test():
    print("\nTesting get_list() method:")
    employees_with_same_surname = Employee.get_list(surname='Lee')
    if employees_with_same_surname:
        print("Employees with the same surname:")
        for employee in employees_with_same_surname:
            print(employee)
    else:
        print("No employees found with the given surname.")


def get_list_test_for_several_attributes():
    print("\nTesting get_list() method with multiple attributes:")

    employees_with_criteria = Employee.get_list(surname='Johnson', age=25)
    if employees_with_criteria:
        print("Employees matching criteria:")
        for employee in employees_with_criteria:
            print(employee)
    else:
        print("No employees found matching the criteria.")


def update_test():
    print("\nTesting update() method:")
    # Create a new employee
    new_employee = Employee('John', 'Doe', 30)
    new_employee.save()
    print(f"Original employee details: {Employee.get(new_employee.id)}")

    # Update the employee's name
    new_employee.name = 'Jane'
    new_employee.age = 35
    new_employee.save()
    print(f"Updated employee details: {Employee.get(new_employee.id)}")


def delete_test():
    print("\nTesting delete() method:")
    new_employee = Employee.get(2)
    print(f"Employee to be deleted: {new_employee}")

    # Delete the employee
    new_employee.delete()
    print("Employee deleted from the database.")
    print(f"{Employee.get(new_employee.id)}")


def create_test():
    print("\nTesting create() methods:")

    new_employee = Employee('Natia', 'Pruidze', 22)
    print(f"New employee created: {new_employee}")

    # Save the employee to the database
    new_employee.save()
    print("Employee saved to the database.")

    # Retrieve the employee from the database
    retrieved_employee = Employee.get(new_employee.id)
    print(f"Retrieved employee: {retrieved_employee}")


def comparison_test():
    print("\nTesting comparison methods:")
    employee1 = Employee('Alice', 'Jones', 30)
    employee2 = Employee('Bob', 'Smith', 35)

    print(f"Comparison between ages  Alice age: {employee1.age} and Bob age: {employee2.age}:")
    print(f"{employee1} < {employee2}: {employee1 < employee2}")
    print(f"{employee1} <= {employee2}: {employee1 <= employee2}")
    print(f"{employee1} == {employee2}: {employee1 == employee2}")
    print(f"{employee1} != {employee2}: {employee1 != employee2}")
    print(f"{employee1} > {employee2}: {employee1 > employee2}")
    print(f"{employee1} >= {employee2}: {employee1 >= employee2}")


def main():
    # get_test()
    # delete_test()
    # get_list_test()
    # create_test()
    # update_test()
    # get_list_test_for_several_attributes()
    # comparison_test()
    conn.close()


if __name__ == "__main__":
    if not Employee.employees_exist():
        save_info()
    main()

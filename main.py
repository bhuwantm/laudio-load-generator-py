from core.employee import Employee
from core.user_account import UserAccount
from core.user_relationship import UserRelationships

if __name__ == '__main__':
    employee_count = 0
    while employee_count == 0:
        input_employee_count = input("Enter an even number of employees to be generated: ")
        try:
            if int(input_employee_count) % 2 != 0:
                raise ValueError("Old integer detected.")
            employee_count = int(input_employee_count)
        except ValueError as e:
            print(e)
            pass

    user_count = 0
    while user_count == 0:
        input_user_count = input("Enter the number of users to be generated from the above employee: ")
        try:
            if int(input_user_count) > employee_count:
                raise ValueError('Number of users cannot be greater than number of employee.')
            user_count = int(input_user_count)
        except ValueError as e:
            print(e)
            pass

    # employees generation
    employee = Employee(employee_count)
    employee_list = employee.generate_csv()

    # users generation from employees
    user_accounts = UserAccount(employee_list, user_count)
    user_accounts.generate_csv()

    # user relationship generation based on employee and users
    user_relationships = UserRelationships(employee_list)
    user_relationships.generate_csv()

command = input()
company = {}
while command != "End":

    company_name, employee_id = command.split("->")
    if company_name in company:
        current_employee_id = company[company_name]
        if employee_id not in current_employee_id:
            company[company_name] = current_employee_id + [employee_id]
    else:
        company[company_name] = [employee_id]

    command = input()

for company_name, employee_id in company.items():
    print(f"{company_name}")
    for employee in employee_id:
        print(f"--{employee}")
employees = []

def add_employee(emp_id, name):
    employees.append({
        "id": emp_id,
        "name": name
    })

add_employee(101, "Srinath")

print(employees)
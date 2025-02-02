
from administrator.models import EmployeeWork, SalaryType
from employee.models import Employee, Filial



def get_all_filials():
    return Filial.objects.all()

def get_filial_with_id(id):
    return Filial.objects.get(id=id)

def create_employee(username:str, password:str, first_name:str, last_name:str,  role:str):
    try:
        Employee.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=role
        )
        return True
    except:
        return False

def set_employee_to_filial(employee: Employee, filial: Filial, salary_type: SalaryType):
    if isinstance(employee, Employee) and isinstance(filial, Filial) and isinstance(salary_type, SalaryType):
        EmployeeWork.objects.create(
            employee=employee,
            filial=filial,
            salary_type = salary_type
            )

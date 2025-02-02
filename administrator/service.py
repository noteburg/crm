

from employee.models import Employee, Filial



def get_all_filials():
    return Filial.objects.all()

def get_filial_with_id(id):
    return Filial.objects.get(id=id)

def create_employee(username:str, password:str, first_name:str, last_name:str,  role:str, filial:Filial):
    try:
        Employee.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=role,
            filial=filial
        )
        return True
    except:
        return False
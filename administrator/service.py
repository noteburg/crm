from administrator.models import EmployeeWork, Student, Group, Lesson, GroupStudent
from employee.models import Employee, Filial



"""
filial create, get_one, get_all +++
student create, get_one, get_all, get_all_active,  ++++
group create, get_one, get_all, get_all_active, ++++
student in group create, delete, get 
"""

# funks for filial model start
def create_filial(name: str, region:str) -> Filial:
    return Filial.objects.create(name=name, region=region)

def get_all_filials():
    return Filial.objects.all()

def get_filial_with_id(id):
    return Filial.objects.get(id=id)

# funks for filial model end


# funks for Employee model start
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

def set_employee_to_filial(employee: Employee, filial: Filial):
    if isinstance(employee, Employee) and isinstance(filial, Filial):
        EmployeeWork.objects.create(
            employee=employee,
            filial=filial
            )

# funks for Employee model end


# funks for student model start
def create_student(first_name:str, last_name:str, phone:str):
    """Student yaratish"""
    if first_name and last_name and phone:
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )
        return True

def get_student_with_id(id):
    """Student modelidan id orqali studentni olish"""
    return Student.objetcs.get(id=id)

def get_all_active_students():
    """Hozirgi mavjud guruhlardan o'quvchilarni olish"""
    students = []
    groups = get_active_groups()
    for group in groups:
        students.extend(group.students.filter(is_active=True))
    return students

def get_all_students():
    """Student modelidan barcha studentlarni olish"""
    return Student.objects.all()

# funks for student model end

# funks for group_student model start

def create_group(filial:Filial, teacher:Employee, name:str, lesson:Lesson, teacher_per:int):
    """yangi guruh yaratish. guruh nofaol holatda yaratiladi, sabibi guruhga o'quvchi yig'ish vaqtida
       guruh nofaol turishi kerak, o'quv kuni boshlanganda guruh administrator tomonidan faollashtiriladi
    """
    if (filial, teacher, name, lesson, teacher_per):
        return Group.objects.create(
            filial=filial,
            teacher=teacher,
            name=name,
            lesson=lesson,
            teacher_per=teacher_per
            )
    else:
        raise Exception('kerakli barcha argumentlarni kiriting')

def get_group_with_id(id):
    """Group modelidan guruhni id orqali olish"""
    return Group.objects.get(id=id)

def get_all_active_students_from_group(group:Group):
    return GroupStudent.students.filter(is_active=True)

def get_active_groups():
    """Hozirdagi mavjud guruhlarni olish"""
    return Group.objects.filter(status='2')

def get_not_started_groups():
    return Group.objects.filter(status='1')

def get_inactive_groups():
    return Group.objects.filter(status='3')

def get_all_groups():
    """Group modelidan barcha guruhlarni qaytaradi"""
    return Group.objects.all()

def get_active_students_from_group(group:Group):
    """guruhdan active studentlarni olish"""
    return group.students.filter(is_iactive=True)

# funks for group_student model end

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from administrator import service
# from employee.models import Employee

class HomePageView(View):
    def get(self, request):
        if request.user.is_authenticated:
            print(True)
        else:
            print(False)
        return render(request, 'index.html')


class RegisterEmployee(View):
    def get(self, request):
        filials = service.get_all_filials()
        print(filials)
        for filial in filials:
            print(filial.name)
            print(filial.region)
        return render(request, 'employee/register.html', {'filials': filials})

    def post(self, request):
        username = request.POST.get('username-input')
        first_name = request.POST.get('first-name-input')
        last_name = request.POST.get('last-name-input')
        password = request.POST.get('password-input')
        role = request.POST.get('role')
        filial = service.get_filial_with_id(request.POST.get('filial'))
        employee = service.create_employee(username, password, first_name, last_name, role, filial)
        if employee is False:
            messages.warning(request,message=f"{username} nomi band ")
            return redirect('register')
        messages.success(request, message=f"Xodim ma'lumotlari saqlandi")
        return redirect('home')
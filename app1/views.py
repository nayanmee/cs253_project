from django.shortcuts import render,redirect
from app1.models import Profile,Student,Department
from django.contrib.auth.models import User, auth
#import . from models
import openpyxl


def upload(request):
    if "GET" == request.method:
        return render(request, 'index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)

        return render(request, 'index.html', {"excel_data":excel_data})



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user_dummy = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        user_dummy.save()
        role=request.POST['role']
        pro=Profile.objects.create(user=user_dummy,role=role)
        #user=user_dummy
        
        pro.save()
        print("hi")
        print(pro.role)
        print(pro.user.username)

        #add messages latter
        return redirect('/register')
    else:
        return render(request,'register.html')


def login(request):
    if(request.method=="POST"):

        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            actual_user = Profile.objects.get(user=user)
            i=0
            if(actual_user.role=='Ta'):
                i=i+1
                #code for ta
            
            elif(actual_user.role=='Manager'):
                i=i+1
                #code for manager
            else:
                i=i+1
                #code for admin

                
            return redirect('/register')
        else:
            print('invalid Credentials')
            return redirect('/register')
    else:
        return render(request,'login.html')
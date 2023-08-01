from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from app.functions.functions import handle_uploaded_file

# Create your views here.
def login(request):
    try:
        userid=request.session['userid']
        return redirect("/home/")
    except:
        if request.method=="POST":
            userid=request.POST['username']
            password=request.POST['password']
            form=Employee.objects.filter(UserId=userid) & Employee.objects.filter(Password=password)
            if(len(form)==1):
                request.session['userid']=userid
                return redirect("/home/")
            else:
                messages.error(request,"Username or Password are Incorrect")
                return redirect("/")
        else:
            return render(request,"login.html")


def personalinfo(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            studentname=request.POST['studentname']
            dob=request.POST['dob']
            gender=request.POST['gender']
            phone=request.POST['phone']
            street=request.POST['street']
            city=request.POST['city']
            state=request.POST['state']
            pincode=request.POST['pincode']
            aadharnumber=request.POST['aadharnumber']
            postaladdress=request.POST['postaladdress']
            nationality=request.POST['nationality']
            form=Student_pinfo(Student_name=studentname,DOB=dob,Gender=gender,Phone=phone,Street=street,City=city,State=state,Pincode=pincode,AadharNumber=aadharnumber,PostalAddress=postaladdress,Nationality=nationality)
            if(len(Student_pinfo.objects.filter(AadharNumber__iexact=aadharnumber))==0):
                try:
                    form.save()
                    messages.success(request,"Form Submitted")
                    return redirect("/personalinfo/")
                except:
                    messages.error(request,"Data Not Submitted")
                    return redirect("/personalinfo/")
            else:
                messages.warning(request,"Aadharnumber already exist")
                return redirect("/personalinfo/")
        else:
            return render(request,"pinfo.html")
    except:
        return redirect("/")


def schoolinfo(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            studentid=request.POST['studentid']
            studentname=request.POST['studentname']
            totalfee=request.POST['totalfee']
            initialpaid=request.POST['initialpaid']
            balance=request.POST['balance']
            cl=request.POST['cl']
            datejoined=request.POST['datejoined']
            profilepicture=request.POST['ppicture']
            signaturepicture=request.POST['spicture']
            if(len(Student_sinfo.objects.filter(Student_id=studentid))==0):
                pform=Student_pinfo.objects.get(Student_name=studentname)
                if(Student_sinfo.objects.filter(Student_name=studentname).count()==0):
                    form=Student_sinfo(Student_id=studentid,Student_name=pform,TotalFee=totalfee,InitialPaid=initialpaid,Balance=balance,Class=cl,DateJoined=datejoined,ProfilePicture=profilepicture,SignaturePicture=signaturepicture)
                    try:
                        form.save()
                        handle_uploaded_file(profilepicture)
                        handle_uploaded_file(signaturepicture)
                        messages.success(request,"Form Submitted")
                        return redirect("/schoolinfo/")
                    except:
                        messages.error(request,"Data Not Submitted")
                        return redirect("/schoolinfo/")
                else:
                    message.error(request,"Student name already exist")
                    return redirect('/schoolinfo/')
            else:
                messages.warning(request,"StudentId already exist")
                return redirect("/schoolinfo/")
        else:
            return render(request,"sinfo.html")
    except:
        return redirect("/")


def home(request):
    try:
        userid=request.session['userid']
        return render(request,"home.html",{'userid':userid})
    except:
        return redirect("/")

def logout(request):
    del request.session['userid']
    return redirect("/")


def balancecheck(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            studentid=request.POST['studentid']
            try:
                form=Student_sinfo.objects.filter(Student_id__iexact=studentid)
                return render(request,'balancecheck.html',{'form':form})
            except:
                messages.warning(request,"Student Id doesn't exist")
                return render(request,'balancecheck.html') 
        else:
            return render(request,'balancecheck.html')
    except:
        return redirect("/")

def transactions(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            searchid=request.POST['search']
            form=Transaction.objects.filter(Student_id=searchid)
            return render(request,'transactions.html',{'form':form})
        else:
            form=Transaction.objects.all()
            return render(request,'transactions.html',{'form':form})
    except:
        return redirect("/")



def clearfee(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            studentid=request.POST['studentid']
            studentname=request.POST['studentname']
            amount=request.POST['amount']
            ttype=request.POST['ttype']
            date=request.POST['date']
            time=request.POST['time']
            status=request.POST['status']
            try:
                form=Student_sinfo.objects.get(Student_id__iexact=Student_id)
                pform=Student_pinfo.objects.get(Student_name=studentname)
                if(len(form.Student_name==studentname)!=0 and studentname==form.Student_name):
                    tform=Transaction(Student_id=form,Student_name=pform,Amount=amount,TransactionType=ttype,Date=date,Time=time,Status=status)
                    Amount=form.Balance
                    Amount=int(Amount)-amount
                    form.Balance=Amount
                    try:
                        form.save()
                        tform.save()
                        messages.success(request,"Form Submitted")
                        return render(request,"clearfee.html",{'form':form})
                    except:
                        messages.error(request,"Form not submitted")
                        return redirect('/clearfee/')
                else:
                    messages.error(request,"Student name doesn't match")
                    return redirect('/clearfee/')
            except:
                messages.error(request,"studentid doesn't match")
                return redirect('/clearfee/')
        else:
            return render(request,"clearfee.html")
    except:
        return redirect("/")  

                
def updatepinfo(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            searchid=request.POST['search']
            try:
                form=Student_sinfo.objects.get(Student_id__iexact=searchid)
                pform=Student_pinfo.objects.get(Student_name__iexact=form.Student_name)
                return render(request,"updatepinfo.html",{'pform':pform})
            except:
                messages.error(request,"Studentid doesn't exist")
                return render(request,"updatepinfo.html")
        else:
            return render(request,"updatepinfo.html")
    except:
        return redirect("/")

def updatesinfo(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            searchid=request.POST['search']
            try:
                form=Student_sinfo.objects.get(Student_id__iexact=searchid)
                return render(request,"updatesinfo.html",{'form':form})
            except:
                messages.error(request,"Studentid doesn't exist")
                return render(request,"/updatesinfo.html")
        else:
            return render(request,"updatesinfo.html")
    except:
        return redirect("/")

def deletestudent(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            searchid=request.POST['searchid']
            searchname=request.POST['searchname']
            try:
                sform=Student_sinfo.objects.filter(Student_id__iexact=searchid)
                pform=Student_pinfo.objects.filter(Student_name__iexact=sform.Student_name)
                try:
                    del sform
                    try:
                        del pform
                    except:
                        messages.error(request,"personal data not deleted")
                        return redirect("/deletestudent/")
                except:
                    messages.error(request,"data not deleted")
                    return redirect("/deletestudent/")
            except:
                messages.error(request,"Credentials are not matched")
                return redirect("/deletestudent/")
        else:
            return render(request,"deletestudent.html")
    except:
        return redirect("/")
    
def student(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            searchid=request.POST['searchid']
            searchname=request.POST['searchname']
            try:
                form=Student_sinfo.objects.get(Student_id__iexact=searchid)
                pform=Student_pinfo.objects.get(form.Student_name__iexact==searchname)
                return render(request,"student.html",{'form':form,'pform':pform})
            except:
                messages.error(request,"Student not found")
                return render(request,"student.html")
        else:
            return render(request,"student.html")
    except:
        return redirect("/")

def addemployee(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            uid=request.POST['uid']
            name=request.POST['name']
            phone=request.POST['phone']
            password=request.POST['password']
            jobdescription=request.POST['jobdescription']
            status=request.POST['status']
            if(len(Employee.objects.filter(UserId__iexact=uid))==0):
                form=Employee(UserId=uid,Name=name,Phone=phone,Password=password,JobDescription=jobdescription,Status=status)
                try:
                    form.save()
                    messages.success(request,"Employee added")
                    return redirect("/addemployee/")
                except:
                    messages.error(request,"Employee not added")
                    return redirect("/addemployee/")
            else:
                messages.warning(request,"User Id already exist")
                return redirect("/addemployee/")
        else:
            return render(request,"addemployee.html")
    except:
        return redirect("/")
                
def alltransactions(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            
            form=Transaction.objects.all()
            return render(request,'alltransactions.html',{'form':form})
        else:
            return render(request,'alltransactions.html')
    except:
        return redirect("/")


def allstudents(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            form=Student_sinfo.objects.all()
            print(form)
            pform=Student_pinfo.objects.all()
            return render(request,'allstudents.html',{'form':form,'pform':pform})
        else:
            return render(request,'allstudents.html')
    except:
        print("warning")
        return redirect("/")


def up(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            aadharnumber=request.POST['aadharnumber']
            form=Student_pinfo.objects.get(AadharNumber__iexact=aadharnumber)
            if(len(form)!=0):
                form.Student_name=request.POST['studentname']
                form.DOB=request.POST['dob']
                form.Gender=request.POST['gender']
                form.Phone=request.POST['phone']
                form.Street=request.POST['street']
                form.City=request.POST['city']
                form.State=request.POST['state']
                form.Pincode=request.POST['pincode']
                form.AadharNumber=aadharnumber
                form.PostalAddress=request.POST['postaladdress']
                form.Nationality=request.POST['nationality']
                try:
                    form.save()
                    messages.success(request,"Form Submitted")
                    return redirect("/up/")
                except:
                    messages.erreo(request,"Submission Failed")
                    return redirect("/up/")
        else:
            return render(request,"up.html")
    except:
        return redirect("/")

def us(request):
    try:
        userid=request.session['userid']
        if(request.method=="POST"):
            studentid=request.POST['studentid']
            form=Student_sinfo.objects.get(Student_id=studentid)
            if(len(form)!=0):
                form.Student_id=studentid
                form.Student_name=request.POST['studentname']
                form.TotalFee=request.POST['totalfee']
                form.InitialPaid=request.POST['initialpaid']
                form.Balance=request.POST['balance']
                form.Class=request.POST['cl']
                form.DateJoined=request.POST['datejoined']
                form.ProfilePicture=request.FILES['ppicture']
                form.SignaturePicture=request.FILES['spicture']
                try:
                    form.save()
                    messages.success(request,"Form Submitted")
                    return redirect("/us/")
                except:
                    messages.error(request,"Submission Failed")
                    return redirect("/us/")
        else:
            return render(request,"us.html")
    except:
        return redirect("/")
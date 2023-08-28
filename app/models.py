from django.db import models

class Student_pinfo(models.Model):
    Student_name=models.CharField(max_length=250,primary_key=True)
    DOB=models.DateField(max_length=10)
    Gender=models.CharField(max_length=250)
    Phone=models.BigIntegerField()
    Street=models.CharField(max_length=250)
    City=models.CharField(max_length=250)
    State=models.CharField(max_length=250)
    Pincode=models.CharField(max_length=250)
    AadharNumber=models.CharField(max_length=250)
    PostalAddress=models.TextField(max_length=250)
    Nationality=models.CharField(max_length=250)
    class Meta:
        db_table="PersonalInformation"
    def __str__(self):
        return str(self.Student_name)

class Student_sinfo(models.Model):
    Student_id=models.CharField(max_length=250,primary_key=True)
    Student_name=models.ForeignKey(Student_pinfo,on_delete=models.CASCADE)
    TotalFee=models.IntegerField()
    InitialPaid=models.IntegerField()
    Balance=models.CharField(max_length=250)
    Class=models.CharField(max_length=250)
    DateJoined=models.DateField(max_length=10)
    ProfilePicture=models.ImageField(max_length=250,upload_to='app/static/uploaded/')
    SignaturePicture=models.ImageField(max_length=250,null=True,upload_to='app/static/uploaded/')
    class Meta:
        db_table="SchoolInformation"
    def __str__(self):
        return str(self.Student_id)

class Employee(models.Model):
    UserId=models.CharField(max_length=250)
    Name=models.CharField(max_length=250)
    Phone=models.BigIntegerField()
    Password=models.CharField(max_length=250)
    JobDescription=models.CharField(max_length=250)
    Status=models.CharField(max_length=250,default="Active")
    class Meta:
        db_table="Employee"
    def __str__(self):
        return str(self.UserId)

class Transaction(models.Model):
    Student_id=models.ForeignKey(Student_sinfo,on_delete=models.CASCADE)
    Student_name=models.ForeignKey(Student_pinfo,on_delete=models.CASCADE)
    Amount=models.CharField(max_length=250)
    TransactionType=models.CharField(max_length=250)
    Date=models.DateField(auto_now_add=True)
    Time=models.TimeField(auto_now_add=True)
    Status=models.CharField(default="Incomplete",max_length=250)
    class Meta:
        db_table="Transaction"
    def __str__(self):
        return str(self.Student_id)
    

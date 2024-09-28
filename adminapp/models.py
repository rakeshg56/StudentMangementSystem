from django.db import models

# Create your models here.



class Admin(models.Model):
    #id=models.AutoField(primary_Key=True) AutoField  -AutoIncrement
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False)


    class Meta:
        db_table="admin_table"

    def __str__(self):
        return  self.username

class Course(models.Model):
    id=models.AutoField(primary_key=True) #AutoField  -AutoIncrement
    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(Honors)", "CSE(H)"))
    department=models.CharField(max_length=100,blank=False,choices=department_choices)
    academic_choices = (("2023-24", "2023-24"), ("2022-23", "2022-23"))
    program = models.CharField(max_length=100, blank=False)  # Add this line

    academicyear = models.CharField(max_length=20, blank=False,choices=academic_choices)
    sem_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))

    semester=models.CharField(max_length=10, blank=False,choices=sem_choices)

    year=models.IntegerField(blank=False)
    coursecode=models.CharField(max_length=20,blank=False)
    coursetitle = models.CharField(max_length=100, blank=False)
    ltps=models.CharField(max_length=10,blank=False)
    credits=models.FloatField(blank=False)

    class Meta:
        db_table="course_table"

    def __str__(self):
        return self.coursecode

class Student(models.Model):
    id=models.AutoField(primary_key=True) #AutoField  -AutoIncrement
    studentid=models.BigIntegerField(blank=False,unique=True)
    fullname=models.CharField(max_length=100,blank=False)
    gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"))
    gender=models.CharField(max_length=20,blank=False,choices=gender_choices)
    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(Honors)", "CSE(H)"))

    department=models.CharField(max_length=50,blank=False,choices=department_choices)
    program=models.CharField(max_length=50,blank=False)
    semester=models.CharField(max_length=10,blank=False)
    year=models.IntegerField(blank=False)
    password=models.CharField(max_length=100,blank=False,default="klu123")
    email=models.CharField(max_length=100,blank=False,unique=True)
    contact=models.CharField(max_length=20,blank=False,unique=True)

    class Meta:
        db_table="student_table"

class Faculty(models.Model):
    id=models.AutoField(primary_key=True) #AutoField  -AutoIncrement
    facultyid=models.BigIntegerField(blank=False,unique=True)
    fullname=models.CharField(max_length=100,blank=False)
    gender=models.CharField(max_length=20,blank=False)
    department=models.CharField(max_length=50,blank=False)
    qualification=models.CharField(max_length=50,blank=False)
    designation=models.CharField(max_length=50,blank=False)


    password=models.CharField(max_length=100,blank=False,default="klu123")
    email=models.CharField(max_length=100,blank=False,unique=True)
    contact=models.CharField(max_length=20,blank=False,unique=True)

    class Meta:
        db_table="faculty_table"

    def __str__(self):
        return str(self.facultyid)

class FacultyCourseMapping(models.Model):
    mappingid = models.AutoField(primary_key=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)#course is an obj of type Course
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    COMPONENT_CHOICES = (
        ("L", "Lecture"),
        ("T", "Tutorial"),
        ("P", "Practical"),
        ("S", "Skilling"),
    )

    component = models.CharField(max_length=10, blank=False, choices=COMPONENT_CHOICES, default="L")
    type = models.BooleanField(blank=False, default=True,verbose_name="Faculty Type")  # True - Main faculty, False - Assistant faculty
    section = models.IntegerField(blank=False, default=1)
    class Meta:
        db_table = "facultycoursemapping_table"

    def __str__(self):
        return f"{self.course.coursetitle}-{self.faculty.fullname}"










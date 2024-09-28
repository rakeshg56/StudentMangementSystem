from django import forms
from .models import Faculty,Student

class AddFacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty  #model name
        fields="__all__"#autofield hide
        exclude={"password"}
        label={"facultyid":"Enter Faculty Id"}

class AddStudentForm(forms.ModelForm):
    class Meta:
        model=Student  #model name
        fields="__all__"#autofield hide
        exclude={"password"}
        label={"studentid":"Enter student Id"}


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        exclude={"studentid"}


class FacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields="__all__"
        exclude={"facultyid"}








from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "age", "email", "attendance"]

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 18:
            raise forms.ValidationError("jashy 18 den kop bolushu kerek")

        return age

    def clean_attendance(self):
        attendance = self.cleaned_data["attendance"]
        if attendance <= 0:
            raise forms.ValidationError("sen student emessin")
        return attendance

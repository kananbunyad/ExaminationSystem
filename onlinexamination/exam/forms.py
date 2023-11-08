from django import forms
from . import models

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))



class CourseForm(forms.ModelForm):
    class Meta:
        model= models.Course
        fields=['course_name','question_number','total_marks']

class EnterCourseForm(forms.Form):
    courseID=forms.ModelChoiceField(queryset=models.Course.objects.all(), empty_label="Course Name", to_field_name="id")

class QuestionForm(forms.ModelForm):
    
    #this will show dropdown __str__ method course model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in course model and return it
    courseID=forms.ModelChoiceField(queryset=models.Course.objects.all(), empty_label="Course Name", to_field_name="id")
    class Meta:
        model= models.Question
        fields=['quiz_pic','answer1','answer2','answer3','answer4','answer5','answer6','answer7','answer8','answer9','answer10']

class StudentAnswerForm(forms.ModelForm):
    class Meta:
        model= models.StudentAnswer
        fields=['answer1','answer2','answer3','answer4','answer5','answer6','answer7','answer8','answer9','answer10']
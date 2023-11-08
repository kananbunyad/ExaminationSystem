from django.contrib import admin
from .models import Course, Question, Result, StudentAnswer

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 10

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'question_number', 'total_marks')
    inlines = [QuestionInline]

class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'marks', 'date')
    list_filter = ['exam']

class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7', 'answer8', 'answer9', 'answer10')


admin.site.register(Course, CourseAdmin)
admin.site.register(Question)
admin.site.register(Result, ResultAdmin)
admin.site.register(StudentAnswer, StudentAnswerAdmin)
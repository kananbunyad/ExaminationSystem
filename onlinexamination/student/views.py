from django.shortcuts import render
from . import forms,models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from exam import models as QMODEL
from exam import forms as QFORM


#for showing signup/login button for student
def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'student/studentclick.html')

def student_signup_view(request):
    userForm= forms.StudentUserForm()
    studentForm= forms.StudentForm()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm= forms.StudentUserForm(request.POST)
        studentForm= forms.StudentForm(request.POST, request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request,'student/studentsignup.html',context=mydict)

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_dashboard_view(request):
    dict={
    
    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    }
    return render(request,'student/student_dashboard.html',context=dict)

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_exam_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/student_exam.html',{'courses':courses})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def take_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    total_questions=QMODEL.Question.objects.all().filter(course=course).count()

    
    return render(request,'student/take_exam.html',{'course':course,'total_questions':total_questions})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def start_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    question=QMODEL.Question.objects.get(course=course)
    student_ins=request.user.student
    studentForm= QFORM.StudentAnswerForm()
    response= render(request,'student/start_exam.html',{'course':course,'question':question,'studentForm':studentForm})
    if request.method=='POST':
        studentForm= QFORM.StudentAnswerForm(request.POST,request.FILES)
        if studentForm.is_valid():
            student=studentForm.save(commit=False)
            student.student=student_ins
            student.course=course
            if not QMODEL.StudentAnswer.objects.filter(student=student_ins,course=course).exists():
                student.save()
            calculate_marks_view(request)
            return HttpResponseRedirect('/student/view-result')
    response.set_cookie('course_id',course.id)
    return response

def calculate_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course = QMODEL.Course.objects.get(id=course_id)
        total_marks = 0
        print(course)
        print(request.user.student)
        student_answers = QMODEL.StudentAnswer.objects.get(course=course, student=request.user.student)
        for i in range(1, 11):

            selected_ans = getattr(student_answers, f'answer{i}')
            real_answer_field = f'answer{i}'  # Field name for correct answer
            real_answer = getattr(QMODEL.Question.objects.get(course=course), real_answer_field)
            print(selected_ans, real_answer)

            if selected_ans == real_answer:
                total_marks += 10  # Assuming each correct answer adds 1 mark

        student = models.Student.objects.get(user_id=request.user.id)
        result = QMODEL.Result()
        result.marks = total_marks
        result.exam = course
        result.student = student
        result.save()



@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def view_result_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/view_result.html',{'courses':courses})
    

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def check_marks_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    student = models.Student.objects.get(user_id=request.user.id)
    results= QMODEL.Result.objects.all().filter(exam=course).filter(student=student)
    return render(request,'student/check_marks.html',{'results':results})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_marks_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/student_marks.html',{'courses':courses})
  
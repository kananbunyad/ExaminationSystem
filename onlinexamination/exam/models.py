from django.db import models

from student.models import Student


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.course_name


class Question(models.Model):
    quiz_pic = models.ImageField(upload_to='quiz_pic', blank=True)
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='question')

    cat = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    )

    answer1 = models.CharField(max_length=200, choices=cat, blank=True)
    answer2 = models.CharField(max_length=200, choices=cat, blank=True)
    answer3 = models.CharField(max_length=200, choices=cat, blank=True)
    answer4 = models.CharField(max_length=200, choices=cat, blank=True)
    answer5 = models.CharField(max_length=200, choices=cat, blank=True)
    answer6 = models.CharField(max_length=200, choices=cat, blank=True)
    answer7 = models.CharField(max_length=200, choices=cat, blank=True)
    answer8 = models.CharField(max_length=200, choices=cat, blank=True)
    answer9 = models.CharField(max_length=200, choices=cat, blank=True)
    answer10 = models.CharField(max_length=200, choices=cat, blank=True)


class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    cat = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    )

    answer1 = models.CharField(max_length=200, choices=cat, blank=True)
    answer2 = models.CharField(max_length=200, choices=cat, blank=True)
    answer3 = models.CharField(max_length=200, choices=cat, blank=True)
    answer4 = models.CharField(max_length=200, choices=cat, blank=True)
    answer5 = models.CharField(max_length=200, choices=cat, blank=True)
    answer6 = models.CharField(max_length=200, choices=cat, blank=True)
    answer7 = models.CharField(max_length=200, choices=cat, blank=True)
    answer8 = models.CharField(max_length=200, choices=cat, blank=True)
    answer9 = models.CharField(max_length=200, choices=cat, blank=True)
    answer10 = models.CharField(max_length=200, choices=cat, blank=True)


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

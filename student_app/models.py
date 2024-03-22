from django.db import models
from django.core import validators as v 
from .validators import validate_name_format, validate_student_email, validate_combination_format
from subject_app.models import Subject

# Create your models here.
# models.Model tell Django this is a Model that should be reflected on our database
class Student(models.Model):
    # CharField is a character field and has a default max length of 255 characters
    name = models.CharField(
        max_length=100, 
        null = False, 
        blank = False, 
        validators=[validate_name_format]
        )
    student_email = models.EmailField(
        unique = True, 
        null = False, 
        blank = False, 
        validators=[validate_student_email]
        )
    personal_email = models.EmailField(
        unique = True, 
        null = False, 
        blank = False
        )
    locker_number = models.IntegerField(
        unique = True, 
        default = 110, 
        null = False, 
        blank = False,  
        validators=[v.MinValueValidator(1), v.MaxValueValidator(200)]
        )
    locker_combination = models.CharField(
        max_length = 20, 
        default = "12-12-12", 
        null = False, 
        blank = False, 
        validators=[validate_combination_format]
        )
    good_student = models.BooleanField(
        default = True
        )
    subjects = models.ManyToManyField(
        Subject, 
        related_name = 'students'
        )
    
    # migrations are not necessary when adding/updating methods
    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number} - {self.good_student}"

    # sets student new locker assignment
    def locker_reassignment(self, new_locker_number):
        self.locker_number = new_locker_number
        self.save()

    def student_status(self):
        # switches status from True to False and vise versa
        self.good_student = not self.good_student
        self.save()
        
    def add_subject(self, subject_id):
        total_subjects = self.subjects.count()
        if total_subjects < 8:
            self.subjects.add(subject_id)
        else:
            raise Exception("This students class schedule is full!")
        
    def remove_subject(self, subject_id):
        total_subjects = self.subjects.count()
        if total_subjects > 0:
            self.subjects.remove(subject_id)
        else:
            raise Exception("This students class schedule is empty!")
        
    
    
    
    
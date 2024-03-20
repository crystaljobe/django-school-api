from django.db import models

# Create your models here.
# models.Model tell Django this is a Model that should be reflected on our database
class Student(models.Model):
    # CharField is a character field and has a default max length of 255 characters
    name = models.CharField(max_length=100, null = False, blank = False)
    student_email = models.EmailField(unique = True, null = False, blank = False)
    personal_email = models.EmailField(unique = True, null = False, blank = False)
    locker_number = models.IntegerField(unique = True, default=110, null = False, blank = False)
    locker_combination = models.CharField(max_length=20, default = "12-12-12", null = False, blank = False)
    good_student = models.BooleanField(default=True)
    
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
    
    
    
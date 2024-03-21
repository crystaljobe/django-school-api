from django.core.exceptions import ValidationError
import re

# validate name to only accepts string in the following format "First M. Last" 
# Validation Error: 'Name must be in the format "First Middle Initial. Last"'
def validate_name_format(name):
    regex = r'^[A-Za-z]+ [A-Z]\. [A-Z][a-z]+$'
    good_name = re.match(regex, name)
    if good_name:
        return name
    else: 
        raise ValidationError('Name must be in the format "First Middle Initial. Last"')
    
# validate_school_email: Only accepts string ending with "@school.com" # Validation Error: 'Invalid school email format. Please use an email ending with "@school.com".'
def validate_student_email(student_email):
    regex = r'^[\w.\-]+@school.com$'
    good_email = re.match(regex, student_email)
    if good_email:
        return student_email
    else:
        raise ValidationError('Invalid school email format. Please use an email ending with "@school.com".')

# validate_combination_format: Only accepts string in the following format "12-12-12" (Ensures there are numbers only)
# Validation Error: 'Combination must be in the format "12-12-12"'
def validate_combination_format(locker_combination):
    regex = r'^\d{2}-\d{2}-\d{2}$'
    good_combination = re.match(regex, locker_combination)
    if good_combination:
        return locker_combination
    else: 
        raise ValidationError('Combination must be in the format "12-12-12"')
    


from django.core.exceptions import ValidationError
import re

def validate_subject_format(subject_name):
    regex = r'^([A-Z][a-z]+\s)*[A-Z][a-z]+$'
    valid_subject = re.match(regex, subject_name)
    if valid_subject:
        return subject_name
    else:
        raise ValidationError('Subject must be in title case format.')

def validate_professor_name(professor):
    words = professor.split()
    if len(words) != 2:
        raise ValidationError('Professor name must be in the format "Professor Adam"')
    elif words[0] != 'Professor':
        raise ValidationError('Professor name must be in the format "Professor Adam"')
    elif words[1] != words[1].title():
        raise ValidationError('Professor name must be in the format "Professor Adam"')
    else:
        return professor
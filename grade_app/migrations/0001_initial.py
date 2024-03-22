# Generated by Django 5.0.3 on 2024-03-22 01:33

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_app', '0008_student_subjects'),
        ('subject_app', '0002_alter_subject_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=2, default=100.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('a_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='subject_app.subject')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='student_app.student')),
            ],
        ),
    ]

from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    num_students = models.IntegerField()
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    from faker import Faker
    from .models import Teacher

    def generate_teachers(n):
        fake = Faker()
        for _ in range(n):
            teacher = Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                subject=fake.job(),
                experience_years=fake.random_int(min=1, max=30),
                qualification=fake.random_element(elements=("Ph.D.", "Masters", "Bachelor"))
            )
            teacher.save()

    # groups/utils.py
    from faker import Faker
    from .models import Group
    from teachers.models import Teacher

    def generate_groups(n):
        fake = Faker()
        teachers = Teacher.objects.all()
        for _ in range(n):
            group = Group.objects.create(
                name=fake.company(),
                year=fake.year(),
                course=fake.random_element(elements=("Mathematics", "Physics", "Chemistry")),
                department=fake.random_element(elements=("Science", "Arts", "Commerce")),
                num_students=fake.random_int(min=10, max=50),
                teacher=fake.random_element(teachers)
            )
            group.save()
            from django.shortcuts import render
            from .models import Teacher

            def get_teachers(request):
                teachers = Teacher.objects.all()
                return render(request, 'teachers/teachers_list.html', {'teachers': teachers})

            # groups/views.py
            from django.shortcuts import render
            from .models import Group

            def get_groups(request):
                groups = Group.objects.all()
                return render(request, 'groups/groups_list.html', {'groups': groups})
            #c view пока проблемы(
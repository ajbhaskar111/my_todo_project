from django.db import models


# Create your models here.
class master(models.Model):
    Role = models.ForeignKey(Role, on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length = 25)
    IsActive = models.BooleanField(default=False)


gender_choise =(
    ('m', 'male'),
    ('f', 'female')
)
class users(models.Model):
    master = models.ForeignKey(master, on_delete=models.CASCADE)
    ProfileImage = models.FileField(upload_to='users/avatars', default='avatar.png')
    FullName = models.CharField(max_length = 35, blank=True, null=True)
    Gender = models.CharField(max_length=2, choices=gender_choise)
    Dob = models.DateField()
    Phone = models.CharField(max_length = 10, unique = True, blank=True, null=True)
    Pincode = models.CharField(max_length= 5, blank=True, null=True)
    Website = models.CharField(max_length = 35, blank=True, null=True)
    Languages = models.CharField(max_length = 35, blank=True, null=True)
    City = models.CharField(max_length = 35, blank=True, null=True)
    State = models.CharField(max_length = 35, blank=True, null=True)
    Address_1 = models.CharField(max_length = 35, blank=True, null=True)
    Address_2 = models.CharField(max_length = 35, blank=True, null=True)
    Country = models.CharField(max_length = 35, blank=True, null=True)
    Twitter = models.CharField(max_length = 35, blank=True, null=True)
    Instagram = models.CharField(max_length = 35, blank=True, null=True)
    Website = models.CharField(max_length = 35, blank=True, null=True)
    Facebook = models.CharField(max_length = 35, blank=True, null=True)
    
    
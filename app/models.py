from django.db import models

class Expert(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    date_of_birth = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Image(models.Model):
    expert = models.OneToOneField(Expert, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to=f'profile_pictures', blank=True, null=True)

class ContactDetails(models.Model):
    expert = models.OneToOneField(Expert, on_delete=models.CASCADE, related_name='contact_details')
    email_address = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.email_address} \n {self.phone}'

class Experience(models.Model):
    expert = models.OneToOneField(Expert, on_delete=models.CASCADE, related_name='experience')
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    duration = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.company_name} \n {self.position} \n {self.duration}'

class Education(models.Model):
    expert = models.OneToOneField(Expert, on_delete=models.CASCADE, related_name='education')
    institution = models.CharField(max_length=1000)
    degree = models.CharField(max_length=100)
    duration = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.institution} \n {self.degree} \n {self.duration}'

class Service(models.Model):
    expert = models.OneToOneField(Expert, on_delete=models.CASCADE, related_name='service')
    name = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'

class Project(models.Model):
    expert = models.OneToOneField(Expert, on_delete=models.CASCADE, related_name='project')
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='project_images', null=True)

    def __str__(self):
        return f'{self.project_name} \n {self.link}'

class Document(models.Model):
    expert = models.OneToOneField(Expert, on_delete=models.CASCADE, related_name='document')
    resume = models.FileField(upload_to='documents/resume')



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'Name: {self.name} \n Email: {self.email} \n Subject: {self.subject}'

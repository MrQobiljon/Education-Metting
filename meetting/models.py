from django.db import models

from django.core.validators import FileExtensionValidator

# Create your models here.



class Navbar(models.Model):
    prev_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    video = models.FileField(upload_to='video/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
                             help_text="Upload video.\nVideo resolution should be 960x600.")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Navbar'
        verbose_name_plural = 'Navbars'


class Strongest(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    logo = models.ImageField(upload_to='strongest/', help_text='Let the size of the logo be 60x60.')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'The strongest'
        verbose_name_plural = 'The strongest'


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Meeting Category'
        verbose_name_plural = 'Meeting Categories'



class Meeting(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='meeting/', help_text="Image size should be 370x215.")
    location = models.CharField(max_length=255)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Meeting'
        verbose_name_plural = 'Meetings'



class TimeMeeting(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    date_meeting_1 = models.DateField(blank=True, null=True)
    time_meeting_1 = models.TimeField(blank=True, null=True)
    date_meeting_2 = models.DateField(blank=True, null=True)
    time_meeting_2 = models.TimeField(blank=True, null=True)


class Phone(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, default='+')



class Course(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='course/', help_text="Image size should be 270x170")



class AboutUniversity(models.Model):
    succesed_students = models.IntegerField(default=100, blank=True, null=True)
    new_students = models.IntegerField(default=1, blank=True, null=True)
    current_teachers = models.BigIntegerField(blank=True, null=True)
    awards = models.IntegerField(blank=True, null=True)
    video = models.URLField(blank=True, null=True, help_text="Paste the youtube html code of the video")

    def __str__(self):
        return "About University"

    class Meta:
        verbose_name = 'About University'
        verbose_name_plural = 'About University'



class AboutMe(models.Model):
    phone = models.CharField(max_length=15, default='+')
    mail = models.EmailField()
    address = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return "About Me"

    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'



class Message(models.Model):
    name = models.CharField(max_length=255)
    mail = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
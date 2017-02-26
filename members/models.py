from django.db import models

# from django.utils import timezone
# from django.core.validators import MaxValueValidator, MinValueValidator

class Member(models.Model):
    name = models.CharField(max_length=255)
    place_of_residence = models.CharField(max_length=255)
    email_addr = models.EmailField()
    joined = models.DateTimeField(auto_now_add=True)
    confirmed_member = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# class Observation(models.Model):
#     title = models.CharField(max_length=255)
#     tags = TaggableManager(through=TaggedItem)
#     # timestamp = models.DateTimeField(default=timezone.now)
#     start_time = models.DateTimeField(default=timezone.now)
#     subject = models.CharField(max_length=255, default="Me")
#     annotation = models.CharField(max_length=2048)
#
#     def __str__(self):
#         return self.title
#
# class SpannedObservation(Observation):
#     # title = models.CharField(max_length=255)
#     # tags = TaggableManager(through=TaggedItem)
#     # start_time = models.DateTimeField(default=timezone.now)
#     end_time = models.DateTimeField()
#     # subject = models.CharField(max_length=255, default="Me")
#     # annotation = models.CharField(max_length=2048)
#     # def __str__(self):
#     #     return self.title
#
# class PsychoState(models.Model):
#     title = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(default=timezone.now)
#     valence = models.FloatField(
#         validators=[MinValueValidator(-100), MaxValueValidator(100)]
#     )
#     arousal = models.FloatField(
#         validators=[MinValueValidator(0), MaxValueValidator(100)]
#     )
#     annotation = models.CharField(max_length=2048)
#
#     def __str__(self):
#         return ', '.join([self.title, str(self.valence), str(self.arousal)])

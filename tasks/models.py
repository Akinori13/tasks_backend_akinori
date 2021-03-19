from django.db import models

# Create your models here.
class Tasks(models.Model):
    status_List = [
        (0, "To do"),
        (1, "In progress"),
        (2, "Done"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.IntegerField(choices=status_List)

    def __str__(self) -> str:
        return self.title
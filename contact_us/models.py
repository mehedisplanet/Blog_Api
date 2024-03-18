from django.db import models

# Create your models here.

class Contact_us(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField(null=False)
    message=models.TextField(null=False)

    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f"Name : {self.name} Email : {self.email}"
    
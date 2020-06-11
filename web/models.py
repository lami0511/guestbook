from django.db import models

# Create your models here.
class Message(models.Model):
    user = models.CharField("姓名", max_length=50)
    subject = models.CharField("主題", max_length=200)
    content = models.TextField("內容")
    publication = models.DateTimeField("留言時間",  auto_now_add=True)

    def __str__(self):
       return self.user + ":"  + self.subject
       
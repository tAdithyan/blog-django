from django.db import models

# Create your models here.
class Blog(models.Model):
  name=models.CharField(max_length=100)
  title=models.CharField(max_length=100)
  short_desc=models.CharField(max_length=500)
  content=models.TextField()
  thmbnail=models.ImageField(upload_to='blogimages')
  created_at=models.TimeField(auto_now_add=True)
  def __str__(self) -> str:
    return self.title
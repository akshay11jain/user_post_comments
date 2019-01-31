from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    token = models.CharField(max_length = 150)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "User"

class Post(models.Model):
    post_Id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post_title = models.CharField(max_length = 50)
    post_description = models.CharField(max_length = 500)
    def __str__(self):
        return self.post_title
    class Meta:
        verbose_name_plural = "post"

class Comments(models.Model):
    comment_Id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.CharField(max_length = 200)
    def __str__(self):
        return self.post.post_title
    class Meta:
        verbose_name_plural = "Comment"
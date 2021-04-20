from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce import models as tinymce_models


User = get_user_model()

class Author(models.Model):
    profile_picture = models.ImageField()
    user =  models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length = 30)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length = 100) 
    overview = models.TextField()
    content = tinymce_models.HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    thumbnail_picture = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey('self', related_name = 'previous',on_delete = models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name = 'next', on_delete = models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs ={
            'id':self.id,
        })

    def get_update_url(self):
        return reverse('post-update', kwargs ={
            'id':self.id,
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs ={
            'id':self.id,
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def view_count(self):
        return Postviews.objects.filter(post=self).count()

    @property
    def comment_count(self):
        return Postviews.objects.filter(post=self).count()



class Comment(models.Model):
    user =  models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    post = models.ForeignKey('Post', related_name = 'comments' ,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.user.username


class Postviews(models.Model):
    user =  models.ForeignKey(User ,on_delete = models.CASCADE)
    post = models.ForeignKey('Post',on_delete = models.CASCADE )


    def __str__(self):
        return self.user.username

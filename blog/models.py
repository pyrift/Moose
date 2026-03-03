from django.db import models


class CreatedDate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Author(CreatedDate):
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='author_img')
    profession = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


class Tag(CreatedDate):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(CreatedDate):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='post_img')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class About(CreatedDate):
    title  = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_img')

    author_name = models.CharField(max_length=50)
    author_image = models.ImageField(upload_to='about_img')
    author_information = models.TextField()

    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

class Comment(CreatedDate):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField()

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Contacts(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.full_name



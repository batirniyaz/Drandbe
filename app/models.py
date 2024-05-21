from django.db import models
from django.contrib.auth.models import User


class AboutModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    telegram = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    youtube = models.URLField(max_length=200)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class OurPartnersModel(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/')
    url = models.URLField(max_length=200, default='https://drandbe/')

    def __str__(self):
        return self.name


class ServicesModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title


class TestimonialModel(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.name


class ProjectCategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PortfolioModel(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = 'PUBLISHED', 'Published'
        DRAFT = 'DRAFT', 'Draft'
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(ProjectCategoryModel, on_delete=models.CASCADE)
    client = models.CharField(max_length=100, default='')
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='portfolio/')
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class TeamMembersModel(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='team_images/')
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class FaqModel(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question


class BlogCategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(BlogCategoryModel, on_delete=models.CASCADE)
    author = models.ForeignKey(TeamMembersModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AwardsModel(models.Model):
    name_of_award = models.CharField(max_length=100)
    description = models.TextField()
    certificate = models.ImageField(upload_to='award_images/')
    place = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_of_award

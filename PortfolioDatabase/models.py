from django.db import models

# Create your models here.


class Hobbies(models.Model):

    def __str__(self):
        return self.hobby_name+ "- " + self.hobby_desc

    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=200)
    hobby_image = models.CharField(max_length=500, default="https://pbs.twimg.com/profile_images/630563733656350720/tDOhLnsW_400x400.jpg")


class Portfolio(models.Model):
    def __str__(self):
        return self.portfolio_name + "- " + self.portfolio_desc

    portfolio_name = models.CharField(max_length=200)
    portfolio_desc = models.CharField(max_length=200)
    portfolio_image = models.CharField(max_length=500,
                                   default="https://images.idgesg.net/images/article/2018/09/macos-high-sierra-folder-icon-100773103-large.jpg")

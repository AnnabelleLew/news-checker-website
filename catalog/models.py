from django.db import models
from django.contrib.auth.models import User

# Create Article model (stores the article text and link)
class Article(models.Model):
    """Model representing an article."""
    url = models.CharField(max_length=300, help_text='Enter URL for article')
    text = models.TextField(help_text='Enter article text')

    def __str__(self):
        """String for representing the Model object."""
        return self.url

# Create ArticleBias model (stores the article, as well as the reader and their thoughts on it's bias)
class ArticleBias(models.Model):
    """Model representing the bias of an article."""
    article = models.ForeignKey('Article', on_delete=models.SET_NULL, null=True)
    bias = models.IntegerField()
    reader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.article} ({self.bias})'

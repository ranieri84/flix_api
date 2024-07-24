from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):

    title = models.CharField(max_length=200)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='movies')    # busca todos os movies que tem o mesmo objeto
    actors = models.ManyToManyField(Actor, related_name='movies')
    release_date = models.DateField(blank=True, null=True)
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

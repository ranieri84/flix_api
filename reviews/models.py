from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'  # ao fazer obj.review sendo o obj movie, ele busca os campos reviews
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Não pode ser inferior a 0 estrelas'),
            MaxValueValidator(5, 'A valianão não pode ser superior a 5 estrelas')])
    comment = models.TextField(null=True, blank=True)

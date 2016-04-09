from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=100)
    _99popularity = models.FloatField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=400)
    imdb_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'movies'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __unicode__(self):
        return str(self.name)[:50]
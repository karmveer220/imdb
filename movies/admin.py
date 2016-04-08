from django import forms
from django.contrib import admin
from movies.models import Movies

class MovieForm(forms.ModelForm):
    name = forms.CharField(min_length=2, max_length=100, help_text="Please enter movie name between 2 to 100 characters")
    _99popularity = forms.FloatField(min_value=0.0,max_value=100.0, help_text="Please enter 99popularity between 0.0 to 100.0")
    director = forms.CharField(min_length=2, max_length=100, help_text="Please enter director name between 2 to 100 characters")
    genre = forms.CharField(max_length=400, help_text="Please give comma separated values")
    imdb_score = forms.FloatField(min_value=0.0,max_value=10.0, help_text="Please enter imdb score between 0.0 to 10.0")

    class Meta:
        model = Movies
        
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name', '_99popularity','director','genre', 'imdb_score', 'created_at')
    list_per_page = 30
    fields = ('name', '_99popularity','director','genre', 'imdb_score')
    search_fields = ['name', 'director']
    ordering = ['name']
    readonly_fields = ('created_at',)
    
    form = MovieForm
     
admin.site.register(Movies, MoviesAdmin)
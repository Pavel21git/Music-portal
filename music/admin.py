from django.contrib import admin
from .models import Artist, Album, Song, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class SongInline(admin.TabularInline):
    model = Song
    extra = 1


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'release_date')
    list_filter = ('genre', 'release_date')
    search_fields = ('title', 'artist__name')
    inlines = [SongInline]


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'album', 'duration')
    search_fields = ('title', 'artist_name', 'album_title')
    list_filter = ('artist', 'album')

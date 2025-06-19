from django.core.management.base import BaseCommand
from faker import Faker
import random
from music.models import Artist, Album, Song, Genre
from datetime import timedelta

class Command(BaseCommand):
    help = 'Generates fake data for artists, albums, songs, and genres.'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear old data
        Song.objects.all().delete()
        Album.objects.all().delete()
        Artist.objects.all().delete()
        Genre.objects.all().delete()

        genres = ['Pop', 'Rock', 'Hip-Hop', 'Jazz', 'Classical']
        genre_objs = [Genre.objects.create(name=g) for g in genres]

        for _ in range(5):  # Artists
            artist = Artist.objects.create(name=fake.name())

            for _ in range(random.randint(1, 3)):  # Albums
                album = Album.objects.create(
                    title=fake.word().capitalize(),
                    artist=artist,
                    genre=random.choice(genre_objs),
                    release_date=fake.date_between(start_date='-5y', end_date='today')
                )

                for _ in range(random.randint(3, 7)):  # Songs
                    Song.objects.create(
                        title=fake.word().capitalize(),
                        album=album,
                        artist=artist,
                        duration=timedelta(seconds=random.randint(120, 300)),
                        file='songs/example.mp3'  # placeholder file
                    )

        self.stdout.write(self.style.SUCCESS('✅ Fake data generated successfully!'))
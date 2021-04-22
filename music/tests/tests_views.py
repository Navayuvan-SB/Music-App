from django.test import TestCase
from music.models import MusicDirector, Music, Genre, Album, Label
from django.urls import reverse


class MusicListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        music_director = MusicDirector.objects.create(
            name="Sam Henry",
            website="https://google.co.in",
            date_of_birth="1980-06-11",
            phone_number="9897927297"
        )

        label = Label.objects.create(
            name="Sample Label Company",
            founded_date="1989-03-12",
            headquarters="USA"
        )

        number_of_genres = 2
        for genre_id in range(number_of_genres):
            Genre.objects.create(
                title=f"Genre {genre_id}"
            )
        genres = Genre.objects.all()

        album = Album.objects.create(
            name="Album Name",
            subtitle="A sample description",
            music_director=music_director,
            label=label,
            asin="8574ASDASD",
            release_date="2014-03-24"
        )
        album.genre.set(genres)
        album.save()

        number_of_musics = 10
        for music_id in range(number_of_musics):
            music = Music.objects.create(
                name=f"Music {music_id}",
                music_director=music_director,
                duration="03:11",
                album=album)

            music.genre.set(genres)
            music.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/musics/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("musics"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("musics"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "music/music_list.html")

    def test_view_render_all_movies(self):
        response = self.client.get(reverse("musics"))
        self.assertEqual(len(response.context["music_list"]), 10)


class MusicDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        music_director = MusicDirector.objects.create(
            name="Sam Henry",
            website="https://google.co.in",
            date_of_birth="1980-06-11",
            phone_number="9897927297"
        )

        label = Label.objects.create(
            name="Sample Label Company",
            founded_date="1989-03-12",
            headquarters="USA"
        )

        number_of_genres = 2
        for genre_id in range(number_of_genres):
            Genre.objects.create(
                title=f"Genre {genre_id}"
            )
        genres = Genre.objects.all()

        album = Album.objects.create(
            name="Album Name",
            subtitle="A sample description",
            music_director=music_director,
            label=label,
            asin="8574ASDASD",
            release_date="2014-03-24"
        )
        album.genre.set(genres)
        album.save()

        number_of_musics = 3
        for music_id in range(number_of_musics):
            music = Music.objects.create(
                name=f"Music {music_id}",
                music_director=music_director,
                duration="03:11",
                album=album,
                slug=f"music-{music_id}"
            )

            music.genre.set(genres)
            music.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/musics/music/music-1")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(
            reverse("music-detail", kwargs={"slug": "music-1"})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse("music-detail", kwargs={"slug": "music-1"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "music/music_detail.html")

    def test_view_displays_correct_movie(self):
        response = self.client.get(
            reverse("music-detail", kwargs={"slug": "music-1"})
        )
        self.assertContains(response, "Music 1")


class AlbumListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        music_director = MusicDirector.objects.create(
            name="Sam Henry",
            website="https://google.co.in",
            date_of_birth="1980-06-11",
            phone_number="9897927297"
        )

        label = Label.objects.create(
            name="Sample Label Company",
            founded_date="1989-03-12",
            headquarters="USA"
        )

        number_of_genres = 2
        for genre_id in range(number_of_genres):
            Genre.objects.create(
                title=f"Genre {genre_id}"
            )
        genres = Genre.objects.all()

        number_of_albums = 10
        for album_id in range(number_of_albums):
            album = Album.objects.create(
                name=f"Album Name {album_id}",
                subtitle="A sample description",
                music_director=music_director,
                label=label,
                asin="8574ASDASD",
                release_date="2014-03-24"
            )
            album.genre.set(genres)
            album.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/musics/albums/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("albums"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("albums"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "music/album_list.html")

    def test_view_render_all_movies(self):
        response = self.client.get(reverse("albums"))
        self.assertEqual(len(response.context["album_list"]), 10)



class AlbumDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        music_director = MusicDirector.objects.create(
            name="Sam Henry",
            website="https://google.co.in",
            date_of_birth="1980-06-11",
            phone_number="9897927297"
        )

        label = Label.objects.create(
            name="Sample Label Company",
            founded_date="1989-03-12",
            headquarters="USA"
        )

        number_of_genres = 2
        for genre_id in range(number_of_genres):
            Genre.objects.create(
                title=f"Genre {genre_id}"
            )
        genres = Genre.objects.all()

        number_of_albums = 2
        for album_id in range(number_of_albums):
            album = Album.objects.create(
                name=f"Album Name {album_id}",
                subtitle="A sample description",
                music_director=music_director,
                label=label,
                asin="8574ASDASD",
                release_date="2014-03-24",
                slug=f"album-{album_id}"
            )
            album.genre.set(genres)
            album.save()


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/musics/albums/album-1")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(
            reverse("album-detail", kwargs={"slug": "album-1"})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse("album-detail", kwargs={"slug": "album-1"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "music/album_detail.html")

    def test_view_displays_correct_movie(self):
        response = self.client.get(
            reverse("album-detail", kwargs={"slug": "album-1"})
        )
        self.assertContains(response, "Album Name 1")




class GenreListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        music_director = MusicDirector.objects.create(
            name="Sam Henry",
            website="https://google.co.in",
            date_of_birth="1980-06-11",
            phone_number="9897927297"
        )

        label = Label.objects.create(
            name="Sample Label Company",
            founded_date="1989-03-12",
            headquarters="USA"
        )

        number_of_genres = 10
        for genre_id in range(number_of_genres):
            Genre.objects.create(
                title=f"Genre {genre_id}"
            )
        genres = Genre.objects.all()

        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/musics/genres/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("genres"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("genres"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "music/genre_list.html")

    def test_view_render_all_movies(self):
        response = self.client.get(reverse("genres"))
        self.assertEqual(len(response.context["genre_list"]), 10)


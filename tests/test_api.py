try:
    from app import create_app
except ModuleNotFoundError:
    import os,sys
    from os.path import dirname, join, abspath
    sys.path.insert(0, abspath(join(dirname(__file__), '..')))    
    from app import create_app

import unittest
import json
from flask import current_app
from app.models import Song,Podcast,Audiobook
from datetime import datetime,timedelta


class TestCreateWithInvalidData(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        from random import randint
        self.fmt = "%Y-%m-%d %H:%M:%S"
        self.record = randint(10,100)
        self.uploaded = (datetime.now()+timedelta(days=self.record)).strftime(self.fmt)

    @classmethod
    def tearDownClass(self):
        _song = Song.objects(song_id=self.record).first()
        _podcast = Podcast.objects(podcast_id=self.record).first()
        _audiobook = Audiobook.objects(audiobook_id=self.record).first()
        if _song:
            _song.delete()
        if _podcast:
            _podcast.delete()
        if _audiobook:
            _audiobook.delete()
        self.app_context.pop()
    
    def test_create_song_with_id_as_string(self):
        _song = {
            "id": str("id"),
            "name": "Name-{}".format(self.record),
            "duration" : self.record,
            "uploaded": self.uploaded
        }
        response = self.client.post('/song', json=_song,content_type='application/json')
        self.assertEqual(response.status_code,400)
    
    def test_create_song_with_name_as_integer(self):
        _song = {
            "id": self.record,
            "name": self.record,
            "duration" : self.record,
            "uploaded": self.uploaded
        }
        response = self.client.post('/song', json=_song,content_type='application/json')
        self.assertEqual(response.status_code,400)
    
    def test_create_song_with_duration_as_string(self):
        _song = {
            "id": self.record,
            "name": "Name-{}".format(self.record),
            "duration" : "duration",
            "uploaded": self.uploaded
        }
        response = self.client.post('/song', json=_song,content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_create_song_with_uploaded_as_string(self):
        _song = {
            "id": self.record,
            "name": "Name-{}".format(self.record),
            "duration" : self.record,
            "uploaded": "uploaded"
        }
        response = self.client.post('/song', json=_song,content_type='application/json')
        self.assertEqual(response.status_code,400)
    
    def test_create_podcast_with_id_as_string(self):
        _podcast = {
            "id": str("id"),
            "name": "Name-{}".format(self.record),
            "duration": self.record,
            "uploaded": self.uploaded,
            "host":"Host-{}".format(self.record),
            "participants": ["Participant-{}".format(i) for i in range(self.record%10)]
        }
        response = self.client.post('/podcast', json=_podcast,content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_create_podcast_with_name_as_integer(self):
        _podcast = {
            "id": self.record,
            "name": self.record,
            "duration": self.record,
            "uploaded": self.uploaded,
            "host":"Host-{}".format(self.record),
            "participants": ["Participant-{}".format(i) for i in range(self.record%10)]
        }
        response = self.client.post('/song', json=_podcast,content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_create_podcast_with_duration_as_string(self):
        _podcast = {
            "id": self.record,
            "name": "Name-{}".format(self.record),
            "duration": "duration",
            "uploaded": self.uploaded,
            "host":"Host-{}".format(self.record),
            "participants": ["Participant-{}".format(i) for i in range(self.record%10)]
        }
        response = self.client.post('/podcast', json=_podcast,content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_create_podcast_with_uploaded_as_string(self):
        _podcast = {
            "id": self.record,
            "name": "Name-{}".format(self.record),
            "duration": self.record,
            "uploaded": "uploaded",
            "host":"Host-{}".format(self.record),
            "participants": ["Participant-{}".format(i) for i in range(self.record%10)]
        }
        response = self.client.post('/podcast', json=_podcast,content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_create_podcast_with_host_as_integer(self):
        _podcast = {
            "id": self.record,
            "name": "Name-{}".format(self.record),
            "duration": self.record,
            "uploaded": self.uploaded,
            "host": self.record,
            "participants": ["Participant-{}".format(i) for i in range(self.record%10)]
        }
        response = self.client.post('/podcast', json=_podcast,content_type='application/json')
        self.assertEqual(response.status_code,400)
    
    def test_create_audiobook_with_id_as_string(self):
        _audiobook = {
            "id": str("id"),
            "title": "Title-{}".format(self.record),
            "author": "Author-{}".format(self.record),
            "narrator": "Narrator-{}".format(self.record),
            "duration" : self.record,
            "uploaded": self.uploaded
        }
        response = self.client.post('/audiobook', json=_audiobook,content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_create_audiobook_with_title_as_integer(self):
        _audiobook = {
            "id": self.record,
            "title": self.record,
            "author": "Author-{}".format(self.record),
            "narrator": "Narrator-{}".format(self.record),
            "duration" : self.record,
            "uploaded": self.uploaded
        }
        response = self.client.post('/audiobook', json=_audiobook,content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_create_audiobook_with_author_as_integer(self):
        _audiobook = {
            "id": self.record,
            "title": "Title-{}".format(self.record),
            "author": self.record,
            "narrator": "Narrator-{}".format(self.record),
            "duration" : self.record,
            "uploaded": self.uploaded
        }
        response = self.client.post('/audiobook', json=_audiobook,content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_create_audiobook_with_narrator_as_integer(self):
        _audiobook = {
            "id": self.record,
            "title": "Title-{}".format(self.record),
            "author": "Author-{}".format(self.record),
            "narrator": self.record,
            "duration" : self.record,
            "uploaded": self.uploaded
        }
        response = self.client.post('/audiobook', json=_audiobook,content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_create_audiobook_with_duration_as_string(self):
        _audiobook = {
            "id": self.record,
            "title": "Title-{}".format(self.record),
            "author": "Author-{}".format(self.record),
            "narrator": "Narrator-{}".format(self.record),
            "duration" : "duration",
            "uploaded": self.uploaded
        }
        response = self.client.post('/audiobook', json=_audiobook,content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_create_audiobook_with_uploaded_as_string(self):
        _audiobook = {
            "id": self.record,
            "title": "Title-{}".format(self.record),
            "author": "Author-{}".format(self.record),
            "narrator": "Narrator-{}".format(self.record),
            "duration" : self.record,
            "uploaded": "uploaded"
        }
        response = self.client.post('/audiobook', json=_audiobook,content_type='application/json')
        self.assertEqual(response.status_code,400)


class CreateAudioFiles(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        from random import randint
        self.fmt = "%Y-%m-%d %H:%M:%S"
        self.record = randint(10,100)
        self.uploaded = (datetime.now()+timedelta(days=self.record)).strftime(self.fmt)
        self._song = {
            "id": self.record,
            "name": "Name-{}".format(self.record),
            "duration" : self.record,
            "uploaded": self.uploaded
        }
        self._podcast = {
            "id": self.record,
            "name": "Name-{}".format(self.record),
            "duration": self.record,
            "uploaded": self.uploaded,
            "host":"Host-{}".format(self.record),
            "participants": ["Participant-{}".format(i) for i in range(self.record%10)]
        }                
        self._audiobook = {
            "id": self.record,
            "title": "Title-{}".format(self.record),
            "author": "Author-{}".format(self.record),
            "narrator": "Narrator-{}".format(self.record),
            "duration" : self.record,
            "uploaded": self.uploaded
        }

    @classmethod
    def tearDownClass(self):
        _song = Song.objects(song_id=self.record).first()
        _podcast = Podcast.objects(podcast_id=self.record).first()
        _audiobook = Audiobook.objects(audiobook_id=self.record).first()
        if _song:
            _song.delete()
        if _podcast:
            _podcast.delete()
        if _audiobook:
            _audiobook.delete()
        self.app_context.pop()

    def test_create_song(self):
        response = self.client.post('/song', json=self._song,content_type='application/json')
        self.assertEqual(response.status_code,200)

    def test_create_podcast(self):
        response = self.client.post('/podcast', json=self._podcast,content_type='application/json')
        self.assertEqual(response.status_code,200)

    def test_create_audiobook(self):
        response = self.client.post('/audiobook', json=self._audiobook,content_type='application/json')
        self.assertEqual(response.status_code,200)


class GetAudioFile(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        from random import randint
        self.fmt = "%Y-%m-%d %H:%M:%S"
        self.record = randint(10,100)
        self.uploaded = (datetime.now()+timedelta(days=self.record)).strftime(self.fmt)
        self._song = {
            "song_id": self.record,
            "name": "Name-{}".format(self.record),
            "duration" : self.record,
            "uploaded": self.uploaded
        }
        self._podcast = {
            "podcast_id": self.record,
            "name": "Name-{}".format(self.record),
            "duration": self.record,
            "uploaded": self.uploaded,
            "host":"Host-{}".format(self.record),
            "participants": ["Participant-{}".format(i) for i in range(self.record%10)]
        }                
        self._audiobook = {
            "audiobook_id": self.record,
            "title": "Title-{}".format(self.record),
            "author": "Author-{}".format(self.record),
            "narrator": "Narrator-{}".format(self.record),
            "duration" : self.record,
            "uploaded": self.uploaded                
        }
        Song(**self._song).save()
        Podcast(**self._podcast).save()
        Audiobook(**self._audiobook).save()

    @classmethod
    def tearDownClass(self):
        _song = Song.objects(song_id=self.record).first()
        _podcast = Podcast.objects(podcast_id=self.record).first()
        _audiobook = Audiobook.objects(audiobook_id=self.record).first()
        if _song:
            _song.delete()
        if _podcast:
            _podcast.delete()
        if _audiobook:
            _audiobook.delete()
        self.app_context.pop()

    def test_get_song_details(self):
        _url = '/song/{}'.format(self.record)
        response = self.client.get(_url)
        self.assertEqual(response.status_code,200)
        data = response.get_json()
        self.assertIsInstance(data,dict)
        self.assertEqual(len(data),4)
        self.assertIn('id',data)
        self.assertIn('name',data)
        self.assertIn('duration',data)
        self.assertIn('uploaded',data)
        self.assertIsInstance(data['id'],int)
        self.assertIsInstance(data['name'],str)
        self.assertIsInstance(data['duration'],int)
        self.assertIsInstance(data['uploaded'],str)

    def test_get_podcast_details(self):
        _url = '/podcast/{}'.format(self.record)
        response = self.client.get(_url)
        self.assertEqual(response.status_code,200)
        data = response.get_json()
        self.assertIsInstance(data,dict)
        self.assertEqual(len(data),6)
        self.assertIn('id',data)
        self.assertIn('name',data)
        self.assertIn('duration',data)
        self.assertIn('uploaded',data)
        self.assertIn('host',data)
        self.assertIn('participants',data)
        self.assertIsInstance(data['id'],int)
        self.assertIsInstance(data['name'],str)
        self.assertIsInstance(data['duration'],int)
        self.assertIsInstance(data['uploaded'],str)        
        self.assertIsInstance(data['host'],str)
        self.assertIsInstance(data['participants'],list)

    def test_get_audiobook_details(self):
        _url = '/audiobook/{}'.format(self.record)
        response = self.client.get(_url)
        self.assertEqual(response.status_code,200)
        data = response.get_json()
        self.assertIsInstance(data,dict)
        self.assertEqual(len(data),6)
        self.assertIn('id',data)
        self.assertIn('title',data)
        self.assertIn('author',data)
        self.assertIn('narrator',data)
        self.assertIn('duration',data)
        self.assertIn('uploaded',data)
        self.assertIsInstance(data['id'],int)
        self.assertIsInstance(data['title'],str)
        self.assertIsInstance(data['author'],str)
        self.assertIsInstance(data['narrator'],str)
        self.assertIsInstance(data['duration'],int)
        self.assertIsInstance(data['uploaded'],str)


class UpdateAudioFile(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        from random import randint
        self.fmt = "%Y-%m-%d %H:%M:%S"
        self.record = randint(10,100)
        
        self.uploaded = (datetime.now()+timedelta(days=self.record)).strftime(self.fmt)
        self._song = {
            "song_id": self.record,
            "name": "Name-{}".format(self.record),
            "duration" : self.record,
            "uploaded": self.uploaded
        }
        self._podcast = {
            "podcast_id": self.record,
            "name": "Name-{}".format(self.record),
            "duration": self.record,
            "uploaded": self.uploaded,
            "host":"Host-{}".format(self.record),
            "participants": ["Participant-{}".format(i) for i in range(self.record%10)]
        }                
        self._audiobook = {
            "audiobook_id": self.record,
            "title": "Title-{}".format(self.record),
            "author": "Author-{}".format(self.record),
            "narrator": "Narrator-{}".format(self.record),
            "duration" : self.record,
            "uploaded": self.uploaded                
        }
        Song(**self._song).save()
        Podcast(**self._podcast).save()
        Audiobook(**self._audiobook).save()
        self.record_update = randint(1,10)
        self.uploaded_update = (datetime.now()+timedelta(days=self.record)).strftime(self.fmt)
        self.update_song = {
            "id": self.record_update,
            "name": "Update-Name-{}".format(self.record_update),
            "duration" : self.record_update,
            "uploaded": self.uploaded_update
        }
        self.update_podcast = {
            "id": self.record_update,
            "name": "Update-Name-{}".format(self.record_update),
            "duration": self.record_update,
            "uploaded": self.uploaded_update,
            "host":"Update-Host-{}".format(self.record_update),
            "participants": ["Update-Participant-{}".format(i) for i in range(self.record_update%10)]
        }                
        self.update_audiobook = {
            "id": self.record_update,
            "title": "Update-Title-{}".format(self.record_update),
            "author": "Update-Author-{}".format(self.record_update),
            "narrator": "Update-Narrator-{}".format(self.record_update),
            "duration" : self.record_update,
            "uploaded": self.uploaded_update
        }

    @classmethod
    def tearDownClass(self):
        for each_record in [self.record, self.record_update]:
            _song = Song.objects(song_id=each_record).first()
            _podcast = Podcast.objects(podcast_id=each_record).first()
            _audiobook = Audiobook.objects(audiobook_id=each_record).first()
            if _song:
                _song.delete()
            if _podcast:
                _podcast.delete()
            if _audiobook:
                _audiobook.delete()
            # End-If
        # End-For
        self.app_context.pop()

    def test_update_song_details(self):
        _url = '/song/{}'.format(self.record)
        response = self.client.put(_url, json=self.update_song,content_type='application/json')
        self.assertEqual(response.status_code,200)

    def test_update_podcast_details(self):
        _url = '/podcast/{}'.format(self.record)
        response = self.client.put(_url, json=self.update_podcast,content_type='application/json')
        self.assertEqual(response.status_code,200)

    def test_update_audiobook_details(self):
        _url = '/audiobook/{}'.format(self.record)
        response = self.client.put(_url, json=self.update_audiobook,content_type='application/json')
        self.assertEqual(response.status_code,200)


class DeleteAudioFile(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        from random import randint
        self.fmt = "%Y-%m-%d %H:%M:%S"
        self.record = randint(10,100)
        self.uploaded = (datetime.now()+timedelta(days=self.record)).strftime(self.fmt)
        self._song = {
            "song_id": self.record,
            "name": "Name-{}".format(self.record),
            "duration" : self.record,
            "uploaded": self.uploaded
        }
        self._podcast = {
            "podcast_id": self.record,
            "name": "Name-{}".format(self.record),
            "duration": self.record,
            "uploaded": self.uploaded,
            "host":"Host-{}".format(self.record),
            "participants": ["Participant-{}".format(i) for i in range(self.record%10)]
        }                
        self._audiobook = {
            "audiobook_id": self.record,
            "title": "Title-{}".format(self.record),
            "author": "Author-{}".format(self.record),
            "narrator": "Narrator-{}".format(self.record),
            "duration" : self.record,
            "uploaded": self.uploaded                
        }
        Song(**self._song).save()
        Podcast(**self._podcast).save()
        Audiobook(**self._audiobook).save()

    @classmethod
    def tearDownClass(self):
        self.app_context.pop()

    def test_delete_song(self):
        _url = '/song/{}'.format(self.record)
        response = self.client.delete(_url)
        self.assertEqual(response.status_code,200)

    def test_delete_podcast(self):
        _url = '/podcast/{}'.format(self.record)
        response = self.client.delete(_url)
        self.assertEqual(response.status_code,200)

    def test_delete_audiobook(self):
        _url = '/audiobook/{}'.format(self.record)
        response = self.client.delete(_url)
        self.assertEqual(response.status_code,200)


class ListAudioFiles(unittest.TestCase):
    records = 10
    
    @classmethod
    def setUpClass(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        # Create Songs Data
        for each_record in range(self.records):
            record = each_record+1
            uploaded = datetime.now()+timedelta(days=record)
            _song = {
                "song_id": record,
                "name": "Name-{}".format(record),
                "duration" : record,
                "uploaded": uploaded
            }
            _podcast = {
                "podcast_id": record,
                "name": "Name-{}".format(record),
                "duration": record,
                "uploaded": uploaded,
                "host":"Host-{}".format(record),
                "participants": ["Participant-{}".format(i) for i in range(record)]
            }                
            _audiobook = {
                "audiobook_id": record,
                "title": "Title-{}".format(record),
                "author": "Author-{}".format(record),
                "narrator": "Narrator-{}".format(record),
                "duration" : record,
                "uploaded": uploaded                
            }
            Song(**_song).save()
            Podcast(**_podcast).save()
            Audiobook(**_audiobook).save()
        # End-For

    @classmethod
    def tearDownClass(self):
        # Delete Songs Data
        for each_record in range(self.records):
            record = each_record+1
            Song.objects(song_id=record).first().delete()
            Podcast.objects(podcast_id=record).first().delete()
            Audiobook.objects(audiobook_id=record).first().delete()
        # End-For
        self.app_context.pop()

    def test_list_all_songs(self):
        response = self.client.get('/song')
        self.assertEqual(response.status_code,200)
        data = response.get_json()
        self.assertIsInstance(data,list)
        self.assertEqual(len(data),10)
        first_record = data[0]
        self.assertIsInstance(first_record,dict)
        self.assertEqual(len(first_record),4)
        self.assertIn('id',first_record)
        self.assertIn('name',first_record)
        self.assertIn('duration',first_record)
        self.assertIn('uploaded',first_record)
        self.assertIsInstance(first_record['id'],int)
        self.assertIsInstance(first_record['name'],str)
        self.assertIsInstance(first_record['duration'],int)
        self.assertIsInstance(first_record['uploaded'],str)

    def test_list_all_podcasts(self):
        response = self.client.get('/podcast')
        self.assertEqual(response.status_code,200)
        data = response.get_json()
        self.assertIsInstance(data,list)
        self.assertEqual(len(data),10)
        first_record = data[0]
        self.assertIsInstance(first_record,dict)
        self.assertEqual(len(first_record),6)
        self.assertIn('id',first_record)
        self.assertIn('name',first_record)
        self.assertIn('duration',first_record)
        self.assertIn('uploaded',first_record)
        self.assertIn('host',first_record)
        self.assertIn('participants',first_record)
        self.assertIsInstance(first_record['id'],int)
        self.assertIsInstance(first_record['name'],str)
        self.assertIsInstance(first_record['duration'],int)
        self.assertIsInstance(first_record['uploaded'],str)
        self.assertIsInstance(first_record['host'],str)
        self.assertIsInstance(first_record['participants'],list)

    def test_list_all_audiobooks(self):
        response = self.client.get('/audiobook')
        self.assertEqual(response.status_code,200)
        data = response.get_json()
        self.assertIsInstance(data,list)
        self.assertEqual(len(data),10)
        first_record = data[0]
        self.assertIsInstance(first_record,dict)
        self.assertEqual(len(first_record),6)
        self.assertIn('id',first_record)
        self.assertIn('title',first_record)
        self.assertIn('author',first_record)
        self.assertIn('narrator',first_record)
        self.assertIn('duration',first_record)
        self.assertIn('uploaded',first_record)
        self.assertIsInstance(first_record['id'],int)
        self.assertIsInstance(first_record['title'],str)
        self.assertIsInstance(first_record['author'],str)
        self.assertIsInstance(first_record['narrator'],str)
        self.assertIsInstance(first_record['duration'],int)
        self.assertIsInstance(first_record['uploaded'],str)


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
    
    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)
    
    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])


if __name__ == "__main__":
    unittest.main()
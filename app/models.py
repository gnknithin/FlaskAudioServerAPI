from . import mongodb

class Song(mongodb.Document):
    song_id = mongodb.IntField(required=True,min_value=1,unique=True)
    name = mongodb.StringField(required=True,max_length=100)
    duration = mongodb.IntField(required=True,min_value=1)
    uploaded = mongodb.DateTimeField(required=True)

    meta = {'collection': 'song'}

    def to_json(self):
        return {
            'id':self.song_id,
            'name':self.name,
            'duration':self.duration,
            'uploaded':self.uploaded
        }

class Podcast(mongodb.Document):
    podcast_id = mongodb.IntField(required=True,min_value=1,unique=True)
    name = mongodb.StringField(required=True,max_length=100)
    duration = mongodb.IntField(required=True,min_value=1)
    uploaded = mongodb.DateTimeField(required=True)
    host = mongodb.StringField(required=True,max_length=100)
    participants = mongodb.ListField(max_length=10)

    meta = {'collection': 'podcast'}

    def to_json(self):
        return {
            'id':self.podcast_id,
            'name':self.name,
            'duration':self.duration,
            'uploaded':self.uploaded,
            'host':self.host,
            'participants':self.participants
        }


class Audiobook(mongodb.Document):
    audiobook_id = mongodb.IntField(required=True,min_value=1,unique=True)
    title = mongodb.StringField(required=True,max_length=100)
    author = mongodb.StringField(required=True,max_length=100)
    narrator = mongodb.StringField(required=True,max_length=100)
    duration = mongodb.IntField(required=True,min_value=1)
    uploaded = mongodb.DateTimeField(required=True)

    meta = {'collection':'audiobook'}

    def to_json(self):
        return {
            'id':self.audiobook_id,
            'title':self.title,
            'author':self.author,
            'narrator':self.narrator,
            'duration':self.duration,
            'uploaded':self.uploaded
        }
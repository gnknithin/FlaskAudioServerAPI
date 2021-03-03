import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
from . import api
from flask import abort, request, jsonify
from ..models import Song, Podcast, Audiobook
from ..forms import SongForm, PodcastForm, AudiobookForm
from pymongo.errors import ServerSelectionTimeoutError
audioFileTypes = ['song','podcast','audiobook']

@api.route('/<audioFileType>',methods=['GET','POST'])
def AudioFiles(audioFileType):
    audioFileType = audioFileType.lower()
    if audioFileType not in audioFileTypes:
        abort(400)# Raise Bad Request
    # End-If
    if request.method == 'GET':
        cursor = None
        if audioFileType == 'song':
            try:
                cursor = Song.objects().all()
            except ServerSelectionTimeoutError:
                abort(500) # Internal Server Error
            # End-Try-Exception
        elif audioFileType == 'podcast':
            try:
                cursor = Podcast.objects().all()
            except ServerSelectionTimeoutError:
                abort(500) # Internal Server Error
            # End-Try-Exception
        elif audioFileType == 'audiobook':
            try:
                cursor = Audiobook.objects().all()
            except ServerSelectionTimeoutError:
                abort(500) # Internal Server Error
            # End-Try-Exception
        else:
            abort(500) # Internal Server Error
        # End-If-Elif-Else
        if cursor is not None:
            data = []
            for each_record in cursor:
                data.append(each_record.to_json())
            # End-For
            return jsonify(data) # Return
        else:
            abort(500) # Internal Server Error
        # End-If-Else
    elif request.method == 'POST':
        if request.content_type == 'application/json':
            if audioFileType == 'song':
                _form = SongForm.from_json(request.json)
                if _form.validate():
                    _song = Song()
                    _song.song_id = _form.data['id']
                    _song.name = _form.data['name']
                    _song.duration = _form.data['duration']
                    _song.uploaded = _form.data['uploaded']
                    try:
                        _song.save() # Save
                    except Exception:
                        abort(500) # Internal Server Error
                    # End-Try-Exception 
                    return ('Ok',200) # Return
                else:
                    abort(400) # Raise Bad Request
                # End-If-Else
            elif audioFileType == 'podcast':
                _form = PodcastForm.from_json(request.json)
                if _form.validate():
                    _podcast = Podcast()
                    _podcast.podcast_id = _form.data['id']
                    _podcast.name = _form.data['name']
                    _podcast.duration = _form.data['duration']
                    _podcast.uploaded = _form.data['uploaded']
                    _podcast.host = _form.data['host']
                    _podcast.participants = _form.data['participants']
                    try:
                        _podcast.save() # Save
                    except Exception:
                        abort(500) # Internal Server Error
                    # End-Try-Exception 
                    return ('Ok',200) # Return
                else:
                    abort(400) # Raise Bad Request
                # End-If-Else
            elif audioFileType == 'audiobook':
                _form = AudiobookForm.from_json(request.json)
                if _form.validate():
                    _audiobook = Audiobook()
                    _audiobook.audiobook_id = _form.data['id']
                    _audiobook.title = _form.data['title']
                    _audiobook.author = _form.data['author']
                    _audiobook.narrator = _form.data['narrator']
                    _audiobook.duration = _form.data['duration']
                    _audiobook.uploaded = _form.data['uploaded']
                    try:
                        _audiobook.save() # Save
                    except Exception:
                        abort(500) # Internal Server Error
                    # End-Try-Exception
                    return ('Ok',200) # Return
                else:
                    abort(400) # Raise Bad Request
                # End-If-Else
            else:
                abort(500) # Raise Bad Request
            # End-If-Elif-Else
        else:
            abort(400) # Raise Bad Request
        # End-If-Else
    else:
        print("This Stop-Method")
        abort(400) # Raise Bad Request
    # End-If-Elif-Else
    abort(500) # Raise Internal Server Error

@api.route('/<audioFileType>/<audioFileID>',methods=['GET','PUT','DELETE'])
def SpecificAaudioFile(audioFileType,audioFileID):
    audioFileType = audioFileType.lower()
    if audioFileType not in audioFileTypes:
        abort(400)# Raise Bad Request
    # End-If
    try:
        audioFileID = int(audioFileID)
    except Exception:
        abort(400)# Raise Bad Request
    # End-Try-Exception
    if request.method == 'GET':
        obj = None
        if audioFileType == 'song':
            try:
                obj = Song.objects(song_id=audioFileID).first()
            except ServerSelectionTimeoutError:
                abort(500) # Internal Server Error
            # End-Try-Exception
        elif audioFileType == 'podcast':
            try:
                obj = Podcast.objects(podcast_id=audioFileID).first()
            except ServerSelectionTimeoutError:
                abort(500) # Internal Server Error
            # End-Try-Exception
        elif audioFileType == 'audiobook':
            try:
                obj = Audiobook.objects(audiobook_id=audioFileID).first()
            except ServerSelectionTimeoutError:
                abort(500) # Internal Server Error
            # End-Try-Exception
        else:
            abort(500) # Raise Bad Request
        # End-If-Elif-Else
        if obj is not None:
            return jsonify(obj.to_json())
        else:
            abort(400) # Raise Bad Request
        # End-If-Else
    elif request.method == 'PUT':
        if request.content_type == 'application/json':
            if audioFileType == 'song':
                _form = SongForm.from_json(request.json)
                if _form.validate():
                    _song = Song.objects(song_id=audioFileID).first()
                    _song.song_id = _form.data['id']
                    _song.name = _form.data['name']
                    _song.duration = _form.data['duration']
                    _song.uploaded = _form.data['uploaded']
                    try:
                        _song.save() # Save
                    except Exception:
                        abort(500) # Internal Server Error
                    # End-Try-Exception 
                    return ('Ok',200) # Return
                else:
                    abort(400) # Raise Bad Request
                # End-If-Else
            elif audioFileType == 'podcast':
                _form = PodcastForm.from_json(request.json)
                if _form.validate():
                    _podcast = Podcast.objects(podcast_id=audioFileID).first()
                    _podcast.podcast_id = _form.data['id']
                    _podcast.name = _form.data['name']
                    _podcast.duration = _form.data['duration']
                    _podcast.uploaded = _form.data['uploaded']
                    _podcast.host = _form.data['host']
                    _podcast.participants = _form.data['participants']
                    try:
                        _podcast.save() # Save
                    except Exception:
                        abort(500) # Internal Server Error
                    # End-Try-Exception 
                    return ('Ok',200) # Return
                else:
                    abort(400) # Raise Bad Request
                # End-If-Else
            elif audioFileType == 'audiobook':
                _form = AudiobookForm.from_json(request.json)
                if _form.validate():
                    _audiobook = Audiobook.objects(audiobook_id=audioFileID).first()
                    _audiobook.audiobook_id = _form.data['id']
                    _audiobook.title = _form.data['title']
                    _audiobook.author = _form.data['author']
                    _audiobook.narrator = _form.data['narrator']
                    _audiobook.duration = _form.data['duration']
                    _audiobook.uploaded = _form.data['uploaded']
                    try:
                        _audiobook.save() # Save
                    except Exception:
                        abort(500) # Internal Server Error
                    # End-Try-Exception
                    return ('Ok',200) # Return
                else:
                    abort(400) # Raise Bad Request
                # End-If-Else
            else:
                abort(500) # Raise Bad Request
            # End-If-Elif-Else
        else:
            abort(400) # Raise Bad Request
        # End-If-Else
    elif request.method == 'DELETE':
        obj = None
        if audioFileType == 'song':
            try:
                obj = Song.objects(song_id=audioFileID).first()
            except ServerSelectionTimeoutError:
                abort(500) # Internal Server Error
            # End-Try-Exception
        elif audioFileType == 'podcast':
            try:
                obj = Podcast.objects(podcast_id=audioFileID).first()
            except ServerSelectionTimeoutError:
                abort(500) # Internal Server Error
            # End-Try-Exception
        elif audioFileType == 'audiobook':
            try:
                obj = Audiobook.objects(audiobook_id=audioFileID).first()
            except ServerSelectionTimeoutError:
                abort(500) # Internal Server Error
            # End-Try-Exception
        else:
            abort(500) # Raise Bad Request
        # End-If-Elif-Else
        if obj is not None:
            obj.delete() # Delete
            return ('Ok',200) # Return
        else:
            abort(400) # Raise Bad Request
        # End-If-Else
    else:
        abort(400) # Raise Bad Request
    # End-If-Elif-Else
    abort(500) # Raise Internal Server Error

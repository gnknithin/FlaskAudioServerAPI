try:
    import json
    from datetime import datetime
    from flask_wtf import FlaskForm
    from wtforms import IntegerField,StringField, DateTimeField, Field
    from wtforms.validators import ValidationError, InputRequired,DataRequired
except ModuleNotFoundError:
    print("\nFlask-WTF must be Installed\n")
    sys.exit(0)

class ListField(Field):
    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist
        else:
            self.data = []

    def pre_validate(self, form):
        super().pre_validate(form)
        if self.data:
            try:
                json.dumps(self.data)
            except TypeError:
                raise ValueError('This field contains invalid JSON')

class SongForm(FlaskForm):
    id = IntegerField(validators=[InputRequired()])
    name = StringField(validators=[InputRequired()])
    duration = IntegerField(validators=[InputRequired()])
    uploaded = DateTimeField(validators=[InputRequired()])

    class Meta:
        csrf = False
    
    def validate_id(form,field):
        if not isinstance(field.data,int):
            raise ValidationError
        # End-If
        if field.data < 0:
            raise ValidationError
        # End-If
    
    def validate_name(form,field):
        try:
            field.data = int(field.data)
            raise ValidationError
        except Exception:
            pass
        if not isinstance(field.data,str):
            raise ValidationError
        if len(field.data) > 100:
            raise ValidationError
        # End-If
    
    def validate_duration(form,field):
        if not isinstance(field.data,int):
            raise ValidationError
        # End-If
        if field.data < 0:
            raise ValidationError
        # End-If

    def validate_uploaded(form,field):
        if not isinstance(field.data,datetime):
            raise ValidationError
        # End-If
        _today = datetime.now()
        if _today > field.data:
            raise ValidationError
        # End-If

class PodcastForm(FlaskForm):
    id = IntegerField(validators=[InputRequired()])
    name = StringField(validators=[InputRequired()])
    duration = IntegerField(validators=[InputRequired()])
    uploaded = DateTimeField(validators=[InputRequired()])
    host = StringField(validators=[InputRequired()])
    participants = ListField()

    class Meta:
        csrf = False
    
    def validate_id(form,field):
        if not isinstance(field.data,int):
            raise ValidationError
        # End-If        
        if field.data < 0:
            raise ValidationError
        # End-If
    
    def validate_name(form,field):
        try:
            field.data = int(field.data)
            raise ValidationError
        except Exception:
            pass
        if not isinstance(field.data,str):
            raise ValidationError
        # End-If
        if len(field.data) > 100:
            raise ValidationError
        # End-If
    
    def validate_duration(form,field):
        if not isinstance(field.data,int):
            raise ValidationError
        # End-If
        if field.data < 0:
            raise ValidationError
        # End-If

    def validate_uploaded(form,field):
        if not isinstance(field.data,datetime):
            raise ValidationError
        # End-If
        _today = datetime.now()
        if _today > field.data:
            raise ValidationError
        # End-If

    def validate_host(form,field):
        try:
            field.data = int(field.data)
            raise ValidationError
        except Exception:
            pass        
        if not isinstance(field.data,str):
            raise ValidationError
        # End-If
        if len(field.data) > 100:
            raise ValidationError
        # End-If
    
    def validate_participants(form, field):
        if not isinstance(field.data,list):
            raise ValidationError
        # End-If
        if field.data is not None:
            for each_participant in field.data:
                if isinstance(each_participant,str):
                    if len(each_participant) > 100:
                        raise ValidationError
                    # End-If
                else:
                    raise ValidationError('Value must be String')
                # End-If-Else
            # End-For
        else:
            field.data= []
        # End-If-Else

class AudiobookForm(FlaskForm):
    id = IntegerField(validators=[InputRequired()])
    title = StringField(validators=[InputRequired()])
    author = StringField(validators=[InputRequired()])
    narrator = StringField(validators=[InputRequired()])
    duration = IntegerField(validators=[InputRequired()])
    uploaded = DateTimeField(validators=[InputRequired()])

    class Meta:
        csrf = False
    
    def validate_id(form,field):
        if not isinstance(field.data,int):
            raise ValidationError
        # End-If
        if field.data < 0:
            raise ValidationError
        # End-If

    def validate_title(form,field):
        try:
            field.data = int(field.data)
            raise ValidationError
        except Exception:
            pass
        if not isinstance(field.data,str):
            raise ValidationError
        # End-If
        if len(field.data) > 100:
            raise ValidationError
        # End-If

    def validate_author(form,field):
        try:
            field.data = int(field.data)
            raise ValidationError
        except Exception:
            pass        
        if not isinstance(field.data,str):
            raise ValidationError
        # End-If
        if len(field.data) > 100:
            raise ValidationError
        # End-If

    def validate_narrator(form,field):
        try:
            field.data = int(field.data)
            raise ValidationError
        except Exception:
            pass
        if not isinstance(field.data,str):
            raise ValidationError
        # End-If
        if len(field.data) > 100:
            raise ValidationError
        # End-If

    def validate_duration(form,field):
        if not isinstance(field.data,int):
            raise ValidationError
        # End-If
        if field.data < 0:
            raise ValidationError
        # End-If

    def validate_uploaded(form,field):
        if not isinstance(field.data,datetime):
            raise ValidationError
        # End-If
        _today = datetime.now()
        if _today > field.data:
            raise ValidationError
        # End-If

    
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, IMAGES

images = UploadSet('images', IMAGES)

class UploadForm(FlaskForm):
    upload = FileField('image', validators=[FileRequired(),FileAllowed(images, 'Images only!')])
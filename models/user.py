from mongoengine import Document,StringField,EmailField
class User(Document):
    username = StringField()
    password = StringField()

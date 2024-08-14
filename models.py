from tortoise.models import Model
from tortoise import fields

statuses = ['pupil', 'student', 'teacher']
viloyatlar = ["Navoi","Buxoro","Farg'ona","Jizzax","Qashqadaryo","Andijon","Namangan","Samarqand", "Sirdaryo","Surxondaryo","Toshkent","Xorazm", "Nukus"]


class User(Model):
    fio = fields.CharField(max_length=255)
    username = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    status = fields.CharField(max_length=255, choices=[(i, i) for i in statuses])
    viloyat = fields.CharField(max_length=255, choices=[(i, i) for i in viloyatlar])
    password = fields.CharField(max_length=255) 
    email_verified = fields.BooleanField(default=False)
    def __str__(self):
        return self.username
    
class AuthToken(Model):
    token = fields.CharField(max_length=255, unique=True) # generatsiya, 26^100 randomda, va yana bitta 26^100 randomda [1,2,3,4,5]
    user = fields.ForeignKeyField(
        "models.User", 
        on_delete=fields.CASCADE,
    )

    class Meta:
        table = "auth_tokens"

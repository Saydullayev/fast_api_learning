from pydantic import BaseModel, EmailStr

class UserRegistration(BaseModel):
    fio: str
    username: str
    email: EmailStr
    viloyat: str
    password: str

    @classmethod
    def validate_viloyat(cls, viloyat: str):
        viloyat = ("Navoi","Buxoro","Farg'ona","Jizzax","Qashqadaryo","Andijon","Namangan","Samarqand", "Sirdaryo","Surxondaryo","Toshkent","Xorazm", "Nukus")
        if viloyat not in viloyat:
            raise ValueError(f"Invalid viloyat. Must be one of {viloyat}")
        return viloyat
from passlib.context import CryptContext

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

class UserService:

    def __init__(self, repository: UserRepository):

        self.repository = repository


    def create(self, data: UserCreate):

        user = self.repository.get_by_email(data.email)

        if user:

            raise Exception("El correo ya existe.")


        new_user = User(

            nombres=data.nombres,

            apellidos=data.apellidos,

            email=data.email,

            password=pwd_context.hash(data.password)

        )

        return self.repository.create(new_user)


    def get_all(self):

        return self.repository.get_all()

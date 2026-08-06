from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.schemas.user import UserResponse
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Usuarios"]
)

@router.post(
    "",
    response_model=UserResponse
)
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        repository = UserRepository(db)
        service = UserService(repository)
        return service.create(data)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "",
    response_model=list[UserResponse]
)

def get_users(

    db: Session = Depends(get_db)

):
    repository = UserRepository(db)
    service = UserService(repository)
    return service.get_all()

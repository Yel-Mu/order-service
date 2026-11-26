from fastapi import APIRouter, Depends
from schemas import UserCreate, UserRead
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session

router = APIRouter(prefix="/services", tags=["services"])


@router.post("/create", response_model=UserRead)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    raise NotImplementedError("Order creation is not implemented yet")


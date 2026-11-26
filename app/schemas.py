from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    product: str
    quantity: str


class UserRead(BaseModel):
    config = model_config = ConfigDict(from_attributes=True)

    id: int
    product: str
    quantity: str
    status: str
    created_at: str

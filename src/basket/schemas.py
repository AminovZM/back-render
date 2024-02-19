from pydantic import BaseModel


class BasketCreate(BaseModel):
    id: int
    quantity: int
    id_user: int
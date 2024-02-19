from pydantic import BaseModel


class ProductCreate(BaseModel):
    id: int
    name: str
    category: str
    price: int
    remainder: str

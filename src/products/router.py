from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from products.models import product
from products.schemas import ProductCreate


router = APIRouter(
    prefix="/products",
    tags=["Product"]
)

@router.get("/")
async def get_specific_products_by_category(product_category: str, session: AsyncSession = Depends(get_async_session)):
    query = select(product).where(product.c.category == product_category)
    result = await session.execute(query)

    # Преобразуем каждую строку в словарь с использованием метода ._asdict()
    rows_as_dicts = [row._asdict() for row in result.all()]

    return rows_as_dicts


@router.get("/id")
async def get_specific_products_by_id(product_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(product).where(product.c.id == product_id)
    result = await session.execute(query)

    # Преобразуем каждую строку в словарь с использованием метода ._asdict()
    rows_as_dicts = [row._asdict() for row in result.all()]

    return rows_as_dicts


@router.post("/")
async def add_specific_products(new_product: ProductCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(product).values(**new_product.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.get("/name")
async def get_serch_products_by_name(product_name: str, session: AsyncSession = Depends(get_async_session)):
    query = select(product).where(product.c.name.ilike(f"%{product_name}%"))
    result = await session.execute(query)

    # Преобразуем каждую строку в словарь с использованием метода ._asdict()
    rows_as_dicts = [row._asdict() for row in result.all()]

    return rows_as_dicts

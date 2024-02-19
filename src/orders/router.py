from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from orders.models import order
from orders.schemas import OrderCreate


router = APIRouter(
    prefix="/orders",
    tags=["Order"]
)


@router.get("/")
async def get_orders_by_id(id_user: int, session: AsyncSession = Depends(get_async_session)):
    query = select(order).where(order.c.id_user == id_user)
    result = await session.execute(query)

    # Преобразуем каждую строку в словарь с использованием метода ._asdict()
    rows_as_dicts = [row._asdict() for row in result.all()]

    return rows_as_dicts


@router.post("/")
async def add_orders(new_order: OrderCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(order).values(**new_order.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
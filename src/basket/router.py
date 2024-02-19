from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from basket.models import basket
from basket.schemas import BasketCreate


router = APIRouter(
    prefix="/baskets",
    tags=["Basket"]
)

@router.get("/")
async def get_all_products(id_user: int, session: AsyncSession = Depends(get_async_session)):
    query = select(basket).where(basket.c.id_user == id_user)
    result = await session.execute(query)

    # Преобразуем каждую строку в словарь с использованием метода ._asdict()
    rows_as_dicts = [row._asdict() for row in result.all()]

    return rows_as_dicts


@router.post("/")
async def add_specific_products(new_basket: BasketCreate, session: AsyncSession = Depends(get_async_session)):
    async with session.begin():
        # Проверяем, существует ли товар с указанным id в базе данных
        stmt = select(basket).where((basket.c.id == new_basket.id) & (basket.c.id_user == new_basket.id_user))
        result = await session.execute(stmt)
        existing_product = result.scalar_one_or_none()

        if existing_product:
            # Если товар существует, обновляем его количество
            stmt = basket.update().where((basket.c.id == new_basket.id) & (basket.c.id_user == new_basket.id_user)).values(quantity=basket.c.quantity + new_basket.quantity)
            await session.execute(stmt)
        else:
            # Если товар не существует, добавляем его
            stmt = insert(basket).values(**new_basket.dict())
            await session.execute(stmt)

    return {"status": "success"}

@router.delete("/")
async def delete_all_products(id_user: int, session: AsyncSession = Depends(get_async_session)):
    query = delete(basket).where(basket.c.id_user == id_user)
    result = await session.execute(query)
    await session.commit()
    return {"message": f"All products for user with id {id_user} deleted successfully"}


@router.delete("/{id_user}/{id_product}")
async def delete_product(id_user: int, id_product: int, session: AsyncSession = Depends(get_async_session)):
    async with session.begin():
        # Проверяем существование товара
        stmt = select(basket).where(basket.c.id_user == id_user, basket.c.id == id_product)
        result = await session.execute(stmt)
        product = result.scalar_one_or_none()
        if product is None:
            raise HTTPException(status_code=404,
                                detail=f"Product with id {id_product} for user with id {id_user} not found")

        # Удаляем товар
        stmt = delete(basket).where(basket.c.id_user == id_user, basket.c.id == id_product)
        await session.execute(stmt)
        await session.commit()

        return {"message": f"Product with id {id_product} for user with id {id_user} deleted successfully"}




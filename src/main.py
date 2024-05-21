from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate, UserUpdate


from products.router import router as router_product
from basket.router import router as router_basket
from orders.router import router as router_order

app = FastAPI(
    title="Online store"
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["Users"],
)

app.include_router(router_product)

app.include_router(router_basket)

app.include_router(router_order)


#router_current_user = APIRouter(
#    prefix="/current_user",
#    tags=["Users"]
#)

#current_user = fastapi_users.current_user()
#@router_current_user.post("/")
#def protected_route(user: User = Depends(current_user)):
#    return {"username": user.username}
#app.include_router(router_current_user)


origins = [
    "https://front-end-l0jy.onrender.com",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization", "Accept", "Accept-Language", "Connection", "Content-Type", "Origin", "Referer"
                   "Sec-Fetch-Dest", "Sec-Fetch-Mode", "Sec-Fetch-Site", "User-Agent", "sec-ch-ua",
                   "sec-ch-ua-mobile", "sec-ch-ua-platform", "access-control-allow-credentials"],
)
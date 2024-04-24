import uvicorn
from fastapi import FastAPI
from routers.product import product_router
from routers.categories import categories_router
from routers.orders import orders_router

app = FastAPI()
app.include_router(product_router)
app.include_router(categories_router)
app.include_router(orders_router)

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000)

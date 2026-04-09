from pydantic import BaseModel


class ProductQuantity(BaseModel):
    product_id: int
    quantity: int


class CreateOrder(BaseModel):
    client_id: int
    products: list[ProductQuantity]


class AddProduct(BaseModel):
    order_id: int
    product_id: int
    quantity: int

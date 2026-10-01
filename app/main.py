import typing as t

import pydantic

restaurants = [
    {
        "restaurant_id": 1,
        "name": "Spice House",
        "cuisine": "Indian",
        "ratings": 4.7,
        "address":{
            "street":"Sector 135",
            "city": "Noida",
            "pincode": 412345
        }
    },
    {
        "restaurant_id": 2,
        "name": "Ching China",
        "cuisine": "Chinese",
        "ratings": 4.0,
        "address":{
            "street":"HauzKhas",
            "city": "Delhi",
            "pincode": 202122
                }
    },
    {
        "restaurant_id": 3,
        "name": "Pasta La Vista",
        "cuisine": "Italian",
        "ratings": 4.9,
        "address":{
                    "street":"Sector 21",
                    "city": "Gurgaon",
                    "pincode": 404001
                }
    },
]

class Address(pydantic.BaseModel):
    street: str
    city: str
    pincode: int

class Restaurant(pydantic.BaseModel):
    restaurant_id: int
    name: str
    cuisine: str
    ratings: t.Annotated[float,pydantic.Field(ge=1, le=5)]
    address: Address

class RestaurantCreate(pydantic.BaseModel):
    name: str
    cuisine: str
    ratings: t.Annotated[float,pydantic.Field(ge=1, le=5)]
    address: Address

restaurant_list = [
    Restaurant.model_validate(data)
    for data in restaurants
]

for restaurant in restaurant_list:
    data = restaurant.model_dump()
    print(type(data))
    print(data)
    json_data = restaurant.model_dump_json(indent=4)
    print(type(json_data))
    print(json_data)
# app = fastapi.FastAPI()

# @app.get("/restaurants", response_model=list[Restaurant]) 
# def restaurants_list(
#     Address: str | None = None,
#     cuisine: str | None = None,
#     min_rating: t.Annotated[float | None, fastapi.Query(ge=1, le=5)] = None,
#     limit: t.Annotated[int, fastapi.Query(ge=1, le=50)] = 10
# ):
#     result = restaurants.copy()
#     if Address is not None:
#         result=[
#             restaurant
#             for restaurant in result
#             if restaurant["address"] == Address
#         ]
#     if cuisine is not None:
#         result=[
#             restaurant
#             for restaurant in result
#             if restaurant["cuisine"] == cuisine
#         ]
#     if min_rating is not None:
#         result = [
#             restaurant
#             for restaurant in result
#             if restaurant["ratings"] >= min_rating
#         ]
#     result = result[:limit]
#     return result


# @app.get("/restaurants/{restaurant_id}", response_model=Restaurant)
# def restaurant_detail(
#     restaurant_id: t.Annotated[int, fastapi.Path(ge=1)],
# ):
#     for restaurant in restaurants:
#         if restaurant["restaurant_id"] == restaurant_id:
#             return restaurant

#     raise fastapi.HTTPException(
#         status_code=404,
#         detail="Restaurant not found",
#     )

# @app.post("/restaurants", response_model=Restaurant, status_code=201)
# def create_restaurant(data: RestaurantCreate):
#     new_id = max(
#         restaurant["restaurant_id"]
#         for restaurant in restaurants
#     ) +1
#     new_resaturant = {
#         "restaurant_id": new_id,
#         **data.model_dump(),
#     }
#     restaurants.append(new_resaturant)
#     return new_resaturant

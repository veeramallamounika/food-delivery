from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Food Delivery API is running"}


@app.get("/foods")
def get_foods():
    return [
        {
            "id": 1,
            "name": "Pizza",
            "price": 250
        },
        {
            "id": 2,
            "name": "Burger",
            "price": 150
        },
        {
            "id": 3,
            "name": "Biryani",
            "price": 200
        },
        {
            "id": 4,
            "name": "French Fries",
            "price": 100
        }
    ]
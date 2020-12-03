
## Steps to run the project

Create and active virtual environment using

```
python -m venv env
cd env
scripts\activate
```

Change the directory using

```
cd ..
cd pizzaAPI
```

Now you need to install python packages to run the app

```
pip install -r requirements.txt
```

Change postgreSQL database credentials in pizzaAPI/settings.py file

Run commands for migration and migrate

```
python manage.py makemigrations
python manage.py migrate
```

Create superuser

```
python manage.py createsuper
```

Run Django app

```
python manage.py runserver
```


# Endpoints are

## Creating pizza

```
POST http://127.0.0.1:8000/
```

```
{
    "pizza_type": "Regular",
    "pizza_size_category": null,
    "pizza_topping_category": null
}
```

## Get list of pizza

```
GET http://127.0.0.1:8000/pizza/list
```

```
{
        "id": 1,
        "pizza_type": "Regular",
        "pizza_size_category": {
            "id": 1,
            "pizza_size": "Small"
        },
        "pizza_topping_category": {
            "id": 1,
            "pizza_topping": "Onion"
        }
    },
```

## Update an pizza

```
PUT http://127.0.0.1:8000/pizza/update/1
```

```
{
    "pizza_type": "Regular",
    "pizza_size_category": null,
    "pizza_topping_category": null
}
```

## Remove an pizza

```
DELETE http://127.0.0.1:8000/api/v1/orders/1/
```
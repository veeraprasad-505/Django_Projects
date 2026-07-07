# Product Inventory Management System (Django + DRF)

A REST API-based Product Inventory Management System built with Django, Django REST
Framework, Models, Serializers (ModelSerializer), and function-based views, using
SQLite by default.

## Project Structure
```
ProductInventory/
├── manage.py
├── ProductInventory/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── product/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── migrations/
```

## Setup Instructions

1. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install django djangorestframework
   ```

3. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the development server:
   ```
   python manage.py runserver
   ```

5. The API will be available at `http://127.0.0.1:8000/`

## Product Model

| Field        | Type                        |
|--------------|------------------------------|
| product_name | CharField (max_length=100)  |
| category     | CharField (max_length=100)  |
| brand        | CharField (max_length=100)  |
| price        | FloatField                  |
| quantity     | IntegerField                |
| supplier     | CharField (max_length=100)  |

## API Endpoints

| Method | Endpoint                     | Description             |
|--------|--------------------------------|--------------------------|
| POST   | `/products/add/`               | Add a new product       |
| GET    | `/products/`                   | Retrieve all products   |
| PUT    | `/products/update/<id>/`       | Update product details  |
| DELETE | `/products/delete/<id>/`       | Delete a product        |

## Testing with Postman

### 1. Add Product — POST `/products/add/`
```json
{
    "product_name": "Wireless Mouse",
    "category": "Electronics",
    "brand": "Logitech",
    "price": 899,
    "quantity": 50,
    "supplier": "ABC Distributors"
}
```
Response:
```json
{
    "message": "Product Added Successfully",
    "product": {
        "id": 1,
        "product_name": "Wireless Mouse",
        "category": "Electronics",
        "brand": "Logitech",
        "price": 899,
        "quantity": 50,
        "supplier": "ABC Distributors"
    }
}
```

### 2. Get All Products — GET `/products/`
Returns a JSON array of all product records.

### 3. Update Product — PUT `/products/update/1/`
```json
{
    "product_name": "Wireless Mouse",
    "category": "Electronics",
    "brand": "Logitech",
    "price": 999,
    "quantity": 45,
    "supplier": "ABC Distributors"
}
```
Response:
```json
{
    "message": "Product Updated Successfully",
    "product": { ... }
}
```

### 4. Delete Product — DELETE `/products/delete/1/`
Response:
```json
{
    "message": "Product Deleted Successfully"
}
```

## Sample Testing Data

| Product Name        | Category    | Brand    | Price | Quantity | Supplier         |
|----------------------|-------------|----------|-------|----------|-------------------|
| Wireless Mouse       | Electronics | Logitech | 899   | 50       | ABC Distributors  |
| Mechanical Keyboard  | Electronics | Redragon | 2499  | 20       | XYZ Suppliers     |
| USB-C Charger        | Accessories | Samsung  | 1499  | 35       | Tech World        |
| Gaming Headset       | Electronics | HyperX   | 3999  | 15       | Gaming Store      |
| External Hard Disk   | Storage     | Seagate  | 5499  | 10       | Digital Hub       |

## Notes
- All endpoints have been tested end-to-end (add, list, update, delete) and
  confirmed to return the exact response shapes described in the project spec.
- The Product model is also registered in Django Admin (`/admin/`) for easy
  inspection (create a superuser with `python manage.py createsuperuser`).

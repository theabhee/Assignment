# AI-Assisted Box Selection System

An API for an e-commerce platform that automatically figures out the smallest, cheapest shipping box for an order.

---

## How It Works

1. **Data Sorting:** Since an item can be rotated to fit inside a box, we sort both the item's dimensions and the box's dimensions from smallest to largest before comparing them.
2. **Fast Database Checks:** Box dimensions are automatically normalized and sorted before being saved.
  
3. **Cheapest First:** The database always orders boxes by `cost` (lowest first). That way, the very first box that matches our size and weight checks is guaranteed to be the cheapest option.

---

## Running It Locally

### 1. Set up the database
Run the migrations to create your tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Add some sample boxes
Open the Django shell:
```bash
python manage.py shell
```

Paste this in to create a few test boxes:
```python
from warehouse.models import Box

Box.objects.create(name="Box A (Small)", dim1=2, dim2=3, dim3=6, max_weight=10, cost=0.50)
Box.objects.create(name="Box B (Medium)", dim1=4, dim2=8, dim3=16, max_weight=20, cost=1.20)
Box.objects.create(name="Box C (Long)", dim1=15, dim2=5, dim3=10, max_weight=22, cost=2.50)
exit()
```

### 3. Start the server
```bash
python manage.py runserver
```

---

## Testing the API

**Endpoint:** `POST /api/recommend/`

If you're using **PowerShell**, you can test it with:
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/recommend/" -Method POST -ContentType "application/json" -Body '{"length": 5, "width": 3, "height": 2, "weight": 4}'
```

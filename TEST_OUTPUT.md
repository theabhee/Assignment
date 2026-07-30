# Output

## Test Case 1: Box Fits Successfully

**Request**

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/recommend/" `
-Method Post `
-ContentType "application/json" `
-Body '{"length": 4, "width": 9, "height": 14, "weight": 10}'
```

**Response**

```text
success    : True
box_name   : Box C (Long)
dimensions : {5, 10, 15}
max_weight : 22
cost       : 2.50
```

---

## Test Case 2: No Suitable Box Found

**Request**

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/recommend/" `
-Method Post `
-ContentType "application/json" `
-Body '{"length": 4, "width": 9, "height": 14, "weight": 100}'
```

**Response**

```text
Invoke-RestMethod : {"success": false, "message": "No box fits"}
```

---

## Test Case 3: Smaller Box Selected

**Request**

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/recommend/" `
-Method Post `
-ContentType "application/json" `
-Body '{"length": 4, "width": 9, "height": 1, "weight": 10}'
```

**Response**

```text
success    : True
box_name   : Box B (Medium)
dimensions : {4, 8, 16}
max_weight : 20
cost       : 1.20
```

---

## API Output Screenshot

![API Output](https://github.com/user-attachments/assets/7c68898e-babe-4043-8bed-26809261356b)

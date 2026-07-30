import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Box

@csrf_exempt
def recommend_box(request):
    if request.method != "POST":
        return JsonResponse({"error": "Send a POST request"}, status=405)

    try:
        data = json.loads(request.body)
        # Sort the incoming item dimensions!
        arr = sorted([int(data['length']), int(data['width']), int(data['height'])])
        w = int(data['weight'])
    except (ValueError, KeyError, json.JSONDecodeError):
        return JsonResponse({"error": "Invalid JSON payload"}, status=400)

    # Loop through the boxes in the database
    boxes = Box.objects.all()
    for box in boxes:
        if (arr[0] <= box.dim1 and 
            arr[1] <= box.dim2 and 
            arr[2] <= box.dim3 and 
            w <= box.max_weight):
            
            return JsonResponse({
                "success": True,
                "box_name": box.name,
                "dimensions": [box.dim1, box.dim2, box.dim3],
                "max_weight": box.max_weight,
                "cost": str(box.cost)
            })

    return JsonResponse({"success": False, "message": "No box fits"}, status=404)
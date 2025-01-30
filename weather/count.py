# weather/count.py

from weather.models import Place

def is_place_model_empty():
    if not Place.objects.exists():
        print("The Place model is empty.")
        return True
    else:
        print(f"The Place model contains {Place.objects.count()} records.")
        return False

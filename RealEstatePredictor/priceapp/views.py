from django.shortcuts import render
import joblib
import pandas as pd
import os

# Load your trained pipeline model
model_path = os.path.join(os.path.dirname(__file__), '..', 'real_estate_price_pipeline.pkl')
model = joblib.load(model_path)

def index(request):
    return render(request, 'index.html')

def predict_price(request):
    if request.method == 'POST':
        try:
            site_size = float(request.POST.get('site_size'))
            city_range = float(request.POST.get('city_range'))
            road_distance = float(request.POST.get('road_distance'))

            input_data = pd.DataFrame([[site_size, city_range, road_distance]],
                                      columns=["Site Size (sq ft)", "City Range (km)", "Road Distance (m)"])

            predicted_price = model.predict(input_data)[0]

            return render(request, 'result.html', {
                'predicted_price': round(predicted_price, 2),
                'site_size': site_size,
                'city_range': city_range,
                'road_distance': road_distance
            })
        except Exception as e:
            return render(request, 'result.html', {'error': str(e)})
    return render(request, 'index.html')

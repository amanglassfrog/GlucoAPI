from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ml_service.recommendations.glucosyncandroid import get_recommendations


@csrf_exempt
def recommendations(request):
    if request.method == 'POST':
        try:
            diabetic_level = int(request.POST['diabetic_level'])
            result = get_recommendations(diabetic_level, (70, 201))
            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})
    

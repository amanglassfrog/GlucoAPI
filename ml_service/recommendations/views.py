from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .glucosyncandroid import get_recommendations


@csrf_exempt
def recommendations(request):

    if request.method == 'GET':


        try:
            diabetic_level = request.GET.get('diabetic_level')

            # Check if diabetic_level is None or empty
            if diabetic_level is None or not diabetic_level.strip():
                return JsonResponse({'error': 'diabetic_level parameter is missing or empty.'})


            print(diabetic_level)

            result = get_recommendations(int(diabetic_level), (70, 201))
            
            return JsonResponse(result)
        
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})
    



def testing(request): 
    if request.method == 'GET':
        return JsonResponse({'success':'hello world'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
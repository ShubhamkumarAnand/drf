from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({
        "message": "Hi there! From Django here is your API response"
    })

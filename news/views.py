from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse(f"<mark>Hello</mark>, My Home!<hr>"
                        f"Request method: <b style='color: green;'>{request.method}</b>")


def randomize(request):
    import random
    a = random.randint(1, 100)
    b = random.randint(100, 10000)
    c = a + b
    return HttpResponse(f"Random: {a} + {b} = {c} ")


def calc(request):
    a = 10
    b = 3
    c = a + b
    return HttpResponse(f"{a} + {b} = {c}")


def calc_int(request, number):
    a = 10
    b = 3
    response = ""
    if number:
        c = a + b + number
        response = f"{a} + {b} + {number} = {c}"
    else:
        c = a + b
        response = f"{a} + {b}  = {c}"

    return HttpResponse(f"response"
                        f"<hr>"
                        f"<img style='width: 300px;' src='https://upload.wikimedia.org/wikipedia/commons/7/7a/Logonetflix.png' alt='netflix rasm'>"
                        f"<p>{request.META}</p>"
                        f"<p>{request.user}</p>"
                        f"<p>{request.method}</p>")


def get_data(request, text):
    context = {
        "vorisxon": "<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0JcNajPTR_Fxg_B81uJnvlWfi-iJVGfNZcCAKcCTHZA&s' alt='vorisxon rasmi'>"
                    "<br>"
                    "Salom men Vorisxonman yoshim 22 da.",
        "jasur": "Salom men Jasurman yoshim 24 da.",
        "muhammad": "Salom men Muhammad yoshim 18 da"
    }
    return HttpResponse(context.get(text, 'Kechirasiz bu ma`lumot topilmadi.'))



from django.shortcuts import render
# Create your views here.


def platform(request):
    return render(request, 'platform.html')


def games(request):
    text1 = "Atomic Heart"
    text2 = "Cyberpunk 2077"
    text3 = "PayDay 2"
    context = {"text1": text1, "text2": text2, "text3": text3, }
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')

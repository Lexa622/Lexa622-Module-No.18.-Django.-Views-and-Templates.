from django.shortcuts import render

# Create your views here.


def platform(request):
    title = "Главная страница"
    context = {"Title": title, }
    return render(request, 'platform.html', context)


def games(request):
    buy = "Купить"
    title = "Игры"
    games = ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]
    context = {"games": games, "Title": title, "buy": buy, }
    return render(request, 'games.html', context)


def cart(request):
    title = "Корзина"
    text = "Извините, ваша корзина пуста"
    context = {"Title": title, "text": text, }
    return render(request, 'cart.html', context)

from django.shortcuts import render
from task5.forms import UserRegister
# Create your views here.
users = ["Dima", "Viktor", "Pavel"]


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = int(request.POST.get("age"))
        if password == repeat_password and age >= 18 and username not in users:
            context = f"Приветствуем, {username}!"
            return render(request, "registration_page.html", {"context": context})
        elif password != repeat_password:
            info['error'] = "Пароли не совпадают"
        elif age < 18:
            info['error'] = "Вы должны быть старше 18"
        elif username in users:
            info['error'] = "Пользователь уже существует"
    return render(request, "registration_page.html", context=info)


def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = int(form.cleaned_data["age"])
            if password == repeat_password and age >= 18 and username not in users:
                context = f"Приветствуем, {username}!"
                return render(request, "registration_page.html", {"context": context})
            elif password != repeat_password:
                info['error'] = "Пароли не совпадают"
            elif age < 18:
                info['error'] = "Вы должны быть старше 18"
            elif username in users:
                info['error'] = "Пользователь уже существует"
        return render(request, "registration_page.html", context=info)
    else:
        form = UserRegister()
    return render(request, "registration_page.html", {"form": form})

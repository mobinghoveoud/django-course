from django.shortcuts import render


def hello(request):
    return render(request, "hello.html", {
        "user": "ehsan",
        "is_valid": False
    })

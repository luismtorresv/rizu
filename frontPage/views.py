from django.shortcuts import render


def frontPage(request):
    context = {}

    if request.user.is_authenticated:
        context["user_role"] = request.user.role
        return render(request, "frontPage.html", context)

    return render(request, "frontPage.html", context)

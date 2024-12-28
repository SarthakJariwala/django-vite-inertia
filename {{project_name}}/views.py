from inertia import render


def home(request):
    return render(request, "Index")

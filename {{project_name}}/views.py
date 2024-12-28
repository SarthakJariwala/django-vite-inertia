from django.contrib import messages
from inertia import render


def home(request):
    messages.success(request, "Hello from Inertia!")
    return render(
        request,
        "Index",
        props={
            "events": ["Event 1", "Event 2"],
        },
    )

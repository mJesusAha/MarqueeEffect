from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from marquee_effect.marquee_effect import *
from .models import *


def index(request):
    n = len(Runtext.objects.all()) - 10 if len(Runtext.objects.all()) >= 10 else 0
    n = Runtext.objects.all()[n::]
    t = render_to_string("index.html", {"table_text": n})
    return HttpResponse(t)


def runtext(request):
    if request.method == "GET":
        text_ = request.GET["text"] if "text" in request.GET else "text"
        color_ = request.GET["color"] if "color" in request.GET else "#ffffff"
        background_ = (
            request.GET["background"] if "background" in request.GET else "#61177c"
        )
    Runtext.objects.create(text=text_, color=color_, background=background_)
    address = "video/moving_text.mp4"
    n = GenerateMarqueeEffect(
        text=text_, font_color=color_, background_color=background_, address = address
    ).create_movie()
    if n == -1:
        n = GenerateMarqueeEffect(text=text_, address = address).create_movie()
    with open(address, "rb") as f:
        response = HttpResponse(f, content_type="application/MP4")
        response["Content-disposition"] = 'attachment; filename="video.MP4"'

    return response

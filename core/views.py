from django.shortcuts import render
from core.models import Artist
from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.


def artists_view(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        artists = Artist.objects.filter(name__icontains=url_parameter)
    else:
        artists = Artist.objects.all()

    ctx["artists"] = artists
    if request.is_ajax():

        html = render_to_string(
            template_name="artists-results-partial.html", context={"artists": artists}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "artists.html", context=ctx)

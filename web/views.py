from django.shortcuts import render, redirect

from web.forms import UrlForm
from web.models import URL

from web.utils import decode_base62


def page(request):
    if not request.session or not request.session.session_key:
        request.session.save()

    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['url']
            url = URL.objects.filter(session=request.session.session_key).filter(original_url=original_url).first()
            if url is None:
                url = URL(session_id=request.session.session_key, original_url=original_url)
                url.save()

            short_url = request.build_absolute_uri() + f"{url.url_slug}"
            return render(request, 'index.html', {"url": short_url, "clicks": url.clicks})
    else:
        form = UrlForm()
    return render(request, 'index.html', {"form": form})


def redirect_short_url(request, slug):
    url = URL.objects.get(pk=decode_base62(slug))
    url.clicks += 1
    url.save()
    return redirect(url.original_url)

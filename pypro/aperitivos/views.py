from django.shortcuts import render

from pypro.aperitivos.models import Video

videos = [
      Video(slug='demo-spotify', titulo='Demo Spotify:', vimeo_id='6268154'),
      Video(slug='motivacao', titulo='Video Motivação:', vimeo_id='429413311')
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = Video.objects.get(slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})

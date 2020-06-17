from django.shortcuts import render


videos = [
        {'slug': 'demo-spotify', 'titulo': 'Demo Spotify:', 'vimeo_id': 6268154},
        {'slug': 'motivacao', 'titulo': 'Video Motivação:', 'vimeo_id': 429413311}
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Motivação:', 'vimeo_id': 429413311}
    return render(request, 'aperitivos/video.html', context={'video': video})

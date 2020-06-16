from django.shortcuts import render


def video(request, slug):
    videos = {
        'demo-spotify': {'titulo': 'Demo Spotify', 'vimeo_id': 6268154},
        'motivacao': {'titulo': 'Video Motivação:', 'vimeo_id': 429413311}
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

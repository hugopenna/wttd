from django.shortcuts import render, get_object_or_404

from eventex.core.models import Speakers


def home(request):
    speakers = Speakers.objects.all()
    return render(request, 'index.html', {'speakers': speakers})

def speaker_detail(request, slug):
    speaker = get_object_or_404(Speakers, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})

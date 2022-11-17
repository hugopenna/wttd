from django.views.generic import DetailView
from django.views.generic.list import ListView

from eventex.core.models import Speakers, Talk

home = ListView.as_view(template_name='index.html', model=Speakers)

speakers_detail = DetailView.as_view(model=Speakers)

talk_list = ListView.as_view(model=Talk)

from django.views.generic.list import ListView
from django.shortcuts import get_list_or_404

# Create your views here.
from forum.models import Topic


class TopicListView(ListView):
    model = Topic
    allow_empty = False

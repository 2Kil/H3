import json
from django.shortcuts import render
from .models import H3_works
from .post_video import Get_json as add_video
from django.core import serializers

# Create your views here.
def index(request):
    video_list = H3_works.objects.all().order_by('-id')[:6]
    #video_list = H3_works.objects.filter(age = '90后')
    json_data = serializers.serialize('json', video_list)
    json_data = json.loads(json_data)
    context = {
        'data':json_data
    }
    add_video()
    return render(request,'index.html',context=context)

def add_videos(request):
    add_video()
    return render(request,'index.html')


import json, time
from django.shortcuts import render
from .models import H3_works
from .post_video import Get_json as add_video
from django.core import serializers

# Create your views here.
def index(request):
    # 随机获取
    video_list = H3_works.objects.order_by('?')[:9]
    # 获取末尾6条
    # video_list = H3_works.objects.all().order_by('-id')[:6]
    # 按条件筛选
    #video_list = H3_works.objects.filter(age = '90后')
    json_data = serializers.serialize('json', video_list)
    json_data = json.loads(json_data)
    context = {
        'data':json_data
    }
    # i = 0
    # while True:
    #     add_video()
    #     i += 8
    #     print(i)
    #     time.sleep(5)
    add_video()
    return render(request,'index.html',context=context)

def add_videos(request):
    add_video()
    return render(request,'index.html')


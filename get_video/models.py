from django.db import models

# Create your models here.
class H3_works(models.Model):
        #作者id   data.author.short_id   357169028
    short_id = models.IntegerField()
        #作者昵称   data.author.nickname   家庭🌷菜艺
    nickname = models.TextField()
        #作者年龄   data.author.birthday_description   90后
    age = models.CharField(max_length=20,null=True)
        #作者地区   data.author.city   沧州
    city = models.CharField(max_length=20,null=True)
        #作者16位id    data.circle.id     1634694769107979
    id_16 = models.BigIntegerField()
        #视频标题   data.title     感恩老师，您辛苦了！
    title = models.TextField(null=True)
        #视频封面   data.video.url_list.0   http://p9-hs.byteimg.com/img/tos-cn-i-0000/be6856d3b0434709aca0d24738c701d2~tplv-hs-large.jpg
    jpg_url = models.TextField()
        #视频动图   data.video.gif_url_list.0   http://p9-hs.byteimg.com/img/tos-cn-p-0000/5ade5ebea6344ebe8042c6144c168441~n
        # oop.image
    gif_url = models.TextField()
        #视频地址   data.video.url_list.0      https://api.huoshan.com/hotsoon/item/video/_source/?video_id=v0300ced0000blrc1n6409jqdk
        # msgiqg&line=0&app_id=1112&vquality=normal&watermark=0&long_video=0&sf=1&ts=1570273560
    video_url = models.TextField()
        #视频id   data.video.video_id        v0300ced0000blrc1n6409jqdkmsgiqg
    video_id = models.CharField(max_length=100)
        #视频宽度   data.video.width       576
    video_with = models.IntegerField()

    class Meta:
        db_table = 'video'
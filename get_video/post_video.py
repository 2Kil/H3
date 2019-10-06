import requests
from .models import H3_works


def Get_json():
    url = 'https://hotsoon-a.snssdk.com/hotsoon/feed/?type=video&version_code=5.9.5&app_name=live_stream&vid=962C0849-E2' \
          '6B-4912-8662-BB4444760B15&device_id=57512771558&channel=App%20Store&livestream_show_tab_while_no_login=526414' \
          '&aid=1112&screen_width=750&client_request_id=a02be7f28f4226c8f579c3f7a9b89584&openudid=939354e9cc33e3b6955079' \
          '8daa6105175907359b&live_sdk_version=5.9.5&update_version_code=5951&os_api=18&ac=WIFI&mccmnc=46001&os_version=' \
          '12.2&device_platform=iphone&iid=68003486951&device_type=iPhone10,1&idfa=00000000-0000-0000-0000-000000000000&' \
          'diff_stream=1&ad_user_agent=Mozilla%2F5.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2012_2%20like%20Mac%20OS%20X%29%' \
          '20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Mobile%2F15E148&req_from=feed_refresh&action=refre' \
          'sh&mas=00add0e4a9bdd7f9da9d40fb1a3721e8d235d54feb8db22707672e&as=a22556ba5b3c2ce8b53395&ts=1554344139'
    head = {
        'User-Agent':'ç«å±±å°è§é¢ 5.1.2 rv:5951 (iPhone; iOS 12.2; zh-Hans_HK) Cronet'
    }
    html = requests.get(url,headers = head)
    json = html.json()
    json = json['data']
    for i in json:
        try:
            short_id = i['data']['author']['short_id']
            nickname = i['data']['author']['nickname']
            age = i['data']['author']['birthday_description']
            city = i['data']['author']['city']
            try:
                id_16 = i['data']['circle']['id']
            except Exception:
                id_16 = 0
            title = i['data']['title']
            jpg_url = i['data']['video']['cover']['url_list'][0]
            gif_url = i['data']['video']['gif_url_list'][0]
            video_url = i['data']['video']['url_list'][0]
            video_id = i['data']['video']['video_id']
            video_with = i['data']['video']['width']
            print('标题'+title)
        except Exception as e:
            print(e)
        else:
            video = H3_works(short_id=short_id,nickname=nickname,age=age,city=city,id_16=id_16,title=title,
                             jpg_url=jpg_url,gif_url=gif_url,video_url=video_url,video_id=video_id,video_with=video_with)
            video.save()

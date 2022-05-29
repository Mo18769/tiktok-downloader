import os
import json
import requests
import http.client

#https://www.tiktok.com/@yg2times/video/7072890445533056262                                        
#                                      ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯     

#for example 7072890445533056262      
video_id = input("Please type in the video id: ")                                                                  
                                                                                                     

DOWNLOAD_HEADERS = {'user-agent': 'TelegramBot (like TwitterBot)'}

conn = http.client.HTTPSConnection("api.tiktokv.com")
payload = ''
headers = {
    
}
conn.request("GET", "/aweme/v1/multi/aweme/detail/?aweme_ids=%5B" + video_id + "%5D", payload, headers)
res = conn.getresponse()
data = res.read()
obj = json.loads(data.decode("utf-8"))
download_url =  obj["aweme_details"][0]["video"]["play_addr"]["url_list"][0];


if not os.path.exists('videos'):
    os.mkdir('videos')


get_video = requests.get(download_url, headers=DOWNLOAD_HEADERS, allow_redirects=True)
with open(f"videos/{video_id}.mp4", "wb") as file_stream:
    video_content = get_video.content
    file_stream.write(video_content)





    
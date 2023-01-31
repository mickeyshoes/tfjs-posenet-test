import os, sys, requests, time

# ref : https://api.ncloud-docs.com/docs/ai-naver-poseestimation-pose

url = "https://naveropenapi.apigw.ntruss.com/vision-pose/v1/estimate"

# image_1 : none
# image_2 : 1.6 sec

files = {'image': open('model_images/images_1.jpg', 'rb')}
# print(files)
headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
start = time.time()
response = requests.post(url,  files=files, headers=headers)
end = time.time()
print(f'time : {end -start:.5f} sec')
rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print("Error Code: ", rescode)
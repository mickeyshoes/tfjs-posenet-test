import time, requests

# ref : https://developers.kakao.com/docs/latest/ko/pose/dev-guide#see-more
print('kakao test\n image must be over 320px')

# 1155x649 : 1.6 sec, score : 0.625
# IMAGE_URL = 'https://i0.wp.com/post.healthline.com/wp-content/uploads/2020/10/Female_Yoga_1296x728-header-1296x729.jpg?w=1155&h=2268'

#1136x852 : 1.5 sec, score : 0.644
# IMAGE_URL = 'https://i.insider.com/600af7c2c94799001992cc62?width=1136&format=jpeg'

#732x549 : 1.2 sec, score : 0.504
IMAGE_URL = 'https://post.healthline.com/wp-content/uploads/2020/01/yoga-pose-downward-dog-732x549-thumbnail-732x549.jpg'

session = requests.Session()
session.headers.update({'Authorization': 'KakaoAK ' + APP_KEY})

# URL로 이미지 입력시
start = time.time()
response = session.post('https://cv-api.kakaobrain.com/pose', data={'image_url': IMAGE_URL})
end = time.time()
print(f'time : {end -start:.5f} sec')
print(response.status_code, response.json())
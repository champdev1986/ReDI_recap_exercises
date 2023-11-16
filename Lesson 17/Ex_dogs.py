import requests

GET_ALL_DOGS_URL = 'https://dog.ceo/api/breeds/list/all'
GET_RANDOM_IMAGE_URL = 'https://dog.ceo/api/breeds/image/random'
GET_DOG_URL = 'https://dog.ceo/api/breed/<breed_name>/images'

def get_all_dogs():
    response = requests.get(GET_ALL_DOGS_URL)
    json_data = response.json()
    print(f"{json_data['message']}")

get_all_dogs()

def get_random_image():
    response = requests.get(GET_RANDOM_IMAGE_URL)
    json_data = response.json()
    img_response = requests.get(json_data['message'])
    with open('Lesson 17/random_dog.jpg', 'wb') as f:
        f.write(img_response.content)

get_random_image()

def get_dog(breed_name):
    response = requests.get(f'https://dog.ceo/api/breed/{breed_name}/images')
    json_data = response.json()
    img_response = requests.get(json_data['message'])
    with open(f'Lesson 17/{breed_name}.jpg', 'wb') as f:
        f.write(img_response.content)

get_dog("african")


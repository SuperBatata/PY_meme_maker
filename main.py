import requests
import urllib
import datetime

username = 'superbatata'
password = "15010933"

userAgent= 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'


data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']


images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]


#List all the memes
print('Here is the list of available memes : \n')
ctr = 1
for img in images:
    print(ctr,img['name'],img['url'] ,img['id'])
  
    ctr = ctr+1





#https://api.imgflip.com/caption_image

id = int(input('Enter the serial number of the meme : '))
text0 = input('Enter first text : ')
text1 = input('Enter second text : ')
#Fetch the generated meme
URL = 'https://api.imgflip.com/caption_image'

params = {
    'username':username,
    'password':password,
    'template_id':images[id-1]['id'],
    'text0':text0,
    'text1':text1
}
response = requests.request('POST',URL,params=params).json()
print(response)



my_meme =response['data']['url']

basename="image_meme"
suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
filename = "_".join([basename,suffix])

response = requests.get(my_meme)

open(filename+".jpg" ,"wb").write(response.content)
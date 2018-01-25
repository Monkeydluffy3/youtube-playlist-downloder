import bs4 as bs
import urllib.request as req
import down as manhas

length = int(input('Enter your How many video of playlist u want to downlode :'))

link = input('Enter the url of 1st video : ')#'https://www.youtube.com/watch?v=P6YJy2fmJ1o&list=RDP6YJy2fmJ1o'
name = ''

main_list = []
main_list.append(link)
list1 = []
sou = req.urlopen(link).read()
soup = bs.BeautifulSoup(sou,'lxml')

#for item in soup.find_all('h1'):
#   name = item.text
#print(name)

item = soup.find('div' , {'id' :'content'})

for io in soup.find_all('a'):
   list1.append(io.get('href'))

list1 = list1[6:(length+6)]
#print(list1)    

for string in list1:
  main_list.append('https://en.savefrom.net/#url=https://youtube.com'+string+'&utm_source=youtube.com&utm_medium=short_domains&utm_campaign=www.ssyoutube.com')

  
main_list[0] = 'https://en.savefrom.net/#url='+link+'&list=RDP6YJy2fmJ1o&utm_source=youtube.com&utm_medium=short_domains&utm_campaign=www.ssyoutube.com' 
z = 0  
for i in range(0,length):
  manhas.downlode(main_list[i])
    
#link = "https://en.savefrom.net/#url=http://youtube.com/watch?v=89lQ5k5F_hM&list=RDMM89lQ5k5F_hM&utm_source=youtube.com&utm_medium=short_domains&utm_campaign=www.ssyoutube.com"


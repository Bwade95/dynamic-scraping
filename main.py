import requests
import os

class Unsplash:
  def __init__(self,search_term,per_page,quality):
    self.search_term = search_term
    self.per_page = per_page
    self.pages = 0
    self.quality = quality
    self.headers = {
      "Accept":	"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
      "Accept-Encoding":	"gzip, deflate, br",
      "Accept-Language":	"en-GB,en;q=0.5",
      "Host":	"unsplash.com",
      "User-Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
    }

  def set_url(self):
    return f"https://unsplash.com/napi/search?query={self.search_term}&xp=&per_page={self.per_page}&page={self.pages}"

  def make_request(self):
    url = self.set_url()
    return requests.request("GET",url,headers=self.headers)
  
  def get_data(self):
    self.data = self.make_request().json()

  def save_path(self,name):
    download_dir = "Cats"
    if not os.path.exists(download_dir):
      os.mkdir(download_dir)
    return f"{os.path.join(os.path.realpath(os.getcwd()),download_dir,name)}.jpg"
  
  def download(self,url,name):
    filepath = self.save_path(name)
    with open(filepath,"wb") as f:
      f.write(requests.request("GET",url,headers=self.headers).content)

  def scraper(self,pages):
    for page in range(0,pages+1):
      self.make_request()
      self.get_data()
      for item in self.data['photos']['results']:
        name = item['id']
        url = item['urls'][self.quality]
        self.download(url,name)
        self.pages += 1

scraper = Unsplash("cat","20","thumb")
scraper.scraper(2)


    


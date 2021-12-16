import requests
from bs4 import BeautifulSoup
import urllib3

post_count=2712772
for x in range(0,10):
    response = requests.get(
        url="https://forums.nasioc.com/forums/forumdisplay.php?f=90"
    )
    print(response.status_code)
    soup = BeautifulSoup(response.content, "html.parser")
    print("thread_title_"+str(post_count))
    page_title = soup.find(id="thread_title_"+str(post_count))
    
    print(page_title.string)
    post_count+=10

#%%
# Jimmy Hickey
# 18-07-21
# Download Wikiversity picture of the day every day.
# https://en.wikiversity.org/wiki/Wikiversity:Main_Page'
#%%

# to open session
import requests
# to parse web page
import bs4
# to find text in page
import re
# to download the picture
import urllib.request


def pic_of_day(yesterdays_image):
    # start a session and get the page
    sess = requests.Session()
    page = sess.get('https://en.wikiversity.org/wiki/Wikiversity:Main_Page')

    # Parse the page into html
    soup = bs4.BeautifulSoup(page.content, 'html.parser')

    # Find the "Educational Media Awareness Campaign" anchor
    # Then back up to its parent table data entry
    # Use this to go down the table entry to find the image
    parent = soup.find("a", {"title": "Educational Media Awareness Campaign"}).find_parent('td')
    # Location of the image
    img_location = parent.find("a", class_="image")

    # If the image has changed since yesterday, continue to follow it
    if img_location != yesterdays_image:
        # Follow the URL of the image to get a higher quality version
        img_url = "https://en.wikiversity.org%s" % img_location['href']
        page = sess.get(img_url)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')

        # Find the higher quality image on the page
        # Then find it's href and follow to the image's page
        img_link = soup.find("div", {"id": "file"})
        final_img = img_link.find("a")
        href = final_img['href']
        img_url = "https:%s" % href

        # Strip the image name off to use as the downloaded file's name
        m = re.search('[^/]+$', href)
        file_name = m.group(0)

        # Download the image and keep its name
        urllib.request.urlretrieve(img_url, file_name)

        # close the session!
        sess.close()

    return img_location


# TODO: Make this run once a day
def main():
    pic_of_day(None)


if __name__ == '__main__':
    main()

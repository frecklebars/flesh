import requests
import argparse

parser = argparse.ArgumentParser(description="FLickr turnEd Static Html cli")
parser.add_argument("user", metavar="USER_ID")
parser.add_argument("-a", "--album", dest="album")
parser.add_argument("-k", "--key", dest="key")
args = parser.parse_args()

user_id = args.user
album_id = args.album
key = args.key

if key is None:
    with open("./key", "r") as f:
        key = f.read()
print("key found")

template = "<a href='{photo_page}'><img src='{photo_preview}'></a>\n"

# calls
if album_id is not None:
    flickr_call = "https://www.flickr.com/services/rest/?method=flickr.photosets.getPhotos&api_key={key}&photoset_id={album_id}&user_id={user_id}&format=json&nojsoncallback=1"
    flickr_call = flickr_call.format(key=key, user_id=user_id, album_id=album_id)
else:
    flickr_call = "https://www.flickr.com/services/rest/?method=flickr.people.getPublicPhotos&api_key={key}&user_id={user_id}&format=json&nojsoncallback=1"
    flickr_call = flickr_call.format(key=key, user_id=user_id)

print("constructed call")

# links
photo_preview_link_template = "https://live.staticflickr.com/{server_id}/{photo_id}_{secret}.jpg"
photo_webpage_link_template = "https://www.flickr.com/photos/{user_id}/{photo_id}"

if album_id is not None:
    photo_webpage_link_template = photo_webpage_link_template + "in/album-{album_id}/".format(album_id=album_id)

# main
print("making request to: " + flickr_call)
response = requests.get(flickr_call).json()
print("request successful")

if album_id is not None:
    photos = response["photoset"]["photo"]
else:
    photos = response["photos"]["photo"]

print("photos found, building gallery")
gallery = ""
for photo in photos:
    photo_id = photo["id"]
    server = photo["server"]
    secret = photo["secret"]

    photo_preview_link = photo_preview_link_template.format(server_id=server, photo_id=photo_id, secret=secret)
    photo_page_link = photo_webpage_link_template.format(user_id=user_id, photo_id=photo_id)

    photo_entry = template.format(
        photo_page = photo_page_link,
        photo_preview = photo_preview_link
    )

    gallery += photo_entry

print("dumping gallery")
with open("gallery.html", "w") as f:
    f.write(gallery)

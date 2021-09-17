import requests

with open("key", "r") as f:
    key = f.read()

# params
user_id = ""
template = "<a href='{photo_page}'><img src='{photo_preview}'></a>\n"

# calls
get_user_public_photos_call = "https://www.flickr.com/services/rest/?method=flickr.people.getPublicPhotos&api_key={key}&user_id={id}&format=json&nojsoncallback=1"
get_user_public_photos_call = get_user_public_photos_call.format(key=key, id=user_id)

# links
photo_preview_link_template = "https://live.staticflickr.com/{server_id}/{photo_id}_{secret}.jpg"
photo_page_link_template = "https://www.flickr.com/photos/{user_id}/{photo_id}"

# main
response = requests.get(get_user_public_photos_call).json()
photos = response["photos"]["photo"]

gallery = ""
for photo in photos:
    photo_id = photo["id"]
    server = photo["server"]
    secret = photo["secret"]

    photo_preview_link = photo_preview_link_template.format(server_id=server, photo_id=photo_id, secret=secret)
    photo_page_link = photo_page_link_template.format(user_id=user_id, photo_id=photo_id)

    photo_entry = template.format(
        photo_page = photo_page_link,
        photo_preview = photo_preview_link
    )

    gallery += photo_entry

with open("gallery.html", "w") as f:
    f.write(gallery)

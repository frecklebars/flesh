# FLESH - FLickr turnEd Static Html
simple script that turns your flickr photostream (or album/photoset now) into static html ready to be pasted in your based static website

## usage
`python flesh.py [-h] [-a ALBUM] [-k KEY] USER_ID`

* `USER_ID` is the user id of the user whose photostream/album you want to gallerify
* `KEY` is required but can be skipped and put in a file at `./key` instead

in the code itself (ln 19) you can also mess with `template` which is the way you want an image entry to look in your gallery. pretty self explainatory. using both `{photo_page}` and `{photo_preview}` is not required.

output is `./gallery.html`

[example gallery](https://main.freckleskies.net/files/DCIM/)
import json

#generate list of urls from the chrome bookmarks of a user
def bookmarksToUrls(profile_name, unsorted_folder_name="other"):
    path = r'C:\Users\MichaelE\AppData\Local\Google\Chrome\User Data\\'
    path += profile_name
    path += '\Bookmarks'

    with open(path, encoding="utf8") as json_file:
        bookmarks = json.loads(json_file.read())

    unsorted = bookmarks["roots"][unsorted_folder_name]
    unsorted_urls = [bookmark["url"] for bookmark in unsorted["children"]]
    return unsorted_urls

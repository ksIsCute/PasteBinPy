import os
#####################
import pastebinpy # import required module

# define our variable for our paste
paste = pastebinpy.paste(os.environ['api_key'], "title", "content", "2")

# returns the pastebin url
print(paste)
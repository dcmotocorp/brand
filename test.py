from googleapiclient.discovery import build
#this is is thehoj sdfl; dsjkf;lk
#sf;lkjsdfl;k 
#fds fdsf 

from googleapiclient.errors import HttpError




"""lsdkjfklsdnfms;l m ldfmnkl/dasmlk/f
    df, asmdnf,.msdf '
    sdf
     ;asd
     'f;a
     s'd;f 
     asd
     f 
     asd
      asd 
      g
      asd 
      gad
       g 
       asd 
       ga 
       dg
       asd 
       g
       as dg
       asd 
       g
        s
    """
#this is the first api

#thsdoifj 
api_key = 'AIzaSyBYkInQobwWohKd8VGkhUvOCO3Fvu2GfJQ'
youtube = build('youtube', 'v3', developerKey=api_key)



response = youtube.videos().list(
    part='snippet',
    chart='mostPopular',
    regionCode='IN',
    videoCategoryId='0',
    maxResults=100
).execute()


tag_counts = {}

for item in response['items']:
     tags = item['snippet'].get('tags')
     print(tags)
     print("================")
#     for tag in tags:
#         if tag in tag_counts:
#             tag_counts[tag] += 1
#         else:
#             tag_counts[tag] = 1


# sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)
# for i in range(100):
#     print(sorted_tags[i][0])

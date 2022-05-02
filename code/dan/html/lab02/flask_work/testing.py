import json 
import pprint
with open('blog_items.json', 'r') as f:
        data = json.load(f)
        #pprint.pprint(data)
        
        pprint.pprint(data ['items'][0]['blog_title'])
        
        
title = data['items'][0]['blog_title']
print (title)
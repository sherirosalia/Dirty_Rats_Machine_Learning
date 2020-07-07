import json
import csv 
import pandas as pd 
import pprint

#this is the precursor to app.py
with open('notebooks/data_file.json') as f:
  data = json.load(f)
  print(data[0])
  print(len(data))

businesses = []

for biz in data:
    
    id_ = biz['id']
    name = biz['name']
    phone = biz['phone']
    if 'price' in biz:
        price = biz['price']
    else:
        price = None
    addresses = biz['location']['display_address']
    address = '  '.join(addresses)
    
    services = biz['categories']
    
    alias = ''
    title = ''
    
    for service in services:
        alias += service['alias'] + ', '
        title += service['title'] + ', '
        
    # more verbose alternate
    #for service in services
#         a_alias = service['alias']
#         alias += a_alias
        
    
    rating = biz['rating']
    review_count = biz['review_count']
    lat = biz['coordinates']['latitude']
    lon = biz['coordinates']['longitude']
    
    if lat is None:
        continue
    if lon is None:
        continue

    yelp_dict = {
                    'id': id_,
                    'name': name,
                    'phone': phone,
                    'address' : address,
                    'category_alias': alias,
                    'category_title': title,
                    'price': price,
                    'rating' : rating,
                    'review_count' : review_count,
                    'lat': lat,
                    'lon': lon,
                        }



    # pprint(yelp_dict)

    businesses.append(yelp_dict)
#     print(biz['coordinates'])
df = pd.DataFrame(businesses)
print(df.head())
print(df['price'].head(10))

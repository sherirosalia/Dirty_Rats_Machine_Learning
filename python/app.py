## load json pull from yelp api, skip anything that does not have lat and lon coordinates, keeping one copy 
## each restaurant (remove dupes), converted price to 0-3 scale and prepped cuisine type (ftype variable)
## for machine learning ergo the 301 columns. File labeled basic.py has non ml material
## sequel to this script is merge.py where violation information will be pulled in

import json
import csv 
import pandas as pd 
import pprint

with open('notebooks/data_file.json') as f:
  data = json.load(f)
  print(data[0])
  print(len(data))

businesses = []
#create a set of unique ids so that duplicates are eliminated
unique_ids = set()

for biz in data:
    
    id_ = biz['id']
    if id_ in unique_ids:
        continue
    else:
        unique_ids.add(id_)
        
    name = biz['name']
    phone = biz['phone']
    if 'price' in biz:
        price = len(biz['price'])
    else:
        price = 0
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
    for service in services:
        #ftype is food type
        ftype = service['title']
        yelp_dict[ftype]=True


    # pprint(yelp_dict)

    businesses.append(yelp_dict)
#     print(biz['coordinates'])
df = pd.DataFrame(businesses)
print(len(df['id'].unique()))
# exit()
df.fillna(False, inplace=True)
print(df.head())
# print(df['price'].head(10))
print(len(df))

# saving the dataframe 
df.to_csv('csv_files/rest_ml.csv') 


    
#     print(name  + '  ' +  phone + '  ' + review_count  + '  ' + lat   + '  ' + lon    + '\n' +
#           '  ' +  address  + '  ' +  rating) 


# simpler version of what is above

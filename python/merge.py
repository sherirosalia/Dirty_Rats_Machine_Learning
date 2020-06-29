import pandas as pd

#violations csv
v=pd.read_csv('csv_files/restaurants.csv')
print(v.head())
#ratings
r=pd.read_csv('csv_files/rest_ml.csv')
print('next dataframe')
print(r.head())

#normalized name columns for each dataframe
r['n_name'] = r['name'].map(lambda name: name.lower().replace("'",""))
print(r['n_name'].head())

# unique restaurants
r_u=r.groupby('n_name').count()
r_u=r_u[r_u['id']==1]
print(len(r_u))

# non chain
nc=r_u.index
print(nc)
# print(r['n_name'].isin(nc))

# unique restaurants
ur=r[r['n_name'].isin(nc)]
print(ur.head())


# r_u.to_csv('csv_files/r_u.csv')

v['n_name'] = v['FACILITY_NAME'].map(lambda name: name.lower().replace("'",""))
print(v['n_name'].head())

in_=pd.merge(ur,v, how='inner', left_on=['n_name'], right_on=['n_name'])
print(in_.head())
print(len(in_))
# in_=pd.merge(r,v, how='inner', left_on=['n_name'], right_on=['n_name'])
# print(in_.head())
# print(len(in_))

# csv of yelp restaurants that are not a chain (only one location in city 900 zips) that  also have
# health violations. One row per violation
print(len(in_['id'].unique()))
in_.to_csv('csv_files/yelp_violations.csv')






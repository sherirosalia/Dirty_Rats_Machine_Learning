import pandas as pd
import numpy as np 


# This is the sequel to merge.py, and precursor to forest.py

# open csv
csv=pd.read_csv('csv_files/yelp_violations.csv')
# print(csv.head())
cl_ml=pd.read_csv('csv_files/rest_ml_clean.csv')
print(cl_ml.head())

# check for violation codes
# print(csv['violation_code'].unique())
# ['F023' 'F038' 'F029' 'F022' 'F041' 'F051']


#assign variable so we can loop through it
vc=csv['violation_code'].unique()
has_violations=set()
for violation in vc:
    print(violation)
    #making sure loop works and comment out after
    # violation_loop =csv['violation_code']== violation
    #print(violation_loop)

    #loop works so now filtered data frame that only works with this violation
    vio=csv[csv['violation_code']== violation]
    #print(vio.head())
    #print count of unique items
    uvio=vio['id'].unique()
    has_violations.update(uvio)

    #generate a list of whether a restaurant has had a type of violation from yelp data (ml_clean)
    cl_ml[violation]=cl_ml['id'].isin(uvio)
    
    # rint(cl_ml['id'].isin(uvio))
# print(cl_ml.head())
#sending to csv where we will delete some unneeded columns before sending to ml / random forest

cl_ml['has_violations']=cl_ml['id'].isin(has_violations)

cl_ml.to_csv('csv_files/prep_w_cols.csv', index=False)







# # unique restaurants
# r_u=r.groupby('n_name').count()
# r_u=r_u[r_u['id']==1]
# print(len(r_u))

# # non chain
# nc=r_u.index
# print(nc)
# # print(r['n_name'].isin(nc))

# # unique restaurants
# ur=r[r['n_name'].isin(nc)]
# print(ur.head())
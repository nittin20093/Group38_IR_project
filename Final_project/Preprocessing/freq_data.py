
import pandas as pd
from collections import OrderedDict
import numpy as np

df1 = pd.read_csv('delhi_hotels_details_final.csv')
print(df1)

amenities = df1.iloc[:, -161:]

amen_sums = amenities.sum()


amen_names = amenities.columns.tolist()
print(amen_names)


amen = dict(zip(amen_names, amen_sums))
# print(amen)
# sorted_amen=sorted(amen)
# sorted_amen = sorted(amen.items(), key=lambda x:x[1])

keys = list(amen.keys())
values = list(amen.values())
sorted_value_index = np.argsort(values)
sorted_amen = {keys[i]: values[i] for i in sorted_value_index}
all_amen=[]
all_amen=list(sorted_amen.keys())
print(sorted_amen)
print("len of sorted amen", len(sorted_amen))
print(all_amen)
print("len of all amen", len(all_amen))

## for high freq amenities(top 13 were taken)
high_freq_amen=[]
keys = list(sorted_amen.keys())[-13:]
for i in keys:
    high_freq_amen.append(i)
# print(high_freq_amen)

## for mid freq amenities(middle 12 were taken)
low_freq_amen=[]
keys = list(sorted_amen.keys())[129:141]
for i in keys:
    low_freq_amen.append(i)
# print(low_freq_amen)
# print(len(low_freq_amen))

kept_freq=low_freq_amen+high_freq_amen

print(kept_freq)
print("len of kept amen", len(kept_freq))

##removing extra columns

list1=[i for i in kept_freq if i not in all_amen]
list2=[j for j in all_amen if j not in kept_freq]

removed_amen= list1+list2

# print(df1)
# print(removed_amen)
print("len of removed amen", len(removed_amen))
for i in removed_amen:
    df1.drop(i, axis=1, inplace=True)

# print(df1)

for i in range(len(df1)):
    amenities=df1.at[i, 'amenities']
    # print(type(df1.at[i, 'amenities']))
    res = amenities.strip('][').split(', ')
    new_result = list()
    for e in res:
        e = e[1:]
        e = e[:-1]
        new_result.append(e)
    
    # print(type(new_result))
    # print(new_result)

    

    # print(type(amenities))
    for j in removed_amen:
        # print(j)
        # print(amenities)
        
        if j in new_result:
            new_result.remove(j)
            # print(amenities)
    df1.at[i, 'amenities']=new_result
df1.to_csv('delhi_hotels_details_final_freq.csv')
# df1['amenities'] = df1['amenities'].apply(lambda x: [item.split() for item in map(str, x)])
# df1['amenities'] = df1['amenities'].map(lambda x: [item for item in x if item not in removed_amen])
# df1['amenities'] = df1['amenities'].map(lambda x: [item.split(',') if isinstance(item, str) and ',' in item else item for item in x if item not in removed_amen])
# df1['amenities'] = df1['amenities'].map(lambda x: [item.split(',') if isinstance(item, str) and ',' in item else item for item in x if item not in removed_amen])
# df1['amenities'] = df1['amenities'].map(lambda x: [word.strip() for word in str(x).split(',')])

# for i, row in df1.iterrows():
#     df1.at[i, 'amenities'] = [item for item in row['amenities'] if item not in removed_amen]

# df1['amenities'] = df1['amenities'].apply(lambda x: [item for item in x if item not in removed_amen])

# print(df1)

# df1.to_csv('delhi_hotels_details_final_freq.csv')

 
# print(sorted_amen)
# print(len(sorted_amen))
# print(sorted_amen)

# # ## removing less freq amenities
# less_freq_amen=[]
# for key, value in sorted_amen.items():
#     if value < 15:
#         less_freq_amen.append(key)
# # print(less_freq_amen)

# # ## removing more freq amenities
# more_freq_amen=[]
# for key, value in sorted_amen.items():
#     if value > 400:
#         more_freq_amen.append(key)
# # # print(more_freq_amen)

# for i in less_freq_amen:
#     df1.drop(i, axis=1, inplace=True)
# for i in more_freq_amen:
#     df1.drop(i, axis=1, inplace=True)

# kept_freq=[]
# kept_freq.append(less_freq_amen)
# kept_freq.append(more_freq_amen)







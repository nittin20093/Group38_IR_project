import pandas as pd
import numpy as np
import json
import SimilarImages

# delhi/BasicRankedHotelsDelhi.csv
# basic_ranked_datasets
def filter_data(parent_df ,type_of_rank, min_price, max_price ,min_ratings , amenities):
    df = pd.read_csv('./home/' + type_of_rank +'/' + parent_df)

    for i in range(len(df)):
        df.at[i,'price'] = df.at[i,'price'].replace("," , "")



    df['price'] = df['price'].astype(int)
    
    indexes = list()

    for l in range(len(df)):
        if(df.at[l , 'price'] <= max_price and df.at[l , 'price'] >= min_price):
            indexes.append(l)
        
    # print(len(indexes))
    # return indexes
    
    new_idx = list()

    for idx in indexes:
        # print(df['amenities'])
        # break
        temp  = df.at[idx , 'amenities'].strip('][').split(', ')
        for w in range(len(temp)):
            temp[w] = temp[w][:-1]
            temp[w] = temp[w][1:]
        intersect = list()
        for e in amenities:
            if e in temp:
                intersect.append(e)
        if(intersect == amenities):
            new_idx.append(df.at[idx  , 'Unnamed: 0.2'])

    
    # res = stringA.strip('][').split(', ')
    # temp = temp[1:]
    # print(temp[0])

    # return df
    # print(len(new_idx))
    return new_idx

def filter_with_similarity(parent_df ,type_of_rank, min_price, max_price ,min_ratings , amenities , selected_photos , all_photos , dataset_name):
    



    # finding old datatset

    df = pd.read_csv('./home/' + type_of_rank +'/' + parent_df)

    for i in range(len(df)):
        df.at[i,'price'] = df.at[i,'price'].replace("," , "")


    df['price'] = df['price'].astype(int)
    
    indexes = list()

    for l in range(len(df)):
        if(df.at[l , 'price'] <= max_price and df.at[l , 'price'] >= min_price):
            indexes.append(l)
        
    # print(len(indexes))
    # return indexes
    
    new_idx = list()

    for idx in indexes:
        # print(df['amenities'])
        # break
        temp  = df.at[idx , 'amenities'].strip('][').split(', ')
        for w in range(len(temp)):
            temp[w] = temp[w][:-1]
            temp[w] = temp[w][1:]
        intersect = list()
        for e in amenities:
            if e in temp:
                intersect.append(e)
        if(intersect == amenities):
            new_idx.append(df.at[idx  , 'Unnamed: 0.2'])

    not_selected = list()
    for el in new_idx:
        if el not in selected_photos:
            not_selected.append(el)

    user_not_interested_removed = list()

    for eac in new_idx:
        if eac not in not_selected or eac in selected_photos:
            user_not_interested_removed.append(eac)

    ress = list()
    for ea in selected_photos:
        l = int(20/len(selected_photos))
        res = SimilarImages.find_similar(ea,l , dataset_name)
        for every in res:
            ress.append(every)

    return ress

    

    


# print(filter_data('delhi/BasicRankedHotelsDelhi.csv' , 'basic_ranked_datasets' , 1000 , 2000 ,['Soundproofing']))
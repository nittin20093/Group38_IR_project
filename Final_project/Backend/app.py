from flask import Flask, redirect, url_for, request
import SimilarImages
import filter_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app , origins=["http://localhost:3001", "http://localhost:5000"])


@app.route('/ranked_with_filter', methods = ['POST'])
def ranked_with_filter():
    if request.method == 'POST':
        u = request.get_json()
        print(u)
        if(u['city']=='Delhi'):
            notpresentidx = [148,173,201,208,228,232,261,274,300,348,354,361,368,385,396,402,409,415,427,433,436,439,442,446,467,476,481,484,491,501,503,504,507,509,512,516,523,524,530,535,550,551,560,565,566,570,573,574,575,576,577,578,586,587,588,589,590,591,605,606,608,609,612,613,615,625,629,630,632,637]
            ranked_filtered_idxs = filter_data.filter_data(notpresentidx,'delhi/BasicRankedHotelsDelhi.csv' , 'basic_ranked_datasets' , u['budget']['min'] , u['budget']['max'],  u['rating'] ,u['amenities'] )
        if(u['city']=='Goa'):
            notpresentidx = [2,24,166,179,188,196,227,286,291,341,370,373,420,430,448,472,474,516]
            ranked_filtered_idxs = filter_data.filter_data(notpresentidx,'goa/BasicRankedHotelsGoa.csv' , 'basic_ranked_datasets' , u['budget']['min'] , u['budget']['max'],  u['rating'] ,u['amenities']  )
        if(u['city']=='Bangalore'):
            notpresentidx = [5,14,25,27,44,45,50,55,68,69,77,90,95,102,104,105,106,107,117,118,119,120,138,142,148,154,169,180,186,194,267,291,372,387,458,514,538,542,549,552,556,562,565,567,577,581,596,605,607,642,651,662,671,688,696,699,703,710,713,716,718,721]
            ranked_filtered_idxs = filter_data.filter_data(notpresentidx,'banglore/BasicRankedHotelsBangalore.csv' , 'basic_ranked_datasets' ,  u['budget']['min'] , u['budget']['max'],  u['rating'] ,u['amenities']  )
        print(ranked_filtered_idxs)
        return {'ranked_filtered_idxs': str(ranked_filtered_idxs)}


@app.route('/similarity', methods = ['POST'])
def similarity():
    if request.method == 'POST':
        u = request.get_json()
        print(u)
        if(u['city']=='Delhi'):
            notpresentidx = [148,173,201,208,228,232,261,274,300,348,354,361,368,385,396,402,409,415,427,433,436,439,442,446,467,476,481,484,491,501,503,504,507,509,512,516,523,524,530,535,550,551,560,565,566,570,573,574,575,576,577,578,586,587,588,589,590,591,605,606,608,609,612,613,615,625,629,630,632,637]
            similar_images_index_list = filter_data.filter_with_similarity(notpresentidx, 'delhi/BasicRankedHotelsDelhi.csv' , 'basic_ranked_datasets' , u['budget']['min'] , u['budget']['max'],  u['rating'] ,u['amenities'], u['selectedphotos'],u['allphotos'],'delhi_dataset')
        if(u['city']=='Goa'):
            notpresentidx = [2,24,166,179,188,196,227,286,291,341,370,373,420,430,448,472,474,516]
            similar_images_index_list = filter_data.filter_with_similarity(notpresentidx,'goa/BasicRankedHotelsGoa.csv' , 'basic_ranked_datasets' , u['budget']['min'] , u['budget']['max'],  u['rating'] ,u['amenities'], u['selectedphotos'],u['allphotos'],'goa_dataset')
        if(u['city']=='Bangalore'):
            notpresentidx = [5,14,25,27,44,45,50,55,68,69,77,90,95,102,104,105,106,107,117,118,119,120,138,142,148,154,169,180,186,194,267,291,372,387,458,514,538,542,549,552,556,562,565,567,577,581,596,605,607,642,651,662,671,688,696,699,703,710,713,716,718,721]
            similar_images_index_list = filter_data.filter_with_similarity(notpresentidx,'banglore/BasicRankedHotelsBangalore.csv' , 'basic_ranked_datasets' , u['budget']['min'] , u['budget']['max'],  u['rating'] ,u['amenities'], u['selectedphotos'],u['allphotos'],'banglore_dataset')
        print(similar_images_index_list)
        return {'similar_images_indexes': str(similar_images_index_list)}


@app.route('/get_hotel_links', methods = ['POST'])
def ranked():
    if request.method == 'POST':
        u = request.get_json()
        print(u)
        # similar_images_index_list = SimilarImages.find_similar(0,3,'goa_dataset')
        if(u['city']=='Delhi'):
            links = filter_data.get_hotel_data('delhi_hotels_details_final_freq.csv' , u['indexes'])
        if(u['city']=='Goa'):
            links = filter_data.get_hotel_data('goa_hotels_details_final_freq.csv' ,u['indexes'])
        if(u['city']=='Bangalore'):
            links = filter_data.get_hotel_data('banglore_hotels_details_final_freq.csv' , u['indexes'])
        print(links)
        return {'similar_images_indexes': links}
    


# main driver function
if __name__ == '__main__':
    app.run()
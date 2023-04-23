from flask import Flask, redirect, url_for, request
import SimilarImages
import filter_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3002", "http://localhost:5000"])


@app.route('/ranked_with_filter', methods = ['POST'])
def ranked_with_filter():
    if request.method == 'POST':
        u = request.get_json()
        print(u)
        if(u['city']=='Delhi'):
            ranked_filtered_idxs = filter_data.filter_data('delhi/BasicRankedHotelsDelhi.csv' , 'basic_ranked_datasets' , u['budget']['min'] ,u['budget']['max'] ,  u['rating'] , u['amenities'] )
        if(u['city']=='Goa'):
            ranked_filtered_idxs = filter_data.filter_data('goa/BasicRankedHotelsGoa.csv' , 'basic_ranked_datasets' ,  u['budget']['min'] ,u['budget']['max'] ,  u['rating'] , u['amenities'] )
        if(u['city']=='Bangalore'):
            ranked_filtered_idxs = filter_data.filter_data('banglore/BasicRankedHotelsBangalore.csv' , 'basic_ranked_datasets' ,  u['budget']['min'] ,u['budget']['max'] ,  u['rating'] , u['amenities'] )
        print(ranked_filtered_idxs)
        # jsonn = dict()
        # for e in range(len(ranked_filtered_idxs)):
        #     jsonn[e] = str(ranked_filtered_idxs[e])
        return {'ranked_filtered_idxs': str(ranked_filtered_idxs)}
        # return jsonn


@app.route('/similarity', methods = ['POST'])
def similarity():
    if request.method == 'POST':
        u = request.get_json()
        print(u)
        u['selected_indexes']
        u['all_indexes']
        not_selected = list()
        for ele in u['all_indexes']:
            if ele not in u['selected_indexes']:
                not_selected.append(ele)
        if(u['city']=='Delhi'):
            similar_images_index_list = SimilarImages.find_similar(u['selected_indexes'],3,'delhi_dataset')
        if(u['city']=='Goa'):
            similar_images_index_list = SimilarImages.find_similar(0,3,'goa_dataset')
        if(u['city']=='Bangalore'):
            similar_images_index_list = SimilarImages.find_similar(0,3,'bangalore_dataset')
        print(similar_images_index_list)
        return {'similar_images_indexes': similar_images_index_list}


@app.route('/top_100', methods = ['POST'])
def ranked():
    if request.method == 'POST':
        u = request.get_json()
        print(u)
        similar_images_index_list = SimilarImages.find_similar(0,3,'goa_dataset')
        print(similar_images_index_list)
        return {'similar_images_indexes': similar_images_index_list}
    


# main driver function
if __name__ == '__main__':
    app.run(host='192.168.53.147' , port=5001)
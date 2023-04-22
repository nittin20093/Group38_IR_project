from flask import Flask, redirect, url_for, request
import SimilarImages



app = Flask(__name__)

@app.route('/similarity', methods = ['POST'])
def similarity():
    if request.method == 'POST':
        u = request.get_json()
        print(u)
        similar_images_index_list = SimilarImages.find_similar(0,3,'goa_dataset')
        print(similar_images_index_list)
        return similar_images_index_list
 
# main driver function
if __name__ == '__main__':
    app.run(host='192.168.53.147' , port=5000)
import numpy as np
import pickle
import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow_datasets as tfds
import tensorflow_hub as hub
import functools
import os, os.path
import urllib.request
from PIL import Image
from sklearn.neighbors import NearestNeighbors
from annoy import AnnoyIndex

def forInputImages(Image_index,no_of_images,t):
  return t.get_nns_by_item(Image_index,no_of_images)

def find_similar(target_photo_index , no_of_images_to_find_similar , pickle_data_file_name):
  dbfile = open('./home/'+pickle_data_file_name, 'rb')     
  dataset = pickle.load(dbfile)

  t = AnnoyIndex(1536, metric='angular')
  # t = AnnoyIndex(1536, metric='cosine')

  for i,j in dataset.items():
    t.add_item(i,j[0])

  t.build(len(dataset))

  ans=forInputImages(target_photo_index, no_of_images_to_find_similar, t)
  dbfile.close()
  return ans
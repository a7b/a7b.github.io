import os
import json

# specify your path
path = 'images/pictures/'

image_files = [f for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png')]

with open('pictures.json', 'w') as json_file:
    json.dump(image_files, json_file)
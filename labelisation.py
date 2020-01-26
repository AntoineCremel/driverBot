#!/usr/bin/python3

import os
import json
from PIL import Image

data_dir = "lane_images"

# First, read the dictionnary that we have already created
dic_file_name = os.path.join(data_dir, "labels.json")
with open(dic_file_name, 'r') as dic_file:
	label_dic = json.load(dic_file)

file_list = os.listdir(data_dir)
print(file_list)
for file_name in file_list:
	if not file_name in label_dic.keys():
		# Open and show the image
		image_file_name = os.path.join(data_dir, file_name)
		image = Image.open(image_file_name)
		image.show()
		# Save the label to the dic
		label = input("What label do you wish to give to this image? F, R, L, B for directon labels, X to quit ")
		if label in ['F', 'R', 'L', 'B']:
			label_dic[file_name] = label
		elif label == 'X':
			break
		else:
			print("Incorrect label.", label, "given. Expected F, R, L or B. Moving on...")

print("Saving to", dic_file_name, "...")
with open(dic_file_name, 'w') as dic_file:
	json.dump(label_dic, dic_file, indent="\t", sort_keys=True)

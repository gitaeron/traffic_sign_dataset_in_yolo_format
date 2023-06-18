import os
import random
import shutil

DATASET_PATH = os.path.abspath(r"X:\X-Data\dataset\turn_right\turn_right")
# print(DATASET_PATH)


TRAIN_IMAGES_PATH = os.path.abspath(DATASET_PATH + "\\images\\train")
TRAIN_LABELS_PATH = os.path.abspath(DATASET_PATH + "\\labels\\train")
# print(TRAIN_IMAGES_PATH)
# print(TRAIN_LABELS_PATH)


VAL_IMAGES_PATH = os.path.abspath(DATASET_PATH + "\\images\\val")
VAL_LABELS_PATH = os.path.abspath(DATASET_PATH + "\\labels\\val")
# print(VAL_IMAGES_PATH)
# print(VAL_LABELS_PATH)


train_images_file_name = os.listdir(TRAIN_IMAGES_PATH)
train_labels_file_name = os.listdir(TRAIN_LABELS_PATH)
# print(train_images_file_name[255])
# print(train_labels_file_name[255])


amount_for_random = int(len(train_images_file_name) * 0.2)
# print(amount_for_random)


rand_idx_list = random.sample(range(0, len(train_images_file_name)-1), amount_for_random)
# print(rand_idx_list)

images_random_list = []
labels_random_list = []


for i in rand_idx_list:
    images_random_list.append(train_images_file_name[i])
    labels_random_list.append(train_labels_file_name[i])
# print(len(images_random_list))
# print(len(labels_random_list))


for i in range(amount_for_random):
    images_random_list[i] = os.path.abspath(TRAIN_IMAGES_PATH + "\\" + images_random_list[i])
# print(images_random_list[233])

for i in range(amount_for_random):
    labels_random_list[i] = os.path.abspath(TRAIN_LABELS_PATH + "\\" + labels_random_list[i])
# print(labels_random_list[233])


dst_images_path = VAL_IMAGES_PATH
dst_labels_path = VAL_LABELS_PATH
# print(dst_images_path)
# print(dst_labels_path)

for i in range(amount_for_random):
    shutil.move(images_random_list[i], dst_images_path)
    shutil.move(labels_random_list[i], dst_labels_path)



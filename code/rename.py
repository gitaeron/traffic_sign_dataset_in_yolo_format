import os

IMG_PATH = os.path.abspath(r"X:\X-Data\image")
LABEL_PATH = os.path.abspath(r"X:\X-Data\label")
print(IMG_PATH)
print(LABEL_PATH)


img_name_list = os.listdir(IMG_PATH)
label_name_list = os.listdir(LABEL_PATH)
print("="*50)
print("Test - 1")
print(img_name_list[23])
print(label_name_list[23])


img_file_path = []
for i in range(len(img_name_list)):
    tmp = os.path.abspath(IMG_PATH + "\\" + img_name_list[i])
    img_file_path.append(tmp)

label_file_path = []
for i in range(len(label_name_list)):
    tmp = os.path.abspath(LABEL_PATH + "\\" + label_name_list[i])
    label_file_path.append(tmp)

print("="*50)
print("Test - 2")
print(img_file_path[23])
print(label_file_path[23])


for i in range(len(img_file_path)):
    dst = os.path.abspath(IMG_PATH + "\\" + "turn_left_" + str(i+1) + ".jpg")
    os.rename(src=img_file_path[i], dst=dst)

for i in range(len(label_file_path)):
    dst = os.path.abspath(LABEL_PATH + "\\" + "turn_left_" + str(i+1) + ".txt")
    os.rename(src=label_file_path[i], dst=dst)

print("="*50)
print("After")

img_after = os.listdir(IMG_PATH)
label_after = os.listdir(LABEL_PATH)
print(img_after[0])
print(label_after[0])

# About this project

This project is a dataset of road traffic signs (straight, left turn, and right turn) created in the YOLO universal format.

Each folder directory is as follows:

- direct - dataset of straight traffic sign
- turn_left - dataset of left turn traffic sign
- turn_right - dataset of right turn traffic sign
- code - code related to dataset processing

Moreover, each dataset image within the subcategory directory only contains the corresponding traffic sign for the current classification. For example, each image in the 'direct' folder only contains a straight traffic sign and background, without any other objects added or annotated.

For more information, please check the direct/images folder.

---

## Directory structure

The folder structure of this dataset is as follows:

- direct
    - images
        - train
        - val
    - labels
        - train
        - val
    - classes.txt

The directory structure of the three folders 'direct', 'turn_left', and 'turn_right' are the same.

---

## Categories

There are three classes in the 'classes' section:

- direct
- turn_left
- turn_right

---

## dataset.yaml

The basic content is included in it. If you want to use it directly, please modify the 'path' to the relative or absolute path of your project.

> According to the official tutorial of yolov8, you can place this file anywhere. Just specify data=dataset.yaml in CLI or Python program.

---

## code

This folder contains the code written by myself when processing the dataset. Currently, two files are provided:

- random_dataset.py
    - This program divides dataset images in an 80%/20% ratio.

- rename.py
    - This program renames image and label files in a fixed format.

Regardless of which file is used, please make sure to modify it appropriately based on your understanding before using it.

---

# Contact

Aeron Atlantis - @Aeron.Atlantis@gmail.com -　[gitaeron.github.io](https://gitaeron.gtihub.io)

Project Link: https://github.com/gitaeron/gitaeron.github.io

# License

All contents of this project were taken, cleaned, and anonymized by myself and annotated by myself. If any part of the content (such as an image) infringes upon your legal rights, please contact me to have it removed. My contact information is at the end of this document.

This project is for educational purposes only and cannot be used for commercialization. We strongly oppose some individuals who repack and resell this project. If you encounter the above situation, please report it to the relevant platform and the platform where the content is resold. Please do not give money to these illegal resellers. Thank you for your cooperation.

> This project is owned by me and is licensed under CC BY NC. 
>
> Commercial use is prohibited! Commercial use is prohibited! Commercial use is prohibited!
>
> For details, please refer to License.md.

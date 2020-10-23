import argparse
import os
import sys
import numpy
import cv2
import glob

print("INFO : all the modules are imported.")

parser = argparse.ArgumentParser(description="This is a test which help you to know about the func")

parser.add_argument(
    "dataset",
    type=str,
    help="select the path to the folder of dataset", 
)

args = parser.parse_args()
print(args.dataset)

fruit_names = [
    'Apple Braeburn',
    'Apple Golden 1',
    'Apple Golden 2',
    'Apple Golden 3',
    'Apple Granny Smith',
    'Apple Red 1',
    'Apple Red 2',
    'Apple Red 3',
    'Apple Red Delicious',
    'Apple Red Yellow 1',
    'Apple Red Yellow 2',
    'Apricot',
    'Avocado',
    'Avocado ripe',
    'Banana',
    'Banana Lady Finger',
    'Banana Red',
    'Cactus fruit',
    'Cantaloupe 1',
    'Cantaloupe 2',
    'Carambula',
    'Cherry 1',
    'Cherry 2',
    'Cherry Rainier',
    'Cherry Wax Black',
    'Cherry Wax Red',
    'Cherry Wax Yellow',
    'Chestnut',
    'Clementine',
    'Cocos',
    'Dates',
    'Granadilla',
    'Grape Blue',
    'Grapefruit Pink',
    'Grapefruit White',
    'Grape Pink',
    'Grape White',
    'Grape White 2',
    'Grape White 3',
    'Grape White 4',
    'Guava',
    'Hazelnut',
    'Huckleberry',
    'Kaki',
    'Kiwi',
    'Kumquats',
    'Lemon',
    'Lemon Meyer',
    'Limes',
    'Lychee',
    'Mandarine',
    'Mango',
    'Mangostan',
    'Maracuja',
    'Melon Piel de Sapo',
    'Mulberry',
    'Nectarine',
    'Orange',
    'Papaya',
    'Passion Fruit',
    'Peach',
    'Peach 2',
    'Peach Flat',
    'Pear',
    'Pear Abate',
    'Pear Kaiser',
    'Pear Monster',
    'Pear Williams',
    'Pepino',
    'Physalis',
    'Physalis with Husk',
    'Pineapple',
    'Pineapple Mini',
    'Pitahaya Red',
    'Plum',
    'Plum 2',
    'Plum 3',
    'Pomegranate',
    'Pomelo Sweetie',
    'Quince',
    'Rambutan',
    'Raspberry',
    'Salak',
    'Strawberry',
    'Strawberry Wedge',
    'Tamarillo',
    'Tangelo',
    'Tomato 1',
    'Tomato 2',
    'Tomato 3',
    'Tomato 4',
    'Tomato Cherry Red',
    'Tomato Maroon',
    'Walnut'
]

image_path = args.dataset
print("INFO : Training image path is {}".format(image_path))

###########################################################################
#       saving the training data into the .npy file
###########################################################################
train_data = []
train_labels = []
train_lyf_names = []

for fruit in fruit_names :
    # print(fruit)
    folder_path = image_path
    # path = image_path + "Training" + fruit
    folder_path = os.path.join(image_path, "Training", fruit)   
    # just files name, not absolute path
    images = os.listdir(folder_path)

    for i in range(len(images)) :
        final_path = os.path.join(folder_path, images[i])
        img = cv2.imread(final_path, cv2.IMREAD_COLOR)
        dims = numpy.shape(img)
        img = numpy.reshape(img, (dims[2], dims[0], dims[1]))
        train_data.append(img)
        train_labels.append(fruit_names.index(fruit))
    print("INFO : {} is done! Label is {}".format(fruit, train_labels[-1]))
    
numpy_train_data = numpy.array(train_data)
print(numpy_train_data.shape)
numpy_train_labels = numpy.array(train_labels)
print(numpy_train_labels.shape)

print("OK: Training data is created.")
continue_or_not = input("Continue to save the data to .npy file? (y/n) : \n")
if continue_or_not == "y" :
    print("INFO : Begin saving image data into .npy file...")
else :
    print("INFO : Programme stop. Exit now...")
    eixt(0)

numpy.save("train_data.npy", train_data)
check_data = numpy.load("train_data.npy")
numpy.save("train_labels.npy", train_labels)
check_labels = numpy.load("train_labels.npy")

print("INFO : The train_data.npy shape is : {}".format(check_data.shape))
print("INFO : The train_labels.npy shape is : {}".format(check_labels.shape))

continue_or_not = input("OK : Training data is done. Continue to process test data? (y/n)\n")
if continue_or_not == "y" :
    print("Continue to process test data...")
else :
    print("Programme stopped. Exit now...")
    exit(0)

###########################################################################
#       saving the test data to .npy file
###########################################################################
test_data = []
test_labels = []
for fruit in fruit_names : 
    folder_path = os.path.join(image_path, "Test", fruit)
    images = os.listdir(folder_path)

    for i in range(len(images)) :
        final_path = os.path.join(folder_path, images[i])
        if not os.path.isfile(final_path):
            print("This path does not exist : {}".format(final_path))
            continue
        img = cv2.imread(final_path, cv2.IMREAD_COLOR)
        dims = numpy.shape(img)
        img = numpy.reshape(img, (dims[2], dims[0], dims[1]))
        test_data.append(img)
        test_labels.append(fruit_names.index(fruit))

test_data = numpy.array(test_data)
print("The test_data shape is : {}".format(test_data.shape))
test_labels = numpy.array(test_labels)
print("The test_labels shape is : {}".format(test_labels.shape))

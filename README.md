# What-s-the-Price

# Deep Learning Project: Retail image classification and regression
A quick guide on installation of important libraries and running the code.
The project has four .ipynb files - watch_classification.ipynb, regression_watch.ipynb, bags_classification and bags_regression.ipynb

## Libraries required for Classification and Regression
**Basic Libraries**
1. numpy
2. matplotlib
3. seaborn
4. cv2

**sklearn imports**

5. from sklearn.model_selection import train_test_split
6. from sklearn.metrics import classification_report, confusion_matrix

**tensorflow and keras**

7. import tensorflow as tf
8. from tensorflow.keras.preprocessing import image
9. from tensorflow.keras import Input, Model
10. from keras.models import Sequential
11. from keras.callbacks import EarlyStopping
12. from keras.layers import Dense, Dropout, Activation, Flatten, MaxPooling2D,AveragePooling2D, Conv2D, BatchNormalization, GlobalAveragePooling2D
13. from tensorflow.keras.applications import DenseNet121, DenseNet201, ResNet50, VGG19, InceptionV3, EfficientNetB7
14. from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
15. from tensorflow.keras.callbacks import EarlyStopping,ReduceLROnPlateau
16. from keras.metrics import AUC.

**others**

17. from random import randint
18. from tqdm import tqdm
19. from contextlib import suppress

## Watch and Bags Classification and Regression
Both of the classification and Regression ipynb files consists of 3 models each namely a Custom Model, InceptionV3 Transfer Learning model, DenseNet201 Transfer learning model. Thus in a way we trained 12 models for this project.

## How to use the project
We have built a streamlit application which takes an image input of a bag or a watch. The website then predicts the brand and the estimated price of the product given as input.
Note: Our models take a lot of space and hence the web application is about 2 to 3 GB. We are facing some storage issue while deploying it currently

## Problems and Challenges
<img width="955" alt="image" src="https://user-images.githubusercontent.com/46833935/168212252-db61ede6-65bb-463b-9003-f4b5d669110c.png">
<img width="837" alt="image" src="https://user-images.githubusercontent.com/46833935/168212272-669e6447-0d40-4426-8414-eb702c541920.png">
<img width="799" alt="image" src="https://user-images.githubusercontent.com/46833935/168212296-6a002c1a-4c1d-424a-b68a-0ede8f94a833.png">

## Lessons Learned and Perspectives

To create efficient models , it is important to have good quality data. Maybe more in-depth pre-processing techniques could help improve the model performance.

1. Image Data Generator helps reduce overfitting our data.
2. Using complex models will improve performance but needs more computation power and might not always be the best solution.
3. Image regression for price prediction is a difficult task when you have many unique price points. Regression may be improved if we put prices range in various categorical bins.

## Contributors
© Sameer Mahajan © Harsh Deokuliar

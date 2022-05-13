{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4a8b3fb6",
   "metadata": {},
   "source": [
    "# Deep Learning Project: Retail image classification and regression\n",
    "\n",
    "**Version 1.0.0**\n",
    "\n",
    "A quick guide on installation of important libraries and running the code.\n",
    "\n",
    "The project has four .ipynb files - watch_classification.ipynb, regression_watch.ipynb, bags_classification and bags_regression.ipynb\n",
    "\n",
    "## Libraries required for Classification and Regression\n",
    "\n",
    "**Basic Libraries**\n",
    "1. numpy\n",
    "2. pandas\n",
    "3. matplotlib.pyplot\n",
    "4. import seaborn as sns\n",
    "5. import cv2\n",
    "\n",
    "**slearn libraries**<br/>\n",
    "6. from sklearn.model_selection import train_test_split<br/>\n",
    "7. from sklearn.metrics import classification_report, confusion_matrix<br/>\n",
    "\n",
    "**tensorflow and keras**<br/>\n",
    "8. import tensorflow as tf<br/>\n",
    "9. from tensorflow.keras.preprocessing import image<br/>\n",
    "10. from tensorflow.keras import Input, Model<br/>\n",
    "11. from keras.models import Sequential<br/>\n",
    "12. from keras.callbacks import EarlyStopping<br/>\n",
    "13. from keras.layers import Dense, Dropout, Activation, Flatten, MaxPooling2D,AveragePooling2D, Conv2D, BatchNormalization, GlobalAveragePooling2D<br/>\n",
    "14. from tensorflow.keras.applications import DenseNet121, DenseNet201, ResNet50, VGG19, InceptionV3, EfficientNetB7<br/>\n",
    "15. from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img<br/>\n",
    "16. from tensorflow.keras.callbacks import EarlyStopping,ReduceLROnPlateau<br/>\n",
    "17. from keras.metrics import AUC.<br/>\n",
    "\n",
    "**others**<br/>\n",
    "18. from random import randint<br/>\n",
    "19. from tqdm import tqdm<br/>\n",
    "20. from contextlib import suppress<br/>\n",
    "\n",
    "## Watch and Bags Classification  and Regression\n",
    "Both of the classification and Regression ipynb files consists of 3 models each namely a Custom Model, InceptionV3 Transfer Learning model, DenseNet201 Transfer learning model. Thus in a way we trained 12 models for this project.\n",
    "\n",
    "## How to use the project\n",
    "We have built a streamlit application which takes an image input of a bag or a watch. The website then predicts the brand and the estimated price of the product given as input.\n",
    "\n",
    "> **Note:** Our models take a lot of space and hence the web application is about 2 to 3 GB. We are facing some storage issue while deploying it currently\n",
    "\n",
    "\n",
    "## Contributors\n",
    "\n",
    "© Sameer Mahajan\n",
    "© Harsh Deokuliar\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ab33b1f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.7 64-bit ('base': conda)",
   "language": "python",
   "name": "python397jvsc74a57bd03121fd09dad9126b26dc57210f7bcfce9b3a245856eab5b71ab58cb3a561abb2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

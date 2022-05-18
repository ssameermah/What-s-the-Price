# What-s-the-Price

# Deep Learning Project: Retail image classification and regression
A quick guide on installation of important libraries and running the code.
The project has four .ipynb files - watch_classification.ipynb, regression_watch.ipynb, bags_classification and bags_regression.ipynb

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

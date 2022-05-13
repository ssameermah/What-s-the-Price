import streamlit as st
from PIL import Image
from run_models import watch_classification, watch_regression, bags_classification, bags_regression


st.set_page_config(layout="wide")

header = st.container()
dataset = st.container()
testing = st.container()
 
with header:
    st.title('Deep Learning Project: What Product is that?')
    st.header('What\'s in it for you?')
    st.text('Most of the times we see someone having a particular watch or handbag and we instantly want to know what brand and price that product might be.')
    st.text('This idea motivated us to build this project where you can upload the product image and get its brand and price estimate!')

with dataset:
    st.header('Datasets')
    st.text('In this project we have used more than 31000 images and there prices that were scraped from websites such as Redbag.com which was used for handbags and chrono24.com which was used to collect watches ')
    st.text('After getting all the data , the data for further filtered based on the number of images in each class( min 300 images). After filtering , we got 8 classes for handbags and 5 classes for watches.')
    st.text('Imbalanced data was handled by up sampling minority classes using the albuminations library, which is used to create augmentations. Using this we up sampled images to get a balanced dataset.')
    st.text('We added augmentations like rotate, horizontal flip and transpose to balance the data.')
    st.text('The ImageDataGenerator from Keras was also used to train the models')

with testing:
    st.header('Time to Test our model!')
    st.text("Upload an image of a handbag or a Watch")
    product_type = st.radio(
     "What is your product?",
     ('Watch', 'Handbag'))
    if product_type == 'Watch':
        watch_file = st.file_uploader("Choose a Watch image", type="png")
    else:
        bag_file = st.file_uploader("Choose a Handbag image", type="jpg")

    watch_col, bags_col = st.columns(2)
    



    if product_type == 'Watch':
        if watch_file is not None:
            image = Image.open(watch_file)
            watch_col.text('Getting Predictions for Watches')
            watch_col.image(image, caption='Uploaded Watch.', use_column_width=False)
            watch_col.write("")
            watch_col.write("Predicting...")
            # label = teachable_machine_classification(image, 'brain_tumor_classification.h5')
            # if label == 0:
            #     watch_col.write("The MRI scan has a brain tumor")
            # else:
            #     watch_col.write("The MRI scan is healthy")
    else:
        if bag_file is not None:
            image = Image.open(bag_file)
            watch_col.text('Getting Predictions for Handbag')
            watch_col.image(image, caption='Uploaded Handbag.', use_column_width=False)
            watch_col.write("")
            watch_col.write("Predicting...")

        # # uploaded_file = bags_col.file_uploader("Choose a brain MRI ...", type="jpg")
        # if uploaded_file is not None:
        #     image = Image.open(uploaded_file)
        #     bags_col.text('I am bags colum')
        #     bags_col.image(image, caption='Uploaded MRI.', use_column_width=True)
        #     bags_col.write("")
        #     bags_col.write("Classifying...")
        #     label = teachable_machine_classification(image, 'brain_tumor_classification.h5')
        #     if label == 0:
        #         bags_col.write("The MRI scan has a brain tumor")
        #     else:
        #         bags_col.write("The MRI scan is healthy")
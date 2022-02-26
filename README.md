# Disaster Response Pipeline Project
![intro](https://user-images.githubusercontent.com/23631502/155820090-914027b9-480c-4855-bfae-cf36a7dcc388.png)


### Summary:
This is a web application written in python to automatically classify text messages into different categories of disaster management. Furthermore, two visualizations from the data set are available as examples.
The project consists of 3 areas. 
1. ETL pipeline (process_data.py) to cleans data and store data for further processing
2. ML pipeline (train_classifier.py) to train and save a classifier model
3. Flask web app (run.py) for interactive classification based on trained model of arbitary text data and visualisations of some data

### Requierments:
You need following python packages: 
* flask
* plotly
* sqlalchemy
* pandas
* numpy
* sklearn
* nltk

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/


### Screenshots:
![sample_input](https://user-images.githubusercontent.com/23631502/155820148-420df3df-c874-4872-9257-463a92b2d2bc.png)
![sample_output](https://user-images.githubusercontent.com/23631502/155820162-c44d52c1-271f-458c-91b5-de12470e9597.png)
![main_page](https://user-images.githubusercontent.com/23631502/155820168-6eb0833a-69e1-40c7-af55-9de809cbfdf9.png)
![main_page (1)](https://user-images.githubusercontent.com/23631502/155820170-e56a3205-dea5-4e91-ba45-ae9988f1db86.png)
![main_page (2)](https://user-images.githubusercontent.com/23631502/155820175-75c85d8d-b36e-4e30-90b4-710a66037993.png)
![process_data](https://user-images.githubusercontent.com/23631502/155820183-5bef17b7-85c1-4281-afc4-32e5043f4229.png)
![train_classifier](https://user-images.githubusercontent.com/23631502/155820188-1e9e548c-b5fa-4667-b6e9-4f5e99db2bd8.png)
![train_classifier_category_precision_recall](https://user-images.githubusercontent.com/23631502/155820192-fafec84b-f488-4ba2-84c4-4f1867190f2d.png)

# imdb-movie-recommender
End to end ML project deployed on Azure cloud (Data Gathering/Building Solution/Deployment). 

PART 1: Data Scraping

Data was scraped from IMDB website(using beautiful-soup library). Refer <a href="https://github.com/ujoshidev/imdb-movie-recommender/blob/main/data_scrapper.py" target="_blank"><strong>data_scrapper.py script</strong></a> in this repository. This dataset consists of top 1000 movies (user configurable) based on popularity.

PART 2: Creating a Content Based Recommendation system

Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback. Refer <a href="https://github.com/ujoshidev/imdb-movie-recommender/blob/main/recommender.py" target="_blank"><strong>recommender.py</strong></a> in this repository.

PART 3: Frontend creation for model serving

I have created a frontend using streamlit. This web-interface fetches input from the user and provides top 5 similar movies based on the input. This is all done with the help of recommendation system that we have created in the above step.

STEP 4: Model Deployment

Created model has been containerized using docker and its been pushed to container repository. Its then deployed Azure cloud services. This is helpful to manage and increase scalability of the application.

![image](https://user-images.githubusercontent.com/25796899/154909314-72d45122-2e7a-4e00-a632-bff74495f42a.png)


Click <a href="https://imdb-movie-recommender.azurewebsites.net/" target="_blank"><strong>HERE</strong></a> to acess application UI. 


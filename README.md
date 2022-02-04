# NLP_SDLC_project
This is my project for the SDLC practice (5th semester) part at UCU

The main idea behind this project is about development of an efficent news classification model, able to label future streams of news with sufficient accuracy.
It is important to mention that the project is trying to resolve a multiclass classification problem.

## Data overview

### Data structure
The main dataset is retrieved in .json format from the following [source](https://www.kaggle.com/rmisra/news-category-dataset).
Data preprocessing was done majorly with *pandas* (although there were some manual fixes done to the structure of an initial file in order to properly parse the .json file),
dataset was presented as pandas.DataFrame.
Each data point (each row) of the dataset is represented by:
- **category** it belongs to, *category* column;
- **headline**, a sentence describing the main event of the news, *headline* column;
- **authors** who took part in writing the news, *authors* column;
- **link** to the original news source, *link* column;
- **short description** of the news, a text of 2 sentences on average, *short_description* column;
- **date** which the given news relates to, *date* column;

### News distribution
A total of 200853 news are in the dataset

#### Across categories
It is important to mention that there are 41 different news categories, moreover, as the below graphs shows, their distribution is far from equal, which might be a problem for some classifiers.
![Bar plot in descending order, the largest categories are: POLITICS, WELLNESS, ENTERTAINMENT](https://github.com/romapavelko01/NLP_SDLC_project/blob/main/EDA/cats_distribution_SNS.png)


#### Across time
Unlike per-category news distribution, the distribution across time (more specifically, time period from 28th January, 2012 up to 26th May, 2018) seems to be a bit more linearly stable, despite the spike in the beginning and fall in the ending parts of the graph.
![\---/-like distribution across time](https://github.com/romapavelko01/NLP_SDLC_project/blob/main/EDA/date_distribution_SNS.png)

### The most common words per category
For this part, I have decided to use *wordcloud* visualisations for the three largest (by number of news) categories; 
each wordcloud contains up to 100 words, where the bigger words correspond to their higher frequency for news of specific category

**NOTE** Since across the entire dataset there are a lot of words which are used in literally any sentence, such as 'he', 'will', 'their', 'can', 'with' and many others, aka the ***stopwords***, they had to be removed in order to draw more significant insights about most common words for each of the categories

**Wordcloud for Politics news:**
<p align="center">
  <img src="https://github.com/romapavelko01/NLP_SDLC_project/blob/main/EDA/POLITICS_wordcloud_100_words.JPEG" width="750" height="450" />
</p>


**Wordcloud for Entertainment news:**
<p align="center">
  <img src="https://github.com/romapavelko01/NLP_SDLC_project/blob/main/EDA/ENTERTAINMENT_wordcloud_100_words.JPEG" width="750" height="450" />
</p>


**Wordcloud for Wellness news:**
<p align="center">
  <img src="https://github.com/romapavelko01/NLP_SDLC_project/blob/main/EDA/WELLNESS_wordcloud_100_words.JPEG" width="750" height="450" title="Wordcloud for Wellness news:"/>
</p>

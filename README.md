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
![Bar plot in descending order, the largest categories are: POLITICS, WELLNESS, ENTERTAINMENT](EDA/cats_distribution_SNS.png)


#### Across time
Unlike per-category news distribution, the distribution across time (more specifically, time period from 28th January, 2012 up to 26th May, 2018) seems to be a bit more linearly stable, despite the spike in the beginning and fall in the ending parts of the graph.
![\---/-like distribution across time](EDA/date_distribution_SNS.png)

### The most common words per category
For this part, I have decided to use *wordcloud* visualisations for the three largest (by number of news) categories; 
each wordcloud contains up to 100 words, where the bigger words correspond to their higher frequency for news of specific category

**NOTE** Since across the entire dataset there are a lot of words which are used in literally any sentence, such as 'he', 'will', 'their', 'can', 'with' and many others, aka the ***stopwords***, they had to be removed in order to draw more significant insights about most common words for each of the categories

**Wordcloud for Politics news:**
<p align="center">
  <img src="EDA/POLITICS_wordcloud_100_words.JPEG" width="750" height="450" />
</p>


**Wordcloud for Entertainment news:**
<p align="center">
  <img src="EDA/ENTERTAINMENT_wordcloud_100_words.JPEG" width="750" height="450" />
</p>


**Wordcloud for Wellness news:**
<p align="center">
  <img src="EDA/WELLNESS_wordcloud_100_words.JPEG" width="750" height="450" title="Wordcloud for Wellness news:"/>
</p>

## Classifications with Machine Learning models

For this, I decided to first work with text data from only the top 5 most frequent news categories, and then with data from all categories.

### What classification was made on
Since the goal was to develop the most efficient model possible, I decided to track the performance of classification made 
both on *preprocessed* and *raw* data, and or any type of text data available, that is: 
* news article body from *short_description* column;
* news article headline from *headline* column;
* combined text data from *short_descrption* and *headline* from separate *full_text* column;

### Data preprocessing
Models, trained on preprocessed data, needed to have the text data processed in some way. 

First of all, it was important to remove words that are used in almost any sentence, such as 'the', 'a', 'and', 'is', etc.
The reason is simple, they carried much weight in each category, making some category-spesific words relatively invisible.
These are the so called ***stopwords***, and, hopefully, Python library named **nltk** provides a possibility for such operations
in the form of a specific set of stopwords. Each piece of text data in the columns specified above was transformed to lower-case and stopwords were removed from it.

Then, I made sure any numeric and non-alphanumeric symbols were removed too. Examples of such symbols are punctuation symbols, '$', '#' and others that might make the data noisy. 

### Vectorization
Machine learning models heavily rely on numerical data, or at least categorical. However, when in our case we have a total of thousands of unique words,
it makes sense to convert text data to some model-friendly format. This can be done with the technique called ***vectorization***, which is basically a numerical
representation of text.

For this project I mainly focused on 2 types of vectorizers, available in the *sklearn*:
* CountVectorizer
* TfidfVectorizer

**CountVectorizer** is the so called *bag-of-words* - that represents each word as the number of times it appears in the documents. CountVectorizer converts
collection of text documents to a matrix of token counts.

**TfidfVectorizer** - from **TF-IDF**, `Term Frequency x Inverse Document Frequency`, which multiplies the term frequency in specific document *d* by the inverse document frequency, the log of (number of documents/(number of documents that have a token *t* + 1)), in such a way discarding the importance of very frequent words - converts a collection of raw documents to a matrix of TF-IDF features.


**NOTE:** Since both vectorizers can be specified with what stopwords to use (parameter `stop_words`), I still decided to go with the `nltk`'s set, since it has more words.

Also, as for checking performance, I decided to let the vectorizers analyze different word combinations, by setting `ngram_range` parameter to specific tuple values:
* (1, 1) lets the vectorizer analyze singe words only, the so called *Unigrams*
* (1, 2) lets the vectorizer analysze both single words and word pairs, *Unigrams* and *Bigrams*
* (2, 2) lets the vectorizer analyze word pair only, the *Bigrams*

! vectorizers do have the possibility to remove stopwords !


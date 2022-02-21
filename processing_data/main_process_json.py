"""
Module for processing json-file and performing slight EDA
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import STOPWORDS, WordCloud

df = pd.read_json('data/final_news_category_dataset.json', orient='split')


freq_by_cats = df.category.value_counts()
labels, y = freq_by_cats.index, freq_by_cats.values
x = list(range(1, len(labels) + 1))

# print(df.head())

BUILD_GRAPH_CATS = True  # this and some other name-capitalized boolean variables are used to
# run the processes all in one .py file; by switching the values from True to False, we disable to run
# the entire script
SNS = True
if BUILD_GRAPH_CATS:
    if not SNS:
        plt.figure(figsize=(15, 5))
        plt.bar(x, y)
        for label, x_, y_ in zip(labels, x, y):
            plt.text(x_, y_, label, rotation='vertical')
        plt.xticks([])
        plt.savefig("EDA/news_category_distibution.png")

    else:
        def show_values_on_bars(axs, h_v="v", space=0.4):
            """
            Function for giving labels to the bars
            :param axs: matplotlib.figure.Figure
            :param h_v: str
            :param space: float
            :return: None
            """

            def _show_on_single_plot(ax):
                if h_v == "v":
                    for p in ax.patches:
                        _x = p.get_x() + p.get_width() / 2
                        _y = p.get_y() + p.get_height()
                        value = int(p.get_height())
                        ax.text(_x, _y, value, ha="center")
                elif h_v == "h":
                    for p in ax.patches:
                        _x = p.get_x() + p.get_width() + float(space)
                        _y = p.get_y() + p.get_height()
                        value = int(p.get_width())
                        ax.text(_x, _y, value, ha="left")

            if isinstance(axs, np.ndarray):
                for idx, ax in np.ndenumerate(axs):
                    _show_on_single_plot(ax)
            else:
                _show_on_single_plot(axs)


        plt.figure(figsize=(15, 5))
        sns.set_theme(style='whitegrid')
        ax = sns.barplot(x=x, y=y, orient='v', dodge=True)
        for p, label in zip(ax.patches, labels):
            ax.annotate(label, (p.get_x() + p.get_width() / 2, p.get_height()),
                        ha='center', va='center', xytext=(0, 9), textcoords='offset points',
                        rotation=45.0, fontsize=8.0)
        ax.set(xticklabels=[])
        # plt.show()
        plt.savefig('EDA/cats_distribution_SNS.png')


BUILD_GRAPH_DATE = False

if BUILD_GRAPH_DATE:
    freq_by_date = df.date.value_counts()
    freq_by_date = freq_by_date.resample('M').sum()
    dt_x = freq_by_date.index
    dt_y = freq_by_date.values
    plt.figure(figsize=(17, 7))
    if SNS:
        sns.set_theme(style='whitegrid')
        dt_ax = sns.lineplot(dt_x, dt_y)
        dt_ax.set(title="Monthly distribution of news across time", ylabel="Number of news")

        plt.savefig("EDA/date_distribution_SNS.png")
    else:
        pass

###  wordcloud for short_description

BUILD_WORD_CLOUD = False

if BUILD_WORD_CLOUD:
    ctg_set = ['POLITICS', 'WELLNESS', 'ENTERTAINMENT']
    for ctg in ctg_set:
        adj_df = df[df['category'] == ctg]
        texts = adj_df.short_description.values
        cv = CountVectorizer()
        cv_fit = cv.fit_transform(texts)
        word_list = cv.get_feature_names()
        count_list = cv_fit.toarray().sum(axis=0)
        freq_zip = zip(word_list, count_list)
        final_freq_zip = list()
        for word, count in freq_zip:
            if word not in STOPWORDS:
                final_freq_zip.append((word, count))

        # the below script creates a descendingly sorted by values dict of the most frequent words by category
        # and also saves a beautiful wordcloud visualisation
        top_100_words = sorted(final_freq_zip, key=lambda par: par[1], reverse=True)[:100]
        top_100_dict = dict(top_100_words)
        wc_100 = WordCloud(width=900, height=500, max_words=1628, relative_scaling=1,
                           normalize_plurals=False).generate_from_frequencies(top_100_dict)
        plt.imshow(wc_100)
        plt.axis('off')
        plt.savefig(f'UPD_EDA/{ctg}_wordcloud_100_words.JPEG', quality=95, dpi=300, bbox_inches='tight', pad_inches=0)
    # print(dict(top_20_words))

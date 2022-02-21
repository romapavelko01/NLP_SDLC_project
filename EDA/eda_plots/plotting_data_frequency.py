import json
import matplotlib.pyplot as plt
from datetime import datetime


f = open('data/final_news_category_dataset.json')
data = json.load(f)["data"]

# dict_keys(['category', 'headline', 'authors', 'link', 'short_description', 'date'])
# print(data[0]['date']) - 2018-05-26 - year-month-day

# print(len(data)) #
## - 200853 total rows of news
dates_arr = sorted([datetime.strptime(i['date'], '%Y-%m-%d') for i in data])
# print(f"News flow begins at {str(dates_arr[0])} and ends at {str(dates_arr[-1])}")
## - News flow begins at 2012-01-28 00:00:00 and ends at 2018-05-26 00:00:00

# count_dict = dict()
# day_dict = dict()
# year_month_dict = dict()
# year_dict = dict()
# for i in data:
#     date = datetime.strptime(i['date'], '%Y-%m-%d')
#     day, month, year = date.day, date.month, date.year
#     month_year = str(year) + '-' + str(month)
#     if year not in year_dict:
#         year_dict[year] = 0
#     if month_year not in year_month_dict:
#         year_month_dict[month_year] = 0
#     if i["category"] not in count_dict:
#         count_dict[i["category"]] = 0
#     if i['date'] not in day_dict:
#         day_dict[i['date']] = 0
#     count_dict[i["category"]] += 1
#     day_dict[i['date']] += 1
#     year_month_dict[month_year] += 1
#     year_dict[year] += 1
# #
# #
# catg_labels = [key for key in count_dict.keys()]
# x_index_catg_arr = list(range(1, len(catg_labels) + 1))
# y_catg_arr = [value for value in count_dict.values()]
#
# day_dict = {k: v for k, v in sorted(day_dict.items(), key=lambda item: item[0])}
# day_labels = [day for day in day_dict.keys()]
# x_index_day_arr = list(range(1, len(day_labels) + 1))
# y_day_arr = [value for value in day_dict.values()]
#
# year_month_dict = {k: v for k, v in sorted(year_month_dict.items(), key=lambda item: item[0])}
# year_month_labels = [key for key in year_month_dict.keys()]
# x_index_ym_arr = list(range(1, len(year_month_labels) + 1))
# y_ym_arr = [value for value in year_month_dict.values()]
#
#
# year_dict = {k: v for k, v in sorted(year_dict.items(), key=lambda item: item[0])}
# year_labels = [key for key in year_dict.keys()]
# x_index_year_arr = year_labels.copy()
# y_year_arr = [value for value in year_dict.values()]
#
# plt.figure(figsize=(15, 5))
#
# plt.subplot(4, 1, 1)
# plt.bar(x_index_catg_arr, y_catg_arr)
# for index, (x, y) in enumerate(zip(x_index_catg_arr, y_catg_arr)):
#     plt.text(x, y, catg_labels[index], rotation=90)
# plt.ylabel("Number of news")
# plt.xlabel("Categories")
#
#
# plt.subplot(4, 1, 2)
# plt.bar(x_index_day_arr, y_day_arr)
# # for index, (x, y) in enumerate(zip(x_index_catg_arr, y_catg_arr)):
# #     plt.text(x, y, catg_labels[index], rotation=90)
# plt.ylabel("Number of news")
# plt.xlabel("Days")
#
#
# plt.subplot(4, 1, 3)
# plt.bar(x_index_ym_arr, y_ym_arr)
# # for index, (x, y) in enumerate(zip(x_index_catg_arr, y_catg_arr)):
# #     plt.text(x, y, catg_labels[index], rotation=90)
# plt.ylabel("Number of news")
# plt.xlabel("Year-month")
#
# plt.subplot(4, 1, 4)
# plt.bar(x_index_year_arr, y_year_arr)
# # for index, (x, y) in enumerate(zip(x_index_year_arr, y_year_arr)):
# #     plt.text(x, y, year_labels[index])
# plt.ylabel("Number of news")
# plt.xlabel("Year")
#
# plt.show()


# spec_date = datetime.strptime(data[0]['date'], '%Y-%m-%d')
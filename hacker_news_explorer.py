"""
Hacker News Explorer
Author : Vignesh A

This module is used to explore and analyse the Hacker News Feeds
"""
import csv
import datetime as dt

with open("HN_posts_year_to_Sep_26_2016.csv", "r+", encoding="utf-8") as fp:
    hn = csv.reader(fp)

    hn = list(hn)

header = hn[0]

hn = hn[1:]

ask_posts, show_posts, other_posts = [], [], []

for row in hn:
    title = row[1]

    if title.lower().startswith("ask hn"):
        ask_posts.append(row)
    elif title.lower().startswith("show hn"):
        show_posts.append(row)
    else:
        other_posts.append(row)

total_ask_comments = 0

for row in ask_posts:
    num_comments = row[4]

    if num_comments != "":
        num_comments = int(num_comments)
    else:
        num_comments = 0
    total_ask_comments += num_comments

avg_ask_comments = total_ask_comments / len(ask_posts)

print(avg_ask_comments)

total_show_comments = 0

for row in show_posts:
    num_comments = row[4]

    if num_comments != "":
        num_comments = int(num_comments)
    else:
        num_comments = 0
    total_show_comments += num_comments

avg_show_comments = total_show_comments / len(show_posts)

print(avg_show_comments)

if avg_ask_comments < avg_show_comments:
    print("Show Posts receive more comments on an average")
elif avg_ask_comments > avg_show_comments:
    print("Ask Posts receive more comments on an average")
else:
    print("Both Posts receive same number of comments on an average")

result_list = []

for post in ask_posts:
    created_at = post[6]

    num_comments = post[4]

    if num_comments != "":
        num_comments = int(num_comments)
    else:
        num_comments = 0

    result_list.append([created_at, num_comments])

counts_by_hour = {}
comments_by_hour = {}

for result in result_list:
    created_at = result[0]

    created_at = dt.datetime.strptime(created_at, "%m/%d/%Y %H:%M")

    hour = created_at.strftime("%H")

    if hour not in counts_by_hour:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = result[1]
    else:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += result[1]

avg_by_hour = []

for hour in comments_by_hour:
    avg_by_hour.append([hour, comments_by_hour[hour] / counts_by_hour[hour]])

swap_avg_by_hour = []

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])

sorted_swap = sorted(swap_avg_by_hour, reverse=True)

print("Top 5 hours for Ask Posts Comments")

for row in sorted_swap[:5]:
    print("{}:00: {:.2f} average comments per post".format(row[1], row[0]))




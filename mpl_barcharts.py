#import csv
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# with open('data.txt') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     prog_langs = list(r["LanguagesWorkedWith"].split(";") for r in csv_reader)

prog_langs = pd.read_csv('data.txt')["LanguagesWorkedWith"]

lang_freqs =  Counter(list(l for lang_list in prog_langs for l in lang_list.split(";")))
languages, popularity = zip(*lang_freqs.most_common(15))

plt.barh(languages[::-1], popularity[::-1])

plt.title("Most Popular Languages")
#plt.ylabel("Programming Languages")
plt.xlabel("Number of Users")

plt.tight_layout()

plt.show()
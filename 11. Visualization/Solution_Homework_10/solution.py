import pandas as ps
import numpy as np
from matplotlib import pyplot as plt

# 1.a
data = ps.read_csv('imdb_top_10000.csv', sep='\t')
data = data.dropna()
print(data.shape[0])

# 1.b
data['runtime'] = [int(r.split(' ')[0]) for r in data['runtime']]

# 1.c
# prepare the splits
sp = [r.split('|') for r in data['genres']]

# get unique genres
genres = np.unique(sum(sp, [])).tolist()

# create columns
for g in genres:
    data[g] = [g in s for s in sp]

# delete the column
del data['genres']

# 1.d
# print statistics
print(data[['runtime', 'score', 'votes', 'year']].describe())

# select rows with non zero runtime
data = data[data['runtime']>=0.1]

# 1.e
# plot a histogram of the movies per year
cm = plt.cm.get_cmap('RdYlBu_r')

n, bins, patches = plt.hist(data['year'], bins=np.arange(1950, 2013), label=['Movie count'], color='#cccccc')
col = (n-n.min())/(n.max()-n.min())
plt.legend()
plt.ylim([0, 600])
plt.xlabel('Release Year')
plt.ylabel('# of instances')
for c, p in zip(col, patches):
    plt.setp(p, 'facecolor', cm(c))
plt.savefig('1.e.png')
plt.show()

# 1.g
# obtain yearly means of scores
year_mean = data.groupby(data['year'])['score'].mean()

# produce the plot
plt.clf()
t = data['score']
plt.scatter(data['year'], data['score'], alpha=0.1, c=t, cmap='viridis', label='Score data')
plt.plot(year_mean.index, year_mean.values, color='black', label='Score means')
plt.xlabel("Year")
plt.ylabel("IMDB Rating")
plt.legend()
plt.savefig('1.g.png')
plt.show()

# 1.7
print(data[data.score == data.score.min()][['title', 'score']])
print(data[data.score == data.score.max()][['title', 'score']])
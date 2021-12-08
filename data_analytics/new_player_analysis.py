#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !{sys.executable} -m pip install tensorflow
import sys

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
import keras
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer, StandardScaler
from sklearn.cluster import KMeans

from sklearn.decomposition import PCA
from sklearn import metrics

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout


def main(input1, input2, new_name, output):
    # nba_data = pd.read_csv('output_tmp1/part-00000-2948d5f4-25b2-45e0-a545-48869c80843b-c000.csv')
    nba_data = pd.read_csv(input1 + '/part-00000-2948d5f4-25b2-45e0-a545-48869c80843b-c000.csv')

    # In[2]:

    nba_data.head()
    nba_data.describe()
    nba_data.isnull().sum()
    nba_data = nba_data.fillna(0)
    print("how many rows contain NA: %s" % nba_data.isnull().sum().sum())
    # nba_data.isnull().sum()

    # In[3]:

    # newest year undrafted percent
    sns.barplot(y=nba_data.loc[nba_data.year == 2020].draft_year.value_counts().index,
                x=nba_data.loc[nba_data.year == 2020].draft_year.value_counts())
    total_players = len(nba_data.loc[nba_data.year == 2020].player_name.unique())
    undrafted_players = len(
        nba_data.loc[(nba_data.year == 2020) & (nba_data.draft_year == 'Undrafted')].player_name.unique())
    undrafted_percent = 100 * (undrafted_players / total_players)
    print("In 2020, %s of players were undrafted" % undrafted_percent)
    plt.savefig(output + '/draft_year.png')

    # In[4]:

    # since 60 players are selected in each draft. We replaced the undrafred string to 61
    nba_data['draft_number'].replace('Undrafted', value=61, inplace=True)
    nba_data['draft_round'].replace('Undrafted', value=2, inplace=True)

    def fx(x):
        if x['draft_year'] == 'Undrafted':
            return x['year']
        else:
            return x['draft_year']

    nba_data['draft_year'] = nba_data.apply(lambda x: fx(x), axis=1)
    nba_data['diff_year'] = nba_data.year - nba_data.draft_year.astype(int)
    # nba_data['position']=pd.factorize(nba_data['player_position'])[0]+1
    # nba_data['draft_number']= pd.to_numeric(nba_data['draft_number'])

    drop = ['TEAM_ID', 'player_name', 'team_abbreviation', 'draft_year', 'PLAYER_ID', 'year', 'player_position', 'age',
            'draft_round', 'diff_year', 'draft_number']
    nba_droped = nba_data.drop(columns=drop)
    nba_droped.head()
    # nba_data

    # In[5]:

    nba_position = nba_data[['player_position', 'player_name']].groupby(['player_position']).count()
    nba_position.plot(kind='bar')
    plt.savefig(output+ '/position.png')
    nba_newold = nba_data[['player_name', 'diff_year']].groupby(['diff_year']).count()
    nba_newold.plot(kind='bar')
    plt.savefig(output+ '/number_of_year.png')

    # In[6]:

    from sklearn.preprocessing import MinMaxScaler
    # from scipy.cluster.hierarchy import linkage
    # from scipy.cluster.hierarchy import dendrogram
    # from sklearn.metrics import silhouette_samples, silhouette_score
    scaler = MinMaxScaler()
    nba_scaled = pd.DataFrame(scaler.fit_transform(nba_droped))
    nba_scaled.columns = nba_droped.columns
    nba_scaled

    # In[7]:

    inertia = []
    for i in range(1, 20):
        km = KMeans(n_clusters=i,
                    init='k-means++',
                    n_init=10,
                    max_iter=300,
                    random_state=42)
        km.fit(nba_scaled)
        inertia.append(km.inertia_)
    plt.clf()
    plt.plot(range(1, 20), inertia, marker='o')

    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.savefig(output + '/cluster_number.png')
    plt.clf()
    # plt.tight_layout()



    # In[8]:



    n_clusters = 7
    k_means = KMeans(n_clusters=n_clusters, random_state=123)
    k_means.fit(nba_scaled)
    cluster_labels = k_means.labels_

    nba_scaled.head()

    # In[25]:

    from sklearn.decomposition import PCA
    pca_2 = PCA(2)
    plot_columns = pca_2.fit_transform(nba_scaled)

    # show_plot(plot_columns)

    # In[10]:

    def show_plot(data):
        plt.scatter(x=data[:, 0], y=data[:, 1], c=data[:, 2])


    # In[26]:

    plt.scatter(x=plot_columns[:, 0], y=plot_columns[:, 1], c=cluster_labels)
    plt.savefig(output + '/cluster.png')

    # In[11]:
    plt.clf()
    plt.subplots(figsize=(10, 5))
    ax = sns.countplot(x=cluster_labels)
    title = "Histogram of Cluster Counts"
    ax.set_title(title, fontsize=12)
    plt.savefig(output+'/cluster_number_distribution.png')
    # plt.show()

    # In[12]:

    nba_total = np.c_[
        plot_columns, cluster_labels, nba_data.player_name, nba_data.player_position, nba_data.year, nba_data.diff_year]

    old_player = nba_total[nba_total[:, 6] > 1][:, 0:6]
    new_player = nba_total[nba_total[:, 6] <= 1][:, 0:6]

    new_player_name = list(new_player[:, 3])
    with open('new_player.txt', 'w') as f:
        f.write('\n'.join(new_player_name))

    c_group = old_player[old_player[:, 4] == 'C']
    f_group = old_player[old_player[:, 4] == 'F']
    g_group = old_player[old_player[:, 4] == 'G']
    sf_group = old_player[old_player[:, 4] == 'Sf']
    pg_group = old_player[old_player[:, 4] == 'PG']
    sg_group = old_player[old_player[:, 4] == 'SG']
    pf_group = old_player[old_player[:, 4] == 'PF']
    # #['cluster']= cluster_labels
    # nba_scaled['cluster'] = cluster_labels
    # nba_scaled['player_name']=nba_data['player_name']
    # #nba_
    # nba_scaled.head()
    new_player

    # In[13]:

    import math
    def get_distance(old_player, new_player):
        #     print(new_player)
        #     print(new_player[0] - old_player[0])
        #     print(new_player[1] - old_player[1])
        dis = math.sqrt(((new_player[0] - old_player[0]) ** 2) + ((new_player[1] - old_player[1]) ** 2))
        return dis

    def find_similar_player(old_player_list, new_player_list):
        ans = []
        for player in new_player_list:
            least_dis = math.inf
            match_index = math.inf
            for i, old_player in enumerate(old_player_list):
                dis = get_distance(old_player, player)
                if dis < least_dis:
                    least_dis = dis
                    match_index = i
            ans.append(match_index)
        return ans

    # In[14]:

    def get_player_template(inputs, input_group):
        #     inputs = 'Troy Brown Jr.'
        inputs_array = new_player[new_player[:, 3] == inputs][0]
        # print(inputs_array[4])
        old_array = input_group[input_group[:, 4] == inputs_array[4]]
        # print(old_array)
        index = find_similar_player(old_array, [inputs_array])
        print("Player: %s 's performance is the closest approximation to this new player %s in top 100 players data" % (old_array[index][0][3],new_name))
        # find_similar_player(,new_player[new_player[:,3]=='Troy Brown Jr.'])

    # In[16]:

    # use cluster than position

    # In[38]:

    # check old
    xx = new_player[new_player[:, 3] == new_name][0]
    old_array = old_player[old_player[:, 4] == xx[4]]
    index = find_similar_player(old_array, [xx])
    # print(new_name)
    # print(xx)
    # print(old_array)
    # print(old_array[index])
    print("Player: %s 's performance is the closest approximation to this new player in our all players data" % old_array[index][0][3] )

    # In[35]:

    f = open(input2, "r", encoding="utf8")
    players = []
    for x in f:
        players.append(x.split(",")[0])
    f.close()
    # players
    player_group = []
    for pl in players:
        xx = old_player[old_player[:, 3] == pl]
        if len(xx) > 0:
            player_group.append(xx[0])
    # type(player_group)
    # type(old_array)
    new_player_group = np.array(player_group)

    print("We have %s out of 100 top players information in our data" % len(new_player_group))


    # In[36]:

    get_player_template(new_name, new_player_group)

    # In[20]:
    plt.clf()
    show_plot(new_player_group)
    plt.savefig(output + '/new_player_distribution.png')


    # In[39]:

    # import matplotlib
    # def addPoint(scat, new_point, c='k'):
    #     old_off = scat.get_offsets()
    #     new_off = np.concatenate([old_off,np.array(new_point, ndmin=2)])
    #     old_c = scat.get_facecolors()
    #     new_c = np.concatenate([old_c, np.array(matplotlib.colors.to_rgba(c), ndmin=2)])

    #     scat.set_offsets(new_off)
    #     scat.set_facecolors(new_c)

    #     scat.axes.figure.canvas.draw_idle()

    # In[51]:

    player_t = new_player_group.transpose()

    x = player_t[0]
    y = player_t[1]
    name = player_t[3]

    fig, ax = plt.subplots(figsize=(25, 20))
    colors = {'PF': 'tab:blue', 'F': 'tab:orange', 'PG': 'tab:green', 'SF': 'tab:red', 'C': 'tab:purple',
              'SG': 'tab:brown', 'G': 'tab:pink'}
    ax.scatter(x, y,c=pd.Series(player_t[4]).map(colors))

    for i, txt in enumerate(name):
        ax.annotate(txt, (x[i], y[i]))

    new_test = new_player[new_player[:, 3] == new_name]
    new_test = new_test[new_test[:, 5] == max(new_test[:, 5])][0]
    new_test

    new_x = new_test[0]
    new_y = new_test[1]
    new_name = new_test[3]
    ax.plot(new_x, new_y,c=colors[new_test[4]],marker='+' )
    ax.annotate(new_name, (new_x, new_y))
    markers = [plt.Line2D([0, 0], [0, 0], color=color, marker='o', linestyle='') for color in colors.values()]
    plt.legend(markers, colors.keys(), numpoints=1)
    # addPoint(scat, [new_player[0][0], new_player[0][1]], 'y')
    # plt.show()
    plt.savefig(output + '/result.png')

    plt.scatter(x=plot_columns[:, 0], y=plot_columns[:, 1], c=pd.Series(nba_total[:, 4]).map(colors))
    plt.savefig('output/position_distribution.png')


if __name__ == '__main__':
    nba_summary = sys.argv[1]
    top_player = sys.argv[2]
    newplayer_name = sys.argv[3]
    # input_groups = sys.argv[4]
    output_png = sys.argv[4]

    main(nba_summary, top_player, newplayer_name,output_png)
# In[ ]:

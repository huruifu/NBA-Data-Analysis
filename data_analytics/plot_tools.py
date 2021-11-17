import matplotlib.pyplot as plt
import numpy as np

def plot_players_most_injury_bargraph(row_list, x, y, title):
    name_list = []
    count_list = []
    for row in row_list:
        name_list.append(row[x])
        count_list.append(row[y])
    fig, ax = plt.subplots(figsize =(16, 9))    
    plt.barh(name_list,count_list)
    plt.title(title)
    plt.ylabel(x)
    plt.xlabel(y)
    ax.invert_yaxis()
    plt.show()    
    
    
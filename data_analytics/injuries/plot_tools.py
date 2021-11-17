import matplotlib.pyplot as plt
import numpy as np

def plot_barhgraph(row_list, x, y, title):
    """
    [plot horizontal bar graph about the information provided by row_list]

    Args:
        row_list ([row list]): [a list of row data generated from dataframe]
        x ([String]): [field name in row, for label]
        y ([String]): [field name in row, for count]
        title ([String]): [description written in bar graph]
    """
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
    
    
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, STOPWORDS

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
    
def plot_wordfrequency(row_list):
    print(row_list)
    comment_words = ''
    stopwords = set(STOPWORDS)
    for row in row_list:
        print(row)
        injury_name = row["injury_name"]
        print(injury_name)
        comment_words += " ".join(injury_name)+" "
        wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)
    # plot the WordCloud image                      
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()    
          
    
    
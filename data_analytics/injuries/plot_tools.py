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
    # comment_words = ''
    stopwords = set(STOPWORDS)
    text = " ".join(row["injury_name"] for row in row_list)
    # for row in row_list:
    #     injury_name = row["injury_name"].lower()
    #     comment_words += injury_name + " "
    wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=stopwords).generate(text)
    # plot the WordCloud image                      
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()  
    
def plot_validation_result(predicts, actuals):
    predicts_np = np.array(predicts)
    actuals_np = np.array(actuals)
    plt.figure(figsize=(10,10))
    plt.scatter(predicts_np, actuals_np, c='crimson')
    plt.yscale('log')
    plt.xscale('log')
    p1 = max(max(predicts_np), max(actuals_np))
    p2 = min(min(predicts_np), min(actuals_np))
    plt.plot([p1, p2], [p1, p2], 'b-')
    plt.xlabel('Predictions', fontsize=15)
    plt.ylabel('True Values', fontsize=15)
    plt.axis('equal')
    plt.show()
          
          
    
    
import csv
import json
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from operator import itemgetter

from elice_utils import EliceUtils
elice_utils = EliceUtils()


def jsonify(data):
    return json.loads(data.replace("'", '"'))


def preprocess_talks(csv_file):
    talks = []
    
    with open(csv_file) as talks_file: 
        reader =csv.reader(talks_file, delimiter=',') 
        
        for row in reader:
            try:
                talk = {
                    'title': row[14],     
                    'speaker': row[6],  
                    'views': int(row[16]),     
                    'comments': int(row[0]),  
                    'duration': int(row[2]),  
                    'languages': int(row[5]), 
                    'tags': json.loads(row[13].replace("'", '"')),      
                    'ratings': json.loads(row[10].replace("'", '"')),   
                }
            except:
                pass
            talks.append(talk)
    
    return talks

def get_popular_tags(talks, n):
    tag_to_views = {}
    
    for talk in talks:
        tags, views = talk['tags'], talk['views']
        for tag in tags:
            if tag in tag_to_views:
                tag_to_views[tag] += views
            else:
                tag_to_views[tag] = views
    
    tag_view_pairs = list(tag_to_views.items())
    
    top_tag_and_views = sorted(tag_view_pairs, key=itemgetter(1), reverse=True)[:n] 
    top_tags = map(itemgetter(0), top_tag_and_views) 
  
    return list(top_tags)



def completion_rate_by_duration(talks):
    completion_rates = [ talk['comments'] / talk['views'] for talk in talks] 
    durations = [talk['duration'] for talk in talks]

    scatter_plot(durations, completion_rates, '강의 길이', '완수도')

    return completion_rates, durations

def views_by_languages(talks):
    languages = [talk['languages']for talk in talks] 
    views = [talk['views'] for talk in talks] 
    scatter_plot(languages, views, '언어의 수', '조회수')
    

    return views, languages

def show_ratings(talk):
    ratings = talk['ratings']
    keywords = [rating['name'] for rating in ratings] 
    counts =[rating['count'] for rating in ratings] 



    bar_plot(keywords, counts, '키워드', 'rating의 수')
    
    return keywords, counts

def scatter_plot(x, y, x_label, y_label):
    font = fm.FontProperties(fname='./NanumBarunGothic.ttf')
    
    plt.scatter(x, y)
    plt.xlabel(x_label, fontproperties=font)
    plt.ylabel(y_label, fontproperties=font)
    
    plt.xlim((min(x), max(x)))
    plt.ylim((min(y), max(y)))
    plt.tight_layout()
    
    plot_filename = 'plot.png'
    plt.savefig(plot_filename)
    elice_utils.send_image(plot_filename)

def bar_plot(x_ticks, y, x_label, y_label):
    assert(len(x_ticks) == len(y))
    
    font = fm.FontProperties(fname='./NanumBarunGothic.ttf')
    
    pos = range(len(y))
    plt.bar(pos, y, align='center')
    plt.xticks(pos, x_ticks, rotation='vertical', fontproperties=font)
    
    plt.xlabel(x_label, fontproperties=font)
    plt.ylabel(y_label, fontproperties=font)
    plt.tight_layout()
    
    plot_filename = 'plot.png'
    plt.savefig(plot_filename)
    elice_utils.send_image(plot_filename)


def main():
    src = 'ted.csv'
    talks = preprocess_talks(src)
    print(get_popular_tags(talks, 10))

if __name__ == "__main__":
    main()
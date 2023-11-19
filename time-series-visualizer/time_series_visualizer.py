import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = df=pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'],index_col='date')

# Clean data
a=df['value'].quantile(0.975)
b=df['value'].quantile(0.025)
df=df[df['value']<a]
df.dropna()
df=df[df['value']>b]
df=df.dropna()

def draw_line_plot():

    df.plot.line(y='value',xlabel='Date',ylabel='Page Views',figsize=(20,20),subplots=True,)    # Save image and return fig (don't change this part)
    fig=plt.gcf()
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    j=df.groupby([(df.index.year),(df.index.month)]).mean()
    j.index.rename(['year','month'],inplace=True)
    j=j.reset_index()
    j['month']=j['month'].replace([1,2,3,4,5,6,7,8,9,10,11,12],['January','February','March','April','May','June','July','August','September','October','November','December'])
    df_bar=pd.pivot(j,index='year', columns='month', values='value')
    df_bar=df_bar[['January','February','March','April','May','June','July','August','September','October','November','December']]
    df_bar.plot.bar(figsize=(10,10),xlabel='Years',ylabel='Average Page Views')
    fig=plt.gcf()
    # Draw bar plot
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # Draw box plots (using Seaborn)
    f,axs= plt.subplots(1,2,sharey=True,figsize=(10,10))
    sns.boxplot(x='year',y="value",data=df_box,ax=axs[0]).set(title='Year-wise Box Plot (Trend)',xlabel='Year',ylabel='Page Views')
    sns.boxplot(x='month',y='value',data=df_box,ax=axs[1],order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']).set(title='Month-wise Box Plot (Seasonality)',xlabel='Month',ylabel='Page Views') 
    fig=plt.gcf()



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

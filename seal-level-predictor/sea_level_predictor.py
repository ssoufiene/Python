import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot

    df.plot.scatter(x='Year',y='CSIRO Adjusted Sea Level')
    # Create first line of best fit
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    slope, intercept,r,p,std_err=stats.linregress(x,y)
    def my_func(x):
        return slope*x+intercept
    k=np.arange(2014,2051,1)
    k=pd.Series(k)
    j=pd.concat([df['Year'],k])
    modelj=list(map(my_func,j))
    plt.plot(j,modelj)

    # Create second line of best fit
    df2=df.where(df['Year']>=2000)
    df2=df2.dropna()
    x2=df2['Year']
    y2=df2['CSIRO Adjusted Sea Level']
    slope, intercept,r,p,std_err=stats.linregress(x2,y2)
    j2=pd.concat([df2['Year'],k])
    modelj2=list(map(my_func,j2))
    plt.plot(j2,modelj2)

    # Add labels and title
    plt.plot(j2,modelj2)
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
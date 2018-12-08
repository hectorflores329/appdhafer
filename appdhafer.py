#Creating the base plot

#Import the required packages

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
import pandas as pd

#Read the data into the notebook

df = pd.read_csv('all_stocks_5yr.csv')

#Convert the date column to a datetime object and extract the year only.

df['date'] = pd.to_datetime(df['date']).apply(lambda x:x.strftime('%Y'))

#Create the ColumnDataSource Object

data = ColumnDataSource(data = {
    'high' : df[df['date'] == '2013'].high,
    'low' : df[df['date'] == '2013'].low,
    'open' : df[df['date'] == '2013'].open,
    'close': df[df['date'] == '2013'].close,
    'volume': df[df['date'] == '2013'].volume,
    'Name' : df[df['date'] == '2013'].Name
})

#Specify the range of the x and y axis

xmin, xmax = min(df.high), max(df.high)
ymin, ymax = min(df.volume), max(df.volume)

#Create the plot

plot = figure(title = 'Volume traded Vs. High Prices', plot_height = 400, plot_width = 700, x_range = (xmin, xmax),
             y_range = (ymin, ymax))

plot.diamond(x = 'high', y = 'volume', source = data)

plot.xaxis.axis_label = 'High Prices for 2013'

plot.yaxis.axis_label = 'Volume traded in 2013'

#Add the plot to the application

curdoc().add_root(plot)

curdoc().title = 'Volume and High prices of stocks'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#
# Read the CSV:
df= pd.read_csv(
    'fcc-forum-pageviews.csv',
    index_col='date',
    parse_dates=True
)
#
# Filter the top 2.5% and the bottom 2.5% views from the dataset:
top = df['value'].quantile(0.975)
bottom = df['value'].quantile(0.025)
df= df[df['value'].between(bottom, top)]
#
# Create the draw_line_plot function:
def draw_line_plot():
    #
    # Create the plot and it title and its labels:
    fig, ax = plt.subplots(
        figsize=(12,8)
        )
    sns.lineplot(
        df,
        x=df.index, 
        y=df['value'], 
        ax=ax
        )
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    #
    # Save it:
    fig.savefig('line_plot.png')
    return fig
#
# Create the draw_bar_plot function:
def draw_bar_plot():
    #
    # Group the dataset before elaborating the plot:
    data = df.groupby(
        by=[df.index.year.rename('year'), df.index.month.rename('month')]
    ).mean()
    data = data.reset_index()
    #
    # Organize and format it in order to correctly fill the legend:
    data['month'] = pd.to_datetime(
        data['month'], 
        format= '%m'
    ).dt.month_name()
    data['month'] = pd.Categorical(
        data['month'], 
        categories=[
            'January','February','March','April','May','June',
            'July','August','September','October','November','December'
        ], 
        ordered=True
    )
    #
    # Create the image:
    fig, ax = plt.subplots(
        figsize=(12, 8)
        )
    sns.barplot(
        data= data, 
        x='year', 
        y='value', 
        hue='month', 
        palette='Paired'
        )
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(
        title='Months'
        )
    #
    # Save it:
    fig.savefig('bar_plot.png')
    return fig
#
# Create the draw_box_plot function:
def draw_box_plot():
    #
    # Group, organize and format the dataset before elaborating the plot:
    data = df.groupby(
        by=[df.index.year.rename('year'), df.index.month.rename('month')]
    ).mean()
    data = data.reset_index()
    data['month'] = pd.to_datetime(
        data['month'], 
        format= '%m'
    ).dt.month_name()
    data['month'] = data['month'].str[:3]
    data['month'] = pd.Categorical(
        data['month'], 
        categories=[
            'Jan','Feb','Mar','Apr','May','Jun',
            'Jul','Aug','Sep','Oct','Nov','Dec'
        ], 
        ordered=True
    )
    #
    # Create the figure:
    fig, ax = plt.subplots(
        ncols=2,
        figsize=(20, 10)
    )
    #
    # Create the year-wise box plot
    sns.boxplot(
        data=data, 
        x='year', 
        y='value',
        hue='year',
        palette='Set1',
        legend=False,
        ax=ax[0]
        )
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    #
    # Create the month-wise box plot:
    sns.boxplot(
        data=data,
        x='month',
        y='value',
        hue='month',
        palette='Paired',
        legend=False,
        ax=ax[1]
    )
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    #
    # Save the figure:
    fig.savefig('box_plot.png')
    return fig
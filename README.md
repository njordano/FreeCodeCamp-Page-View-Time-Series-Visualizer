# FreeCodeCamp Page View Time Series Visualizer

This project is part of the FreeCodeCamp Data Analysis with Python certification.  
It visualizes forum page views from May 2016 to December 2019 using Matplotlib, Seaborn, and Pandas.  

The goal of this project is to practice data cleaning, grouping, and visualization techniques by creating line plots, bar plots, and box plots that reveal patterns and trends in the dataset.  

---

## Visualizations

### 1. Line Plot
Shows daily page views over time.  
![Line Plot](images/line_plot.png)  

### 2. Bar Plot
Displays the average page views per month, grouped by year.  
![Bar Plot](images/bar_plot.png)  

### 3. Box Plots
- Year-wise Box Plot (Trend): Shows trends in page views by year.  
- Month-wise Box Plot (Seasonality): Highlights seasonality across months.  
![Box Plots](images/box_plot.png)  

---

## Technologies Used
- Python 3  
- Pandas (data wrangling)  
- Matplotlib and Seaborn (visualization)  

---

## Project Structure

FreeCodeCamp-Page-View-Time-Series-Visualizer/  
├─ fcc-forum-pageviews.csv     # Dataset  
├─ pageview_visualizer.py      # Main script with plotting functions  
├─ images/                     # Generated plots  
│   ├─ line_plot.png  
│   ├─ bar_plot.png  
│   └─ box_plot.png  
└─ README.md                   # Project documentation  

---

## FreeCodeCamp Project Requirements

  - Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
  - Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
  - Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.
  - Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
  - Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.

---

## Licenses:

This project was created as a solution to the **Page View Time Series Visualizer** from the FreeCodeCamp *Data Analysis with Python* course.  
Official project page:  
https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer

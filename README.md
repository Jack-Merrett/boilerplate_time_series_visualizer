# Page View Time Series Visualizer

Welcome to the Page View Time Series Visualizer project! This project is part of the Data Analysis with Python certification on freeCodeCamp. The goal of this project is to visualize time series data using line charts, bar charts, and box plots. You will use Pandas, Matplotlib, and Seaborn to explore and visualize a dataset containing page view data from the freeCodeCamp.org forum.

## Getting Started

To begin working on the Page View Time Series Visualizer project, follow these steps:

1. Import the project on Replit.
2. In the .replit window, select "Use run command" and click the Done button.
3. Review the provided videos on the freeCodeCamp.org YouTube channel to gain an understanding of the necessary concepts and tools:
   - [Python for Everybody Video Course](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p)
   - [How to Analyze Data with Python Pandas](https://www.youtube.com/watch?v=H6qk5kHkZr8)
4. Access the "fcc-forum-pageviews.csv" dataset, which contains page view data from 2016-05-09 to 2019-12-03.

## Project Tasks

In this project, you will perform the following tasks:

1. Use Pandas to import the data from "fcc-forum-pageviews.csv" and set the index to the date column.
2. Clean the data by filtering out days when the page views were in the top 2.5% or bottom 2.5% of the dataset.
3. Create a function called `draw_line_plot` that utilizes Matplotlib to draw a line chart similar to "examples/Figure_1.png". The chart should show the daily freeCodeCamp forum page views from 5/2016 to 12/2019.
4. Implement a function called `draw_bar_plot` that draws a bar chart similar to "examples/Figure_2.png". This chart should display the average daily page views for each month grouped by year.
5. Develop a function named `draw_box_plot` that uses Seaborn to draw two adjacent box plots as shown in "examples/Figure_3.png". The box plots should illustrate the distribution of values within a given year or month and how they compare over time.

## Testing and Submission

You can test your functions using the provided `test_module.py` script. The tests will automatically run when you click the "run" button in `main.py`.

Once you have completed the project, copy the URL of your project on Replit and submit it to freeCodeCamp for assessment.

## Resources

For additional support and learning materials, consider exploring the following resources:

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/documentation.html)
- [FreeCodeCamp Data Analysis with Python Course](https://www.freecodecamp.org/learn/data-analysis-with-python/)
- Online tutorials and forums related to data analysis, time series data, and data visualization

## License

This project is licensed under freecodecamp.com

## Acknowledgments

Special thanks to freeCodeCamp for providing this project as part of the Data Analysis with Python certification. The open-source contributions of Pandas, Matplotlib, and Seaborn communities have greatly enriched the capabilities of Python for data analysis and visualization.

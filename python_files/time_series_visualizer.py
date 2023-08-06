import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('../data/fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# Calculate the lower and upper thresholds for filtering
lower_threshold = df['value'].quantile(0.025)
upper_threshold = df['value'].quantile(0.975)

# Filter out days with views below the lower threshold or above the upper threshold
cleaned_df = df[
    (df['value'] >= lower_threshold) & (df['value'] <= upper_threshold)
    ]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(cleaned_df.index, cleaned_df['value'], color='r', linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    # Rotate x-axis tick labels and display every nth label
    n = 100  # Adjust this value based on your data and plot size
    plt.xticks(rotation=45, ha='right')  # Rotate and align labels
    plt.xticks(range(0, len(cleaned_df.index), n), cleaned_df.index[::n])  # Display every nth label

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Create a new column 'Year' based on the year of the index
    cleaned_df['Year'] = cleaned_df.index.year

    # Create a new column 'Month' based on the month of the index
    cleaned_df['Month'] = cleaned_df.index.month_name()

    # Create a pivot table to calculate the average page views for each month in each year
    avg_page_views = cleaned_df.pivot_table(values='value', index='Year', columns='Month', aggfunc='mean', fill_value=0)

    # Define the month order for proper sorting
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    # Sort the columns of the pivot table based on the defined month order
    avg_page_views = avg_page_views.reindex(columns=month_order)

    # Create the bar plot
    ax = avg_page_views.plot(kind='bar', figsize=(12, 6))
    
    # Set labels and title
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.set_title("Average Daily Page Views for Each Month (2016-2019)")
    
    # Set legend title and location
    ax.legend(title="Months", loc='upper left')
    
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    ax.savefig('bar_plot.png')
    return ax

def draw_box_plot():
    # Prepare the data 
    df_box = cleaned_df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Set up the matplotlib figure with two subplots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    # Draw the first box plot (Year-wise)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Draw the second box plot (Month-wise)
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=[
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Adjust layout and show plots
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  
# Import data from epa-sea-level.csv
    df = pd.read_csv('epa-sea-level.csv')

# Scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

# Perform linear regression to get the slope and y-intercept of the line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Create the line of best fit using the linear regression parameters
    line_x = pd.Series([i for i in range(1880, 2051)])  # Years from 1880 to 2050
    line_y = slope * line_x + intercept

# Plot the line of best fit over the top of the scatter plot
    plt.plot(line_x, line_y, color='red', label='Line of Best Fit (1880-2050)')

# Filter data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]

# Perform linear regression on recent data
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

# Create the line of best fit using the recent linear regression parameters
    line_x_recent = pd.Series([i for i in range(2000, 2051)])  # Years from 2000 to 2050
    line_y_recent = slope_recent * line_x_recent + intercept_recent

# Plot the new line of best fit using data from year 2000 through the most recent year
    plt.plot(line_x_recent, line_y_recent, color='green', label='Line of Best Fit (2000-2050)')

# Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

# Show legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
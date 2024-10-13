import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 1. Import the data
df = pd.read_csv('epa-sea-level.csv')

# 2. Create scatter plot
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# 3. Line of best fit for all data
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = pd.Series(range(1880, 2051))
sea_levels_extended = slope * years_extended + intercept
plt.plot(years_extended, sea_levels_extended, color='red')

# 4. Line of best fit for data from year 2000
df_2000 = df[df['Year'] >= 2000]
slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
years_2000_extended = pd.Series(range(2000, 2051))
sea_levels_2000_extended = slope_2000 * years_2000_extended + intercept_2000
plt.plot(years_2000_extended, sea_levels_2000_extended, color='green')

# 5. Label axes and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# 6. Save and show plot
plt.savefig('sea_level_plot.png')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# creating the df 
df = pd.read_csv('FIFA World Cup Attendance.csv')

# dropping the overall row because it skews data 
df = df.drop(index=22)
# creating the axis 
years = df['Year']
attendance = df['Total_Attendance']

# Create the scatter plot
plt.scatter(years, attendance, marker='x')

# Add a title and axis labels
plt.title('World Cup Attendance')
plt.xlabel('years')
plt.ylabel('attendance')

# Get the current Axes object
ax = plt.gca()

# Set the y-axis labels
ax.set_yticklabels(range(0, 4_000_000, 500_000))

# Redraw the plot
plt.draw()
# Display the plot
plt.show()

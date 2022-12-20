import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('FIFA World Cup Attendance.csv')
df = df.drop(index=22)
years = df['Year']
attendance = df['Total_Attendance']

# Create the plot
plt.plot(years, attendance)

# Add a title and axis labels
plt.title('World Cup Attendance')
plt.xlabel('years')
plt.ylabel('attendance')
# Get the current Axes object
ax = plt.gca()

# Set the y-axis tick labels to the thousands values
ax.set_yticklabels(range(0, 4_000_000, 500_000))
# Redraw the plot
plt.draw()
# Display the plot
plt.show()

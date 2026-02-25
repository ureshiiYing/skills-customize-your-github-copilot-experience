import pandas as pd
import matplotlib.pyplot as plt
# import plotly.express as px  # Uncomment if you want to use plotly

# Load data (replace with your own CSV or use a built-in dataset)
data = pd.read_csv('data.csv')  # Make sure data.csv is in the same folder

# Explore data
data.head()
data.describe()

# Bar chart example
plt.figure(figsize=(8, 5))
data['column_name'].value_counts().plot(kind='bar')  # Replace 'column_name' with a real column
plt.title('Bar Chart Example')
plt.xlabel('Category')
plt.ylabel('Count')
plt.savefig('bar_chart.png')
plt.close()

# Line graph example
plt.figure(figsize=(8, 5))
data['numeric_column'].plot(kind='line')  # Replace 'numeric_column' with a real column
plt.title('Line Graph Example')
plt.xlabel('Index')
plt.ylabel('Value')
plt.savefig('line_graph.png')
plt.close()

# (Optional) Plotly example
# fig = px.scatter(data, x='col1', y='col2', title='Scatter Plot Example')
# fig.write_image('scatter_plot.png')

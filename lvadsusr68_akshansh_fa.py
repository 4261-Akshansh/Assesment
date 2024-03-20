# -*- coding: utf-8 -*-
"""LVADSUSR68-Akshansh-FA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ET7UrdfggvSXJTYpmTOIUCXSrkkPtxKx
"""

#1
import pandas as pd
import numpy as  np
df=pd.read_excel('/content/Walmart_Dataset Python_Final_Assessment.xlsx')

df
df.info()
df.describe()
df.columns

#2
df.isnull().sum()
df.duplicated()
df.fillna(0)

#3
df.mean()
df.std()
df.median()

#4
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


for column in df.select_dtypes(include=['int64', 'float64']):
    plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x=column, kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

for column in df.select_dtypes(include=['int64', 'float64']):
    plt.figure(figsize=(8, 6))
    sns.barplot(data=df, x=df.index, y=column)
    plt.title(f'Bar Chart of {column}')
    plt.xlabel('Index')
    plt.ylabel(column)
    plt.show()

sns.pairplot(df.select_dtypes(include=['int64', 'float64']))
plt.suptitle('Pairplot of Numerical Columns')
plt.show()

#5
print("Correlation between the numerical factor of data which include total sales as sales, total sales quantity as quatity, and total profit as profit : ")
df.corr()

#6
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


for column in df.select_dtypes(include=['int64', 'float64']):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, y=column)
    plt.title(f'Box Plot of {column}')
    plt.ylabel(column)
    plt.show()

# for column in df.select_dtypes(include=['int64', 'float64']):
#     plt.figure(figsize=(8, 6))
#     df[column].plot.pie(autopct='%1.1f%%', startangle=140)
#     plt.title(f'Pie Chart of {column}')
#     plt.ylabel('')
#     plt.show()

#7 Trend Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


# print(df.head())
# print(df.info())


# df['Order Date'] = pd.to_datetime(df['Order Date'])
# df.set_index('Order Date', inplace=True)

plt.figure(figsize=(12, 6))
plt.plot(df['Sales'], label='Sales')
plt.plot(df['Profit'], label='Profit')
plt.title('Sales and Profit Trends Over the Years')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()


# decomposition = seasonal_decompose(df['Sales'], model='additive')
# decomposition.plot()
# plt.show()

category_sales = df.groupby('Category')['Sales'].sum()
growth_rates = category_sales.pct_change()

most_growth_category = growth_rates.idxmax()
print("Product category with the most growth in terms of sales:", most_growth_category)


plt.figure(figsize=(10, 6))
growth_rates.plot(kind='bar', color='skyblue')
plt.title('Yearly Sales Growth Rate by Category')
plt.xlabel('Category')
plt.ylabel('Growth Rate')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
growth_rates.plot(kind='bar', color='skyblue')
plt.title('Yearly Sales Growth Rate by Category')
plt.xlabel('Category')
plt.ylabel('Growth Rate')
plt.xticks(rotation=45)
plt.show()

#7 Customer Analysis

import pandas as pd
import numpy as np

# df.info()

top_5_customers_orders = df.groupby('EmailID')['Order ID'].nunique().nlargest(5)
top_5_customers_sales = df.groupby('EmailID')['Sales'].sum().nlargest(5)
print(top_5_customers_orders)
print(top_5_customers_sales)

df['Order Date'] = pd.to_datetime(df['Order Date'])
df.sort_values(['EmailID', 'Order Date'], inplace=True)
df['Time_Between_Orders'] = df.groupby('EmailID')['Order Date'].diff().dt.days
average_time_between_orders = df.groupby('EmailID')['Time_Between_Orders'].mean()
print(average_time_between_orders)

"""Q7 Comprehensive Analytics


i. Optimizing Supply Chain:
   Utilize insights from sales velocity to forecast demand accurately. Higher sales value indicates products that are in high demand, enabling better stock management and allocation of resources.
   Analyze order fulfillment data to identify issues in the supply chain. Focus on, improving logistics, and reducing lead times to enhance overall efficiency.
   Implement technologies such as IoT sensors or RFID to track inventory in real-time, allowing for proactive inventory management and replenishment.

ii. Geographic Sales Distribution and Targeted Marketing:
   Identify underlying factors contributing to geographic sales distribution, such as demographics, cultural preferences, or economic conditions. Use geographic information systems or spatial analysis to visualize sales patterns and identify potential market segments.
   Make marketing strategies based on geographic insights. Develop localized marketing campaigns, promotions, or product offerings that resonate with specific regions or customer segments.
   Leverage digital marketing channels and geotargeting techniques to reach customers in specific geographic areas more effectively. Personalize marketing messages based on regional preferences or interests.

iii. Identifying High-Value Customers and Enhancing Customer Loyalty:
   Identify patterns or predictors of high-value customers, such as purchase frequency, total spending, or product preferences. Use machine learning algorithms or customer segmentation techniques to classify customers into different value tiers.
   Develop personalized loyalty programs or rewards schemes targeted towards high-value customers. Offer exclusive benefits, discounts, or incentives to encourage repeat purchases and foster loyalty.
   Implement data-driven customer relationship management (CRM) systems to track customer interactions, preferences, and feedback. Use this information to provide personalized experiences and anticipate customer needs effectively.

"""
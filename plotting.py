# Seaborn lib proved more options than matplotlib
import seaborn as sns
tips = sns.load_dataset('tips')

# Plotting graph with bars
sns.distplot(tips['total_bill'], kde=False, bins=30)

#Plotting graph with different featues like adding regression line etc
sns.jointplot(x='total_bill',y='tip',data=tips, kind='reg')

# Graphing evry variable wrt to every other variable
sns.pairplot(tips)
sns.pairplot(tips, hue='category') # If categorical data like male or female, 1 or 0, hue can be used to separate with colors

import numpy as np
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)

# Eg dataset is tips from a hotel
sns.barplot(x='sex', y='total_bill', data=tips)
# boxplot but with category
sns.boxplot(x='day',y='total_bill', data=tips, hue='sex')
# More advanced plot
sns.violinplot(x='day',y='total_bill', data=tips)
# Simialr to scatter plot from matplotlib
sns.stripplot(x='day', y='total_bill', data=tips)

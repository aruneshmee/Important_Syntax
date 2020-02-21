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

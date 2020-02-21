# Seaborn lib proved more options than matplotlib
import seaborn as sns
tips = sns.load_dataset('tips')

# Plotting graph with bars
sns.distplot(tips['total_bill'], kde=False, bins=30)

#Plotting graph with different featues like adding regression line etc
sns.jointplot(x='total_bill',y='tip',data=tips, kind='reg')

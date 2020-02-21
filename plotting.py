import seaborn as sns
tips = sns.load_dataset('tips')

sns.distplot(tips['total_bill'], kde=False, bins=30)

sns.jointplot(x='total_bill',y='tip',data=tips, kind='reg')

# Mapping into list of integers (Usually required when input contains spaces)
arr = list(map(int,input().split()))

# Taking input as spaces 
a, b = int(input('Enter: ')).split()

# Making bell curves
Y = norm.pdf(X, mean, standard_deviation)

# Plotting basics
plt.xlabel('Name for X Axis')
plt.ylabel('Name for Y Axis')
plt.grid() #Makes grid in the backgrounf
plt.show()

# Displays no of rows and columns from the dataset
df = pd.DataFrame(databyc)
total_c=len(df.axes[0])
total_rlen(df.axes[1)

# Mapping into list of integers (Usually required when input contains spaces)
arr = list(map(int,input().split()))

# Taking input as spaces 
a, b = int(input('Enter: ')).split()

# Making bell curves
Y = norm.pdf(X, mean, standard_deviation)

# Plotting basics
plt.xlabel('Name for X Axis')
plt.ylabel('Name for Y Axis')
plt.grid() #Makes grid in the background
plt.show()

# Displays no of rows and columns from the dataset
df = pd.DataFrame(databyc)
total_c=len(df.axes[0])
total_r=len(df.axes[1)
                   
# Finding thr overlapping area between two bell curves
m1 = ml[g_1-1]
m2 = ml[g_2-1]
std1 = stl[g_1-1]
std2 = stl[g_2-1]
result = solve(m1,m2,std1,std2)
#plot3=plt.plot(result,norm.pdf(result,m1,std1),'y')

#Plots integrated area
r = result[0]
lap = plt.fill_between(x[x>r], 0, norm.pdf(x[x>r],m1,std1),alpha=0.4)
olap = plt.fill_between(x[x<r], 0, norm.pdf(x[x<r],m2,std2),alpha=0.4)  
area = norm.cdf(r,m2,std2) + (1.-norm.cdf(r,m1,std1))
                   
# Function to find the roots for finding the area under the curve
def solve(m1,m2,std1,std2):
  a = 1/(2*std1**2) - 1/(2*std2**2)
  b = m2/(std2**2) - m1/(std1**2)
  c = m1**2 /(2*std1**2) - m2**2 / (2*std2**2) - np.log(std2/std1)
  return np.roots([a,b,c])
      
# Basics of class and its attribute
class Dog():
    
    # Class object attribute
    # Same for any ind=satnce of class
    species = 'mammal'
    
    def __init__(self, breed, name):
        
        # Attributes
        # We take in argumnet
        # Assign it using
        self.breed = breed
        self.name = name
        
    # Operation/actions
    def bark(self, number):
        print('Woof my name is {} and num is {}'.format(self.name, number))
                    
# Class Example
import math
class point():
    
    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2
    
    def distance(self):
        d = math.sqrt((self.coord1[0]-self.coord2[0])**2+(self.coord1[1]-self.coord2[1])**2)
        return d
    
    def get_slope(self):
        s = (self.coord2[1]-self.coord1[1])/(self.coord2[0]-self.coord1[0])
        return s

# numpy basics
import numpy
n, m, p = map(int,input().split())
mat = []
for _ in range(n+m):
    arr = list(map(int,input().split()))
    mat.append(arr)
print(numpy.reshape(mat,(n+m,p)))

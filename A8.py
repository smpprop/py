from pandas import *

# Create first data frame
data1 = {     'rollno': [1, 2, 3],    'name': ['Veena', 'Peter', 'Vikas'], 
    'Total_Marks': [250, 270, 290]
}

df1 = DataFrame(data1)

# Create second data frame
data2 = {
    'rollno': [4, 5, 6],     'name': ['Jahnavi', 'Tulsi', 'Varsha'],
    'Total_Marks': [260, 280, 275]
}

df2 = DataFrame(data2)

# Join the two data frames along rows
result = concat([df1, df2], ignore_index=True)

# Display the result
print(result)

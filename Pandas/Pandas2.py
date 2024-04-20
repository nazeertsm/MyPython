# Importing the necessary libraries
import pandas as pd
import lxml

# Reading the Titanic dataset from a URL
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Printing the first 3 rows of the dataset
print(df.head(3))

# Printing the rows where the age of the passenger is greater than 60
print(df[df['Age'] > 60])
print("--------------1")

# Printing the rows where the age of the passenger is greater than 60 and the passenger class is 1
print(df[(df['Age'] > 60) & (df['Pclass'] == 1)])
print("--------------2")

# Printing the rows where the passenger survived
print(df[df['Survived'] == 1])
print("--------------3")

# Printing the rows where the passenger is female
print(df[df['Sex'] == 'female'])
print("--------------4")

# Assigning the sum of 'SibSp' and 'Parch' to a new column 'Family' and then printing it
df['Family'] = df['SibSp'] + df['Parch']
print(df['Family'])
print("--------------5")

# Dropping the 'Family' column from the DataFrame
df = df.drop(columns=['Family'])
print(df.head(3))
print("--------------6")

# Printing the number of unique values in the 'Embarked' column
print(df['Embarked'].nunique())
print("--------------7")

print(df.loc[0:2, ['Name', 'PassengerId', 'Survived', 'Pclass']])
print("--------------8")
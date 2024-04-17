# Importing the pandas library
import pandas as pd
import lxml

# Reading the CSV file "services.csv" into a pandas DataFrame
df = pd.read_csv("services.csv")

# Printing the first 3 rows of the DataFrame
# The head() function is used to get the first n rows.
# This function returns first n rows from the object based on position.
# It is useful for quickly verifying data, for example, after sorting or appending rows.
print(df.head(3))

print("--------------1")
# Printing the shape of the DataFrame
# The shape attribute returns a tuple representing the dimensionality of the DataFrame.
# In this case, it returns the number of rows and columns.
print(df.shape)
print("--------------2")

# Printing the last 3 rows of the DataFrame
# The tail() function is used to get the last n rows.
# This function returns last n rows from the object based on position.
# It is useful for quickly verifying data, for example, after sorting or appending rows.
print(df.tail(3))
print("--------------3")
# Printing the type of the DataFrame
# The type() function in Python returns the data type of the object passed to it as an argument.
# This function is used to check the type of the object.
print(type(df))
print("--------------4")
# Printing the list of column names in the DataFrame
# The columns attribute returns the column labels of the given Dataframe.
# We convert it to a list for better readability.
print(list(df.columns))
print("--------------5")

# Printing the 'status' column of the DataFrame
# We can access a specific column of a DataFrame by using square brackets and the column name.
print(df['status'])
print("--------------6")
# Printing the type of the 'status' column of the DataFrame
# The type() function in Python returns the data type of the object passed to it as an argument.
print(type(df['status']))
print("--------------7")

# Printing the 'status' column of the DataFrame as a list
# We can convert a specific column of a DataFrame to a list using the tolist() function.
print(df['status'].tolist())
print("--------------8")

# Printing the 'status' column of the DataFrame as a DataFrame
# We can access a specific column of a DataFrame as a DataFrame by using double square brackets.
print(df[['status']])
print("--------------9")
# Printing the type of the 'status' column of the DataFrame as a DataFrame
# The type() function in Python returns the data type of the object passed to it as an argument.
print(type(df[['status']]))
print("--------------10")

# Printing the list of column names in the DataFrame
# The columns attribute returns the column labels of the given Dataframe.
# We convert it to a list for better readability.
print(list(df.columns))
print("--------------11")

# Printing the 'email', 'keywords', and 'name' columns of the DataFrame
# We can access specific columns of a DataFrame by using square brackets and the column names.
print(df[['email','keywords','name']])
print("--------------12")

# Printing the data types of the DataFrame
# The dtypes attribute returns the data types of the columns in the DataFrame.
print(df.dtypes)
print("--------------13")
# Printing the type of the DataFrame 'df1'
# The type() function in Python returns the data type of the object passed to it as an argument.
print(type(df))
print("--------------14")

# Printing the list of column names in the DataFrame 'df1'
# The columns attribute returns the column labels of the given Dataframe.
# We convert it to a list for better readability.
print(list(df.columns))
print("--------------15")

# Reading the CSV file from the URL into a pandas DataFrame 'df2'
df2 = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Printing the first 3 rows of the DataFrame 'df2'
# The head() function is used to get the first n rows.
# This function returns first n rows from the object based on position.
# It is useful for quickly verifying data, for example, after sorting or appending rows.
print(df2.head(3))
print("--------------16")

# Printing the list of column names in the DataFrame 'df2'
# The columns attribute returns the column labels of the given Dataframe.
# We convert it to a list for better readability.
print(list(df2.columns))
print("--------------17")

# Printing the type of the DataFrame 'df2'
# The type() function in Python returns the data type of the object passed to it as an argument.
print(type(df2))
print("--------------18")
# Printing the 'Survived' column of the DataFrame 'df2'
# We can access a specific column of a DataFrame by using square brackets and the column name.
print(df2['Survived'])
print("--------------19")

# Printing the type of the 'Survived' column of the DataFrame 'df2'
# The type() function in Python returns the data type of the object passed to it as an argument.
print(type(df2['Survived']))
print("--------------20")

# Printing the 'Survived', 'Pclass', and 'Name' columns of the DataFrame 'df2'
# We can access specific columns of a DataFrame by using square brackets and the column names.
print(df2[['Survived', 'Pclass', 'Name']])
print("--------------21")

# Printing the last 3 rows of the DataFrame 'df2'
# The tail() function is used to get the last n rows.
# This function returns last n rows from the object based on position.
# It is useful for quickly verifying data, for example, after sorting or appending rows.
print(df2.tail(3))
print("--------------22")

# Reading the HTML tables from the URL into a list of pandas DataFrames 'url_data'
url_data = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2015_totals.html")

# Printing the type of 'url_data'
# The type() function in Python returns the data type of the object passed to it as an argument.
print(type(url_data))
print("--------------23")

# Printing the length of 'url_data'
# The len() function in Python returns the number of items in an object.
print(len(url_data))
print("--------------24")
# Assigning the first DataFrame in 'url_data' to 'df3'
df3 = url_data[0]

# Printing the DataFrame 'df3'
print(df3)
print("--------------25")
# Printing the first 5 rows of the DataFrame 'df3'
# The head() function is used to get the first n rows.
# This function returns first n rows from the object based on position.
# It is useful for quickly verifying data, for example, after sorting or appending rows.
print(df3.head())
print("--------------26")
# Printing the last 3 rows of the DataFrame 'df3'
# The tail() function is used to get the last n rows.
# This function returns last n rows from the object based on position.
# It is useful for quickly verifying data, for example, after sorting or appending rows.
print(df3.tail(3))
print("--------------27")

# Printing the list of column names in the DataFrame 'df3'
# The columns attribute returns the column labels of the given Dataframe.
# We convert it to a list for better readability.
print(list(df3.columns))
print("--------------28")
# Printing the data types of the DataFrame 'df3'
# The dtypes attribute returns the data types of the columns in the DataFrame.
print(df3.dtypes)
print("--------------29")

# Printing the 'Pos', 'Age', and 'Tm' columns of the DataFrame 'df3'
# We can access specific columns of a DataFrame by using square brackets and the column names.
print(df3[['Pos', 'Age', 'Tm']])
print("--------------30")
# Saving the DataFrame 'df3' to a CSV file "players_data.csv"
# The to_csv() function is used to write the DataFrame to a comma-separated values (CSV) file.
# The index=False argument is used to write row names (index).
df3.to_csv("players_data.csv", index=False)


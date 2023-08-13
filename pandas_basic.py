'''Q1'''
from gettext import install

import pip

import pandas as pd

data = [4, 8, 15, 16, 23, 42]
series = pd.Series(data)

print(series)

'''Q2'''

data_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
series = pd.Series(data_list)

print(series)

'''Q3'''
data = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'Gender': ['Female', 'Male', 'Female']
}

df = pd.DataFrame(data)

print(df)

'''Q4'''
'''In Pandas, a `DataFrame` is a two-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns). It is similar to a spreadsheet or a SQL table, where you have rows and columns to organize and store data. Each column in a `DataFrame` can be thought of as a `Series`.

A `Series` is a one-dimensional labeled array that can hold data of any type, similar to a column in a table or a list in Python.

Here's an example to illustrate the difference between a `DataFrame` and a `Series`:

```python'''
import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'Gender': ['Female', 'Male', 'Female']
}

df = pd.DataFrame(data)

# Creating a Series
ages = pd.Series([25, 30, 27], name='Age')

# Printing the DataFrame and Series
print("DataFrame:")
print(df)
print("\nSeries:")
print(ages)

'''In this example, the `DataFrame` contains three columns: 'Name', 'Age', and 'Gender', each of which is a `Series` with different data. The `Series` named 'ages' is extracted from the 'Age' column of the `DataFrame`.

Key differences between a `DataFrame` and a `Series`:

1. **Dimensionality**:
   - `DataFrame` is a two-dimensional structure, like a table with rows and columns.
   - `Series` is a one-dimensional array-like structure.

2. **Usage**:
   - `DataFrame` is used to store and manipulate tabular data, where each column can be of different data types.
   - `Series` is used to store a sequence of data values with labels (index), often representing a single column or row of data.

3. **Structure**:
   - A `DataFrame` is composed of multiple `Series` (columns) that share the same index.
   - A `Series` consists of data values and an index, which uniquely labels each data point.

4. **Functionality**:
   - `DataFrame` offers more functionality for data manipulation, analysis, and cleaning as it handles multiple columns and can represent complex relationships.
   - `Series` provides simpler functionality for working with a single sequence of data.

In summary, a `DataFrame` is a higher-level structure that holds multiple `Series` with aligned indexes. It's suitable 
for managing and analyzing tabular data, while a `Series` is more suitable for working with individual columns or rows of 
data.'''

'''Q5'''
'''Pandas provides a wide range of functions for data manipulation in a DataFrame. Here are some common functions along with examples of when you might use them:

1. **Filtering Data** (`df[df['column'] > value]`):
   - Use to filter rows based on a condition.
   - Example: Filtering rows where the 'Age' column is greater than 25.

2. **Sorting Data** (`df.sort_values(by='column')`):
   - Use to sort rows based on one or more columns.
   - Example: Sorting the DataFrame by the 'Age' column in ascending order.

3. **Grouping Data** (`df.groupby('column').agg(func)`):
   - Use to group rows based on a column and apply aggregation functions.
   - Example: Grouping by 'Gender' and calculating the mean age for each gender.

4. **Aggregating Data** (`df['column'].agg(func)`):
   - Use to calculate summary statistics for a specific column.
   - Example: Calculating the maximum age in the 'Age' column.

5. **Joining Data** (`pd.merge(df1, df2, on='column')`):
   - Use to combine data from different DataFrames based on common columns.
   - Example: Joining two DataFrames based on a shared 'ID' column.

6. **Pivoting Data** (`df.pivot_table(index='row_col', columns='col_col', values='value_col', aggfunc=func)`):
   - Use to create a pivot table by rearranging data based on columns and rows.
   - Example: Creating a pivot table to show average ages by 'Gender' and 'Age Group'.

7. **Dropping Columns** (`df.drop('column', axis=1)`):
   - Use to remove one or more columns from the DataFrame.
   - Example: Dropping the 'Gender' column from the DataFrame.

8. **Handling Missing Data** (`df.dropna()` and `df.fillna(value)`):
   - Use to remove or fill missing values in the DataFrame.
   - Example: Removing rows with missing data using `dropna()`, or filling missing values with a specific value using `fillna()`.

9. **Adding Columns** (`df['new_column'] = values`):
   - Use to create and populate new columns in the DataFrame.
   - Example: Adding a new column that calculates the difference between the 'Age' and the average age.

10. **Applying Functions** (`df.apply(func)`):
    - Use to apply a function to each element or row/column in the DataFrame.
    - Example: Applying a custom function to transform values in a specific column.

These are just a few examples of the many functions available in Pandas for data manipulation. The choice of function depends on the specific task you're trying to accomplish with your data. Pandas documentation and tutorials can provide more detailed information and examples for each function.'''

'''Q6'''
'''Among the options you provided, both `Series` and `DataFrame` are mutable in nature, while `Panel` is no longer actively supported in recent versions of Pandas (since version 0.25.0) and is not recommended for use. Instead, Pandas emphasizes the use of `DataFrame` for most data manipulation tasks.

Mutable means that you can modify the data within the structure after it's created.

- **Series**: A `Series` is mutable. You can change the values of individual elements in a `Series` after it has been created.

- **DataFrame**: A `DataFrame` is also mutable. You can modify values, add or remove columns, and perform various data manipulations on the `DataFrame`.

- **Panel**: While `Panel` used to be a 3D data structure in Pandas, it has been deprecated and is no longer recommended for most use cases. It has been replaced with more versatile structures like `MultiIndex DataFrames`. As of my knowledge cutoff in September 2021, `Panel` is not the recommended way to handle multi-dimensional data.

Please note that my information is based on the state of Pandas up to September 2021, and there might have been further changes or developments since then. Always refer to the latest Pandas documentation for the most accurate and up-to-date information.'''

'''Q7'''
'''Certainly! You can create a DataFrame using multiple Series by passing a dictionary of Series to the `pd.DataFrame()` constructor. Each Series will become a column in the resulting DataFrame.

Here's an example:'''

```python
import pandas as pd

# Creating individual Series
names = pd.Series(['Alice', 'Bob', 'Claire'])
ages = pd.Series([25, 30, 27])
genders = pd.Series(['Female', 'Male', 'Female'])

# Creating a DataFrame using the Series
data = {
    'Name': names,
    'Age': ages,
    'Gender': genders
}

df = pd.DataFrame(data)

# Printing the DataFrame
print(df)
```

'''Output:

```
     Name  Age  Gender
0   Alice   25  Female
1     Bob   30    Male
2  Claire   27  Female
```

In this example:

1. We create three separate Series (`names`, `ages`, and `genders`) that contain data for the 'Name', 'Age', and 'Gender' columns, respectively.

2. We create a dictionary `data` where each key corresponds to a column name, and each value is one of the Series we created.

3. We use `pd.DataFrame(data)` to create a DataFrame using the provided dictionary. Each Series becomes a column in the DataFrame.

4. Finally, we print the resulting DataFrame.

The resulting DataFrame has three columns ('Name', 'Age', and 'Gender') and three rows, where each row represents the data from the corresponding position in the original Series.'''
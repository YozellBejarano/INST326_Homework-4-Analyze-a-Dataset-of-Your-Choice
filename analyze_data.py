import pandas as pd

# Step 1: Read the CSV dataset into a DataFrame
# Using index_col to set PassengerId as the index for label-based operations
df = pd.read_csv("titanic.csv", index_col="PassengerId")

# Print the first five rows
print("First five rows of the DataFrame:")
print(df.head())
print("\n" + "="*50 + "\n")

# Display DataFrame structure
print("DataFrame info:")
df.info()
print("\n" + "="*50 + "\n")

# Show summary of numerical statistics
print("Numerical statistics summary:")
print(df.describe())
print("\n" + "="*50 + "\n")

# Step 2: Demonstrate accessing data with loc and iloc
print("Accessing data examples:")

# Single row by its label (using PassengerId as index)
print("Single row by label (PassengerId=1):")
print(df.loc[1])
print()

# Single row by its position
print("Single row by position (index 0):")
print(df.iloc[0])
print()

# Slice of rows by label
print("Slice of rows by label (PassengerId 1 to 5):")
print(df.loc[1:5])
print()

# Slice of rows by position
print("Slice of rows by position (rows 0 to 4):")
print(df.iloc[0:5])
print()

# Single column by name
print("Single column by name ('Age'):")
print(df['Age'].head())  # Showing first 5 for brevity
print()

# Single cell by both row and column labels
print("Single cell by row label and column label (PassengerId=1, 'Age'):")
print(df.loc[1, 'Age'])
print("\n" + "="*50 + "\n")

# Step 3: Filter the DataFrame using Boolean conditions
print("Filtering examples:")

# Filter 1: Comparison operator (select rows where Age > 30)
filtered1 = df[df['Age'] > 30]
print("Filtered DataFrame (Age > 30), first five rows:")
print(filtered1.head())
print()

# Filter 2: Combine two conditions (Sex == 'female' AND Pclass == 1)
filtered2 = df[(df['Sex'] == 'female') & (df['Pclass'] == 1)]
print("Filtered DataFrame (Sex == 'female' AND Pclass == 1), first five rows:")
print(filtered2.head())
print("\n" + "="*50 + "\n")

# Step 4: Add and remove columns
print("Adding and removing columns:")

# Add a new column: FamilySize = SibSp + Parch + 1 (self)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print("New column 'FamilySize' added. First five rows with new column:")
print(df[['SibSp', 'Parch', 'FamilySize']].head())
print()

# Remove a column: Drop 'Ticket' as it's not needed for this analysis
df.drop('Ticket', axis=1, inplace=True)
print("Column 'Ticket' removed. New list of columns:")
print(list(df.columns))
print("\n" + "="*50 + "\n")

# Step 5: Groupby operation
print("Groupby operation:")

# Group by 'Sex' (categorical) and compute mean of 'Age' (numerical)
grouped = df.groupby('Sex')['Age'].mean()
print("Mean Age by Sex:")
print(grouped)
print("\n" + "="*50 + "\n")

print("Analysis complete.")
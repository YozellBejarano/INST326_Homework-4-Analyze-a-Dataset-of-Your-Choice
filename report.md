The dataset I selected is the Titanic passenger dataset (train.csv), which contains information about 891 passengers from the Titanic shipwreck, including details like survival status, 
passenger class, age, sex, and family relationships. I obtained it from Kaggle's Titanic competition page (https://www.kaggle.com/c/titanic/data?select=train.csv ), 
where it's provided as a standard CSV file for educational purposes. Once I downloaded it, I renamed it to “titanic.csv” for clarity. 
This dataset is well-suited for demonstrating pandas operations due to its mix of categorical (e.g., Sex, Pclass) and numerical (e.g., Age, Fare) columns.

In my analysis script, I performed the following pandas operations: reading the CSV into a DataFrame with an index column set; printing the first five rows, structure info, 
and numerical statistics; accessing data via loc (by labels) and iloc (by positions), including single rows, slices, columns, 
and cells; filtering rows with a single Boolean condition (Age > 30) and a combined condition (Sex == 'female' AND Pclass == 1); 
adding a new column (FamilySize, derived from SibSp and Parch); removing an unnecessary column (Ticket); and grouping by Sex to compute the mean Age. 
From these operations, I observed that females had a slightly higher average age than males, 
and first-class female passengers were a small subset with potentially higher survival implications. 
Limitations include missing values in the Age column (about 20% are NaN), which could skew statistics, and the dataset's sample size (only 891 out of over 2,200 passengers), 
making it not fully representative of the entire ship. Additionally, some columns, such as Cabin, have many missing entries, which limits deeper analyses. 
Overall, the dataset provided a solid foundation for practising pandas techniques without requiring advanced preprocessing.

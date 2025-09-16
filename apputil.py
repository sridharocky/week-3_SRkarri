import pandas as pd         #importing the pandas library 

dataset = "https://raw.githubusercontent.com/melaniewalsh/Intro-Cultural-Analytics/master/book/data/bellevue_almshouse_modified.csv"
#data set taken from pandas -lab

#Reading the dataset from the url into a DataFrame named 'data'
data = pd.read_csv(dataset)
data_frame = data.copy()   
 #creating a copy of the original DataFrame to preserve the original data

def task_3():
    print("\nExercise 3:")  #prints the header exercise for clarity

    data_frame["gender"] = data_frame["gender"].astype(str).str.strip().str.capitalize()
    #cleans the "column": convert all values to string and removes leading/trailing spaces and 
    # capitalizes the first letter of each value

    print("Unique gender values:", data_frame["gender"].unique())
    #print the unique gender values after claening

    result = data_frame.groupby("gender")["age"].mean()
    #Group the data by gender and calcluate the average age for each gender
    print(result)

task_3()#callign the function
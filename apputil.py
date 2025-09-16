import pandas as pd         #importing the pandas library 

dataset = "https://raw.githubusercontent.com/melaniewalsh/Intro-Cultural-Analytics/master/book/data/bellevue_almshouse_modified.csv"
#data set taken from pandas -lab

#Reading the dataset from the url into a DataFrame named 'data'
data = pd.read_csv(dataset)
data_frame = data.copy()   
 #creating a copy of the original DataFrame to preserve the original data

def task_2():
    print("\nExercise 2: \n")   #printing header "exercise 2" for clarity

    result = data_frame.groupby("date_in").size().reset_index(name="total_admissions")
    #Grouping the data by the 'date_in' column, which represents admission dates,
    #counts the number of rows per date using size()
    #then resets the index to turn the grouped data back into a DataFrame

    print(result)   #prints the result to show how many admisisons at each date


task_2()
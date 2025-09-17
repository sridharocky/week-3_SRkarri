########################EXERCISE 1#######################

def fibonacci(n):             
    #Defining a function to calculate nth Fibonacci number
    if n == 0:
        # If n is 0, return 0(first Fibonacci number)
        return 0

    elif n == 1:
        #If n is 1, return 1 (second fibonacci number)
        return 1
    else:
        #Recursive case:
        #The nth Fibonacci number is the sum of the (n-1)th and (n-2)th numbers
        ##becasue current fib is sum of last 2 fibs
        return fibonacci(n-1) + fibonacci(n-2)

print("fibonacci(9)=", fibonacci(9))

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))




        ######################exercise2#########################################
def to_binary(n):
    #convert the integer n into its binary using bin() function
    #bin(n) returns a string like '0b10' ob means binary
    binary = bin(n).replace("0b","") #removes the "0b" prefix, leaving only the binarydigits
    #print the binary representaion
    return binary

#testing the function with examples

print(to_binary(2))# output should be 10





######################exercise 3 ##########################

import pandas as pd         #importing the pandas library 

dataset = "https://raw.githubusercontent.com/melaniewalsh/Intro-Cultural-Analytics/master/book/data/bellevue_almshouse_modified.csv"
#data set taken from pandas -lab

#Reading the dataset from the url into a DataFrame named 'data'
data = pd.read_csv(dataset)
data_frame = data.copy()   
 #creating a copy of the original DataFrame to preserve the original data


def task_1():
    #Defining a function to perfrom task1: analyzing missing values
    
    print("\n Exercise 1: \n") 
    
    missing_count = data.isnull().sum().reset_index() #count the number of missing(null) values in each column
    missing_count.columns = ["column","missing"]
    print(missing_count)    
     #prints the missing value counts
    
    sort_cols = missing_count.sort_values(
        by=["missing", "column"], 
        kind="mergesort"    ## 'kind="mergesort"' is used because it's a stable sort (preserves the order of equal elements).
    )["column"].tolist()
    
    return sort_cols


def task_2():
    print("\nExercise 2: \n")   #printing header "exercise 2" for clarity

    result = data_frame.groupby("date_in").size().reset_index(name="total_admissions")
    total_admissions = result["total_admissions"].sum()
    #Grouping the data by the 'date_in' column, which represents admission dates,
    #counts the number of rows per date using size()
    #then resets the index to turn the grouped data back into a DataFrame

    return result, total_admissions  #prints the result to show how many admisisons at each date


def task_3():
    print("\nExercise 3:")  #prints the header exercise for clarity

    data_frame["gender"] = data_frame["gender"].astype(str).str.strip().str.capitalize()
    #cleans the "column": convert all values to string and removes leading/trailing spaces and 
    # capitalizes the first letter of each value

    print("Unique gender values:", data_frame["gender"].unique())
    #print the unique gender values after claening

    result = data_frame.groupby("gender")["age"].mean()
    #Group the data by gender and calcluate the average age for each gender
    return result


def task_4():
    print("\nExercise4: \n")

    #checks if there are any missing values in the "profession" column
    if data_frame["profession"].isnull().any():
        print("Note: some entries have missing profession data.")

    #get the top 5 most common professions using value_counts()
    top_5 = data_frame["profession"].value_counts().head(5).index.tolist()
    return top_5


 #calling the function ot run
print(task_1())
print(task_2())
print(task_3())
print(task_4())

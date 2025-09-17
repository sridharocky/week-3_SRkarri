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
    print("\n Exercise 1: \n") 
    
    # Count missing values in each column (Series preserves column order)
    missing_count = data.isnull().sum()
    print(missing_count)
    
    # Sort only by number of missing values, keep dataset column order for ties
    sort_cols = missing_count.sort_values(kind="mergesort").index.tolist()
       
    return sort_cols


def task_2():
    print("\nExercise 2: \n")   #printing header "exercise 2" for clarity

    data['date_in'] = pd.to_datetime(data['date_in'], errors='coerce')

    # Extract year
    data['year'] = data['date_in'].dt.year

    # Group by year and count entries
    result = data.groupby('year').size().reset_index()

    # Rename columns
    result.columns = ['year', 'total_admissions']
    return result


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

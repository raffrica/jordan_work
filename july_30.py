import pandas as pd
# from io import StringIO


csv = pd.read_csv("gapminder_Canada.csv")
csv_numeric_column_names = csv.columns.tolist()[1:]


#abstracted printing function
def print_function(function_name, string_of_singular_function):
    def print_function_once(column_name):
        print("The {} for Column {}: {}".format(string_of_singular_function, column_name, 
              function_name(column_name)))
        
    [print_function_once(column_name) for column_name in csv_numeric_column_names]


# function that takes a column name (string) and produces the mean for that column
def mean_of_column(column_name):
    list_of_column = csv[column_name].values
    return sum(list_of_column) / len(list_of_column)


# function that takes a column name (string) and produces the variance for that column     
def variance_of_column(column_name):
    list_of_column = csv[column_name].values
    mean = mean_of_column(column_name)
    sum_of_squares = sum([(x-mean)**2 for x in list_of_column])
    final = sum_of_squares/(len(list_of_column)-1)
    return final
   
    
# function that prints strings for all the means of each column in csv DataStructure
def print_means():
    # excluded first column because non-numeric
    print_function(mean_of_column, "Mean")


# function that takes a column name (string) and produces the variance for that column  
def print_variances():
    print_function(variance_of_column, "Variance")
    
    
#print all 
def print_all_functions():
    print("\n")
    print_means()
    print_variances()
        

print_all_functions()

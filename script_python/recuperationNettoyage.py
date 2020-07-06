#Import the necessary libraries
import pandas as pd
import numpy as np
from datetime import date

#Getting Data from the web data.gov

immobilier19= pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/3004168d-bec4-44d9-a781-ef16f41856a2',sep = '|' ,)
immobilier18= pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/1be77ca5-dc1b-4e50-af2b-0240147e0346',sep = '|' ,)
immobilier17= pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/7161c9f2-3d91-4caf-afa2-cfe535807f04',sep = '|' ,)
immobilier16= pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/0ab442c5-57d1-4139-92c2-19672336401c',sep = '|' ,)
immobilier15= pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/09f013c5-9531-444b-ab6c-7a0e88efd77d',sep = '|' ,)
# Cleaning data

result_imm19 =immobilier19.drop(immobilier19.columns[[0,1,2,3,4,5,6,7,9,12,20,23,25,26,27,28,29,30,31,32,33,34,37,41,40]], axis = 1)
result_immobiler19 =result_immobilier.drop_duplicates(keep='first')
result_imm18 =immobilier18.drop(immobilier18.columns[[0,1,2,3,4,5,6,7,9,12,20,23,25,26,27,28,29,30,31,32,33,34,37,41,40]], axis = 1)
result_immobilier18 =result_imm18.drop_duplicates(keep='first')
result_imm17 =immobilier17.drop(immobilier17.columns[[0,1,2,3,4,5,6,7,9,12,20,23,25,26,27,28,29,30,31,32,33,34,37,41,40]], axis = 1)
result_immobilier17 =result_imm17.drop_duplicates(keep='first')
result_imm16 =immobilier16.drop(immobilier16.columns[[0,1,2,3,4,5,6,7,9,12,20,23,25,26,27,28,29,30,31,32,33,34,37,41,40]], axis = 1)
result_immobilier16 =result_imm16.drop_duplicates(keep='first')
result_imm15 =immobilier15.drop(immobilier15.columns[[0,1,2,3,4,5,6,7,9,12,20,23,25,26,27,28,29,30,31,32,33,34,37,41,40]], axis = 1)
result_immobilier15 =result_imm15.drop_duplicates(keep='first')

# concatenation of the data from 2015 to 2019
result = pd.concat([result_immobiler19, result_immobilier18, result_immobilier17,result_immobilier16,result_immobilier15])

# Droping the NAN rows for column  'Type local'
result_immobilier_v1 = result.dropna(subset=['Type local'])

#Metadata of our data
result_immobilier_v1.info() 

#Optimization function which checks the type and size of each column

def max_length(result_immobilier_v1):
   

    # Initializing data frames used to gather necessary info : 
    df_col_name = []  # df to store col names.
    df_col_dtype = []  # df to store col data type.
    df_max_length = []  # df to store the max for a col.
    df_min_length = []  # df to store the min for a col.
    df_before_dot = []
    df_after_dot = []

    df_header = ["Col Name", "Col Type", "Min" ,"Max", "Digit before .", "Digit after ."]  # df to display col name of final result.
    
    #Create a copy of the df:
    df = result_immobilier_v1.copy()
    
    # Entering FOR loop to process our df :
    for col in df:
        df_col_name.append(col)  # Stores current col name.
        
        nb_unique_values = len(df[col].unique())  # Count number of unique values for the current col.
        if nb_unique_values < 11:
            print("Column {} has {} unique values, it's worth considering data type category for this variable".format(col, nb_unique_values))
            nb_values = df[col].unique()
            print("Unique values for column {} are {}".format(col, nb_values), end='\n\n')
            
        # Case if column type is object:
        if df[col].dtypes.kind == 'O':
            df_col_dtype.append('object (nb caracters)')  # Store the data type for the current col.
            max = df[col].str.len().max()  # Get the max nbr of characters for the current col. 
            df_max_length.append(max)  # Stores the max value.
            min = df[col].str.len().min()  # Get the min nbr of characters for the current col. 
            df_min_length.append(min)  # Stores the max value.
            df_before_dot.append('N/A')
            df_after_dot.append('N/A')

        
        # Case if column type is integer :
        elif df[col].dtypes.kind == 'i':
            df_col_dtype.append('int64 (max min)')  # Store the data type for the current col.
            max = df[col].replace('None', 0).max()  # Get the max number of  the current col (NaN removed). 
            df_max_length.append(max)  # Stores the max value.
            min = df[col].replace('None', 0).min()  # Get the min number of the current col (NaN removed).
            df_min_length.append(min)  # Stores the min value.
            df_before_dot.append('N/A')
            df_after_dot.append('N/A')
            
        elif df[col].dtypes.kind == 'f':
            df_col_dtype.append('float64 (max min)') # Store the data type for the current col.
            max = df[col].replace('None', 0).max()  # Get the max  max number of current col (NaN removed). 
            df_max_length.append(max)  # Stores the max value.
            min = df[col].replace('None', 0).min()  # Get the min number of the current col (NaN removed).
            df_min_length.append(min)  # Stores the min value.
            # Count number of digits before and after the decimal point:
            nb_before = len(str(int(max)))
            df_before_dot.append(nb_before)
            df['AFTER DECIMAL'] = df[col].astype(str).str.split('.').str[1]
            nb_after = df['AFTER DECIMAL'].astype(str).apply(lambda x: len(x)).max()
#             nb_after = df[col].astype(str).str.split('.').str[1].max()
#             nb_after = len(str(int(nb_after)))
            df_after_dot.append(nb_after)
            
        # Case if column type is DATE TIME :
        elif df[col].dtypes.kind == 'M':
            df_col_dtype.append('date/time (oldest most recent)') # Store the data type for the current col.
            max = df[col].replace('None', 0).max()  # Get the max  max number of current col (NaN removed).
            df_max_length.append(max)
            min = df[col].replace('None', 0).min()  # Get the max  max number of current col (NaN removed).
            df_min_length.append(min)
            df_before_dot.append('N/A')
            df_after_dot.append('N/A')


            # Exiting FOR loop to display the results : 
    result = list(zip(df_col_name, df_col_dtype, df_min_length, df_max_length, df_before_dot, df_after_dot)) # Merges the lists containing col names & max values.
    df_result = pd.DataFrame(result, columns = df_header) # Creates df from merged list & title columns.
    
    display(HTML(df_result.to_html())) # Displays result as html table.

# END OF FUNCTION

max_length(result_immobilier_v1)

# Create today date 
today = date.today()
period = today.strftime("%d-%m-%Y")
print("period =", period)

#Create  csv file
filename = r"dataImmobilier_fr{}.csv".format(period)
filename
#Saving data as csv file
result_immobilier_v1.to_csv(filename,encoding='utf-8', index=False)
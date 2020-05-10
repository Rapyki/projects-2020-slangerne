
def initial_rename(df,varname):
    """ Renames 'OMRÅDE' to 'municipality' and 'TID' to 'year'. Also renames the data variable 'INDHOLD' to a chosen name

    Args:
        df (pd.DataFrame): pandas dataframe with the columns "year" and "municipality" as strings
        varname (String): the wanted name for the given variable for 'INDHOLD'

    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    
    
    df.rename(columns = {'OMRÅDE':'municipality'}, inplace=True)
    df.rename(columns = {'TID':'year'}, inplace=True)
    df.rename(columns = {'INDHOLD':varname}, inplace=True)
    

    return df


def quarter_to_year(df):
    """ Keeps only the first quarter observation if the dataset is quarterly, and also removes the Q notation, so only the year
    appears

    Args:
        df (pd.DataFrame): pandas dataframe with the column "year" as a string

    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    df['year'] = df['year'].astype(str) #Ensures the year variable is a string
    
    for year in df.year.str.contains('Q'): #checks whether the year variable is quarterly or yearly
        if year == True: # If it is quarterly the following code keeps only the first quarter 
            U = df.year.str.contains('Q1')
            df = df.loc[U == True] # keep only that one
            df.year = df.year.str[0:4] # deletes 'Q1'
            break
        else:
            continue #If the data is yearly this function does nothing
        
    return df


def sort_reset(df):
    """ Sorts after municipality and year. Also resets index

    Args:
        df (pd.DataFrame): pandas dataframe with the columns "year" and "municipality" as strings

    Returns:
        df (pd.DataFrame): pandas dataframe

    """
    df = df.sort_values(['municipality','year'])
    df.reset_index(drop=True, inplace=True)

    return df



def only_keep_municipalities_and_years(df,diff,startyear,endyear):
    """ Deletes all non-municipalities, and also Christiansø and Bornholm. This is done as these two municipalities are not
    included in all the collected datasets. It also restricts the period of the data series.

    Args:
        df (pd.DataFrame): pandas dataframe with the column "municipality" as a string, 
        diff (Int): as year variable input (Ras is measured in November while fx. population in january)
        startyear (Int): as the wanted starting year of the dataset
        endyear (Int): as the wanted end year of the dataset

    Returns:
        df (pd.DataFrame): pandas dataframe

    """
    df = quarter_to_year(df) #applies the above function to only look at yearly observations
    
    val_list = ['Region', 'Province', 'All Denmark','Christiansø','Bornholm']  #defines rows to remove
    
    # 
    for val in val_list:
        I = df.municipality.str.contains(val)
        df = df.loc[I == False] # keep everything else than the above rows

    #The following defines the sample period 
    df['year'] = df['year'].astype(int)
    df['year'] = df['year'] + diff
    df = df.loc[df['year'] <= endyear ]
    df = df.loc[df['year'] >= startyear ]
    df['year'] = df['year'].astype(str)

    return df


def row_chooser(df,varname,rownames, keep=True): #We have not gotten this function to work yet
    """ Chooses which rows to keep from af given variable

    Args:
        df (pd.DataFrame): pandas dataframe  
        varname: The variable to choose rows from
        rowname: the rows to either keep or drop
        keep=True: statement of whether to keep or drop the given rows

    Returns:
        df (pd.DataFrame): pandas dataframe

    """
    
    for val in rownames: 
        I = df.varname.str.contains(val)
        df = df.loc[I == keep] 
    
    return df
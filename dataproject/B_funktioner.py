
def quarter_to_year(df):
    """ keeps only the first quarter observation if the dataset is quarterly, also removes the Q notation, so only the year
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

def initial_rename(df,varname):
    """ renames 'OMRÅDE' to 'municipality' and 'TID' to 'year'. Also renames the data variable 'INDHOLD' to a chosen name

    Args:
        df (pd.DataFrame): pandas dataframe with the columns "year" and "municipality" as strings
        varname: the wanted name for the given variable for 'INDHOLD'

    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    
    
    df.rename(columns = {'OMRÅDE':'municipality'}, inplace=True)
    df.rename(columns = {'TID':'year'}, inplace=True)
    df.rename(columns = {'INDHOLD':varname}, inplace=True)
    

    return df


def sort_reset(df):
    """ sorts after first municipality and then year. Also resets index

    Args:
        df (pd.DataFrame): pandas dataframe with the columns "year" and "municipality" as strings

    Returns:
        df (pd.DataFrame): pandas dataframe

    """
    df = df.sort_values(['municipality','year'])
    df.reset_index(drop=True, inplace=True)

    return df



def only_keep_municipalities_and_years(df,forskel,startaar,slutaar):
    """ delete all non-municipalities, and alså Christiansø and Bornholm

    Args:
        df (pd.DataFrame): pandas dataframe with the column "municipality" as a string, 
        forskel (int) as year variable input (Ras is measured in November while fx. population in january)
        startaar (int) as the wanted starting year of the dataset
        slutaar (int) as the wanted end year of the dataset
        

    Returns:
        df (pd.DataFrame): pandas dataframe

    """
    df = quarter_to_year(df) #applies the above function
    # Delition list
    val_list = ['Region', 'Province', 'All Denmark','Christiansø','Bornholm']  #defines rows to remove
    
    # 
    for val in val_list:
        I = df.municipality.str.contains(val)
        df = df.loc[I == False] # keep everything else than the above rows


    #the following keeps the sample period
    df['year'] = df['year'].astype(int)
    df['year'] = df['year'] + forskel
    df = df.loc[df['year'] <= slutaar ]
    df = df.loc[df['year'] >= startaar ]
    df['year'] = df['year'].astype(str)


    return df


def row_chooser(df,varname,rownames, keep=True): #We have not gotten this function to work yet
    """ chooses which rows to keep from af given variable

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









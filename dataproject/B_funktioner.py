def only_keep_municipalities(df):
    """ delete all non-municipalities

    Args:
        df (pd.DataFrame): pandas dataframe with the column "municipality" as a string

    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    
    for val in ['Region', 'Province', 'All Denmark']:
        
        I = df.municipality.str.contains(val)
        df = df.loc[I == False] # keep everything else
    
    return df

def quarter_to_year(df):
    """ keeps only the first quarter observation  

    Args:
        df (pd.DataFrame): pandas dataframe with the column "year" as a string

    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    
    for val in ['Q1']: 
        
        I = df.year.str.contains(val)
        df = df.loc[I == True] # keep only that one
        df.year = df.year.str[0:4]
    
    return df

def initial_rename_sort(df):
    """ renames 'Område' to 'municipality' and 'tid' to 'year'. Afterwords it sorts after first municipality and next year

    Args:
        df (pd.DataFrame): pandas dataframe with the columns "year" and "municipality" as strings

    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    
    df.rename(columns = {'OMRÅDE':'municipality'}, inplace=True)
    df.rename(columns = {'TID':'year'}, inplace=True)
    df.sort_values(['municipality','year'])

    
    return df








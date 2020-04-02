def only_keep_municipalities_and_years(df,forskel,startaar,slutaar):
    """ delete all non-municipalities

    Args:
        df (pd.DataFrame): pandas dataframe with the column "municipality" as a string, forskel (int) as year of datarep
        startaar as int and slutaar as int

    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    
    for val in ['Region', 'Province', 'All Denmark']:
        
        I = df.municipality.str.contains(val)
        df = df.loc[I == False] # keep everything else

    
    df['year'] = df['year'].astype(int)
    df['year'] = df['year'] + forskel
    df = df.loc[df['year'] <= slutaar ]
    df = df.loc[df['year'] >= startaar ]
    df['year'] = df['year'].astype(str)
    

    
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

def initial_rename(df):
    """ renames 'Område' to 'municipality' and 'tid' to 'year'. Afterwords it sorts after first municipality and then year

    Args:
        df (pd.DataFrame): pandas dataframe with the columns "year" and "municipality" as strings

    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    
    
    df.rename(columns = {'OMRÅDE':'municipality'}, inplace=True)
    df.rename(columns = {'TID':'year'}, inplace=True)
    

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






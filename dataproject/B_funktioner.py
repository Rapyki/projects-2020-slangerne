
def quarter_to_year(df):
    """ keeps only the first quarter observation if the dataset is quarterly, also removes the Q notation
    

    Args:
        df (pd.DataFrame): pandas dataframe with the column "year" as a string

    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    df['year'] = df['year'].astype(str)
    
    for year in df.year.str.contains('Q'):
        if year == True:
            U = df.year.str.contains('Q1')
            df = df.loc[U == True] # keep only that one
            df.year = df.year.str[0:4]
            break
        else:
            continue
        
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



def only_keep_municipalities_and_years(df,forskel,startaar,slutaar):
    """ delete all non-municipalities

    Args:
        df (pd.DataFrame): pandas dataframe with the column "municipality" as a string, 
        forskel (int) as year variable input (Ras is measured in November while fx. population i january)
        startaar (int) as the wanted starting year of the dataset
        slutaar (int) as the wanted end year of the dataset
        keeps only the first quarter observation if the dataset is quarterly, also removes the Q notation

    Returns:
        df (pd.DataFrame): pandas dataframe

    """
    df = quarter_to_year(df)
    # Delition list
    val_list = ['Region', 'Province', 'All Denmark']
    
    # 
    for val in val_list:
        I = df.municipality.str.contains(val)
        df = df.loc[I == False] # keep everything else


    
    df['year'] = df['year'].astype(int)
    df['year'] = df['year'] + forskel
    df = df.loc[df['year'] <= slutaar ]
    df = df.loc[df['year'] >= startaar ]
    df['year'] = df['year'].astype(str)


    return df









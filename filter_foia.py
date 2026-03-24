import pandas as pd

def filter_foia(df_raw, agency, target_col_names, entity):
    """Filter data from foia.gov to a specific agency. 
    
    Parameters
    --------------
    df_raw : pandas dataframe
        Can be any dataframe. I downloaded data from foia.gov/data as csv
        and converted it into pandas dataframe. 
    agency: string
        Name of the agency or "All agencies" as it appears in foia.gov
    target_col_names: list of strings
        List of columns to keep
    entity: string
        String you want to insert before each column name to identify which 
        agency it belowngs to (e.g. "VA")
        
    Returns
    --------------
    df_filtered: pandas dataframe
        A dataframe filtered to a specific agency or All agencies with labeled
        column names
    """
    
    df_filtered = df_raw[df_raw['Agency']==agency]
    df_filtered = df_filtered[target_col_names]
    for col in target_col_names:
        df_filtered = df_filtered.rename(columns={col: f"{entity} {col}"})
    df_filtered = df_filtered.rename(columns={f"{entity} Fiscal Year": 
                                              "Fiscal Year"})
    df_filtered = df_filtered.sort_values("Fiscal Year").reset_index(drop=True)
    df_filtered['Fiscal Year'] = pd.to_datetime(df_filtered['Fiscal Year'],
                                                format='%Y')
    return df_filtered


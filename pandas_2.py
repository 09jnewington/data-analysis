import numpy as np
import pandas as pd

def cities():
    return pd.DataFrame(np.random.randint(1, 10, (5, 2)), columns=['Population', 'Total Area'], index=['Helskinki', 'Oula', 'Tampere', 'X2', 'X3'])

def power_of_series(series: pd.Series, k:int):
    df = pd.DataFrame(index = series.index)
    for i in range(1, k+1):
        df[i] = series**i
    df.columns = [i for i in range(1, k+1)]
    return df

def mun_finland():
    return pd.read_csv('/workspaces/data-analysis/.local/data/municipal.tsv', sep='\t', index_col=0).loc["Akaa":"Äänekoski"]


def swedish_and_foreigners():
    df = mun_finland()
    df = df[(df['Share of Swedish-speakers of the population, %']> 5) & (df['Share of foreign citizens of the population, %'] > 5)]
    df = df[['Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %']]
    return df


def growing_populations():
    df = mun_finland()
    growers =  df['Population change from the previous year, %'] > 0
    return growers.mean()

def subsetting_by_loc():
    df = mun_finland()
    return df.loc[:, ['Population', 'Share of Swedish-speakers of the population, %']]

def subsetting_by_positions():
    df = pd.read_csv('/workspaces/data-analysis/.local/data/UK-top40-1964-1-2.tsv', sep='\t')
    df = df.loc[:, ['Title', 'Artist']]
    return df.iloc[0:11]

def snow_depth():
    df = pd.read_csv('/workspaces/data-analysis/.local/data/kumpula-weather-2017.csv')
    return df['Snow depth (cm)'].max()

def average_temperature():
    df = pd.read_csv('/workspaces/data-analysis/.local/data/kumpula-weather-2017.csv')
    return df[df.loc[:, 'm'] == 7]['Air temperature (degC)'].mean()

def below_zero():
    df = pd.read_csv('/workspaces/data-analysis/.local/data/kumpula-weather-2017.csv')
    df2 = df['Air temperature (degC)'] < 0
    return sum(df2)


def cyclists():
   df =  pd.read_csv('/workspaces/data-analysis/.local/data/Helsingin_pyorailijamaarat.csv', sep=';')
   df = df.dropna(how='all')
   df = df.dropna(how='all', axis=1)
   return df


def missing_value_types():
    data = {
        "State": ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"],
        "Year of independence": [np.nan, 1917, 1776, 1523, np.nan, 1992],
        "President": [np.nan, "Niinistö", "Trump", np.nan, "Steinmeier", "Putin"],
    }
    df = pd.DataFrame(data)
    df.set_index('State', inplace=True)
    return df

def special_missing_value():
    df = pd.read_csv('/workspaces/data-analysis/.local/data/UK-top40-1964-1-2.tsv', sep='\t')
    df.replace('New', np.nan, inplace=True)
    df.replace('Re', np.nan, inplace=True)
    df['LW'] = pd.to_numeric(df['LW'], errors='coerce')
    return df[df['Pos'] > df['LW']]


full_names = pd.Series(["Donald Trump", "Theresa May", "Angela Merkel", "Vladimir Putin"])
full_names.str.split(expand=True)

def split_date():
    df =  cyclists()
    date_split = df['Päivämäärä'].str.split(expand=True)
    date_split.columns = ["Weekday", "date", "month", "year", "hour"]
    day_mapping = {'ma':'mon', 'ti':'tue', 'ke':'wed'}
    date_split["Weekday"] = date_split["Weekday"].map(day_mapping)
    date_split['hour'] = date_split['hour'].str[:2].astype(int)
    return date_split




def clean_data():
    df = pd.read_csv('/workspaces/data-analysis/.local/data/presidents.tsv', sep='\t')
    df['Start'] = df['Start'].str[:4].astype(int)
    df['Last'] = pd.to_numeric(df['Last'], errors='coerce')
    df['Seasons'] = df['Seasons'].str.replace('two', '2').astype(int)
    df['President'] = df['President'].str.split(',').map(lambda x: " ".join(x[::-1])).str.strip()
    df['Vice-president'] = df['Vice-president'].str.split(',').map(lambda x: " ".join(x[::-1])).str.strip().str.title()
    
    df = df.astype(
        {
            "President": "object",
            "Start": "int",
            "Last": "float",
            "Seasons": "int",
            "Vice-president": "object",
        }
    )

    return df

print(clean_data())
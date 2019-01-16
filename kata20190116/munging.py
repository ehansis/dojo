import pandas as pd


def weather():
    df = pd.read_fwf('weather.dat', skip_empty_rows=True, dtype=str)
    for col in ['Dy', 'MxT', 'MnT']:
        df[col] = pd.to_numeric(df[col].str.replace('*', ''), errors='coerce')
    df = df.dropna(subset=['Dy']).set_index('Dy')
    return df


def analyze(df):
    return (df['MxT'] - df['MnT']).idxmax()

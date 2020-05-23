import logging
import os

import pandas as pd
from numpy import where

import download

if not os.listdir(download.data_directory):
    download.download_all()


def _dataframe_from_download_name(name: str):
    try:
        url = download.datasets[name]
    except KeyError as e:
        logging.error('Not a valid dataset name: %s', name)
        raise e
    data_path = os.path.join(
        download.data_directory,
        os.path.basename(url)
    )
    return pd.read_csv(data_path)


def load_us_mobility() -> pd.DataFrame:
    df = _dataframe_from_download_name('mobility_data')

    df.rename(columns={'sub_region_1': 'state', 'sub_region_2': 'county'}, inplace=True)

    is_us_county = ((df['country_region_code'] == 'US') & ~(df['state'].isnull()) & ~(df['county'].isnull()))
    df = df[is_us_county]
    df = df[df['county'].apply(lambda x: 'county' in str(x).lower())]
    df['county'] = df['county'].str.replace(' County', '')

    select_columns = [
        'state',
        'county',
        'date',
        'retail_and_recreation_percent_change_from_baseline',
        'grocery_and_pharmacy_percent_change_from_baseline',
        'parks_percent_change_from_baseline',
        'transit_stations_percent_change_from_baseline',
        'workplaces_percent_change_from_baseline',
        'residential_percent_change_from_baseline',
    ]
    return df[select_columns]


def load_election_results_2016() -> pd.DataFrame:
    """See election metadata markdown for more info on columns"""
    df = _dataframe_from_download_name('election_data')
    select_columns = [
        'state',
        'county',
        'fips',
        'trump16',
        'clinton16',
        'otherpres16',
        'demsen16',
        'repsen16',
        'othersen16',
        'demhouse16',
        'rephouse16',
        'otherhouse16',
        'demgov16',
        'repgov16',
        'othergov16',
        'total_population',
        'cvap',
        'white_pct',
        'black_pct',
        'hispanic_pct',
        'nonwhite_pct',
        'foreignborn_pct',
        'female_pct',
        'age29andunder_pct',
        'age65andolder_pct',
        'median_hh_inc',
        'clf_unemploy_pct',
        'lesshs_pct',
        'lesscollege_pct',
        'lesshs_whites_pct',
        'lesscollege_whites_pct',
        'rural_pct',
        'ruralurban_cc',
    ]

    df = df[select_columns]
    df['perc_dem_pres_2016'] = df['clinton16']/df['total_population']
    df['perc_rep_pres_2016'] = df['trump16']/df['total_population']
    df['pres_2016_majority'] = where(
        df['perc_dem_pres_2016'] > df['perc_rep_pres_2016'],
        'D',
        'R'
    )
    return df


def load_combined_dataset() -> pd.DataFrame:
    mobility_measures = [
        'retail_and_recreation_percent_change_from_baseline',
        'grocery_and_pharmacy_percent_change_from_baseline',
        'parks_percent_change_from_baseline',
        'transit_stations_percent_change_from_baseline',
        'workplaces_percent_change_from_baseline',
        'residential_percent_change_from_baseline',
    ]

    mobility = load_us_mobility()
    agg_mobility = mobility.groupby(['state', 'county'])[mobility_measures].mean()
    df = agg_mobility.merge(load_election_results_2016(), on=('state', 'county'))
    return df


if __name__ == '__main__':
    df = load_election_results_2016()

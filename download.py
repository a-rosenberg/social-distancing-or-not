"""
Pull raw dataset to data directory
"""
import os
import logging
import requests

data_directory = os.path.join(os.path.dirname(__file__), 'data')
datasets = {
    'election_data': 'https://raw.githubusercontent.com/MEDSL/2018-elections-unoffical/master/election-context-2018.csv',
    'election_metadata': 'https://raw.githubusercontent.com/MEDSL/2018-elections-unoffical/master/election-context-2018.md',
    'mobility_data': 'https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv',
}


def download_all():
    if not os.path.isdir(data_directory):
        os.mkdir(data_directory)

    for name, url in datasets.items():
        logging.info('downloading %s ... ', name)
        landing_path = os.path.join(data_directory, os.path.basename(url))
        response = requests.get(url)
        with open(landing_path, 'w') as fid:
            fid.write(response.text)

    logging.info('complete.')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    download_all()
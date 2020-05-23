"""
EDA to create some leads
"""

from cleaned_datasets import load_combined_dataset

import matplotlib.pyplot as plt
plt.style.use('ggplot')



if __name__ == '__main__':
    df = load_combined_dataset()
    mobility_measure = 'retail_and_recreation_percent_change_from_baseline'

    voting = [
        df.loc[df['pres_2016_majority'] == 'R', mobility_measure],
        df.loc[df['pres_2016_majority'] == 'D', mobility_measure],
        ]

    plt.hist(voting[0], bins=15, color='red')
    plt.show()

    plt.hist(voting[-1], bins=15, color='blue')
    plt.show()

    plt.hist(voting, 30, stacked=True, density=True)
    plt.show()



"""
Simple correlation analysis for election and mobility combined dataset
"""
from cleaned_datasets import load_combined_dataset

df = load_combined_dataset()

corr = df.corr()

print(df.corr()['retail_and_recreation_percent_change_from_baseline']['perc_dem_pres_2016'])
print(df.corr()['retail_and_recreation_percent_change_from_baseline']['perc_rep_pres_2016'])
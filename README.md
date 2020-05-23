# Social Distancing... Or Not

## Setup
1. Run `download.py` to pull latest datasets from Google Mobility Reports and MIT Election Lab.
1. Now play with the `exploratory_*.py` files because that's all I've done so far. 
1. That is it.

## EDA
Look at correlations in `exploratory_correlations.py`.  It appears to me that an increase in percent voting for 
Trump in 2016 is positively correlated (a weak 0.162) with positive average change in average post-covid mobility 
to non-essential locations ("Mobility trends for places like restaurants, cafes, shopping centers, theme parks, museums, 
libraries, and movie theaters") as described in the Google Mobility Reports [Documentation](https://www.google.com/covid19/mobility/data_documentation.html?hl=en).

More dramatic is the negative correlation between percent voting democratic in the 2016 and this type of non-essential 
travel (-0.356). 
 
## So what?
This isn't enough data to make any conclusions from; however, it's interesting so help me look into this further
by further exploring the data and looking for other relevant data sources. 

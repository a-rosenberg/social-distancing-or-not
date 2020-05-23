# Social Distancing... Or Not

## Setup
1. Run `download.py` to pull latest datasets from Google Mobility Reports and MIT Election Lab.
1. Now play with the `exploratory_*.py` files because that's all I've done so far. 
1. That is it.

## EDA
Look at correlations in `exploratory_correlations.py`.  It appears to me that an increase in percent voting for 
Trump in 2016 is positively correlated (a weak pearson-r =0.162) with average post-covid mobility
to non-essential locations ("Mobility trends for places like restaurants, cafes, shopping centers, theme parks, museums, 
libraries, and movie theaters") as described in the Google Mobility Reports [Documentation](https://www.google.com/covid19/mobility/data_documentation.html?hl=en).  More dramatic is the negative correlation between percent voting democratic in the 2016 and this type of non-essential travel (r=-0.356).  They must be close to collinear so not sure how to tease this apart. 

In actual numbers; in the 2277 counties that voted republican the average decrease in non-essential 
mobility is 12.9%, while the in the 435 counties that voted democrat the average decrease in mobility was 21.7%.  This could be the result of prevailing partisan ideals but it could also be the result of confounding variables like percent rural population (a variable we have in the election dataset) or simple population density (which can be teased apart in a more advanced analysis to be done at "not 2:29AM").  Anyways, finding the causal relationship wasn't really the point of the analysis but rather it was to test a hypothesis I developed from anecdotal evidence that the conservative people in my life (and on my feeds) seemed to be the majority of the dissent for COVID-19 mitigation techniques.  This was for reasons relating to the economy, higher tolerance for peronsal and public risk, disbelief in the science or even because of conspiracy theories. 
 
## So what?
This isn't enough data to make any conclusions from; however, it's interesting so help me look into this further
by further exploring the data and looking for other relevant data sources.

## What next?
- Look at other partisan variables? E.g., more recent congressional voting information (in the election datasets!)
- Account for possible counfounding variables.  Even Google warns: "*Location accuracy and the understanding of categorized places varies from region to region, so we don’t recommend using this data to compare changes between countries, or between regions with different characteristics (e.g. rural versus urban areas).*"
- Model this with something clever like a regression analysis.
- Find better datasets to describe adherence to social distancing (or masking or any COVID-19 mitigation technique).  It looks like there are some cool dashboards put out by
states; however the information is coming from for-profit companies like Unacast so the underlying data isn't available.

### Dataset Metadata
[MIT Election Lab](https://github.com/MEDSL/2018-elections-unoffical/blob/master/election-context-2018.md)

[Google Mobility Reports](https://www.google.com/covid19/mobility/data_documentation.html?hl=en)

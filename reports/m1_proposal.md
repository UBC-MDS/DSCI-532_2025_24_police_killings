---
editor_options: 
  markdown: 
    wrap: 72
---

# Group 24: Police Killings Dashboard Proposal

## Motivation and Purpose

Our Role: Data Scientist Consultancy Firm Target Audience: Government
officials, policymakers, general public Police use of excessive (and
lethal) force is a significant societal issue, often disproportionately
affecting underprivileged communities. A major challenge is the lack of
accessible, data-driven insights that can help raise awareness and
inform policy changes to mitigate instances of police brutality.

To address this, we propose developing a data visualization dashboard
that enables users to explore police killing incidents based on
demographic, geographic, and socioeconomic factors. This dashboard will
provide interactive insights into trends over time, highlight high-risk
locations, and analyze the correlation between demographic factors and
police use of force.

Our tool will allow government officials and policymakers to identify
systemic issues, help the general public understand disparities in law
enforcement practices, and support social justice organizations in
advocating for better law enforcement training and accountability
measures.

## Description of the Data

We will be analyzing a dataset containing 2,239 records with 11 variables, documenting police killings in the US from 2015-2016. This dataset is credited to The Guardian ([source](http://www.theguardian.com/thecounted)). Our goal is to explore the demographics of individuals affected by police violence and understand patterns in incidents.  

The dataset includes the following characteristics:  

- Victim demographics (e.g., `age`, `gender`, `raceethnicity`)  
- Incident date and time (`month`, `day`, `year`)  
- Geographic location of the incident (`state`, `city`, `streetaddress`, `latitude`, `longitude`)  
- Fatality circumstances (`classification`, `armed`)  

Data Processing and Engineering:  

- Geocoding: Convert street addresses into `latitude` and `longitude` using 'geopy' to enable heatmap visualizations.  
- Age Grouping: Categorize victims into age groups (`under 19`, `20-39`, `40-59`, `60+`) for better analysis.  
- Datetime Formatting: Combine `month`, `day`, and `year` into a single 'datetime' object for time-series analysis.  

By leveraging this dataset, we aim to identify demographic trends, highlight regions most affected by police violence, and uncover patterns in the circumstances of fatal encounters.

## Research Questions

## App Sketch and Description

![App Sketch](../img/sketch2.jpg)

The app consists of 4 plots that show the relationship between different
variables and the counts of police killings. From the four plots, one
plot shows a heat map over the map of the United States to display the
severity of police killings across all states; one horizontal bar plot
that displays the top 10 states that have the most police killings; one
stacked bar plot that shows the distribution of victims over
race/ethnicity and gender; one density plot that shows a time-series
distribution of police killings.

On the left hand side of the dashboard, users can interact with all the
plots by toggling multiple filters. The filters include the following:

-   Gender classes (i.e. Male, Female, and Non-conforming)

-   Race/ethnicity (i.e. White, Black, Hispanic/Latino, Asian/Pacific
    Islander, Native American, Arab-American, and Other)

-   Age groups (i.e. under 19, 20-39, 40-59, 60+)

-   Year (either 2015 or 2016)

By toggling the filters, users can visualize the distributions with
different combinations of configurations.

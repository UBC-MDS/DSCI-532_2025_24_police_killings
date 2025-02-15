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

Description of dataset:  

- 2239 rows, 11 columns (i.e. age, gender, raceethnicity, month, day, year, streetaddress, city, state, classification, armed)
- Police killings in the US from 2015-2016
- Dataset credit to the Guardian (http://www.theguardian.com/thecounted)
- Linkage: Use the variables to find demographic groups (e.g. race/ethnicity, gender, regions) that are most targeted by police violence.
- Engineering:
  - Geocoding address into longitude and latitude using geopy to help us visualize the heat map across the US.
  - Engineer age into different age groups (i.e. under 19, 20-39, 40-59, 60+)
  - Combine month, day, year into one datetime object for time-series plot

New Feature description:  

- Deceased’s identity: age, gender, raceethnicity
- Time of the police killings: month, day, year
- Geographic locations: state, city, streetaddress, latitude, longitude
- Deceased’s fatality situation: classification, armed

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

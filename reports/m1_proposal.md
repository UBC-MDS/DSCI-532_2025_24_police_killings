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
1. Geographical Concentration of Incidents:
Original Question: Which state and city have the most police killings?
Expanded Version: Among all documented cases of police killings, which state has the highest frequency of such incidents, and within that state (or nationwide), which city reports the most cases? Furthermore, what local factors or conditions might explain this geographic concentration? Consider elements such as local law enforcement policies, demographic patterns, socio-economic challenges, and the nature of community-police interactions.

2. Temporal Patterns in Police Killings:
Original Question: What month and week have the most police killings? What is the reason behind it?
Expanded Version: Analyzing the data over time, during which month of the year and which specific week (or day of the week) do police killings reach their peak? What potential factors could explain these temporal trends? Investigate possibilities such as seasonal influences, local events or protests, shifts in law enforcement strategies during certain periods, or other social and political dynamics that might contribute to the rise in incidents during these times.

3. Racial Disparities in Police Killings:
Original Question: What race has been killed the most? What is the reason behind it?
Expanded Version: When examining the data by race, which racial group is most frequently affected by police killings? What historical, socio-political, and systemic factors might be driving this disparity? Explore potential causes such as institutional bias, economic inequality, historical discrimination, neighborhood demographics, and broader systemic injustices that could contribute to the overrepresentation of this group in police violence statistics.
Each expanded question not only seeks to identify specific data points (e.g., which state, city, month, week, or race) but also encourages a deeper investigation into the contextual factors and underlying causes that may explain these patterns. This approach fosters a more comprehensive analysis and understanding of the complex nature of police killings."

4. Community-Police Relations
Original Question: How do community-police relations impact police killings?
Expanded Version: What is the relationship between community trust in law enforcement and the frequency of police killings? How do historical tensions, cultural differences, and systemic biases affect interactions between police and the communities they serve? Investigate the effectiveness of community policing initiatives, cultural competency training, and efforts to build trust and collaboration between law enforcement and local residents. Additionally, explore how community-led solutions and restorative justice practices could reduce police violence.

5. Weapon Use and Lethal Force
Original Question: What types of weapons are most commonly used in police killings?
Expanded Version: In incidents of police killings, what types of weapons are most frequently involved, and how does this vary by region or demographic group? Are there patterns in the use of lethal force, such as the prevalence of firearms versus less-lethal alternatives? Examine the role of police training, departmental policies, and situational factors (e.g., perceived threat levels) in determining the use of specific weapons. Furthermore, consider how public perception and legal frameworks around the use of force influence these outcomes.



## App Sketch and Description

![App Sketch](../img/sketch.png)

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

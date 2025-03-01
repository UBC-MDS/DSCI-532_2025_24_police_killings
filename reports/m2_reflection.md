Milestone 2 Reflection

- We have essentially completed all types of charts and functionalities from the sketch.

- Here are the improvements we have made differently than in our sketch:  

1. Horizontal Stacked Bar Chart:  

Implementation: We replaced the vertical stacked bar chart with a horizontal one to improve readability and accessibility. The vertical orientation was challenging to interpret due to the large number of categories, and the horizontal layout resolved this issue.  

Deviation from Proposal: The gender filter was removed after our data analysis revealed that the vast majority of victims were male, as gender-based analysis is less informative for our dashboard's purpose.  

2. Scatter Plot on Map:  

Implementation: Instead of a heatmap, we used a scatter plot on a map to visualize the geographic distribution of police killings. This approach provides a clearer and more intuitive representation of data density and location-specific trends.  

Deviation from Proposal: The heatmap was replaced because scatter plots on maps are more effective for spatial data interpretation and allow users to pinpoint specific incidents more easily.  

3. Enhanced Filtering Options:  

Implementation: We added filters for year, age and armed status (e.g. vehicle, firearm, knife).  

Deviation from Proposal: These filters were not initially planned but were added to improve interactivity and user control over the data, making the dashboard more dynamic and user-friendly.  

4. Top n States by Police Killings Plot:  

Implementation: The plot in the sketch is fixed at top 10 states while the one in the app is top n states, where n is a flexible user input. And we introduced an interaction between the top n states plot and time-series plot, enabling users to select specific states for its corresponding time series plot.  

Deviation from Proposal: These features were enhanced to provide more flexibility in analyzing state-level data, allowing users to explore trends and patterns across regions.  

5. Time Series Plot:  

Implementation: The time series plot now compares police killings across states instead of genders, as originally proposed. And we relocated the time series chart to the right side of the interface. Additionally, we introduce a top n states filter on the time-series (the user input on top n states control both the top n state bar plot and the time series plot).  

Deviation from Proposal: This change was made because state-level comparisons were deemed more relevant for understanding trends over time, given the limited variability in gender data. And Layout adjustment will improve the overall layout balance and ensure a more intuitive flow of information for users.  

6. Additional enhancements:  

  - Implemented a tab-based interface to allow users to seamlessly switch between two visualizations:
    - A geographical map displaying the distribution of police killings.  
    - A race distribution chart highlighting demographic breakdowns of police killings.   
  This feature will enhance user interactivity and provide a clearer comparative analysis of the data.  

  - Added interaction between the top states bar plot and the time series plot where users can select a bar from the bar plot and view its corresponding time-series in the time-series plot.  

- Advantage, limitations, good potential future improvements:  

Currently, our dashboard effectively provides clear and interactive visualizations of police killings, allowing users to explore trends based on demographic, geographic, and time-based factors. However, there are some limitations, such as performance issues with large datasets and a need for more contextual insights. Future improvements could include predictive analytics, real-time data updates, and enhanced filtering options for a more comprehensive analysis.
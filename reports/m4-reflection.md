# Milestone 4 Reflection

## Feedback Implementation

### Larger Feedback Items
1. **Map Scaling and Clarity**:
   - **Issue**: The map did not auto-fit to the right scale, and U.S. border lines were unclear, making it hard to identify regions without zooming out.
   - **Action Taken**: We implemented auto-scaling for the map to ensure it fits the screen when the dashboard is first loaded. We also enhanced border visibility by adjusting the map's styling.

2. **Summary Table for Key Insights**:
   - **Issue**: A summary table was suggested to highlight key insights for policymakers.
   - **Action Taken**: We added a summary table that aggregates critical data (e.g., total killings, demographic breakdowns) to provide a quick overview for users.

3. **State-Level Data**:
   - **Issue**: Incorporating state-level data was recommended for localized decision-making.
   - **Action Taken**: We added a state-level breakdown in the "Police Killings by State" section, allowing users to compare trends across states.

4. **Data Consistency (Year Selection)**:
   - **Issue**: The "Police Killing Victims by Month" plot included December 2015 data when only 2016 was selected.
   - **Action Taken**: We fixed the data filtering logic to ensure the plot only displays data for the selected year.

### Smaller Feedback Items
1. **Dropdown Menu Aesthetics**:
   - **Issue**: The dropdown font size and color scheme were distracting.
   - **Action Taken**: We reduced the font size and adjusted the color scheme to make the dropdown less visually dominant.

2. **Bar Chart Consistency**:
   - **Issue**: Bar chart orientations varied by variable (e.g., counts on x-axis for "Race" but y-axis for "Age Group").
   - **Action Taken**: We standardized bar chart orientations to ensure consistency across all variables.

3. **Pie Chart for State Distribution**:
   - **Issue**: A pie chart was suggested as an alternative visualization for state-level data.
   - **Action Taken**: We added a pie chart option alongside the bar chart for state distribution.

---

## Reflection on Dashboard Development

### Insights and Feedback
The feedback from Joel and peers was invaluable in refining our dashboard. Specifically, the suggestions to improve map scaling, add a summary table, and ensure data consistency significantly enhanced the usability and clarity of our app. The recommendation to incorporate state-level data was particularly insightful, as it aligns with the needs of policymakers and adds depth to our analysis.

### Support for Development
While the feedback was highly useful, we would have appreciated more guidance on optimizing performance for large datasets, as this was a challenge we encountered during implementation. Additionally, examples of advanced interactivity (e.g., linked brushing) would have been helpful for creating more dynamic visualizations.

### Implementation Since Milestone 3
Since Milestone 3, we have implemented the following:
- **Summary Table**: Added to provide a quick overview of key insights.
- **State-Level Data**: Incorporated to allow localized analysis.
- **Map Enhancements**: Improved scaling and border visibility.
- **Data Consistency**: Fixed filtering logic for year selection.
- **Aesthetic Improvements**: Adjusted dropdown styling and standardized bar chart orientations.

### Deviations from Proposal/Sketch
- **Pie Chart for State Distribution**: This was not part of our original proposal but was added based on feedback to provide an alternative visualization.
- **Summary Table**: Added to address feedback, as it was not initially planned but proved valuable for policymakers.

### Known Issues
- **Performance with Large Datasets**: The dashboard may experience slight delays when loading large datasets, especially on slower devices.

### Strengths and Limitations
- **Strengths**:
  - Intuitive and user-friendly interface.
  - Comprehensive visualizations (maps, bar charts, pie charts, summary tables).
  - Effective use of interactivity to explore data.
- **Limitations**:
  - Limited to data from 2015-2016.
  - Performance issues with large datasets.
  - Lack of advanced interactivity (e.g., linked brushing).

### Future Improvements
If we had more time, we would:
- Expand the dataset to include more recent years.
- Optimize performance for large datasets.
- Add advanced interactivity features (e.g., linked brushing, drill-down capabilities).
- Incorporate additional demographic variables (e.g., socioeconomic status).

---

## Conclusion
Overall, we are proud of the progress made on our dashboard and believe it effectively communicates critical insights about police killings in the U.S. The feedback from Joel and peers was instrumental in refining the app, and we look forward to continuing to improve it in the future.

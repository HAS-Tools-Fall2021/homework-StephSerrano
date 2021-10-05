### Stephanie Serrano###

**October 3rd, 2021**

**Assignment #6**
___
## Grade 
3/3 : Great work going through all of the examples, very thorough! I like the changes you made but would encourage you to also get more creative with this as these are all still pretty close to the examples I provided you in the starter code. The puprpose of making your own graphs is to plot whatever you think you need to know in order to make a better forecast. I do like how you used the plots in your logic though :) 

___

For your write up you should present your plots and for every plot provide a short summary of (1) how you made it, (2) why you made it and what it tells you.

Your submission should include at least:

**Example 1:** Timeseries of observed weekly flow values
![](assets/Serrano_HW6-d5bada46.md)
  - This figure shows all of the weekly flow values that have been observed throughout the entire data period. I copied the starter code and changed the colour of the graph from green to blue but it is made using the daily average flow as the y-axis values and the dates as the x-axis values.

**Example 2:** Time series of flow values from May 15, 1990 to Dec. 10, 2012
![](assets/Serrano_HW6-97b6bcb7.md)
  - This plot is the same as the one above but the x-axis range is limited to a specific date. I limited mine to January 26th, 2000 to February 1st, 2014. These dates were just randomly picked and have no significance.

**Example 3:** Boxplot of flows by month
![](assets/Serrano_HW6-5701eb6d.md)
  - This was made using seaborn (sns) to create a boxplot command using the sns.boxplot and defining the x-axis, y-axis, and the width of the lines in the boxplot. This was not changed from the starter code. This shows the distribution of the data throughout the entire time period. It shows the median (middle area), minimum (first quartile), and the max (third quartile) for each month.

**Example 4:** September flows for 1990 to 2000
![](assets/Serrano_HW6-dc91ef2e.md)
  - This plot shows the flow for the month of September through the years 1990 to 2000. The point of this plot is to compare the different flows through each year visually. Any range of years could have been chosen from 1989 to 2021 for any of the 12 months. Using September is handy to compare how the final days of Monsoon Season fared over a range of 10 years before I was born (Dec, 2000).

**Example 5:** scatter plot of 2000 flow vs 2001 flow for the month of December
![](assets/Serrano_HW6-e7b466fe.md)
  - This is a scatter plot of flow in the year 2000 vs. flow in the year 2001 for the month of December. This shows the relationship between the flow of December 2000 and December 2001. This can show the correlation between the two. The correlation in this plot is not too strong as there is no clean pattern between the two except for in the beginning of the month where it could be considered a negative, linear relationship. I chose to view the month of December mostly because that is my birth month but also because I have noticed that the end of December is normally more wet than the beginning which (if I am reading the plot correctly) seems to be true.

**Example 6:** Scatter plot of flow vs day for december using the magma colour palette
![](assets/Serrano_HW6-83f80b15.md)
  - This was done by first grabbing the data for the month of December and then screating a scatter plot using the data gathered for the month of December. This is a bubbleplot, a subset of a scatter plot. The bigger the bubble, the more common that flow value was for that given time period. The dots are coloured by the year. This shows us how common certain values were in each year for the month of December. This plot is showing me that the end of the month around the 30th had higher values of flow. The largest bubble hovers almost out of the plot, above the 30 mark, showing again that the end of December seems to have wetter days.

**Example 7:** Multipanel plot histograms of flow for November and December
![](assets/Serrano_HW6-fd8fd161.md)
  - This is a histogram for the flow in the months of November and December. A histogram shows the data over a certain period (this case being either November or December). Both have a positive skew, showing the count of lower log flow values was much higher than higher log flow values. This is useful for comparing two different months and their data over the entire time period. I chose November and December to stay consistent with me choosing the month of December in all of the last examples.

**Example 8:** Same as 7 but using a for loop to do all 12 months
![](assets/Serrano_HW6-8042224e.md)
  - This is the same as the example above except that it uses the data for all of the months. The subplots have to be specified through how many plots one wants to have. x, y where x is the amount of rows and y is the amount of columns. In this case (4, 3) provided 4 rows and 3 columns for 12 months of data. This was also all done in a for loop rather than creating a single plot individually for each month.

***Prediction:***
I think that the values will still continue to decrease but not in a rapid way. The first week will have a flow of **80 cfs** while the second week will have a flow of **75 cfs**. Trends for October showed that the cfs does not go as high as the month of Semptember or December normally do. Although the season has been more wet than the previous years and hints of snow have already fallen throughout the northern part of Arizona, I do not think that it will be enough to make a significant difference in the flow. Using the box plot from Example 5, October seems to not be as spread out as the month of September, further proving to me that the flows will be consistently around where I have been guessing and only decrease slowly (this seems arrogant, is probably going to end up being wrong now, and I will totally have to change my values significantly next week).

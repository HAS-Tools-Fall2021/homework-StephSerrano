### Stephanie Serrano
**September 19th, 2021**

**Assignment #4**

1. Provide a summary of the forecast values you picked and why. Include discussion of the quantitative analysis that lead to your prediction. This can include any analysis you complete but must include at least two histograms and some quantitative discussion of flow quantiles that helped you make your decision.
  - I am predicting that the flow will continue on a decreasing trend. The flow will be **90 cfs** for the first week and will decrease to **80 cfs** the second week. Looking at the 10th, 50th, and 90th percentile (which I don't know if I even did right), there is a decreasing pattern for the month of September. It dips into the 60's for cfs at the 10th percentile which leads me to think that the decrease will be more rapid than I initially expected. The 50th percentile says 157 cfs but recent patterns show that the flow has been in the upper 90's which heavily influenced my guess. The first histogram (hopefully) shows the the trend in the last 18 days and shows the flow being predominantly on the lower end with the highest count being around the 100 cfs mark. The second one is for the entire year (hopefully) and shows a similar trend with the flow being on the lower end.
- ![Histogram_1](.png)
- ![Histogram_2](.png)

2. Describe the variable flow_data:
  - What is it?
    - it is an array (numpy.ndarray)
  - What type of values is is composed of?
    - It is composed of integers
  - What is are its dimensions, and total size?
    - Dimensions:2
    - Size: 47796
    - Shape (for fun): 11949, 4

3. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?
  - 14 (77.8%)

4. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)
  - 2000: 624 (15.5%)
  - 2010: 1024 (38.6%)

5. How does the daily flow generally change from the first half of September to the second?
  - 218.6
  - 107.4

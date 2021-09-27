### Stephanie Serrano
**September 26th, 2021**

**Assignment #5**

***Prediction:***
I think that the flow will continue to decrease but because it seemed to have rained a fair amount throughout Arizona this past weekend, it will not be decreasing as much as I thought it would be. I think that the flow for the first week will be **85 cfs** and drop down to **80 cfs**. My reasoning is still mostly the same as last weeks. The month of September has a minimum value of 37.5 cfs and October has a minimum flow of 59.8 cfs over the entire data period but because it has been a relatively "wet" year, I do not think that the flow will drop that low quite yet and am staying in a similar range as last week. I also do not believe that there will be a drastic enough rain event to significantly push the flow beyond what I had originally predicted in the Week 1 Forecast. 

**Question 1:** Provide a summary of the data frames properties.
What are the column names + data types?
- agency_cd = object
- site_no = int64
- datetime = object
- flow = float64
- code = object
- year = int32
- month = int32
- day = int32

What is its index?
- 0-11956

**Question 2:** Provide a summary of the flow column including the min, mean, max, standard deviation and quartiles.
- Min: 19.0
- Mean: 340.881942
- Max: 63400.0
- Standard Deviation: 1391.168343
- Quartiles:
  - 25%: 93.475
  - 50%: 157.0
  - 75%: 214.0

**Question 3:** Provide the same information but on a monthly basis.

*January*
- Min: 158.0
- Mean: 691.002933
- Max: 63400.0
- Standard Deviation: 2708.527013
- Quartiles:
  - 25%: 201.0
  - 50%: 218.0
  - 75%: 285.0

*February*
- Min: 136.0
- Mean: 903.156652
- Max: 61000.0
- Standard Deviation: 3300.470852
- Quartiles:
  - 25%: 200.0
  - 50%: 238.0
  - 75%: 615.75

*March*
- Min: 97.0
- Mean: 919.477028
- Max: 30500.0
- Standard Deviation: 1625.606804
- Quartiles:
  - 25%: 178.000
  - 50%: 368.0
  - 75%: 1045.00

*April*
- Min: 64.9
- Mean: 295.596970
- Max: 4690.0
- Standard Deviation: 540.712365
- Quartiles:
  - 25%: 111.250
  - 50%: 140.0
  - 75%: 210.00

*May*
- Min: 46.0
- Mean: 104.410850
- Max: 546.0
- Standard Deviation: 50.394386
- Quartiles:
  - 25%: 77.050
  - 50%: 92.0
  - 75%: 117.50

*June*
- Min: 22.1
- Mean: 65.534949
- Max: 481.0
- Standard Deviation: 28.660493
- Quartiles:
  - 25%: 48.925
  - 50%: 60.0
  - 75%: 76.55

*July*
- Min: 19.0
- Mean: 108.447312
- Max: 5270.0
- Standard Deviation: 219.942070
- Quartiles:
   - 25%: 53.500
  - 50%: 71.0
  - 75%: 112.50

*August*
- Min: 29.6
- Mean: 171.500782
- Max: 5360.0
- Standard Deviation: 295.999467
- Quartiles:
  - 25%: 77.950
  - 50%: 116.0
  - 75%: 178.00

*September*
- Min: 37.5
- Mean: 170.820203
- Max: 5590.0
- Standard Deviation: 282.784408
- Quartiles:
  - 25%: 88.600
  - 50%: 118.0
  - 75%: 169.00

*October*
- Min: 59.8
- Mean: 144.094556
- Max: 1910.0
- Standard Deviation: 110.663378
- Quartiles:
  - 25%: 104.750
  - 50%: 124.0
  - 75%: 152.25

*November*
- Min: 117.0
- Mean: 203.198958
- Max: 4600.0
- Standard Deviation: 232.211365
- Quartiles:
  - 25%: 154.000
  - 50%: 174.0
  - 75%: 198.00

*December*
- Min: 155.0
- Mean: 331.986895
- Max: 28700.0
- Standard Deviation: 1080.358791
- Quartiles:
  - 25%: 190.000
  - 50%: 203.0
  - 75%: 226.00

**Question 4:** Provide a table with the 5 highest and 5 lowest flow values for the period of record. Include the date, month and flow values in your summary.

*5 highest:*
- 1993-01-08, 63400.0
- 1993-02-20, 61000.0
- 1995-02-15, 45500.0
- 2005-02-12, 35600.0
- 1995-03-06, 30500.0

*5 lowest:*
- 2012-07-01, 19.0
- 2012-07-02, 20.1
- 2012-06-30, 22.1
- 2012-06-29, 22.5
- 2012-07-03, 23.4

**Question 5:** Find the highest and lowest flow values for every month of the year (i.e. you will find 12 maxes and 12 mins) and report back what year these occurred in.

Month, Min, Max:
- Jan, 158.0, 63400.0
- Feb, 136.0, 61000.0
- March, 97.0, 30500.0
- April, 64.9, 4690.0
- May, 46.0, 546.0
- June, 22.1, 481.0
- July, 19.0, 5270.0
- Aug, 29.6, 5360.0
- Sep, 37.5, 5590.0
- Oct, 59.8, 1910.0
- Nov, 117.0, 4600.0
- Dec, 155.0, 28700.0

**Question 6:** Provide a list of historical dates with flows that are within 10% of your week 1 forecast value.

- 1991-12-15  240.0
- 1991-12-29  240.0     
- 1995-04-20  240.0  
- 2000-11-10  240.0     
- 2004-01-21  240.0    
- 2004-01-24  240.0    
- 2004-02-14  240.0     
- 2004-04-11  240.0    
- 2018-10-06  240.0

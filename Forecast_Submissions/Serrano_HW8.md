### Stephanie Serrano
**September 26th, 2021**

**Assignment #8**

____________
## Grade:
### 1. Forecast Submision: 
**3/3:** Nice work! Your plots look great and I'm glad you got something out of the in class review even if the peer review didn't give you much to go off. 

### 2. Graded Script
Refer to [the rubric](https://github.com/HAS-Tools-Fall2021/Course-Materials21/blob/main/Content/Starter_Codes/week7_code_review_rubric.md) for details on scoring: 
- **Readability:2.5/3** Good work with comments however your docstring is missing descriptions of all of the inputs and outputs of your function. Also your text descriptions in the doc strring should just be documenting what the function does generrically and not the process and reasoning behind it. 
- **Style:3/3** No Pep8 Errors. 
- **Code:2.5/3** Really nice work. I was able to run your code without any errors and I like thhe plots you made. Two comments: 
  - Month and start year are arguments to your function but they are not actually being used. Come see me and I'm happy to show you how to incroporate these as inputs. 
  - Also your 1 week and 2 week functions are are pretty redundant (i.e. they share a lot of the same lines of code). You could instaed try making one function where week1 or week2 is an argument to the function.  Again happy to show you how to do this if you stop by. 
____________

1. An explanation of how you generated your forecasts and why?
  - I generated my forecasts using a function that would pull out the flow value from a specific time in a year. I used October 18th, 2018 for the first week prediction and October 25th, 2018 for the second week. I chose the year 2018 because it was a weird "water year" similarly to how this year has been more "wet" in comparison to the last few years. The dates I chose were just the dates the streamflow predictions fall on this year.


2. The three graphs you are including with an explanation of why you chose these three graphs.
  - I chose a scatterplot, a daily flow, and a general time series of observed flow because that allows me to look at the trends that have occurred in previous years for the month of October and what the current trend seems to be as we begin to approach the end of the month.

![](assets/Serrano_HW8-07dde3a0.png)

![](assets/Serrano_HW8-5fd275b6.png)

![](assets/Serrano_HW8-70e66bdf.png)

3. A brief summary of what you got out of the peer evaluation. How did you make your script better based on the feedback you received?
  - The feedback I received reassured me that not everything I was doing was incorrect. Although there were many kind words in the evaluation, I wish there had been more suggestions as to what I could have added/changed to make my script more efficient or better although I understand that it is difficult to give coding advice. It was not until we did a peer-review in class did I learn there were some things I needed to change.


4. A summary of how you are using timeseries functionality in your script.
  - I used the timeseries functionality to plot the flow trend for the month of October in the year 2018.


5. Describe the part of your script that you are most proud of and why
  - I am just proud that I was able to figure out how to get a value to print out and the summary that I had included.

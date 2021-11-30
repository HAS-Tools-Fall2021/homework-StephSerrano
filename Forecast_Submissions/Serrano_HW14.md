### Steph Serrano
# FAIR Science - Week 14
_____
### Grade
3/3: Great work! I'm sorry you were not able to get it to run but FYI someone else chose this paper too and had similar enviroment issues as you. One of the most common issues with sharing code is environment differences across platforms. This actually could be related to the indentation errors that you saw too.  
___

1. What is the paper or project you picked? Include a title, a link the the paper and a 1-2 sentence summary of what its about.
  - Paper: "SMAP-HydroBlocks, a 30-m satellite-based soil moisture dataset for the conterminous US"
https://www.nature.com/articles/s41597-021-01050-2#Abs1
  - This paper is about the authours' creation of a high-resolution satellite-based surface soil moisture dataset across the United States using satellite data and over 1,192 observational sites.
2. What codes and/or data are associated with this paper? Provide any link to the codes and datasets and a 1-2 sentence summary of what was included with the paper (i.e. was it a github repo? A python package? A database? Where was it stored and how?)
  - https://github.com/chaneyn/HydroBlocks
  - https://github.com/NoemiVergopolan/SMAP-HydroBlocks_postprocessing
  - https://zenodo.org/record/5206725#.YaRNtNDMJPY / https://doi.org/10.5281/zenodo.5206725
  - The first GitHub link listed is the repository where the main code is on Python which includes their HydroBlocks/geospatial tools packages. The second and third link includes the raw data with instructions to convert the data into geographical coordinates for the first link.
3. Summarize your experience trying to understand the repo: Was their readme helpful? How was their organization? What about documentation within the code itself?
  - The ReadMe was straightforward on how to install their HydroBlocks program and their geospatial tools. There was a link  included in the ReadMe with a test dataset to make sure the install was successful. The code was also well documented throughout the script in a simple yet straight-forward manner.
4. Summarize your experience trying to work with their repo: What happened when you tried to run it? Where you successful? Why or why not?
  - I was not successful with running their code. Although I was able to create a new environment named HydroBlocks like the ReadMe mentioned, I could not get the code produce any of the figures shown throughout the paper. One issue, that was definitely not the main reason why I could not get it to work but was just super annoying, is that the main code is full of functions and the spacing (indents) was off for some reason so I had to manually go through a fix the indentation problem on hundreds of lines of code. I kept getting an error that the majority of the functions were not defined when I tried to call them in the interactive window. This issue could have stemmed from downloading the zip file with the data since I am notorious for struggling with geospatial data.
5. Summarize your experience working with the data associated with this research. Could you access the data? Where was it? Did it have a DOI? What format was it in?
  - I was able to access the data using the zenodo/DOI link (https://doi.org/10.5281/zenodo.5206725). I was able to download the zipfile and extract the data. There were two files that could be downloaded, one was Hydrological Response Unit (HRU) space while the other zipfile had NetCDF files.
6. Did this experience teach you anything about your own repo or projects? What suggestions would you give to the authors for how they could do better next time?
  - This experience taught me that spatial data is still something that I struggle with even though I thought I had debugged/figured out a previous map project in the past. The code itself for this project is straightforward and in theory can be easily manipulated as long as the environment and data files are created/imported properly.

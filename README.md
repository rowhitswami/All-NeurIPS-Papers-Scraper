# All NeurIPS Papers Scraper

A quick script to scrap and save all the published papers in [Neural Information Processing Systems](https://nips.cc/) (abbreviated as **NeurIPS** and formerly **NIPS**) from 1987 to 2019.

## Content
The script scrap and save the data in two files.
#### 1. papers.csv

![](https://i.imgur.com/G8atzkU.png)

#### 2. paper_authors.csv

![](https://i.imgur.com/IbIqlSR.png)

## Code
  - Clone the repo.
  
    ```git clone https://github.com/rowhitswami/All-NeurIPS-Papers-Scraper.git```
  - Change the directory.
  
    ```cd All-NeurIPS-Papers-Scraper```
## Usage
**```scrap_neurIPS_papers.py [-h] [-start START_YEAR] [-end END_YEAR]```**

```
Script to scrap NeurIPS Papers
optional arguments:
  -h, --help         show this help message and exit
  -start START_YEAR  The start year to scrap the papers
  -end END_YEAR      The end year to scrap the papers
  ```
### Example
  - Simply run script to scrap and save all the papers.
  
  ```python3 scrap_neurIPS_papers.py```
  - You can specify the range of years in which you want to scrap the papers. Example:
  
  ```python3 scrap_neurIPS_papers.py -start=2002 -end=2010```
  - Get the help
  
  ```python3 scrap_neurIPS_papers.py --help```

## Download the latest dataset
Well, you can skip all the headache to run the script and grab the latest dataset from here. Show your support by upvoting the dataset. 😊

#### [All NeurIPS Papers (Updated) - Kaggle](https://www.kaggle.com/rowhitswami/nips-papers-1987-2019-updated)

## Author

[![Rohit Swami](https://avatars1.githubusercontent.com/u/16516296?v=3&s=144)](https://rohitswami.com/) |
-|
[Rohit Swami](https://rohitswami.com/) |)

## License
[![Apache license](https://img.shields.io/badge/license-apache-blue?style=for-the-badge&logo=appveyor)](http://www.apache.org/licenses/LICENSE-2.0e)

Copyright 2020 Rohit Swami

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Credit
Data collection would not have been possible without [https://nips.cc](https://nips.cc). A huge thanks to **NeurIPS** for making the data public.

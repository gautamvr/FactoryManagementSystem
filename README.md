# Factory Management System

## Data analysis of BTS production line (Base Transceiver Station)

The main objective of this project is to improve the efficiency of the production line of BTS (Base Transceiver Station) by doing a set of data analysis procedures.

- Identified the key parameters (features) involved in the production line and used in the various testing phases.
- Extracted only the relevant features that were needed for predicting the result of the test pipeline. (Features that are highly correlated with the result set)
- Identified other features which are highly correlated with the key features upto a certain threshold.

### Data Used
This study was analyzed with production line data of 2 key BTS products (AHFIB and FRGY)

-  Total data of 2643 modules (Produced in a period of 1 week) were collected for the analysis
-  Data from 2 stages of Testing phase was collected in each module's production line.
-  Data of each submodule were also collected for 1 Transceiver module (2 Submodules in 1 BTS)



### Libraries used
- Numpy
- Pandas
- Seaborn
- MatplotLib
- scikit-learn

analyze the key electronic parameters in the testing of a BTS product (AHFIB and FRGY) and to provide a complete analysis by the correlation of the key parameters with all other testing parameters. With the help of various software libraries like pandas and numpy it was possible segregate the data into a collection of single dataframe which contains only therequired information for correlating the data.
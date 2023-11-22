# datasci_9_data_prep-


Error: I started working on this Nov.21 in Google Shell, but the next morning I kept getting this message. I waited two hours and still was left on the loading screen with no change.

<img width="799" alt="Screen Shot 2023-11-22 at 11 12 54 AM" src="https://github.com/malh718/datasci_9_data_prep-/assets/102617334/7742979a-223b-4a1c-bff4-7897b8cd90eb">

12:10pm - It has started working again, which I am very thankful for this Thanksgiving. 


## 1. Dataset Selection:
   
The dataset I have chosen is Cancer Rates in Lake County, Illinois. 

The second dataset I have chosen is Birth Statistics in Lake County, Illinois. 


## 2. Data Cleaning and Transformation Plan:

Brief Description of Cancer Rates- Lake County, Illinois
This dataset is looking at Rates of cancer present in Lake County, Illinois. Information included are FID, ZIP, Lunc_bronc, Breast_can, Urinary_sy, Prostate_C, and All_cancer. There is also shape area and shape length. All Cancer columns listed are at a rate per 100,000.

The ZIP is the zip codes present in Lake County, the Colorectal Cancer shows cancer in colon and intestines. Breast cancer signigfies breast cancer present in tissue. Lung_broc represents lung cancer present. Prostate_C represents prostate cancer. 

This dataset also has 27 rows and 10 columns.

Intended Machine Learning Task: Regression

Machine Learning Regression is suitable in this dataset because the Dependent variables in this case which are  Lunc_bronc, Breast_can, Urinary_sy, Prostate_C, and All_cancer are all continuous. What this means is that the independent and dependent variables will be studied and using machine learning an algorithm can determine potential results or outcomes. In this case. Using the information that you are giving it, it can make predictions on what is to come. So in this case, we will try to determine the potential rates of cancer for the population present in Lake County, Illinois based on location and other information. 

The indpendent variable in this case would be location.
The dependent variables are Colorectal cancer rate, breast cancer rate, Lung cancer rate, prostate cancer rate, and all cancer rate.

Clean and Transform:

<img width="356" alt="Screen Shot 2023-11-22 at 1 38 21 PM" src="https://github.com/malh718/datasci_9_data_prep-/assets/102617334/205dbdf5-5a99-4f61-a781-5be21059b79b">
No missing values

<img width="690" alt="Screen Shot 2023-11-22 at 1 43 20 PM" src="https://github.com/malh718/datasci_9_data_prep-/assets/102617334/9b5bc399-8b7a-404b-8723-13c5d2a2beb8">

<img width="470" alt="Screen Shot 2023-11-22 at 1 34 07 PM" src="https://github.com/malh718/datasci_9_data_prep-/assets/102617334/331281c8-8607-4694-b817-b95837e52ae1">
This drops the columnns that we do not need, and are not necessary. 

Brief Description of  Birth Statistics- Lake County, Illinois

This dataset looks at birth rates in Lake County, Illinois.

This dataset also has 27 rows and 10 columns.

The columns include LBW which is low birth rate and if a baby is less than 2500 grams that indicates a LBW. This is represented as a percentage. Next there is preterm. This looks at the percent of births that happened before they reached 37 weeks pregnancy. Next is Teen Birth. This looks at the rate of women who gave birth at the ages of 15,16,17,18 and 19. Next is birth rate. This again looks at the rate of people who give birth. Specifically, per every 1,000 women. And the last columns is 1st trimester of Care. This looks at the percent of women who got medical care and support within the first 13 weeks of their pregnancy. 

Intended Machine Learning Task: Regression
So for this specific example the Machine Learning Task is Regression. I am considering the  the Birth Rate as the dependent variable. And using these rates, the primary objective is to determine based on location and other independent variables such as the percentages I mentioned below, the potential number of births.

The indpendent variable is the ZIP code, LBW %, Preterm Birth Percentage, and 1st trimester of care %. The dependent variable in this machine learning regression task would be the Birth Rate. 

Clean and tranform:


<img width="491" alt="Screen Shot 2023-11-22 at 1 35 33 PM" src="https://github.com/malh718/datasci_9_data_prep-/assets/102617334/e375d4ae-2b72-4307-9123-693b9f046882">
This drops the columnns that we do not need, and are not necessary. 


<img width="441" alt="Screen Shot 2023-11-22 at 1 39 09 PM" src="https://github.com/malh718/datasci_9_data_prep-/assets/102617334/802d493e-9543-4aaf-9bb4-4a1595ae98b4">
No missing values 


<img width="315" alt="Screen Shot 2023-11-22 at 1 41 32 PM" src="https://github.com/malh718/datasci_9_data_prep-/assets/102617334/275f072d-072e-4942-bd89-52614e06bac5">
Just double cheking that if there are any missing values they will be dropped. We know there arent any because I did .shape and got the same number of columns and rows we started off with. 

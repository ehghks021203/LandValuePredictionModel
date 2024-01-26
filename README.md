# **LandValuePredictionModel**
> This project, initiated in February 2023, is currently in progress.\
> We participated in the **2023 Big Contest Competition** and **were awarded for** developing an AI model for predicting land value!


_Read this in other languages:_
_[한국어](README.ko-kr.md)_

------

## **Background**
The real estate market is rapidly growing and evolving in our society, making accurate prediction of land value crucial for various sectors such as real estate investment, urban planning, and asset management. The accurate prediction of land value plays a vital role for real estate investors, developers, government agencies, city planners, and citizens, providing benefits to all. 
<br/>
With recent advancements in artificial intelligence and machine learning technologies, there are new opportunities to enhance the accuracy and reliability of land value prediction based on massive datasets. 
<br/>
Therefore, the development of an AI model for land value prediction has become a realistic and essential task.

## **Objective and Significance**
The main objective of this project is to develop an AI model for predicting land value and use this model to forecast the future trends of the real estate market. 
<br/>
The goals include:
- Assisting real estate investors in making accurate investment decisions.
- Providing scientific evidence for decision-making in urban planning to support sustainable city development.
- Increasing transparency in the real estate market to maintain market integrity.

## **Scope of Analysis**
The key tasks performed in this project include:

### **Data Collection and Preprocessing**
We collected land-related data from various sources and conducted preprocessing to enhance data quality. The data includes `land characteristic information`, `land transaction data`, `population statistics`, and more, sourced from the Ministry of Land, Infrastructure and Transport.

### **AI Model Training**
We used XGBoost to train an AI model for predicting land value. The model considers various variables to predict land value, and we utilized large-scale datasets for model training and testing.

### **Model Evaluation and Performance Improvement**
We evaluated the performance of the trained model and conducted experiments to improve its performance if needed. Performance evaluation included metrics such as Root Mean Squared Error (RMSE) and Mean Absolute Percentage Error (MAPE).

### **Results Interpretation and Visualization**
We interpreted the model's results and presented them in an easily understandable manner through visualization. We used map visualization and graphs to visually represent land value prediction results.

### **Application and Expansion**
The trained AI model is designed to be applicable to various fields such as real estate market prediction, urban planning, and asset management. The data is accessible through a web page, providing accurate information for future land value predictions and supporting sustainable city development.

<br/>

## **Key Steps:**
**1. Data Collection and Dataset Creation:**
- We used the Ministry of Land, Infrastructure and Transport's `Land Transaction Report Inquiry Service`, `Land Characteristic Information`, `Land Price Change Rate`, and Statistics Korea's SGIS Open Platform `Population Statistics`, `Business Statistics` data.
- Further enhancements to features for accurate land value prediction are planned.

<br/>

**2. Data Analysis:**
- To understand the impact of each feature on actual transaction prices, we visualized relationships between features using `matplotlib` and `seaborn`.
- Correlation analysis and `box plots` were utilized to assess the relationships within the data.

<br/>

**3. Data Preprocessing:**
- Thorough preprocessing was conducted before inputting the data into the model.
- Tasks included handling missing values, removing outliers, and performing `One-Hot Encoding` for categorical variables.

<br/>

**4. Model Training using XGBoost:**
- We chose the `XGBoost` model to handle nonlinear relationships and interpret complex patterns within the data.
- The model was trained using a subset of the dataset.

<br/>

**5. Evaluation and Validation:**
- `RMSE` was used as the evaluation metric, supplemented by `Mean Absolute Percentage Error (MAPE)`.

<br/>

**6. Hyperparameter Tuning (Not Yet):**
- Hyperparameters were adjusted for optimal model performance.
- Algorithms such as `GridSearchCV`, `RandomSearchCV`, or `BayesSearchCV` were considered for tuning.

<br/>

**7. Deployment and Integration:**
- The model was deployed as a web service or application.
- [Land Price Prediction Web Service](https://blue.kku.ac.kr)

<br/>

## **Project Organization**
```
├── data
│   ├── seoul_data.csv  <= Dataset for the Seoul region
│   ├── seoul_data_add_place_100.csv  <= 100 data points with added surrounding place data
│   └── seoul_data_add_place_500.csv  <= 500 data points with added surrounding place data
├── model
├── notebooks
│   └── lvpm.ipynb      <= Jupyter notebooks. Data preprocessing and visualization, 
│                          model training, and tuning were performed here.
├── src
│   └── data
│       └── make_dataset.py  <= Python code for dataset creation.
└── README.md
```

<br/>

## **TODO:**
- Incorporate cumulative land price change rate data from the base date to the transaction date.
- Add features reflecting interest rates.
- Ensemble learning of XGBoost model and LSTM model.
- Consideration of the outlier selection method for the dataset.

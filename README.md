**End to End SPAM SMS Classification Project**

Link to the Live Server of my SPAM SMS Classifier Application:
https://spam-sms-classifier-dharmendra.streamlit.app/

**Objective**:
The primary objective of the SMS Spam Classification project is to develop a machine learning model capable of distinguishing between spam and non-spam (ham) SMS messages. This model aims to provide an efficient and automated way to filter out unwanted or potentially harmful text messages, ensuring a better user experience for mobile phone users.

**Approach**:
The project began with the acquisition of SMS spam classification data from Kaggle. This dataset posed several initial challenges, including the presence of null values and duplicate records. To address these issues, data preprocessing steps were undertaken:

  1. **Data Cleaning**: The initial dataset contained several columns with a high percentage of null values. To streamline the dataset, these columns were removed, 
     leading to a cleaner and more manageable dataset.

  2. **Duplicate Removal**: Duplicate records were identified and removed, retaining only the first occurrence of each message.

With a refined dataset, the project proceeded with feature engineering and exploratory data analysis (EDA):

  1. **Feature Extraction**: Numerical features were created from the text data, including character counts, word counts, and sentence counts. These features 
     provided valuable insights into the structure and content of the messages.

  2. **Exploratory Data Analysis (EDA)**: EDA was performed to gain a deeper understanding of the data. Key insights included the correlation between numerical 
     features and the distribution of message counts among spam and non-spam (ham) categories.

The project then transitioned to Natural Language Processing (NLP) for text data processing:

  1. **Text Preprocessing**: The text data was subjected to preprocessing steps, which involved converting text to lowercase, removing punctuation, and eliminating 
     common stopwords. These steps enhanced the quality of the text data for modeling.
  2. **Stemming**: A stemming process was applied to reduce words to their root forms, thereby improving text feature consistency.
  3. **TF-IDF Vectorization**: The processed text data was transformed into a TF-IDF vector matrix, creating a numerical representation suitable for model training.

For model development, various machine learning algorithms were evaluated:

  1. **Model Training**: A range of machine learning algorithms, including Logistic Regression, Support Vector Classifier (SVC), Random Forest Classifier, Decision 
     Tree, AdaBoost, Gradient Boosting, Gaussian Naive Bayes, Multinomial Naive Bayes, Bernoulli Naive Bayes, and XGBoost Classifier, were trained on the processed 
     data. Among these, Multinomial Naive Bayes and Random Forest Classifier emerged as top-performing models, achieving an accuracy of 96% and a precision score 
     of 100%.
  2. **Hyperparameter Tuning**: Hyperparameter tuning was explored to optimize model performance. Although Multinomial Naive Bayes did not exhibit significant 
     improvement with hyperparameter tuning, Random Forest Classifier's tuning was computationally expensive due to the extensive grid search.

To make the model accessible as a web application, the following steps were executed:

  1. **Deployment**: The model, along with required objects and files, was saved using the pickle module. A new project was created in PyCharm for deploying the 
     model as a web application.
  2. **Version Control**: All project files, including app.py, requirements.txt, and the saved model files, were organized within a GitHub repository for version 
     control and collaboration.
  3. **Deployment on Streamlit Cloud**: The model was successfully deployed on Streamlit Cloud, making it accessible to users through a web interface.

**Challenges**:
The project encountered several challenges, including data cleaning complexities, model selection, and hyperparameter tuning for certain algorithms. In particular, the computationally expensive nature of Random Forest Classifier hyperparameter tuning required careful consideration.

**Conclusion**:
The SMS Spam Classification project succeeded in creating an efficient machine learning model capable of distinguishing between spam and non-spam SMS messages. The model, trained with Multinomial Naive Bayes and Random Forest Classifier, achieved high accuracy and precision scores. Deployment on Streamlit Cloud made the model accessible and user-friendly, enabling users to classify SMS messages in real-time.

This project serves as a valuable tool for filtering unwanted SMS messages and contributes to improved mobile phone user experiences by safeguarding against spam and potentially harmful messages.

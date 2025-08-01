**SENTIMENT ANALYSIS WEB APP**

This Streamlit-based web application performs sentiment analysis on product reviews. Users can input review text, and the app predicts whether the sentiment is positive or negative, using a trained Naive Bayes classifier. The model was built using TF-IDF vectorization and trained on a labeled dataset of customer reviews, optimized for accuracy and clarity.
The app is designed to be simple, fast, and accessible—ideal for showcasing how machine learning can be applied to real-world consumer feedback.

**_Model Training & Preprocessing_**

Model training was conducted in Google Colab, including:
- Dataset cleaning and preprocessing (Datset taken from Kaggle)
- TF-IDF vectorization
- Model selection & tuning via GridSearchCV
- Handling class imbalance
- Exporting model & vectorizer as .pkl files

**_Colab Notebook_**

Or check the notebook in this repo: Model_training.ipynb

**_Streamlit App Deployment_**

The app was built using Streamlit and deployed via Streamlit Cloud.
Main features include:
- Text input and sentiment prediction
- Modular and readable code (app.py)
- Pickle-loaded model and vectorizer

**_Deployment_**

Live App: [Streamlit Cloud URL](https://sentimentanalysisappapp-j7fjrfgcxuuwg4tkqhqhfc.streamlit.app/)

Repo: [GitHub Repository](https://github.com/Eroor402/SentimentAnalysisStreamlitApp)

**_Acknowledgments_**

Built as part of a learning journey inspired by peer projects and instructor feedback.
Special thanks to collaborators and reviewers for valuable insights.

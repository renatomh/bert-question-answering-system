<h1 align="center"><img alt="BERT Question-Answering System" title="BERT Question-Answering System" src=".github/logo.svg" width="250" /></h1>

# BERT Question-Answering System

## 💡 Project's Idea

This is a simple implementation for a BERT Question-Answering System, in order to provide a CLI application which allow users to receive answers for questions based on contexts.

## 🔍 Features

* Getting answers for questions based on provided contexts;

### **Results evaluation**

Context: [Top 5 AgencyAnalytics Alternatives: Elevate Marketing Reporting](data/agency-analytics-alternatives-competitors.txt)

Model | deepset/bert-base-cased-squad2 | bert-large-uncased-whole-word-masking-finetuned-squad
--- | --- | ---
Question | Answer (Time) | Answer (Time)
What's the best analytics agency competitor? | Improvado (7.56s) | AgencyAnalytics (23.97 s)
What's AgencyAnalytics suitable for? | small-scale marketing agencies (7.77 s) | beginners and non-technical users (24.15 s)
What is one AgencyAnalytics use case? | Overview (7.55 s) | Whatagraph (23.85 s)
What is the top AgencyAnalytics alternative? | Improvado (7.72 s) | Elevate Marketing Reporting (23.98 s)
What is one of Improvado's most popular transformation functionalities? | the Marketing Common Data Model (7.63 s) | marketing analytics (25.74 s)

Context: [Google Ads Dashboard Overview & Metrics to Include](data/google-ads-dashboard.txt)

Model | deepset/bert-base-cased-squad2 | bert-large-uncased-whole-word-masking-finetuned-squad
--- | --- | ---
Question | Answer (Time) | Answer (Time)
What are Google Ads Dashboards? | Adwords dashboard or a Google Adwords dashboard (3.97 s) | a centralized hub where you can track and measure all the most important metric (11.73 s)
What are the benefits of Google Ads Dashboard? | actionable insights and immediate answers (3.89 s) | bring your data to life in an easily-digestible way (11.24 s)
What should be present in a Google Ads Dashboard? | metrics (4.28 s) | Metrics (11.36 s)
What metrics should be present in a Google Ads Dashboard? | most critical (3.99 s) | a centralized hub where you can track and measure (11.15 s)
What are the most critical metrics? | real-time (3.73 s) | saves time, minimizes the likelihood of errors (11.31 s)

Context: [What Are Data Silos and What Problems Do They Cause?](data/data-silos.txt)

Model | deepset/bert-base-cased-squad2 | bert-large-uncased-whole-word-masking-finetuned-squad
--- | --- | ---
Question | Answer (Time) | Answer (Time)
What are data silos? | How Do You Know You Have Data Silo (6.55 s) | A spreadsheet (19.51 s)
How Do You Know You Have Data Silo? | islands of business data that belong to a department or even an individual (6.58 s) | your departments are probably functioning as separate business units (20.10 s)
What causes data silos? | Growing organizations, poor data culture, and a lack of the right technology (6.66 s) | incomplete business data (19.52 s)
What are some Common Examples of Data Silos? | islands of business data that belong to a department or even an individual (6.58 s) | unhealthy competition and a toxic work environment (20.07 s)
What is the problem with data silos? | incomplete business data (6.32 s) | incomplete business data (19.15 s)
How to break down data silos? | part of a complete data management program (6.51 s) | ETL platform (19.94 s)

## 📝 Future Developemnt

Some interesting features which could be added to the application include:

* Web scraping to allow working with online data;
* Testing other models for performance/results;
* Unit testing;
* Better input validation;

## 🛠 Technologies

During the development of this project, the following techologies were used:

- [Python](https://www.python.org/)
- [Hugging Face](https://huggingface.co/)

## 💻 Project Configuration

### Make sure to install the required packages/libs before running the script

#### * Note that the command to install PyTorch can change according to the machine where the project is being executed. Please, make sure to check the correct installation instructions for your environemnt on [PyTorch's instalation page](https://pytorch.org/get-started/locally/).

```bash
$ pip install -r requirements.txt
```

## ⏯️ Running

To run the application locally, execute the following command on the root directory.

#### * Note that the first time you run the application, if you haven't downloaded the selected model yet, it might take a long time to download it, depending on the selected model. After the first run, the model binary file should be cached in your machine, and it should load faster
#### ** Update the "DATA_SOURCE_NAME" to select the file with context for which you want to ask questions

```bash
$ python main.py
```

### Documentation:
* [Start Locally | PyTorch](https://pytorch.org/get-started/locally/)
* [How to Build Q&A Models in Python (Transformers)](https://www.youtube.com/watch?v=scJsty_DR3o&t=913s)

## 📄 License

This project is under the **MIT** license. For more information, access [LICENSE](./LICENSE).

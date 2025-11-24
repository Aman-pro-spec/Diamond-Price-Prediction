<div align="center">

  <h1>💎 End-to-End Diamond Price Prediction System</h1>
  
  <p>
    <strong>A production-ready Machine Learning system for real-time automated diamond valuation.</strong>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge" alt="Maintained">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" alt="License">
    <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Status">
  </p>
  
</div>

<br />

## 📝 About The Project

The traditional diamond valuation process is manual, time-consuming, and prone to human subjectivity. This project solves this problem by automating price estimation based on physical attributes like **Carat, Cut, Color, and Clarity**.

I have architected a production-ready Machine Learning system that streamlines the valuation process, providing instant and objective price estimates for businesses and buyers.

### ✨ Key Features

* **🔄 Automated Data Ingestion:** Systematically ingests raw data from various sources.
* **⚙️ Robust Pipelines:** Transforms data using automated pipelines that handle ordinal encoding and scaling seamlessly.
* **🧠 High-Accuracy Regression:** Trains a sophisticated Regression model to ensure precise valuations.
* **💻 Interactive Web Interface:** Predicts prices in real-time via a user-friendly frontend.

---

## 🛠️ Built With

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
* ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
* ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
* ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

---

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites

* Python 3.8 or higher

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/your_username/diamond-price-prediction.git](https://github.com/your_username/diamond-price-prediction.git)
    cd diamond-price-prediction
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application**
    ```bash
    python app.py
    ```
    
5.  **Access the UI**
    Open your browser and go to `http://127.0.0.1:5000`

---

## 📂 Project Structure

```text
├── artifacts/          # Stores generated models and preprocessors
├── notebook/           # Jupyter notebooks for EDA and experimentation
├── src/                # Source code for the pipeline
│   ├── components/     # Data Ingestion, Transformation, Model Trainer
│   ├── pipeline/       # Prediction and Training pipelines
│   ├── logger.py       # Custom logging setup
│   ├── exception.py    # Custom exception handling
│   └── utils.py        # Utility functions
├── templates/          # HTML templates for Flask
├── app.py              # Application entry point
├── requirements.txt    # Project dependencies
├── setup.py            # Package setup configuration
└── training.py         # Script to initiate model training

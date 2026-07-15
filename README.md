# DECODE_LABS_DATA_ANALYTICS_PROJECT2_EDA
​📌 Project Overview
​This project focuses on executing an automated Exploratory Data Analysis (EDA) pipeline to analyze, visualize, and understand structural patterns and underlying trends within transactional datasets. In contemporary data-driven enterprises, raw operational logs often contain structural noise and inconsistencies. This framework transforms unstructured operational logs into high-fidelity, business-ready intelligence by extracting critical descriptive statistics, identifying mathematical distributions, and mapping out structural bounds.
​🏗️ System Architecture & Framework
​The system is built on a modular data engineering workflow, processing records through sequential computational layers under an IPO Input layer (input -> process -> output) 
framework:
​Input Layer: Ingests raw transactional records and operational logs.
​Process Layer (Statistical Transformation): Computes continuous central tendencies (Mean, Median) and variance boundaries to isolate behavioral anomalies and evaluate structural schema constraints.
​Output Layer (Visual Synthesis): Generates programmatic distribution charts to mathematically validate variables before downstream engineering deployment.
​📊 Core Statistical Insights
​The analysis pipeline processed a batch dataset of 1,200 records with a 98.16% initial data quality validation rate, yielding the following key descriptive metrics:
Statistical MetricOperational ValueAnalytical Significance
Mean (Average)1,053.96 Overall average transaction size; sensitive to extreme outliers.
Median (Middle)823.61 Robust central tendency value; unaffected by right-skewness.
Standard Deviation819.85 Represents moderate variance and spread across operational orders.
Data Range 11.39 to 3,456.40 Absolute minimum and maximum boundary values for transactions.
📈 Visual Analytics & Insights
​The framework generates three critical visualizations to diagnose the dataset's characteristics:
​Distribution & Skewness Analysis (Histogram): The dataset shows a Skewness Value of 0.89, indicating it is Highly Right-Skewed. The majority of purchase frequencies are heavily concentrated in the low-to-medium range (0 to 1,000).
​Outlier Detection (Boxplot): Transactions crossing the $3,300 to $3,500 threshold are plotted as distinct data points. These represent valid, high-value bulk purchases or VIP client interactions rather than data corruption errors.
​Correlation Mapping (Heatmap Matrix): Identifies behavioral relationships between continuous numerical variables. The strongest linear driver of total revenue is Unit Price vs Total Price (Correlation: 0.72), followed by Quantity constraints.
​🚀 Operational Performance Metrics
​During pipeline execution, the diagnostics system maintained optimal performance thresholds:
​Data Ingestion Integrity Rate: 100% computational execution without system failure.
​Operational Interruption Rate: 0.0% (Zero runtime exceptions, memory leaks, or crashes during batch processing).
​System Latency: Near-instantaneous execution time for complete descriptive modeling.
​📂 Repository Deliverables
​This project's execution artifacts are structured as follows:
​📄 Khushi_Sharma_Project2_EDA_Report.docx - Comprehensive formal corporate/academic report detailing executive summaries, visual descriptions, and governance models.
​💻 .ipynb Notebook - Documented Python source code executing the EDA pipeline, generating statistical computations, and rendering visual plots.
.py - Python source code executing the EDA pipeline, generating statistical computations, and rendering visual plots.
📄 Khushi_Sharma_Project2_EDA_Report.pdf-Comprehensive formal corporate/academic report detailing executive summaries, visual descriptions, and governance models.
​Submitted By: Khushi Sharma
Academic Specialization: B.Tech Computer Science and Engineering
Training Platform: DecodeLabs Data Analytics Internship Portfolio

## 🚀 How to Run

To execute the automated EDA framework and data analysis process on your local system, follow these steps:

### Prerequisites
Ensure you have Python installed along with the required analytical libraries:
```bash
pip install pandas numpy matplotlib seaborn scipy
 
python Khushi_Sharma_project_2_EDA.py
 
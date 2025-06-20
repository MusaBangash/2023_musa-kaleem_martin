# Predicting the wind condition of wind turbines using machine learning

## Overview

**Motivation.**
The demand for renewable energy has increased significantly in recent years, and wind energy is a promising alternative to traditional sources of power.
Optimized control strategies are essential for the efficient operation of wind turbines, requiring numerous sensors to be installed on the system.
These sensors capture a variety of data that aid in the prediction of wind speed and system features, like yaw error, pitch angle **error**, etc. which are important for efficient operation of the turbines.

**Problem setting.**
However, due to the delicate nature of these sensors and the intense air current at the height of the turbine, sensor location and temperature can significantly impact their readings.
For example, the anemometer, which measures wind conditions at the hub segmentation behind the rotor blades, can be distorted by the blades' movement.
This **thesis** will explore the impact of these factors on wind turbine sensors and propose solutions to improve their accuracy and reliability.

**Approach.**
We propose in this thesis to explore machine learning (ML) and deep learning (DL) algorithms to improve the accuracy and reliability of sensors and consequently how to improve the efficiency of wind turbines.
Specially we will focus on predicting wind speed, and factors such as yaw error and turbulence, and use the predicted values to optimize wind turbine operation.
The data is derived from simulation models that model sensors installed on wind turbines.
It consists of fine grained time series of regularly spaced sensor readings with up to 33 samples per second.
We will explore models based on interval-based preprocessing as well as models that use the raw data to predict more accurate sensor readings.
For this, we aim to employ end compare various ML and DL algorithms.

**Outlook**
We expect that outcomes will improve wind turbine performance, accurate wind prediction, and novel ML AND DL methodologies for wind turbine performance prediction.
These outcomes have significant implications for the wind energy industry, as they can help optimize
wind turbine operation and improve energy production.

## Tasks

- Data collection and preprocessing
    - Loading and converting data into appropriate data formats for machine learning
    - Data analysis (e.g., clustering)

- Model development and training
    - Feature based models
        - Feature engineering (existing and novel)
        - Baseline models
        - Deep learning models
    - Raw data based models
    - **Advanced modeling techniques**
        - model reduction
        - model variants (e.g., transformers)
        - multitask modeling

- Performance analysis and interpretation
    - model performance
    - model resources (runtime, memory consumption)
    - model analysis (e.g., feature interpretation)

- Documentation (thesis)


## Methodology

1. Data Collection: The data will be collected from the turbine simulation system, which
consists of many sensors measuring various parameters such as wind speed, power,
generator torque, wind angle, and others. From this data, we will select around 20
critical sensors to differentiate between different features of the system. The
collected data will be preprocessed to remove any ambiguous or missing data and to
ensure the consistency and quality of the data.
2. Exploratory Data Analysis: Exploratory data analysis operations will be performed to
understand different aspects of the data, such as dependency, correlation, and
distribution. This stage will help us identify any patterns or trends in the data that
could potentially impact the prediction accuracy. The results of this analysis will be
used to optimize the data preprocessing stage and to select the most appropriate
machine learning algorithms.
3. Machine Learning Modeling: We will use a variety of supervised machine learning
algorithms, such as linear regression, decision trees, and random forests, to develop
accurate models for predicting wind conditions, yaw error, and turbulence. The
models will be trained and evaluated using various performance metrics, such as
mean absolute error, mean squared error, and R-squared. We will also use
techniques such as cross-validation and hyperparameter tuning to ensure the
models are optimized for accuracy and reliability.
4. Advanced Techniques: Advanced techniques such as Convolutional Neural Networks
(CNN), multi-task models and other suitable models will be explored to improve the
outcome. The best model for our goal will be chosen based on its accuracy and
reliability. The models will be compared with benchmark models to evaluate their
performance.
5. Interpretation of Results: The results of the study will be presented in the form of
tables, graphs, and figures, along with a detailed explanation of the model's
performance. The interpretation will involve identifying the most important features
for predicting wind conditions, yaw error, and turbulence, and understanding their
relationships.
# Group 5 Final Project: Student Performance Prediction

A predictive analysis of student final grades using academic, demographic, and 
behavioral data, built to identify which factors most influence student 
outcomes before final grades are in.

## Data set
- Education data from Portugal, covering math course performance
- Includes detailed demographic information: parental education and occupation, 
  family background, study habits, and prior period grades (G1, G2)
- Dataset was clean with no missing values

## Our Method
1. **EDA**: Explored distributions and relationships in the data, checked for 
   missing values and data quality issues (identified 38 students with a final 
   grade of 0, likely representing dropouts rather than low performance)
2. **Preprocessing**: Encoded categorical variables and scaled numeric features; 
   excluded G1/G2 (prior period grades) as predictors since they're too closely 
   tied to the final grade and would make the model artificially accurate 
   without real insight
3. **Unsupervised Model-Clustering Analysis**:

## Key Findings
- Number of past class failures is the strongest predictor of final grade
- Study time shows a modest positive effect on final grade
- Parental education (especially mother's education) shows a weak positive 
  relationship with final grade

## Our Outcome
Our analysis clarifies which background and behavioral factors, rather than 
prior grades, are most predictive of student final grades.

# Dashboard & Final Write-Up:

**EDA & Preprocessing Process**
Dataset & Initial Checks
We used the UCI Student Performance dataset (student-mat.csv), containing 395 students with demographic, family background, study habits, and academic performance data. First step was checking data quality: confirmed there were no missing values across any of the 33 columns, so no imputation was needed.

**Exploring Distributions**
We looked at the distribution of the final grade (G3), which showed a roughly normal spread with a notable spike at 0. Digging into that spike, we found 38 students scored exactly 0 on G3, which we interpreted as likely dropouts rather than simply low performers, since a true 0 is a meaningfully different outcome than a low-but-passing grade. We flagged this as a data quality consideration for the modeling phase rather than treating it as a simple outlier.
We also reviewed the categorical variables (school, sex, address, family size, parents' job/education, etc.) to understand how many unique categories each contained, which informed our encoding approach later.

**Exploring Relationships**
We examined several relationships against the final grade:
G1 (first period) and G2 (second period) grades were highly correlated with G3, which made sense but raised a modeling concern: since they're near-duplicates of the final grade, including them as predictors risks the model appearing artificially accurate without offering meaningful insight. As a team, we decided to exclude G1/G2 as predictors so the model instead learns from background and behavioral factors.
The number of past class failures showed the strongest relationship with final grade, students with more failures tended to score notably lower.
Study time showed a modest positive relationship with final grade.
Parental education (Medu, Fedu) showed weak positive correlations with G3 (0.22 and 0.15 respectively), mother's education slightly more than father's.

**Unsupervied Learning Approach**
We decided to use clustering as our unsupervised model. We were interested in exploring students with similar lifestyles to see if that had any effects on their grades.
Clustering allowed us to separate into groups where students had the most in common. We created the clusters based on study time, free time, 

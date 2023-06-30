# Artificial intelligence with python

**What is AI?**

"The area of computer science that studies how machines can perform tasks that would normally require a sentient angent."

"The area of computer science that studies how machines can closely imitate human intelligence."


**Machine learning:** Is a subset of Artificial Intelligence (AI) that focuses on getting machines to make decisions by feeding them data.  
**Deep learning:** Is a subset of Machine Learning that uses the concept of neural networks to solve complex problems.

**Examples**

- Self driven cars  
- Search engines  
- AI gamers  
- Home monitoring  
- Recommendation systems  
- Medical diagnosis  
- Insurance pricing

**Turing test**

Test "the ability to achieve human-level intelligence during a coversation" by:

- Interrogate the machine through text interface.  
- The human cannot know who they are talking to.  
- The human interacts with two entities (respondents; one human, one machine)  

The machine passes the test if the interrogator is unable to teel which one is the machine and which one is human.

**levels of thought**

- Geometric  
- Kinematic  
- Physical  
- Behavioral  
- Cognitive  

**Rationality within AI:** observe a set of rules and following their logical implications in order to achieve a desirable outcome. 

**Steps in machine learning pipeline**

- Problem definition  
- Data ingestion  
- Data preparation  
- Data segregation  
- Model training  
- Model evaluation  
- Model deployment  
- Performance monitoring:  
	- how accurate are the predictions.
	- Operational performance including CPU utilization, memory usage, disk usage, network traffic, latency (the time it takes for data transfer to occur), throughput (the amount of data succesfully transferred).


**Feature selection** (or variable/attribute selection)

- Method to select features from an initial dataset.  
- This is an important part which can: shorten training time, simplify models and enhance testing set performance.

- Redundant features: doesn't provide much nre information.  
- Irrelevant feature: Low correlation to target feature --> noise.

**Supervised learning:** feeding information via labeled training.

**Unsupervised learning:** No reliance on labeled data.

**Binarization:** converting numerical values into boolean values --> zero and one.

**Mean (average) removal:** To remove bias from the features. 

**Normalization:** Scaling data to be analyzed within a specific range, aim to modify the values so that they sum up to 1. Makes creating, sorting and searching indexes searching faster, less redundant data.

**L1 & L2 normalization**

L1-norm also knows as least absolute deviations (LAD), which minimizes the sum of the absolute differences between the target value and the estimated values.
L1-norm can be summarized as robust, unstable solution and possibly multiple solutions.

L2-norm also known as least squares error (LSE) minimizes the sum of the square of the differences between the target value and the estimated values.
L2 norm can be summarized as not very robust, stable solution and always one solution.

"The method of least absolute deviations finds applications in many areas, due to its robustness compared to the least squares method. Least absolute deviations is robust in that it is resistant to outliers in the data. This may be helpful in studies where outliers may be safely and effectively ignored. If it is important to pay attention to any and all outliers, the method of least squares is a better choice."




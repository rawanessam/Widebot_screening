Task#2 Binary Classification
	In this task it was required to classify a set of data entries into one of 2 groups. 
Data Exploration
	 The first step was to study the data in order to tailor a data preprocessing pipeline along with picking a machine learning algorithm that yields best results.After studying dataset properties the following conclusions were reached: 
The training set involves a great deal of redundancy (3210 out of 3700)
The data set has  numeric and numeric (string) attributes
Many records had a large number of missing (null) attributes 

Data Preprocessing 
	The issues found  while studying the data had  to be resolved in order to reach optimal results. Therefore data preprocessing pipeline went as follows:
Eliminating redundancy
A certain attribute 'variable18' had nearly 50% null entries so it was better to remove that attribute all together rather than reducing dataset size -especially that the dataset was very small after removing redundancy.
A small number of null entries remained in the data so records with null entries were removed (could have been replaced with mean or median if they were not string attributes and replacing null with another average like mode could have affected data balance and classifier bias)
Converting string entries to numeric ones. This was achieved over 2 stages:
For binary string attributes (yes/no or t/f values ), they were replaced with 1/0 (1 or yes/t and 0 for no/f)
For non binary strings, a very simple text preprocessing pipeline was developed, that removes all non ASCII characters and converts characters to their ASCII equivalent. (since the data consisting mainly of a few characters there was no need to use something complicated such as, tokenizer, stemmer or word embedding)
 Classifier training: 
	 Since both the validation and the training datasets were not big in size cross validation was used in training. Data was passed to 4 different classifiers in order to be able to compare and pick the best result. Logistic regression, K-nearest neighbour (KNN), Support vector classification and Decision trees were all passed the same training and validation data. Grid search was used to identify the best parameters for each classifier respectively. 

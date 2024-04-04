## Python Cancer Model, prepared for a cancer.py file

# Import the required libraries for the CancerModel class
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np
import seaborn as sns

class CancerModel:
    """A class used to represent the Cancer Model for passenger survival prediction.
    """
    # a singleton instance of CancerModel, created to train the model only once, while using it for prediction multiple times
    _instance = None
    
    # constructor, used to initialize the CancerModel
    def __init__(self):
        # the cancer ML model
        self.model = None
        self.dt = None
        # define ML features and target
        self.features = ['perimeter_mean', 'radius_mean', 'texture_mean', 'area_mean', 'smoothness_mean', 'concavity_mean', 'symmetry_mean']
        self.target = 'diagnosis'
        # load the Cancer dataset
        self.cancer_data = pd.read_csv('cancer.csv')
        # one-hot encoder used to encode 'embarked' column
        self.encoder = OneHotEncoder(handle_unknown='ignore')

    # clean the cancer dataset, prepare it for training
    # def _clean(self):
        # Drop unnecessary columns
        # self.cancer_data.drop(['diagnosis_cat'], axis=1, inplace=True)

    # train the cancer model, using logistic regression as key model, and decision tree to show feature importance
    def _train(self):
        # split the data into features and target
        X = self.cancer_data[self.features]
        y = self.cancer_data[self.target]
        
        # perform train-test split
        self.model = LogisticRegression(max_iter=1000)
        
        # train the model
        self.model.fit(X, y)
        
        # train a decision tree classifier
        self.dt = DecisionTreeClassifier()
        self.dt.fit(X, y)
        
    @classmethod
    def get_instance(cls):
        """ Gets, and conditionaly cleans and builds, the singleton instance of the CancerModel.
        The model is used for analysis on cancer data and predictions whether the cell is benign or malignant.
        
        Returns:
            CancerModel: the singleton _instance of the CancerModel, which contains data and methods for prediction.
        """        
        # check for instance, if it doesn't exist, create it
        if cls._instance is None:
            cls._instance = cls()
            # cls._instance._clean()
            cls._instance._train()
        # return the instance, to be used for prediction
        return cls._instance

    def predict(self, cell):
        """ Predict the benign or malignant probability of a cell.

        Args:
            passenger (dict): A dictionary representing a passenger. The dictionary should contain the following keys:
                'pclass': The passenger's class (1, 2, or 3)
                'sex': The passenger's sex ('male' or 'female')
                'age': The passenger's age
                'sibsp': The number of siblings/spouses the passenger has aboard
                'parch': The number of parents/children the passenger has aboard
                'fare': The fare the passenger paid
                'embarked': The port at which the passenger embarked ('C', 'Q', or 'S')
                'alone': Whether the passenger is alone (True or False)

        Returns:
           dictionary : contains die and survive probabilities 
        """
        # clean the passenger data
        cell_df = pd.DataFrame(cell, index=[0])
        # cell_df.drop(['diagnosis_cat'], axis=1, inplace=True)
        
        # predict the survival probability and extract the probabilities from numpy array
        malignant, benign = np.squeeze(self.model.predict_proba(cell_df))
        # return the survival probabilities as a dictionary
        return {'malignant': malignant, 'benign': benign}
    
    def feature_weights(self):
        """Get the feature weights
        The weights represent the relative importance of each feature in the prediction model.

        Returns:
            dictionary: contains each feature as a key and its weight of importance as a value
        """
        # extract the feature importances from the decision tree model
        importances = self.dt.feature_importances_
        # return the feature importances as a dictionary, using dictionary comprehension
        return {feature: importance for feature, importance in zip(self.features, importances)} 
    
def initCancer():
    """ Initialize the Cancer Model.
    This function is used to load the Cancer Model into memory, and prepare it for prediction.
    """
    CancerModel.get_instance()
    
def testCancer():
    """ Test the Cancer Model
    Using the CancerModel class, we can predict the survival probability of a passenger.
    Print output of this test contains method documentation, passenger data, survival probability, and survival weights.
    """
     
    # setup passenger data for prediction
    print(" Step 1:  Define theoretical cell data for prediction: ")
    cell = {
        'perimeter_mean': [123],
        'radius_mean': [21],
        'texture_mean': [20],
        'area_mean': [1020],
        'smoothness_mean': [0.1],
        'concavity_mean': [0.2],
        'symmetry_mean': [0.25]
    }
    print("\t", cell)
    print()

    # get an instance of the cleaned and trained Cancer Model
    cancerModel = CancerModel.get_instance()
    print(" Step 2:", cancerModel.get_instance.__doc__)
   
    # print the cell probability
    print(" Step 3:", cancerModel.predict.__doc__)
    probability = cancerModel.predict(cell)
    malignant_probability = probability.get('malignant') * 100
    benign_probability = probability.get('benign') * 100
    print('\t malignant probability: {:.2f}%'.format(malignant_probability))  
    print('\t benign probability: {:.2f}%'.format(benign_probability))
    print()
    
    # print the feature weights in the prediction model
    print(" Step 4:", cancerModel.feature_weights.__doc__)
    importances = cancerModel.feature_weights()
    for feature, importance in importances.items():
        print("\t\t", feature, f"{importance:.2%}") # importance of each feature, each key/value pair
        
if __name__ == "__main__":
    print(" Begin:", testCancer.__doc__)
    testCancer()
import numpy as np
from collections import Counter

from metrics import *

class KNN:
    def __init__(self, 
                 K : int,
                 metric) -> None:
        self.K = K
        self.metric = metric
    

    def fit(self, 
            X_train : np.array,
            y_train : np.array) -> np.array:
        
        self.X_train = X_train
        self.y_train = y_train

    
    def predict(self,
                X_test : np.array) -> np.array:
        
        y_pred = [self._predict(x) for x in X_test]
        return np.array(y_pred)
    
    def _predict(self,
                 x : np.array) -> np.array:
        
        distance = [self.metric(x_train, x) for x_train in self.X_train]
        indexes = np.argsort(distance)[ : self.K]
        k_neighbor_labels = [self.y_train[index] for index in indexes]
        most_common = Counter(k_neighbor_labels).most_common(1)
        return most_common[0][0]

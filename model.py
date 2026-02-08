
import pandas as pd

import numpy as np






#what data we working with ?

df = pd.read_csv("./dataset/email_spam_dataset.csv")

print(df.to_string())


# sidmoid activation function

def sigmoid(z):
    """
    Docstring for sigmoid
    
    :param z: Description
    """
    return 1.0 / (1.0 np.exp(-z))



#gradient

def calc_gradient(theta, X,y):
    """
    Docstring for calc_gradient
    
    :param theta: 
    :param X: Contains all the features and all intances
    :param y: Vector of the results
    """    
    m = y.size # Numer of instances
    # add is the matrix multiplicaiton
    return (X.T @ (sigmoid(X @ theta) -y ) / m



def gradient_decent(X,y, alpha=0.1, num_iter=100, tol=1e-7):
 """
    Docstring for calc_gradient
    
    :param theta: 
    :param X: Contains all the features and all intances
    :param y: Vector of the results
    """ 

    X_b = np.c_[np.ones((X.shape[0],1)),X]

    theta = np.zeros(X_n.shape[1])

    for i in range(num_iter):
                grad = calculate_gradient(theta, X, y)
                theta -= alpha * grad 
            if np.linalg.norm(grad) <tol:
                break
    return theta

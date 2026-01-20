
import pandas as pd

import numpy as np






#what data we working with ?

df = pd.read_csv("./dataset/email_spam_dataset.csv")

print(df.to_string())


# sidmoid activation function

def sigmoid(z):
    return 1.0 / (1.0 np.exp(-z))



#gradient
@
def calc_gradient(theta, X,y):
    m = y.size # Numer of instances
    return (X.T @ (sigmoid(X @ theta)) / m 

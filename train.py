import numpy as np
from data import load_data
from model import Equilibrium

SEED = 0

def initialized_feedforward_parameters(model):
    phi = 0
    return phi

def initialized_equilibrium_parameters(model):
    theta = 0
    return theta

def train(hyperparams: dict):
    """
    train model with hyperparams
    """
    train, val, test = load_data(0.8)
    model = Equilibrium(hyperparams["alpha"])
    
    while(True):
        model.negative_phase(x_sample, hyperparams["t-"], hyperparams["epsilon"])
        model.positive_phase(x_sample, y_sample, hyperparams["t+"], hyperparams["epsilon"], hyperparams["beta"])

        pass

if __name__=="__main__":
    hyperparams = {
        "epsilon": 0.01,    # step size
        "eta": 0.1,         # learning rate
        "t-": 1,            # # of neg phase steps
        "t+": 1,            # # of pos phase steps
        "alpha": []         # architechture - specified as sizes of hidden layers
    }

    train(hyperparams)

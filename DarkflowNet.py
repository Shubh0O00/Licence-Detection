from darkflow.net.build import TFNet
def NetConfig(weights,cfg_file,threshold): # Configuration function to intiate darkflow network for our model
    options = {
    'model': cfg_file,
    'load': weights,
    'threshold': threshold,
    }
    tfnet = TFNet(options)                 # Initiating neural network
    return tfnet
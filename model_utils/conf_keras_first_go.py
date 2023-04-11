
########################################################
########### MODEL CONFIGURATION FILE ###################
########################################################

#Dataset path
dataset_path ='./data/25_cleaned_job_descriptions.csv' #file to be read or processed

#Parameters
vocab_size=50000 #input length on site
max_length=50000 #truncating given values ,To ensure that all the input sequence data is having the same length we pad or truncate the input data points.
batch_size = 500 #the number of training examples in one forward/backward pass
nb_epoch = 50 # number of times training set should go through the model

#Model Parameters
dense=512 # used to create new neural network layers 
dropout=0.1 # used to reset values of some of the attributes in the neural network to avoid overfitting
labels=25 # given to such features to distinguish them from other features
activation_function='relu' #Rectified linear activation unit to train the given function in a linear function whereas relu itself is a non linear function
last_activation_function='softmax' #used for output layer

#Complile Parameters
optimizer = 'adam' # or 'sgd' an attribute used to reduce the losses "adam" or "sgd" is used to implement adam algorithm which is computationally efficient well suited for problems that are large in terms of data/parameters".
loss = 'categorical_crossentropy'#Used as a loss function for multi-class classification model where there are two or more output labels. 

#Model fit
validation_split=0.1 #Fraction of the training data to be used as validation data. The model will set apart this fraction of the training data, will not train on it, and will evaluate the loss and any model metrics on this data at the end of each epoch
verbose=1 # the choice that how you want to see the output of your Nural Network while it's training, its either 0 or 1

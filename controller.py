import sys
import pickle
import numpy as np
import math
import ast


#load the model
with open('./price-predict/neuralnet.sav', "rb") as f:
     loaded_model = pickle.load(f)

#convert the data to float, as the model requires this
location = float(sys.argv[2])

#convert string array to array of floats
season = sys.argv[1]
season = ast.literal_eval(season)       #this line specifically converts the string into a list
seasons = [float(i) for i in season]    #this turns each item in the list into a float

#create input
seasons.extend([8.21, 3.9, 0, 0, 0, 1, 0, 0, location])
data = seasons
# data = [arg_one, 0, 0, 0, 8.21, 3.9, 0, 0, 0, 1, 0, 0, location]
data = np.reshape(data, (1, -1))

#predict and round
predict = loaded_model.predict(data)
rounded = math.ceil(predict[0])
print(rounded)

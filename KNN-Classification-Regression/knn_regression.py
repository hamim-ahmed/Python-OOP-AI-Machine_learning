import numpy as np
import random


class KNN_Regression:

    # already implemented
    def read_data(self, filename):
        '''
        Will take input the filename and read the file as a 2D numpy array.
        Create 3 instance variables of this class for storing the training data, validation data and test data.
        For each datarow from the 2D numpy array
          generate a random number and
          if the number is less than 0.7 then assign that datarow to training data
          otherwise if the number is between 0.7 to 0.85 then assign the datarow to validation data
          otherwise if the number is between 0.85 to 1 then assign the datarow to test data
        '''
        full_dataset = np.genfromtxt(filename, delimiter=",")

        self.training_data = []
        self.validation_data = []
        self.test_data = []

        for eachdata in full_dataset.tolist():
            rand_num = random.random()  # 0.0<=rand_num<1.0
            if rand_num < 0.7:
                self.training_data.append(eachdata)
            elif rand_num < 0.85:
                self.validation_data.append(eachdata)
            else:
                self.test_data.append(eachdata)

        # print(self.training_data)
        # print()
        # print(self.validation_data)

    # already implemented
    def main_knn(self, k, phase):
        '''
        If the value of phase is 1 then perform KNN for the validation data.
        Otherwise if the value of phase is 2 then perform KNN for the test data.

        For each datarow from the validation/test dataset
          predict its class and compare with the real class of this data
          count total no of correctly classified data

        calculate the accuracy value and return the accuracy value
        Note: accuracy=correctly classified data/total number of data
        '''

        if phase == 1:
            dataset = self.validation_data
        else:
            dataset = self.test_data

        right_classify_cnt = 0  # for accuracy calculation
        squared_error = []

        for eachdata in dataset:
            actual_output = eachdata[-1]  # last column contains the real class of the datapoint
            # print("actual output/decision value:", actual_output)
            predicted_output = self.predict_each_data(eachdata, k)
            temp = (actual_output - predicted_output) ** 2
            squared_error.append(temp)  # squared_error list for all validation data with training data.
            # print("squared error list", squared_error)

        squared_error = np.array(squared_error)
        squared_error = squared_error.reshape(1, len(dataset))  # converting into numpy array and reshape into 2d.
        mean_squared_error = squared_error.mean(axis=1) / len(dataset)  # mean_squared error.>> sum_of_all_squared_erro/no_of_datapoints
        # print("mean/final squared error", mean_squared_error)
        # print("\n", "\n", "\n")

        return mean_squared_error

    # just implement this method
    def predict_each_data(self, datapoint, k):
        '''
        Calculate the euclidean distance from the datapoint to all the data in self.training_data
        and then find out the nearest k neighbors
        and return the final predicted class by considering the majority vote
        '''
        np_training_data = np.array(self.training_data, dtype=float)  # converting training_data into numpy array.
        # np_training_data = np_training_data[ :,[0,1,2,3]]                      #excluding column 5 =the decision column
        np_datapoint = np.array(datapoint, dtype=float)  # converting datapoint(validation) into nparray.
        np_datapoint = np_datapoint.reshape(1, 11)
        # np_datapoint = np_datapoint[ :,[0,1,2,3]]                      #excluding column 5 = the decision column
        # print(np_training_data.shape)
        distancearr = ((np_training_data[:, 0:10] - np_datapoint[:, 0:10]) ** 2).sum(axis=1)
        # eucledian distance from 1st 10 column >>11th is decision column.
        sorted_distancearr = np.sort(distancearr)  # sorting the distance array.
        # print(sorted_distancearr)
        # print(distancearr)
        indexlist = []
        pclasslist = []
        for i in range(k):  # k number of nearest neighbour
            index = np.where(distancearr == sorted_distancearr[i])  # taking the k no of nearest data(index tupel) from distance arraay using sortingarray.(return the index as a tuple)
            # print(index[0][0])
            indexlist.append(index[0][0])  # taking the index from index_tuple into indexlist.

        # print(indexlist)
        for i in range(len(indexlist)):
            pclasslist.append(np_training_data[indexlist[i]][-1])  # finding the decision/class(predicted classlist) of those nearest data using their index.
            # print(indexlist[i])
        # print(pclasslist)
        pclasslist = np.array(pclasslist)
        pclasslist = pclasslist.reshape(1, k)  # k no of nearest decision class value list as numpy array.
        poutput = pclasslist.mean(axis=1)  # predicted output. average of k number of decision class value.
        # print("nearest k data decision_class:",pclasslist)
        # print("predicted class/decision value:", poutput[0])

        return poutput[0]  # return the average value from array.



# If your implementation is correct then the following code will work properly.
classifier = KNN_Regression()
classifier.read_data("diabetes.csv")

min_error = 100
best_k = -1
for i in [3, 5, 7, 9, 11, 13, 15]:
    error = classifier.main_knn(i, 1)
    print("For k={}, Validation data Error={}".format(i, error))

    if error < min_error:
        min_error = error
        best_k = i

print("Best value of k =", best_k)

test_accuracy = classifier.main_knn(best_k, 2)
print("Test data Error: ", test_accuracy)
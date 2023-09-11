import numpy as np
import random

class KNN_Classifier:

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
        np.random.shuffle(full_dataset)
        print(full_dataset)


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

        # print(self.training_data,"\n")
        # print(self.validation_data,"\n")
        # print(self.test_data)

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

        for eachdata in dataset:
            actual_class = eachdata[-1]  # last column contains the real class of the datapoint
            # print(actual_class)
            predicted_class = self.predict_each_data(eachdata, k)

            if actual_class == predicted_class:
                right_classify_cnt += 1

        accuracy = right_classify_cnt / len(dataset) * 100
        return accuracy

    # just implement this method
    def predict_each_data(self, datapoint, k):
        '''
        Calculate the euclidean distance from the datapoint to all the data in self.training_data
        and then find out the nearest k neighbors
        and return the final predicted class by considering the majority vote
        '''
        np_training_data = np.array(self.training_data, dtype=float)  # converting training_data into numpy array.
        # print(np_training_data)
        # np_training_data = np_training_data[ :,[0,1,2,3]]                      #excluding column 5 =the decision column
        np_datapoint = np.array(datapoint, dtype=float)  # converting datapoint(validation) into nparray.
        # print(np_datapoint)
        np_datapoint = np_datapoint.reshape(1, 5)
        # print(np_datapoint)
        # np_datapoint = np_datapoint[ :,[0,1,2,3]]                      #excluding column 5 = the decision column

        distancearr = ((np_training_data[:, [0, 1, 2, 3]] - np_datapoint[:, [0, 1, 2, 3]]) ** 2).sum(axis=1)
        # print("distance array","\n", distancearr)
        # print("sorted index array","\n", np.argsort(distancearr))
        sort_distance_index = np.argsort(distancearr)

        # # print(type(distancearr))
        # # eucledian distance from 1st 4 column >>5th is decision column.
        # sorted_distancearr = np.sort(distancearr)  # sorting the distance array.
        # # print(sorted_distancearr)
        # # print(distancearr)
        indexlist = []
        pclasslist = []
        # for i in range(k):  # k number of nearest neighbour
        #     index = np.where(distancearr == sorted_distancearr[
        #         i])  # taking the k no of nearest data(index tupel) from distance arraay using sortingarray.(return the index as a tuple)
        #     print(index)
        #     indexlist.append(index[0])  # taking the index from index_tuple into indexlist.
        #     print(indexlist)
        #
        # # print(indexlist)
        for i in range(k):
            pclasslist.append(np_training_data[sort_distance_index[i]][-1])  # finding the decision/class of those nearest data using their index.
            # print("predicted class list \n", pclasslist)

        # print(pclasslist)
        count1 = pclasslist.count(0)  # total count of decision class 0  >>how many decisions are 0 in predict_class_list;
        count2 = pclasslist.count(1)  # total count of decision class 1
        count3 = pclasslist.count(2)  # total count of decision class 2
        temp = [count1, count2, count3]
        # print(count3,count2,count1, temp)
        temp = np.array(temp)  # taking the decision count into a numpy arrray.
        # # print(temp)
        # print(temp.argmax())
        return temp.argmax()  # return the maxcount index >>>index is same as decision here.


# If your implementation is correct then the following code will work properly.
classifier = KNN_Classifier()
classifier.read_data("iris.csv")

max_accuracy = 0
best_k = -1
for i in [3, 5, 7, 9, 11, 13, 15]:
    accuracy = classifier.main_knn(i, 1)
    print("For k={}, Validation Accuracy={}".format(i, accuracy))

    if accuracy > max_accuracy:
        max_accuracy = accuracy
        best_k = i

print("Best value of k =", best_k)

test_accuracy = classifier.main_knn(best_k, 2)
print("Test Accuracy: ", test_accuracy)


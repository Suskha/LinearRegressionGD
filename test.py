# y = ax + b
import dataParse
import calculationData
import fileOpen
#import downloadUrlFile

a = 0
b = 0
learningRate = 0.5

#Url = "https://s3.amazonaws.com/back-end-training/house-prices.csv"
# dataFileName=downloadUrlFile.download_file(Url,"data_number")

data_list = fileOpen.fileOpen("data_number.csv")

data_x, data_y = dataParse.parseData(data_list)
maxValue = max(data_x)
data_x, data_y = dataParse.normalizeData(data_x, data_y)

for i in range(10000):
    a, b = calculationData.gradientDescent(a, b, data_x, data_y, learningRate)
print("Value of a : ", a)
print ("Value of b : ", b * maxValue)

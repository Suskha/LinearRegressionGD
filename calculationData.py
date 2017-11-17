def Calculate_Error(a, b, dataX, dataY):
    totalError = 0
    numberOfData = len(dataX)
    for i in range(numberOfData):
        totalError += (dataY[i] - (a * dataX[i] + b))**2
    return totalError / float(numberOfData)


def gradientDescent(a, b, dataX, dataY, learningRate):
    actualA = 0
    actualB = 0
    pred = 0
    N = float(len(dataX))
    for i in range(len(dataX)):
        pred = b + (a * dataX[i])
        actualB += (pred - dataY[i])
        actualA += dataX[i] * (pred - dataY[i])
    actualA = a - ((learningRate * actualA) / N)
    actualB = b - ((learningRate * actualB) / N)
    return [actualA, actualB]

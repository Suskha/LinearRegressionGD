def parseData(dataList):
    lines_x = list(range(len(dataList)))
    lines_y = list(range(len(dataList)))
    for i in range(len(dataList)):
        lines_x[i] = 0
        lines_y[i] = 0
    i = 0
    for data in dataList:
        lines = data.split(",")
        lines_x[i] = int(lines[1])
        lines_y[i] = int(lines[0])
        i += 1
    return [lines_x, lines_y]


def normalizeData(dataX, dataY):
    maxDataX = max(dataX)
    for i in range(len(dataX)):
        dataX[i] = dataX[i] / float(maxDataX)
        dataY[i] = dataY[i] / float(maxDataX)
    return [dataX, dataY]

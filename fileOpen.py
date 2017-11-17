def fileOpen(file_name):
	file_read = open(file_name,"r")
	data = file_read.read()
	data_list = list(data.split("\n"))
	return data_list
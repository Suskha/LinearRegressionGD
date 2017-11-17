from urllib import request

def download_file(url_name,data_name):
	data_file_name = data_name + ".csv"
	urllib.request.urlretrieve(url_name, data_file_name)
	return data_file_name
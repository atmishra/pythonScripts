import os,shutil

'''
arrangefiles method takes one argument path which is the path to the directory
to be arranged.
'''
def arrangefiles(path):
	os.chdir(path) # change directory to the path

	all_files = os.listdir('.')

	# list of various file formats and their extensions

	videoformats = ["mkv","flv","vob","ogv","ogg","avi","mov","qt","wmv","mp4","m4p","m4v",".3gp"] 
	imageformats = ["jpeg","jpg","png","gif","bmp","tiff","tif"]
	documentsformats = ["pdf","docs"]
	softwareformats = ["exe"]
	musicformats = ["mp3"]
	compressedformats = []

	directories = ["Documents","Videos","Music","Softwares","Images","Compressed_files"]
	BASE_DIR = os.getcwd()
	# print os.path.join(BASE_DIR,directories[0])

	for directory in directories:
		if os.path.isdir(directory):
			pass
		else:
			os.mkdir(directory)


	for file in all_files:

		if os.path.isfile(file) and '.' in file:

			
			filename,ext = file.rsplit('.',1)
			

			if ext in videoformats:
				shutil.move(file,'./Videos')

			elif ext in imageformats:
				shutil.move(file,'./Images')

			elif ext in documentsformats:
				shutil.move(file,'./Documents')

			elif ext in softwareformats:
				shutil.move(file,'./Softwares')

			elif ext in musicformats:
				shutil.move(file,'./Music')

			else:
				pass

	for directory in directories:
		try:
			if not (os.listdir(os.path.join(BASE_DIR,directory))):
				os.rmdir(os.path.join(BASE_DIR,directory))
		except:
			pass









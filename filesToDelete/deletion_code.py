import os
import time
import shutil
import mimetypes


def main():

    days = 1.5
    time.time()
    seconds = time.time() - (days * 24 * 60 * 60)
    
    path = "/Users/apple/Documents/Airflow_tutorial/"
    # specify the extension
    extension = ".log"
    
    # checking whether the path exist or not
    if os.path.exists(path):
        
        # check whether the path is directory or not
        if os.path.isdir(path):
        
            # iterating through the subfolders
            for root_folder, folders, files in os.walk(path):
                
                # checking of the files
                for file in files:

                    # file path
                    file_path = os.path.join(root_folder, file)

                    # extracting the extension from the filename
                    file_extension = os.path.splitext(file_path)[1]

                    if  extension == file_extension and seconds >= get_file_or_folder_age(file_path):
                        # deleting the file
                        if not os.remove(file_path):
                            # success message
                            print(f"{file_path} deleted successfully")
                            
                        else:
                            # failure message
                            print(f"Unable to delete the {file_path}")
        
        else:
            
            # path is not a directory
            print(f"{path} is not a directory")
    
    else:
        
        # path doen't exist
        print(f"{path} doesn't exist")

def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
    type = mimetypes.guess_type(path)[0]
    if(type==None):
        ctime=0
        print("alias encountered at:")
        print(path)
    else:
        ctime = os.stat(path).st_ctime

	# returning the time
    return ctime

def getDifferenceBetweenCTimeMTime():
    path = "/Users/apple/Documents/Airflow_tutorial/logs/scheduler/2023-07-15/first_dag.py.log"
    ctime = os.stat(path).st_birthtime
    mtime = os.stat(path).st_mtime
    print("difference between mtime and ctime is :")
    print(mtime-ctime)


if __name__ == '__main__':
    # invoking main function
    getDifferenceBetweenCTimeMTime()
    main()
from flask import Flask
import json
import os
from flask import Response, jsonify, request  

app = Flask(__name__)

@app.route('/')
def index():
    return {"Name":"Faizan", "Greetings": "Hi"}

#--------------------------------------
# GET Method : Read a file or Directory
#--------------------------------------

@app.route('/file/<path:fspath>' , methods=['GET'])
def get_data(fspath):
    
    newpath = "./file/" + fspath
    
    print("\n REQUESTING : " + newpath + "\n")
    
    orderby = request.args.get('orderBy')
    orderByDirection = request.args.get('orderByDirection')
    filterByName = request.args.get('filterByName')

    if (dir_check(newpath)):  
        return Response(read_dir(newpath), status=200 , mimetype='application/json')
    elif (file_exists(newpath)):
        return Response(read_file(newpath), status=200 , mimetype='application/json')
        #file_exists(newpath)
    else:
        return Response('{"Error Message" : "Please enter valid path."}', status=404, mimetype='application/json')

#--------------------------------------
# POST Method : Create a file 
#--------------------------------------

@app.route('/file/<path:fspath>' , methods=['POST'])
def create_file(fspath):
    filedata = request.json['data']
    
    newpath = "./file/" + fspath
    
    print("\n REQUESTING : " + newpath + "\n")
    
    if(dir_check(newpath)):
        return Response('{"Error Message" : "This is a directory. Please send new file name in URL and data in JSON"}', status=403, mimetype='application/json')
    elif(file_exists(newpath)):
        return Response('{"Error Message" : "File Already Exists"}', status=403, mimetype='application/json')
    else:
        create_file(newpath,filedata)
        return Response('{"Message":"File created"}', status=200 , mimetype='application/json')

#--------------------------------------
# PATCH Method : Update a file 
#--------------------------------------

@app.route('/file/<path:fspath>' , methods=['PATCH'])
def update_file(fspath):
    
    filedata = request.json['data']
    newpath = "./file/" + fspath
    
    print("\n REQUESTING : " + newpath + "\n")
    
    if(dir_check(newpath)):
       return Response('{"Error Message" : "This is a directory. Please send existing file name in URL and data in JSON"}', status=403 , mimetype='application/json')
    elif (file_exists(newpath)):  
        update_file(newpath, filedata)
        return Response('{"Message" : "File successfully updated"}', status=200 , mimetype='application/json')
    else:
        return Response('{"Error Message" : "File does not Exist"}', status=404 , mimetype='application/json')
        


#--------------------------------------
# DELETE Method : Delete a file 
#--------------------------------------
@app.route('/file/<path:fspath>', methods=['DELETE'])
def delete_file(fspath):
    newpath = "./file/" + fspath
    
    print("from delete method :" + newpath)
    
    if(dir_check(newpath)):
        return Response('{"Error Message" : "This is a directory. Please select file"}', status=403 , mimetype='application/json')
        
    else:
        if (file_exists(newpath)):  
            os.remove(newpath + ".txt")
            return Response('{"Message" : "File successfully removed"}', status=200 , mimetype='application/json')
            
        else:
            return Response('{"Error Message" : "File does not Exist"}', status=200 , mimetype='application/json')
            
   

#--------------------------------------
# Read File and return its content
#--------------------------------------

def read_file(filepath):
    # Using readlines()
    
    file1 = open(filepath + '.txt', 'r')
    
    Lines = file1.readlines()
    
    count = 0
    
    # Strips the newline character
    filecontent = ""
    
    for line in Lines:
        count += 1
        filecontent = filecontent + str(line) + "\n"
    
    return filecontent#{ "File contents :" : filecontent }   

#--------------------------------------
# Get Directory Content
#--------------------------------------

def read_dir(dirpath):
    files = os.listdir(dirpath)
    
    dircontent = {"isdirectory" : "true"}
    
    filelist = []
    
    for f in files:
        if(dir_check(dirpath + "/" + str(f))):
            filelist.append(str(f)+"/")
        else:
            filelist.append(str(f))
    
    
    dircontent["files"] = filelist

    return json.dumps(dircontent)

#--------------------------------------
# Create a file function
#--------------------------------------
def create_file(filepath,data=""):
    fw = open(filepath + ".txt", "w")
    fw.write(data)
    fw.close()
    print("File created")

#--------------------------------------
# Update a file function
#--------------------------------------

def update_file(filepath,data=""):
    fw = open(filepath + ".txt", "a")
    fw.write(data)
    fw.close()
    print("File Updated")

#--------------------------------------
# Check if the path is a directory or not
#--------------------------------------

def dir_check(path):
    if os.path.isdir(path):  
        print(path + " is a directory")
        return True
    else:
        print(path + " is not a directory")
        return False

#--------------------------------------
# Check if the file exists at the path
#--------------------------------------   

def file_exists(path):
    filepath = path + ".txt"
    if os.path.exists(filepath):
        print("file: " + filepath + " exists")
        return True
    else:
        print("file: " + filepath + "doesnt exists")
        return False

To start the project: 
>docker-compose up

The command should start the server at localhost:5000

URL examples: 
GET : 
    localhost:5000/file/root -> Return directory contents
    localhost:5000/file/root/rootfile -> Return rootfile.txt contents
POST : 
    With raw JSON {data: "New data to be written on file"}
    localhost:5000/file/root/rootfile > It will create a file named rootfile.txt with data contents inside

PATCH : 
    With raw JSON {data: "New data to be written on file"}
    localhost:5000/file/root/rootfile > It will append a file named rootfile.txt with data contents inside

DELETE : 
    localhost:5000/file/root/rootfile > It will delete the file if existed at the path


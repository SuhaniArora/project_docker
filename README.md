# project_docker
Step 1 : Create a directory for the project (/root/project)

Step 2 : Create a file named app.py which contains the code you want to run and include a flask app in it before the code, here the code in the app.py file is a code which creates a map using the Latitudes and longitudes of a place and marks that place using a marker , the dataset of the latitudes and longitudes is also given above.

Step 3 : Create a reqirements.txt file which will bw used in the Dockerfile.

Step 4 : Create a Dockerfile that builds a docker image.

Step 5 : Create a docker-compose file which defines the web service.

Step 6 : Run the command docker-compose up.

Now you can access this by running http://localhost:5000 in your system.

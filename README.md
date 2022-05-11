# Test project

This code init test project contains a web application to receive activities documents, validate them as well as store them for future retrieval.

# Installation
1. Open your terminal and follow instructions below

1. Clone this project (presumes github SSH key is properly setup) `git clone git@github.com:MurigaP/codeinit-test.git` or over https `git clone https://github.com/MurigaP/codeinit-test.git`
1. Install Docker 
   1. On Linux :
      1. Follow  https://docs.docker.com/desktop/linux/install/
      Docker has custom installation based per distro, make sure you have followed the installation commands per distro
   2. On MacOS :
      1. Follow  https://docs.docker.com/docker-for-mac/install/

1.Likewise,  Install Docker Compose
   1. On Linux :
      1. Follow  https://docs.docker.com/compose/install/
      Docker compose has custom installation based per distro, make sure you have followed the installation commands per distro
   2. On MacOS :
      1. Follow https://docs.docker.com/compose/install/


1. Make sure Docker is running and then run `docker-compose up` or  `docker-compose up -d` as a long running application. 
   1. This should take a few minutes based on your internet speeds to build and run the code images!
   2. The application should now be up and running! Check terminal / console to confirm.
1. Go to `https://localhost:8000` to access the site
2. From here you can be able to upload the activites xml files from the root `activities_test_files` inside the source code folder
1. Log into the admin page (`https://localhost:8000/admin`) with your super-user credentials.
   1. Administrator Credentials : 
      1. username : admin
      2. password : admin

## Happy testing!

1. To tear down / stop the application you can run  `docker-compose down`. 

# Project notes

The repository is divided into two :
1. Frontend application - The application is built with the Angular framework :
   1. The frontend source code can be found inside the `frontend-ui` folder 
2. Backend application - The application is built with the Django - python framework : 
 1. The backend source code can be found inside the  `api` folder as well as the `iati_app` folder
   3. Programmatically, Django + Angular have been stitched together to have the project as one.

## Cloud hosting / Deployment

1.  A hosted application version is running on Azure &  can be found here: `https://iatibackendtest.azurewebsites.net`


## Developer profile:
1. Name: Peterson Muchiri
1. Email : `murigap@gmail.com`
1. Github link: `https://github.com/MurigaP`
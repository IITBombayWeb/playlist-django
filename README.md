# playlist-django
        
## A Django backend for playlist application
  
**Steps to run Django Backend:**

1. Create a folder and run the following command: 
   ```
   cd <folder_name> 
   ```

2. Create a virtual environment using the following commands:
   ```
   sudo apt install virtualenvwrapper
   virtualenv venv
   ```
   
3. Activate the virtual environment:
   ```
   source ./venv/bin/activate
   ```
   
2. Install all the packages essential for this project:
   ```
   pip install django
   pip install djangorestframework 
   pip install django-cors-headers
   pip install django-rest-swagger
   ```
   
3. Clone the repo in the same directory

>  Link to the site: [Import a Django project from git](https://stackoverflow.com/questions/12400077/how-to-import-a-django-app-from-git-into-a-project)

4. Here, django project name - playlist, django app name - plydjango

5. To run the server: 

   Go to the directory where manage.py file is present and run the following command:
   ```
   python manange.py runserver
   ```
## Frontend using react-js: [playlist-react](https://github.com/IITBombayWeb/playlist-react) 

  **Note**: 
        Some changes has been done in the source code provided in [playlist-react](https://github.com/IITBombayWeb/playlist-react), the changed files has 
        been put in separate folder in this repository, named - playlist-react-changed-files. Please copy the codes from the files and paste it to the 
        corresponding same file after cloning the repository from [playlist-react](https://github.com/IITBombayWeb/playlist-react), it is important, then 
        only backend will run properly with frontend.
        
**Steps to run the frontend:**

1. Go to the directory of your folder name.

2. Install the necessary packages to run react-js. The files are in .tsx format (Typescript)

3. Clone the repo for frontend from [playlist-react](https://github.com/IITBombayWeb/playlist-react)

4. **Important** - Make the changes in the necessary files which has been added in [playlist-react-changed-files](https://github.com/IITBombayWeb/playlist-django/tree/main/playlist-react-changed-files) by copying the codes in files and put it in corresponding files after cloning the repo. Follow the note written above for this step.
    
5. To run the frontdend: Go to the directory: <folder_name>/playlist-react and run the following command:
   ```
   npm start
   ```

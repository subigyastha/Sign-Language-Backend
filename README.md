1. First Create a Virtual Environment (if you have downloaded without env folder)

``
  python -m venv env 
``

2. Then Run Virtual Environment
  
  ``venv\Scripts\activate``

  Note: if There is an error running the environment 
  
    - Run PowerShell in Administration Mode
    
    - Then run the command Set-ExecutionPolicy Unrestricted
    
    - Then run the environment again Set-ExecutionPolicy Restricted

3. Then install Django and other dependencies
  ``
  pip install -r requirements.txt
``
  
  (this file is inside VideoCollect folder)

4. then in terminal open videoCollect folder and run follwing commands
   
    - ``py manage.py makemigrations``
      
    - ``py manage.py migrate``
      
    - ``py mange.py runserver``
  



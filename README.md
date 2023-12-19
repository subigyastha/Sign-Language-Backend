First Create a Virtual Environment (if you have downloaded without env folder)
  python -m venv env 

Then Run Virtual Environment
  venv\Scripts\activate

  Note: if There is an error running the environment 
    - Run PowerShell in Administration Mode
    - Then run the command Set-ExecutionPolicy Unrestricted
    - Then run the environment again Set-ExecutionPolicy Restricted

Then install Django and other dependencies
  pip install -r requirements.txt  (this file is inside VideoCollect folder)




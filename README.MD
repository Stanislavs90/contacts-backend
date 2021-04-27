Intro:
    An api that allows users keep track of thier contacts, connected to a 
    react frontend.


Setup:

   python3 -m venv venv
   
   source env/bin/activate

   pip install -r requirements.txt

   cd into directory 

   python manage.py createsuperuser

   python manage.py runserver

Overview: 

    Navigate to http://127.0.0.1:8000/api/contacts/ to view or create contacts
    
    
    Navigate to http://127.0.0.1:8000/api/contacts/<int:id>/ to delete contacts



    Fields that user can input data:

        Name
        Phone
        Company
        Email
        Related_name - i.e. Nickname
        Birthday



   

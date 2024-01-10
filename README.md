Crud API 

Deployed on Python Anywhere

All end points are:

https://rishabhrj.pythonanywhere.com/admin => For admin panel 

https://rishabhrj.pythonanywhere.com/api/register/ => Api endpoint for user registration

https://rishabhrj.pythonanywhere.com/api/login/ => Api endpoint for login and create token

https://rishabhrj.pythonanywhere.com/api/user/ => Api endpoint for current user details

https://rishabhrj.pythonanywhere.com/api/boxes/ => Api endpoint for list of boxes and adding boxes (get and post)

https://rishabhrj.pythonanywhere.com/api/boxes/<int:id> => Api endpoint for updating box details

https://rishabhrj.pythonanywhere.com/api/my-boxes/ => Api endpoint for user boxes

https://rishabhrj.pythonanywhere.com/api/my-boxes/<int:id> => Api endpoint for user boxes delete funtion

Some user details are:

1. Username:Rj Password:lkjhgfdsa (staff + superuser)
2. Username:Rjjj Password:Pops@123 (staff user)
3. Username:Rjjjj Password:Pops@123 (not a staff user)

Check API using postman detail:

You can create your own user with registration api endpoint
<img width="1006" alt="Screenshot 2024-01-10 at 11 32 53 PM" src="https://github.com/Rishabh-code-do/crud_api/assets/85050354/f1e7facf-9762-4408-a1ae-4b8dda0392a9">

Now login using login api and create token
<img width="1006" alt="Screenshot 2024-01-10 at 11 33 40 PM" src="https://github.com/Rishabh-code-do/crud_api/assets/85050354/292e938d-8503-44fc-83bb-7ec62519e3b5">

Now pass the token by attaching to the header and send to boxes api
<img width="1440" alt="Screenshot 2024-01-10 at 11 36 30 PM" src="https://github.com/Rishabh-code-do/crud_api/assets/85050354/5064aa7c-2aba-4c8c-9576-3027b190edb9">

For filter:
<img width="1006" alt="Screenshot 2024-01-10 at 11 42 33 PM" src="https://github.com/Rishabh-code-do/crud_api/assets/85050354/33c6feba-9fb8-4ff6-b6f7-d59af4bced4f">



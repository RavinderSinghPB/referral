# [Referral Site]

> Features

- user can signup with referral-code and earn point, 'if code is correct'
- more api available at `http://127.0.0.1:8000/api/`
- user can see, how many users has used his code to signup, and point earned ,at `http://127.0.0.1:8000/profile/`
- api to check all users signup with a referCode `http://127.0.0.1:8000/api/referrer-code/<code>/codeUsedBy/`
    where `<code>` is referrer code
- an user earn through referring other user `http://127.0.0.1:8000/api/users/pk/point_earn/`
    where 'pk' is primery-key of user
  

## Packages Used 

- Django 
- Django_rest_framework


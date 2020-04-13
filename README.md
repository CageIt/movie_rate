## Movie Mania (Django REST version) 

a web application (back-end) for reviewing the movies

## Motivation 
To practise how to use back-end framework and the basic of the programming language

## Tech/framework used
Python 3.8, Django REST Framework 3, sqlite3<br/>
<b>Built with</b>
[Atom](https://atom.io/)

## Status : Complete
Date: 13/04/2020<br/>
Duration: 5 - 13/04/2020 (8 days)

## Information
Users

Admin:

Username = admin

Password = adminpass123

Member:

testuser1

testuser2

testuser3

testuser4

testuser5

testuser6

testuser7

password = testpass123

<br>Link Map(All User):</b>

                                               Api_root(127.0.0.1)
                                                       |
                          register(/register)   movie list(/movies)     user list(/users)
                                                       |                       |
                                            movie detail(/movie id)    user detail(/user id)
                                                       |
                                                Review list(/review)

Access Level:
Guest: API root -> movie list -> movie detail(read only) -> review list (read only)<br/>
        API root -> register<br/>
Member: API root -> movie list -> movie detail(read only) -> review list<br/>
          API root -> user list -> user detail (according to the login user)<br/>
          API root -> register<br/>
Admin: API root -> movie list -> movie detail(can edit and delete) -> review list<br/>
        API root > user list -> user detail (can access all user profile and delete)<br/>
        API root -> register<br/>
        127.0.0.1/admin


Note: Create a new movie can only be done in admin site

## How to use
1. install Python<br/>
  1.1 make build path for Python<br/>
  1.2 make build path for pip><br/>
2. install django rest framework by type pip install djangorestframework in cmd
3  after installation you locate your download file in cmd
4. type python manage.py runserver
5. type 127.0.0.1 in any browser engine<br/>
  5.1 You can type 127.0.0.1/admin also if you want to work as an Administrator
6. enjoy the application!


## Credits
https://www.django-rest-framework.org/
## License
MIT © [Panut Sasanaputchot]()







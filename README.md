# Movie Mania (Django REST version)
Programmer: Panut Sasanaputchot

Date: 13/04/2020

Duration: 5 - 13/04/2020 (8 days)

Purpose: Write a web application (back-end) to create a list of movie to rate and comment the movie

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

Link Map(All User):

                                               Api_root(127.0.0.1)
                                                       |
                          register(/register)   movie list(/movies)     user list(/users)
                                                       |                       |
                                            movie detail(/movie id)    user detail(/user id)
                                                       |
                                                Review list(/review)

Access Level:
Guest: API root -> movie list -> movie detail(read only) -> review list (read only)
       API root -> register
Member: API root -> movie list -> movie detail(read only) -> review list
        API root -> user list -> user detail (according to the login user)
        API root -> register
Admin: API root -> movie list -> movie detail(can edit and delete) -> review list
       API root > user list -> user detail (can access all user profile and delete)
       API root -> register
       127.0.0.1/admin


Note: Create a new movie can only be done in admin site

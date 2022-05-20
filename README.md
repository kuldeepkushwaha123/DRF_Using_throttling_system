# DRF_Using_throttling_system
This is a throttling system using DRF

1  POST-    http://127.0.0.1:8000/api/register/  -    register with post method username,email and password .

2  POST-    http://127.0.0.1:8000/api/log/       -    login with username and password with the POST method then it will return a Token for the user.

3  POST-    http://127.0.0.1:8000/api/messages/  -    Use for create message with message and user, where user relate to the username and also
                                                      give the token which is find after login.


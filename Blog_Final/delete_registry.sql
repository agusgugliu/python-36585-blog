-- TO RUN: CTRL + SHIFT + Q

DELETE FROM App_Blog_modelblog;
DELETE FROM sqlite_sequence WHERE name = 'App_Blog_modelblog';

DELETE FROM App_Users_avatar;
DELETE FROM sqlite_sequence WHERE name = 'App_Users_avatar';

DELETE FROM auth_user;
DELETE FROM sqlite_sequence WHERE name = 'auth_user';

DELETE FROM auth_permission;
DELETE FROM sqlite_sequence WHERE name = 'auth_permission';
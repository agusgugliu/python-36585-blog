-- TO RUN: CTRL + SHIFT + Q

DELETE FROM App_Blog_modelblog;
DELETE FROM sqlite_sequence WHERE name = 'App_Blog_modelblog';

DELETE FROM App_Users_avatar;
DELETE FROM sqlite_sequence WHERE name = 'App_Users_avatar';
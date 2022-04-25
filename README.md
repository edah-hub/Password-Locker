# Password-Locker
This project is a python application that manages login and signup credentials of a person for various accounts,it takes username and passwords for each account. It can store the passwords and generates a unique password for a user if they do not want to generate new passwords by themselves.

## Author

[Chepngetich-edah](https://github.com/edah-hub)

## Description

This project is a python application that manages login and signup credentials of a person for various accounts i.e. username and passwords for each account. It also stores the passwords and generates a unique password for a user if they do not want to generate new passwords by themselves.

## User Stories
The user would like to.... :
* To create an account for the application or log into the application.
* Store my existing acounts login details for various accounts that i have registered for.
* Generate new password for an account that i haven't registered for and store it with the account name.   
* Delete stored account login details that i do now want anymore.
* Copy my credentials to the clipboard


## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.6
* pyperclip
* pip

##### Setup Instructions and Installation

- Clone this repository to a location in your file system. `git clone https://github.com/edah-hub/Password-Locker.git`
- Open terminal command line then navigate to the root folder of the application. `cd password-locker1`
- Run `./run.py

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ python3 run.py```|Hello there Welcome to Password Locker <br>* NA ---  Create New Account * LG ---  LogIn (Have An Account) |
|Select  NA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```DEL```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```EX```| exits appliation|

## Technologies Used

- Python3.9
- PyperClip

## Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request

## Known Bugs
If you find a bug (the website couldn't handle the query and or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.

## Contact Information 

If you have any question or contributions, please email me at [cheruiyotedah@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2022 **Chepngetich Edah**


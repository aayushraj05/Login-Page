# Python and MySQL Login System with Tkinter

This project is a basic login system built using Python, Tkinter for the graphical user interface (GUI), MySQL for user data storage, and the Python `mysql-connector` library for database connectivity. The system allows users to register with a username and password (with hashed password storage) and then log in using the same credentials.

## Features
- **User Registration**: Securely register users with hashed passwords.
- **User Login**: Log in with previously registered credentials.
- **MySQL Database**: Uses MySQL to store user data.
- **Graphical Interface**: Built with Tkinter to provide a clean and interactive user interface.
- **Environment Variables**: Uses `.env` file to securely store sensitive configuration data like MySQL credentials.
- **Image Support**: Background images are supported using Pillow (PIL) to enhance the visual appeal of the UI.

## Requirements

### Python Packages:
- `mysql-connector-python`: To communicate with the MySQL database.
- `pillow`: For handling images in the Tkinter UI.
- `python-dotenv`: To load environment variables from a `.env` file.
- `tkinter`: The Python built-in library for GUI creation.

You can install all required packages using the following command:
```bash
pip install mysql-connector-python pillow python-dotenv


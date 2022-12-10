# C3 Cinemas: A Cinema E-Booking App

C3 Cinemas is an application that allows users to browse and filter movies, select a showtime, select seats, purchase tickets, apply promos, and recieve order confirmations.

The system also includes an admin portal for admins to manage movies, showings, ticket prices, promotions, and other users.

## Overview


## Installation
1. Clone project from git hub
```bash
git clone https://github.com/YaliniNadar/Cinema-E-Booking.git
```
2. Install the required packages
```bash
python3 -m pip install -r requirements.txt
```
3. Create a .env file to store the following as environment variables:
```bash
FIELD_ENCRYPTION_KEY=''
TMDB_KEY=''
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD = ''
```

4. To start the app, run
```
cd project
python3 manage.py makemigrations
python3 manage.py migrate
python3 load.py
python3 manage.py runserver
```

## Contributors
- [Bella Humphrey](https://github.com/idhumphrey)
- [Nathan Jacobi](https://github.com/njj67229)
- [Nicholas Kundin](https://github.com/nickundin)
- [Yalini Nadar](https://github.com/YaliniNadar)

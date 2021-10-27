# Book It

<img src="static\assets\media\logo.png" alt="logo" width="200"/>

[Click Here To Visit](https://github.com/kushagra-aa/multlists)

Book It is a Web Application Built using Python-Django, HTML, CSS, and Bootstrap.
It is a Room Rental System,
where a user can register and login, and add their place for a paying guest to find(if they are seller).
or a buyer/PG can find places near them

A Redefined House Hunting Web Application

Built with 🤍 For You!

## Features:

- User Authentication
- User Registration
- Multiple User Types
- Sellers can post the rooms
- Buyers can view the rooms and get contact info of seller

### More About Book It:

    Here At Book It, We Help You Discover A Place You'll Love To Live. Directly Contact The Owner, No Middle Man Required.

## Screenshots:

![Home Page](https://user-images.githubusercontent.com/68841296/137738972-95a8f799-7a2b-4cf3-adb8-8db0060a21b7.png)
### Home Page- Hero Section👆🏻

![Signup](https://user-images.githubusercontent.com/68841296/137739237-920beaee-52be-436a-ad19-5a189ebb0bb2.png)
### Signup Page👆🏻

![Login](https://user-images.githubusercontent.com/68841296/137739163-59c33625-5e00-4d30-87e7-275243cf9190.png)
### Login Page👆🏻

![All Rooms](https://user-images.githubusercontent.com/68841296/137739110-beabd04f-b55b-471f-a98e-f6032c86a896.png)
### Rooms Page👆🏻

![Room Details](https://user-images.githubusercontent.com/68841296/137739342-b5fdd1ad-dc6a-49b9-b57e-072da1590b7a.png)
### Room Details Page👆🏻

![Seller Detials](https://user-images.githubusercontent.com/68841296/137739380-b60fffb4-75a3-4fed-9bce-82cf5c26ee9b.png)
### Seller Details Page👆🏻

![404 Page](https://user-images.githubusercontent.com/68841296/139087971-0d835007-d175-41a3-99bb-130004a7b64c.png)
### 404 error Page👆🏻

## Made Using:

- ### Languages
  - <img src="static/assets/media/images/HTML.png"    width="40" alt="HTML">
  - <img src="static/assets/media/images/CSS.png" width="40" alt="CSS">
  - <img src="static/assets/media/images/Python.png"  width="40" alt="Python">
- ### Frameworks-Libraries
  - <img src="static/assets/media/images/Bootstrap.png"   width="40" alt="Bootstrap">
  - <img src="static/assets/media/images/Django.png"  width="40" alt="Django">
- ### Tools

  - <img src="static/assets/media/images/Figma.png"   width="40" alt="Figma">

  - <img src="static/assets/media/images/vscode.png" width="40" alt="VS Code">

- ### Concepts
  - Custom User Model
  - Templates
  - CSS Animations
  - 404 Error Handling
  - Custom Models
  - Django Authentication
  - Login-Logout
  - Django Admin

## Run Locally:

Clone the project

```bash
  git clone https://github.com/kushagra-aa/bookit.git
```

Go to the project directory

```bash
  cd bookit
```

Install dependencies

```bash
  pip install -r requirements.txt
```

then run

```bash
python manage.py migrate
```

create admin account

```bash
python manage.py createsuperuser
```

then

```bash
python manage.py makemigrations
```

to makemigrations for the app

then again run

```bash
python manage.py migrate
```

to start the development server

```bash
python manage.py runserver
```

and open localhost:8000 on your browser to view the app.

> Debug is set to false, may need to run `py manage.py runserver --insecure`

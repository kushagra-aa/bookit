# Book It

<img src="static\assets\media\logo.png" alt="logo" width="200"/>

[Click Here To Visit](https://github.com/kushagra-aa/multlists)

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

![Signup](https://user-images.githubusercontent.com/68841296/137739237-920beaee-52be-436a-ad19-5a189ebb0bb2.png)

![Login](https://user-images.githubusercontent.com/68841296/137739163-59c33625-5e00-4d30-87e7-275243cf9190.png)

![All Rooms](https://user-images.githubusercontent.com/68841296/137739110-beabd04f-b55b-471f-a98e-f6032c86a896.png)

![Room Details](https://user-images.githubusercontent.com/68841296/137739342-b5fdd1ad-dc6a-49b9-b57e-072da1590b7a.png)

![Seller Detials](https://user-images.githubusercontent.com/68841296/137739380-b60fffb4-75a3-4fed-9bce-82cf5c26ee9b.png)

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

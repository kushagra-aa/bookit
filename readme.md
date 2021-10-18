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

![App Screenshot](https://user-images.githubusercontent.com/68841296/129092327-be3faad7-6010-40ee-821c-34365e90534b.png)
![image](https://user-images.githubusercontent.com/68841296/129092655-f1c18467-84ef-4786-8d2e-cf34ead9f9b1.png)
![image](https://user-images.githubusercontent.com/68841296/129092744-296c32dd-d94c-4548-928c-deb3df71377a.png)

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

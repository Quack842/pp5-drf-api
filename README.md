# QuackyGraphy - A Platform For Sharing Your Masterpiece shots!

Quacky-Graphy is a Social Media Platform for Photographers who Loves sharing their amazing shots! The users will be able to say with what type of camera they took the picture and what theme the picture was intended for. For example, Animals, Sport, Nature and many more. Users will be able to see the details of the most, but will not be able to like, comment or post themselves, if they are not logged in. This code is the back-end of the applications, I'd like to say it is the Brains of the website. This is where the front-end of the website will get all the data it needs to function and store information as well.

You Can View the Live Project [Here!](https://pp5-quackygraphy.herokuapp.com/)

## Links to the Frontend Project

- [Frontend - Repository](https://github.com/Quack842/pp5-quackygraphy)
- [Frontend - Deployment](https://pp5-quackygraphy-app.herokuapp.com/)

## Table of Content

1. [Database](#database)
2. [Testing](#testing)
    - [Validation](#pep8-validation)
    - [Manual Testing](#manual-testing)
    - [Testing Endpoints](#testing-endpoints)
    - [Bugs](#bugs)
3. [Technologies Used](#technologies-used)
    - [Languages and Frameworks Used](#languages-and-frameworks)
    - [Packages Used](#packages-used)
    - [Other Tools](#other-tools)
4. [Deployment](#deployment)
    - [Cloning a Template](#cloning-a-template)
    - [Running in VS Code](#running-in-vs-code)
    - [Deploying with heroku](#deploying-with-heroku)
5. [Credits](#credits)
    - [Code]()
    - [Acknowledgements]()

# Database
[Back to top ⇧](#quackygraphy---a-platform-for-sharing-your-masterpiece-shots) <br />
[Table Of Contents ⇧](#table-of-content)

![SQL Database model](/docs/images/diagrom.png)

# Testing
[Back to top ⇧](#quackygraphy---a-platform-for-sharing-your-masterpiece-shots) <br />
[Table Of Contents ⇧](#table-of-content)

## <u>PEP8 Validation:</u>
All python files was passed through the PEP8 validator with no issues. Few long-line error remains in settings.py
<details>
<summary>Comments</summary>
Models.py

![Comments](./docs/validation/comments-models.png)
Serializers.py

![Comments](./docs/validation/comments-serializers.png)
Urls.py

![Comments](./docs/validation//comments-urls.png)
Views.py

![Comments](./docs/validation/comments-views.png)
</details>
<details>
<summary>Drf-Api</summary>
Permissions.py

![Drf-Api](./docs/validation/drf-api-permissions.png)
Settings.py

![Drf-Api](./docs/validation/drf-api-settings.png)
Serializers.py

![Drf-Api](./docs/validation/drf-api-serializers.png)
Urls.py

![Drf-Api](./docs/validation//drf-api-urls.png)
Views.py

![Drf-Api](./docs/validation/drf-api-views.png)
</details>
<details>
<summary>Followers</summary>
Models.py

![Followers](./docs/validation/followers-models.png)
Serializers.py

![Followers](./docs/validation/followers-serializers.png)
Urls.py

![Followers](./docs/validation//followers-urls.png)
Views.py

![Followers](./docs/validation/followers-views.png)
</details>
<details>
<summary>Likes</summary>
Models.py

![Likes](./docs/validation/likes-models.png)
Serializers.py

![Likes](./docs/validation/likes-serializers.png)
Urls.py

![Likes](./docs/validation//likes-urls.png)
Views.py

![Likes](./docs/validation/likes-views.png)
</details>
<details>
<summary>Posts</summary>
Models.py

![Posts](./docs/validation/posts-models.png)
Serializers.py

![Posts](./docs/validation/posts-serializers.png)
Urls.py

![Posts](./docs/validation//posts-urls.png)
Views.py

![Posts](./docs/validation/posts-views.png)
</details>
<details>
<summary>Profile</summary>
Models.py

![Profile](./docs/validation/profiles-models.png)
Serializers.py

![Profile](./docs/validation/profiles-serializers.png)
Urls.py

![Profile](./docs/validation//profiles-urls.png)
Views.py

![Profile](./docs/validation/profiles-views.png)
</details>


## <u>Manual Testing</u>
Manual testing was used Though-out the development of the API to discover bugs and issues.

### Testing Endpoints
| Application | URL | Expected Result | Pass/Fail |
|---|---|---|---|
| Home Page | rout route | Returns the landing Page of the API | ![Check Mark](/docs/images/check-mark.svg)|
| Admin | admin/ | Returns the Admin view page. Where the admin can manage all user accounts and posts | ![Check Mark](/docs/images/check-mark.svg)|
| Comments | comments/ | Return a list of all the comments in order of creation date | ![Check Mark](/docs/images/check-mark.svg)|
| Comments | comments/int:pk/ | Returns the comment of the selected ID  | ![Check Mark](/docs/images/check-mark.svg)|
| Followers | followers/ | Returns all the profiles with followers  | ![Check Mark](/docs/images/check-mark.svg)|
| Followers | followers/int:pk/ | Returns the selected profile with its follower  | ![Check Mark](/docs/images/check-mark.svg)|
| Likes | likes/ | Returns all the posts that has likes  | ![Check Mark](/docs/images/check-mark.svg)|
| Likes | likes/int:pk/ | Returns the selected post that was like  | ![Check Mark](/docs/images/check-mark.svg)|
| Post | posts/ | Returns all the posts that was created  | ![Check Mark](/docs/images/check-mark.svg)|
| Post | posts/int:pk/ | Returns the selected post  | ![Check Mark](/docs/images/check-mark.svg)|
| Profile | profile/ | Returns all the profiles that was created  | ![Check Mark](/docs/images/check-mark.svg)|
| Profile | profile/int:pk/ | Returns the selected profile  | ![Check Mark](/docs/images/check-mark.svg)|

### Bugs
There was only a small of bugs that was related to using the newest version of django instead of the older version they used on the Moments walkthrough.

The Following error showed when I tried to use any type of authentication method:

![CSRF Error](/docs/images/csrf-error.png)

The follwing Code was suggested by the Tutor (Ed) to fix the problem, this was to be added in the settings.py file;
````
CORS_ALLOWED_ORIGINS = [
    os.environ.get("CLIENT_ORIGIN"),
    os.environ.get("CLIENT_ORIGIN_DEV"),
]
````



# Technologies Used
[Back to top ⇧](#quackygraphy---a-platform-for-sharing-your-masterpiece-shots) <br />
[Table Of Contents ⇧](#table-of-content)

## Languages and Frameworks
- [Python](https://www.python.org/)  - The main programming language
- [Django](https://pypi.org/project/Django/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [Django REST Framework](https://pypi.org/project/djangorestframework/) - A powerful and flexible toolkit for building Web APIs

## Packages Used

- [asgiref](https://pypi.org/project/asgiref/) - A standard for Python asynchronous web apps and servers to communicate with each other.
- [cloudinary](https://pypi.org/project/cloudinary/) - Easily integrate your application with Cloudinary
- [dj-database-url](https://pypi.org/project/dj-database-url/) - Allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
- [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) - API endpoints for handling authentication securely in Django Rest Framework
- [django-allauth](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - package that facilitates integration with Cloudinary by implementing Django Storage API
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) - Adds Cross-Origin Resource Sharing (CORS) headers to responses.
- [django-extensions](https://pypi.org/project/django-extensions/) - Collection of global custom management extensions for the Django Framework.
- [django-filter](https://pypi.org/project/django-filter/) - Declaratively add dynamic QuerySet filtering from URL parameters.
- [django-rest-auth](https://pypi.org/project/django-rest-auth/) - Provides a set of REST API endpoints for Authentication and Registration
- [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) - JSON Web Token authentication plugin for the Django REST Framework.
- [gunicorn](https://pypi.org/project/gunicorn/) - A Python WSGI HTTP Server for UNIX.
- [oauthlib](https://pypi.org/project/oauthlib/) - Implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
- [Pillow](https://pypi.org/project/Pillow/) - Adds image processing capabilities to your Python interpreter
- [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for Python
- [pycodestyle](https://pypi.org/project/pycodestyle/) - A tool to check your Python code against some of the style conventions in PEP 8.   
- [PyJWT](https://pypi.org/project/PyJWT/) - Library for encoding and decoding JSON Web Tokens (JWT)
- [pytz](https://pypi.org/project/pytz/) - Allows accurate and cross platform timezone calculations
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - OAuthlib authentication support for Requests
- [sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.

## Other Tools
- [VSCode](https://code.visualstudio.com/) - Used to create and edit the website.
- [GitHub](https://github.com/) - Used to host and deploy the website as well as manage the project.
- [GitPod](https://www.gitpod.io/) - A cloud development environment for teams to efficiently and securely develop software.
- [Code Anywhere](https://codeanywhere.com/) - A different Cloud IDE Like gitpod, but useless. Would not recommend using.
- [Heroku](https://dashboard.heroku.com) - Used to deploy the website
- [ElephantSQL](https://www.elephantsql.com/) - Provides a browser tool for SQL queries where you can create, read, update and delete data directly from your web browser.
- [Cloudinary](https://cloudinary.com/) - Used to host all static files.

# Deployment

## Cloning a Template

1. Go to the [Template](https://github.com/Code-Institute-Org/gitpod-full-template) your cloning from
2. Click on the "Use This Template" dropdown
3. Within the Dropdown, Click on "Create a new repository"
4. Give your new repository a cool name.
5. Click on the green "Create repository from template"

## Running in VS Code
1. Open VS Code
2. Log into your Github account
3. On the lefthand side, click on the Source Control Icon
![Source Control Screenshot](/docs/deployment/vscode-source-control.png)
4. After Clicking on the "Clone Repository" button, all of your puplic repositories will appear on the top url bar.
![Clone Repository](/docs/deployment/clone-repository.png)
5. Open your newly created repository and happy coding!

<b>Just note!!</b>
If you work on a Cloud IDE like Code Anywhere or Gitpod after commiting and pushing from VS Code, to insure you get all the latest code, first run "git fetch" and then "git pull" in the terminal. When you continue working on the VS Code again, run the same two commands.

## Deploying With Heroku
1. Log into [Heroku Dashboard](https://dashboard.heroku.com/)
1. Click on the "New" dropdown
1. Click on "Create New App"
    - ![Create New App](/docs/deployment/heroku-create.png)
1. Insert a cool for your project in the "App Name" box
1. Change the Region to Europe
1. Click on "Create App"
    - ![Heroku Create](/docs/deployment/heroku-region.png)
1. <b>IMPORTAND!!</b> Heroku loves adding exrta add-ons, so remember to remove those after creating a new app.
1. Go to the "Deploy" tab and Connect your Github repository
1. Click on "Deploy Branch"
1. Go to the "Settings" Tab and add the following to the Config Vars:
    - `ALLOWED_HOST` = `"The name of your deployd site"` <br/>
    <b>EXAMPLE: (pp5-quackygraphy.herokuapp.com)</b>
    - `CLIENT_ORIGIN` = `"The Link of the deployed site"`  <br/>
    <b>EXAMPLE: (https://pp5-quackygraphy-app.herokuapp.com)</b>
    - `CLIENT_ORIGIN_DEV` = "`The link of the DEV site`"  <br/>
    <b>EXAMPLE: (http://localhost:3000)</b>
    - `CLOUDINARY_URL` = "`This will be the link from your cloudinary`"  <br/>
    <b>EXAMPLE: (cloudinary://number:code@letters)</b>
    - `DATABASE_URL` = "`This will be the link to your database`"  <br/>
    <b>EXAMPLE: (postgres://code:randomcode@code.db.elephantsql.com/code)</b>
    - `SECRET_KEY` = "`This can be any random key that is is also the same on the project`" <br/>
    <b>EXAMPLE: (Sup3rS3CreTC0de)</b>
1. After updating the settings, Go to "Deploy" and deploy branch again.

# Credits

- Main credit goes to Code Institute DRF Tutorial Project, used through as a basis for the creation of this API. Originally wanted to build an app based around dungeon and dragons and the type of players they can build, but unfortunalty, I'm away for 2 weeks before my upload deadline. So I kept it simple.

# Acknowledgements

- The tutor support was phenomenal, as always, at helping me fix my little problems. 



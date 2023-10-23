# YOUR PROJECT TITLE
Post submission system
#### Video Demo:  https://www.youtube.com/watch?v=NT3gdQnYyeA
#### Description:
You can create an account and submit a post that can be seen and liked by other users.

This project uses the following languages, libraries, and frameworks:
- SQLite: For the database that contains tables for users, posts, and likes.
- Flask: To build the backend, including signing up, logging in and out, submitting, deleting, and liking a post, as well as using Jinja syntax to render HTML pages.
- SQLAlchemy 2.0: Used instead of CS50's library to gain experience with a tool that is regularly used in the industry to work with databases.
- Flask-sqlalchemy: To make working with SQLAlchemy within Flask easier.
- HTML/CSS: To build the pages of the website, including the template used by Jinja.
- Javascript: To update the number of likes and the look of the like button depending on whether the post was liked or not

Files description:
- app.py: To run the app
- instance/project.db: SQLite3 database that contains tables for users, posts, and likes.
- static/index.js: Javascript file that contains the code to update the displayed number of likes and the look of the like button depending on whether the post was liked or not.
- static/main.css: CSS file that contains the styles used in the front-end of the web app. Relative units and flexbox were used to preserve the app's responsiveness and make it usable on as many screen sizes as possible.
- static/reset.css: CSS file that resets the browser's native styles. This reset ensures that the look of the website is consistent across all browsers.
- templates/layout.html: The base layout used by Jinja. Contains a header with a navbar that changes depending on whether a user is logged in or not.
- templates/home.html: Web page rendered using Jinja where all posts stored in project.db are displayed.
- templates/layout.html: Base template used by Jinja to render the other pages.
- templates/login.html: Web page rendered using Jinja that allows a user to login by providing their username and password.
- templates/new-post.html: Web page rendered using Jinja that allows a user to write a new post.
- templates/sign-up.html: Web page rendered using Jinja for a new user to sign up by providing a username, an email, and a password.
- website/__init__.py: Python file invoked when the website folder is imported in app.py.
- website/auth.py: Python file that contains the code necessary to sign up, log in, and log out. Includes password hashing, username and email checks and validation.
- website/models.py: Python file where the tables in project.db are declared using SQLAlchemy and flask-sqlalchemy
- website/views.py: Python file that contains the functions required to render the home page (contains all the posts), post, delete, and like a post, check the logged in user's posts and all posts sorted in descending order by number of likes.

Potential upgrades:
- A more robust email validation system
- Improve website design
- Limit the number of posts displayed in one page
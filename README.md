# Phone~Box

This project is a comical website for a fictional charity called "Phone~Box". Set up to take donations via the [Stripe](https://stripe.com/) API in order to provide "disenfranchised" children... with mobile phones. Because "How else would they let the world know how important my dog is during a pandemic" - Generic Instagram Teen User.

The Page would facillitate a user to sign up for an account login to a personal profile, and donate money via the donations page.

Live Site can be located here https://phone-box.herokuapp.com/
 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

User Stories
- As a user, Id like to sign up for an account.
- As a user, I'd like to be able to login to my personal account with the username OR email and password I signed up with.
- As a user looking to make a dontation, Id like to navigate to the Donations page in order to make a contributuon with as little confusion as possible.
- As a user who has donated, I may want to show that I have donated.
- As a user who donated, I may want to stay anonymous.
- As a user, I may want my own profile to feel a part of a larger community.
- As a user, I may want to see testimonials to view how past donations have helped those in need.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, I detail the Tools and technologies used to build the project.

- [Visual Studio Code](https://code.visualstudio.com/)
    - This is the IDE or 'Integrated Development Environment' used to build the project.
- [HTML](https://www.w3schools.com/html/html_intro.asp#:~:text=HTML%20stands%20for%20Hyper%20Text,structure%20of%20a%20Web%20page)
    - The Project uses 'Hypertext Markup Language' to create the basic skeleton for each web page.
- [CSS](https://www.w3schools.com/css/default.asp)
    - The project uses 'Cascading Style Sheets' to create the styles for each page and applies them via custom classes and Id's.
- [Python3](https://www.python.org/download/releases/3.0/)
    - The project uses Python as its backend language.
- [Django](https://www.djangoproject.com/)
    - The project uses Django as it's 'Full Stack Framework' in order to create and organise, templates, views, and apps.
- [Django_Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
    - The project uses allauth in order to quickly integreate the abillity for a user to create and login to a user account on the site.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to allow certain function in CDNs and libraries to work properly.
- [Bootstrap4](https://getbootstrap.com/)
    - The project uses Bootstrap to help build the styles with classes and Id's.
- [Materialize0.100.2](http://archives.materializecss.com/0.100.2/)
    - The project uses Materialize to help build the styles with classes and Id's.
- [Stripe](https://stripe.com/gb)
    - The project uses Stripe API to create an integrated payment system, used by the user to make charitable donations by card.
- [Heroku](https://signup.heroku.com/)
    - The project uses Heroku to host the live site and all the required code and static files to serve the site.
    - Find the live site here: [Phone~Box](https://phone-box.herokuapp.com/)
- [Whitenoise](http://whitenoise.evans.io/en/stable/)
    - The project uses whitenoise in order to allow better web serving for Python apps, in this case for serving staticfiles with storage.
- [Git](https://git-scm.com/)
    - The project uses Git to handle version control, and allows for pushing small or large project changes into a github repository.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section give a detailed rundown on how to run the project locally and how it was deployed to the [Heroku](heroku.com) platform.
The live site is avaible here: [Phone~Box](https://phone-box.herokuapp.com/)

To run the code locally via development server:
1) Ensure these variables are correct in settings.py
    - DEBUG = True / DEBUG = 'DEVELOPMENT' in os.environ """depending on your IDE this may not work"""
2) To run the project type into your IDE terminal window
    - python manage.py runserver

The IDE will then run the development server in the terminal window.
- Click on the port to open the landing page in the your web browser.

To Deploy to Heroku:
1) ensure these variable are correct in settings.py
    - DEBUG = False
    - ALLOWED_HOSTS = ['*']
    - WSGI_APPLPICATION = 'charitybox.wsgi.application'
    - MIDDLEWARE = 'whitenoise.middleware.WhiteNoiseMiddleware',  """ paste this at the end of the MIDDLEWARE section """
    - STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    - STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    - STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static',)

2) Ensure you have Procfile
    - pip3 freeze > Procfile

3) Ensure you have requirements.txt
    - pip3 freeze > requirements.txt

4) Use this command in the terminal window to create a 'staticfiles' directory
    - python manage.py collectstatic

5) In terminal, use these commands to save your project to a git repository
    - git init  """ creates a new offline git repo if you havn't already """
    - git add .  """ adds ALL untracked or modified project files to local git repo """
    - git commit -m "your descriptive message here."  """ saves your git repo """

6) Push/Upload git repo to Github
    - Download and install [Github Desktop](https://desktop.github.com/)
    - Ensure you are logged in by following in this in the top left corner of the app: File --> options --> Account --> Sign in
    - Enter your log in details.
    - Select your offline git repo by following: current repository --> filter (type project name) --> yourprojectname
    - Click Push Origin in the top middle of the app screen.
    - Github Desktop will then create your Git repo on Github.com

7) Create and Setup Heroku app
    - Create Heroku account.
    - in Dashboard in the top right corner, follow: New --> Create new app
    - Give you app a name.
    - Select a server closest to you.
    - Click create app.
    - Once redirected, click 'Deploy' tab towards the top left of the screen.
    - Next to the heading 'Deployment Method' select github to connect your account
    - Once connected use filter to search for the repo you created earlier.
    - Click connect
    - Scroll down a little and click 'Enable Automatic Deploys'

8) Ensure these environment variable are in settings, by clicking 'Reveal config Variables':
    - PORT = 5000
    - IP = 0.0.0.0
    - DEBUG = ""
    - DATABASE_URL = postgres://uvqwokrrhljpuz:abcd3b8f65747473a89a9ad8943aa9f880f391e8e440f515991cc6427688a441@ec2-54-72-155-238.eu-west-1.compute.amazonaws.com:5432/d8sgl09bcei9to
    - SECRET_KEY = "Insert you secret key here to keep it out of version control"
    
9) Go Live!
    - Go back to the 'Deploy' tab
    - Scroll to the bottom of the page
    - Next to 'Choose a branch to deploy' click 'Deploy Branch'
    - Watch Heroku Build your live site.
    - At the top of the screen click 'Open app' to load and view the live site.
    - It should look something like: https://phone-box.herokuapp.com/

- PLEASE NOTE:
    - If your custom styles are not being rendered, this is because of Herokus MIME checker
    - If this happens go back to your project and add attribute -- type="text/css" to your .css link in base.html
    - re run this: python manage.py collectstatic
    - Go back through the deployment steps to update your git repository
    - Go back to 'Deploy' in your heroku apps Dashboard, scroll down and click 'Deploy branch'
    - This should have resolved the errors.

## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The image used for the main banner of the site were obtained from [webdesignerdepot](https://www.webdesignerdepot.com/2012/11/6-free-mobile-device-emulators-for-testing-your-site/) by way of google search.

### Acknowledgements

- I received inspiration for this project from X

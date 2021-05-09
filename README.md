# Phone~Box

This project is a comical website for a fictional charity called "Phone~Box". Set up to take donations via the [Stripe](https://stripe.com/) API in order to provide "disenfranchised" children... with mobile phones. Because "How else would they let the world know how important my dog is during a pandemic" - Generic Instagram Teen User.

The Page would facillitate a user to sign up for an account login to a personal profile, and donate money via the donations page.

Live Site can be located here https://phone-box.herokuapp.com/
 
## UX
 
In this section I detail the 'User Experience Design' process (or UXD), Included is some typical user stories, a section containing links to the wireframe diagrams and notes. And a rundown of the aesthetic.

Aesthetic
- The overall colour theme used for the project on navbar and button elements is a light blue colour taken from the materialize library for the backgrounds and white text. My thoughts on this was that not only does it give off a friendly appearance, but the light blue also conveyes a sense of peacefullness.
- The main background (source acknowleged in the acknowledgements section at the bottom of the readme) again was selected for a little bit of comedy sake, as it a grouping of peoples hands holding up older style phones, typically used by people who are either nostalgic or desire a cheaper, more simple phone. With a sky blue background, I thought overall the image fit the colour-pallete and added to the comedy factor. This image would cover the whole of the pages background and be set at a z-index of -1 so that it would sit behind all other page elements.
- The footer, at the bottom of the page I decided to set its position at 'relative' so that it would scroll with the rest of a pages content. I chose an off-white blue with black text, to fit with the main aesthetic of the project, while not being so harsh on a users eyes, but also drew the users gaze once the footer was visible as it contains contact information. AGain the phone number contained in the footer element is the 'Reynholm Industries Emergency Services' telephone from the TV show 'IT Crowd' for the comedy factor.

Colour Palette used<br>
![Colour Pallette](https://github.com/phillpearsondev/phone-box/blob/master/wireframes/images_for_readme/color-pallette.jpg)

User Stories
- As a user, Id like to sign up for an account.
- As a user, I'd like to be able to login to my personal account with the username OR email and password I signed up with.
- As a user looking to make a dontation, Id like to navigate to the Donations page in order to make a contributuon with as little confusion as possible.
- As a user who has donated, I may want to show that I have donated.
- As a user who donated, I may want to stay anonymous.
- As a user, I may want my own profile to feel a part of a larger community.
- As a user, I may want to see testimonials to view how past donations have helped those in need.

Wireframes

The Folder containing wireframes can be found here: [Wireframes](https://github.com/phillpearsondev/phone-box/tree/master/wireframes)

- [Wireframe 01](https://github.com/phillpearsondev/phone-box/blob/master/wireframes/thumbnail_IMG_20210419_134840.jpg) 'Landing Page Design'
- [Wireframe 02](https://github.com/phillpearsondev/phone-box/blob/master/wireframes/thumbnail_IMG_20210419_134851__01.jpg) 'Testimonials Page Design'
- [Wireframe 03](https://github.com/phillpearsondev/phone-box/blob/master/wireframes/thumbnail_IMG_20210419_134902.jpg) 'User Dashboard Design'
- [Wireframe 04](https://github.com/phillpearsondev/phone-box/blob/master/wireframes/thumbnail_IMG_20210419_134913.jpg) 'Checkout Design'
- [Wireframe 05](https://github.com/phillpearsondev/phone-box/blob/master/wireframes/thumbnail_IMG_20210419_134931__01.jpg) 'UserProfile Model Design'
- [Wireframe 06](https://github.com/phillpearsondev/phone-box/blob/master/wireframes/thumbnail_IMG_20210419_134950__01.jpg) 'Register View Design'
- [Wireframe 07](https://github.com/phillpearsondev/phone-box/blob/master/wireframes/thumbnail_IMG_20210419_135008.jpg) 'Text Content Ideas'
- [Wireframe 08](https://github.com/phillpearsondev/phone-box/blob/master/wireframes/thumbnail_IMG_20210419_135016.jpg) 'About Text Ideas'
- [Wireframe 09](https://github.com/phillpearsondev/phone-box/blob/master/wireframes/thumbnail_IMG_20210419_135034.jpg) 'OnClick Text Sound Design'

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

In this section I hope to provide a detailed rundown on how each aspect of the project has been tested during development, and before submission. Included would be an idea of how each link was tested, how user authentication or sign/log in and registration is tested. Aswell as what has been used to run automated tests. Below, I have included the user stories, and their associated tests, updated as that feature has been completed.

During development I used this line in the IDE terminal in order to test via localhost server on port 5000:
- python manage.py runserver

User Stories
- ~~As a user, Id like to sign up for an account.~~
    - On the landing page, you will seee links in the top right corner of the blue navbar.
    - Click the 'Register' link to be taken to a sign up form.
    - Enter your preffered email twice, your preffered username, and your preffered password twice.
    - Click the 'Sign Up' button as the bottom of the form.
    - You should then be redricted and asked to confirm your email address. (I did this by confirming the email sent in IDE terminal window)
    - Once confirming your email address, you should be redirected to the user dashboard.
    - You can access the user dashboard at any time after this by clicking the 'Profile' link in the top right of the navbar element.

- ~~As a user, I'd like to be able to login to my personal account with the username OR email and password I signed up with.~~
    - On the 'landing page' (or any page, where you should see the navbar) in the navbar at the top right of screen, provided you are not currently logged in, click on the link that says 'login'.
    - You will then be redirected to the login form. fill it in using your username and password you used when you created your account previously.
    - Click the 'Sign in' button at the bottom of the form.
    - You will then be redirected to the user dashboard where you should see your personal account information displayed.

- ~~As a user looking to make a dontation, Id like to navigate to the Donations page in order to make a contributuon with as little confusion as possible.~~
    - On the 'landing' page, or any page where you can either see 'Donations' in the navbar or a button that either says 'Donate' or 'Make a Donation' click any of these to be redirected to the Donations page.
    - Select from one of three tiers of donations, cheapest to highest cost from left to right, by clicking the 'Donate' button embedded in their corresponding card element.
    - You will then be redirected to the checkout page.

- As a user who has donated, I may want to show that I have donated.

- ~~As a user who donated, I may want to stay anonymous.~~
    - Navigate to the donations page by either clicking on the 'Donations' link in the navbar or, the 'make a donation' button on the landing page.
    - Once redirected, choose between one of the three tiers of donation, and click the corresponding button to redirect to the checkout page.
    - Once redirected, enter your information and test card details as follows:
    
    Card Number: 4242-4242-4242-4242
    
    Expiry Date: Any future date MM/YY
    
    CVC: Any three numbers ???
    
    - Then click on the donate now button on the bottom of the checkout form to make the payment.
    - You will then be redirected to the success message page which will display the value of your donation within the text.

- ~~As a user, I may want my own profile to feel a part of a larger community.~~
    - Follow the steps above in order to login to your account.
    - Once logged in your will be automatically redirected to the User Dashboard.
    - You can access this Profile at any time simply by going to navbar at the top of the page, and clicking the 'Profile' link.


Automated testing??
Bugs??

## Deployment

This section give a detailed rundown on how to run the project locally and how it was deployed to the [Heroku](heroku.com) platform.
The live site is avaible here: [Phone~Box](https://phone-box.herokuapp.com/)

To run the code locally via development server:
1) Ensure these variables are correct in settings.py
    - DEBUG = True / DEBUG = 'DEVELOPMENT' in os.environ """depending on your IDE this may not work"""
2) To run the project type into your IDE terminal window
    - python manage.py runserver

The IDE will then run the development server in the terminal window.

3) Click on the port to open the landing page in the your web browser.

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
- The text in the About section of the landing page was written by my fiancee Suzy-Erin Collins
- The Text in the 'Big Spender' card element on the donations page makes reference to the lyrics of the song 'Bohemian Rhapsody' by Queen.

### Media
- The image used for the main banner of the site were obtained from [webdesignerdepot](https://www.webdesignerdepot.com/2012/11/6-free-mobile-device-emulators-for-testing-your-site/) by way of google search.

### Acknowledgements

- A Big thank you to my Mentor Reuben Ferrante for his help and advice, and generally being cheerful and supprtive all the while I was losing my head.
- The Phone number in the footer element of the project is the 'Reynholm Industries Emergencies Services' number from the TV show 'IT Crowd'.
- The stripe payments system was inpired by the Youtuber [Dennis Ivy](https://www.youtube.com/channel/UCTZRcDjjkVajGL6wd76UnGg)

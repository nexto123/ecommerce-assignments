# Full-Stack Dev.

A Code Institute Django Project

[![Build Status](https://travis-ci.org/nexto123/ecommerce-assignments.svg?branch=master)](https://travis-ci.org/nexto123/ecommerce-assignments)


## Getting Started

Broken Bucket is an E-commerce web app project. This app should demonstrate a basic understanding of the Django framework and its practical application. The idea behind the app is simply the selling of broken items which promotes the reusable culture. 

## UX

The concept behind the design is a straight forward grid of 3 cards per row. We should have 6 cards per page and if there's more to display would be paginated. The font is Roboto and it's fallback San-Serif if the need arises. The website is heavy with bootstrap4 as most of the components came premade. The navbar, footer and cards can easily be plucked from [bootstrap](www.getbootstrap.com)

 
 
## Prerequisites

To get started let's make some preps. You'd need to have a basic understanding of the python Django framework and at least a grasp on some frontend technologies. Besides the usual HTML, CSS, Javascript, it would be handy to know a bit of bootstrap. Bootstrap is pretty much all that is needed, and a bit CSS for some decoration. 
 
## Virtualenv

The virtualenv, in this case, is a pre-requisite for this project. Virtual env is a tool that serves as a sandbox for your python projects. There are other environments like Conda which are pretty easy to use. But when choosing your env's you should also consider deployment. I decided to go with the basic virtualenv wrapper as I'm familiar with its deployment requirements. The command for this is;
``` 
 [sudo]pip install virtualenv 
```

## Used Extensions for App Dependencies

pip is a package-management system used to install and manage software packages written in Python. These dependencies are installed to assist some features that might not come with Django. In our app we will use this list:

* Pillow - for Image Processing
* Stripe - for Payment Gateway
* Django==2.2 - Python Framework
* Boto3 - Storage requirement for AWS S3 Bucket
* django-crispy-forms==1.7.2 - Premade form template
* psycopg2==2.8.2 - sycopg2 is a DB API 2.0 compliant PostgreSQL driver
* dj-database-url==0.5.0 - DATABASE_URL environment variable
* gunicorn==19.9.0 - Web Server Gateway Interface 



## Database setup

Django comes with a lot of features right out of the box, and SQLite database is one of it. But for more sophisticated functionality and durability, it becomes necessary to migrate your database to a more grounded one like MySQL or PostgreSQL.
To use Heroku Postgres;

1. First, create an account on [Heroku](www.heroku.com)
2. Within the resources tab search add-ons for Heroku postgres
3. Select and validate and move on to the settings tab.
4. within settings reveal config and copy database URL.
5. Update Database Configuration in settings.py and add your Heroku database_url.
6. Finally, you will perform a migration.

```
python manage.py migrate 

```
7. Done! your database is ready. heroku will however only set you up with a very basic 

## Testing

We will use [travis CI](https://travis-ci.org) for our automated tests. This is quite popular too now for tests.

Travis CI is a hosted, distributed continuous integration service used to build and test projects hosted at GitHub. Travis CI automatically detects when a commit has been made and pushed to a GitHub repository that is using Travis CI, and each time this happens, it will try to build the project and run tests.

To use Travis CI;

* Go to www.travis-ci.com and Sign up with GitHub.
* Accept the Authorization of Travis CI. You’ll be redirected to GitHub.
* Click the green Activate button, and select the repositories you want to use with Travis CI.
* Add a .travis.yml file to your repository to tell Travis CI what to do. 
* After connecting to GitHub check your readme file if you are passing.
* Voila!

The app has been tested on these mobile devices; iPad, iPhone 6 and 7,iPhoneX and they respond very well. The font selected 'Roboto' renders perfectly on most browsers, including Mozilla, safari and chrome, as am yet to test them on IE.9 and above.


|    Tested      |    Chrome     | Mozilla    |   Safari  |    
| -------------  |:-------------:|  ---------:|:---------:|
| Animation      |    Yes        |     Yes    |   Fast    |
| Images         |    Yes        |     Yes    |   Fast    |
| SVG            |    Yes        |     Yes    |   Fast    |
| Font awesome   |    Yes        |     Yes    |   Fast    |
| Text-Rendering |    Yes        |     Yes    |   Fast    |
| Responsiveness |   excellent   |     Yes    |   Fast    |
| Functions      |   excellent   |     Yes    |   Fast    |



## Deployment

To deploy our app to a hosting platform like Heroku we'll have to meet these few requirements.

*lets first push the project to our GitHub repo*

* create a new repository;
* first assign a repository name on GitHub since that's what I'm using.
* write a short description of the site to be uploaded.
* You will either select to initialize your repository with a README.md file. (optional)
* create your repository.
* You will perform a git remote login
* And finally, git push -u origin master.


*lets now push the project to Heroku*

Heroku is a cloud platform that lets you build, deliver, monitor and scale apps.
To deploy to Heroku, there are two critical steps to perform even before your final commit message.
We have the Procfile, runtime.txt file and the requirement.txt files. 
These are critical necessities if you are deploying to Heroku.
To get requirement.txt file input this into your cli.
```
sudo pip3 freeze —local > requirements.txt
```
To get the Procfile file input this into your cli.
```
$ echo web: python app.py > Procfile
```
* Inside your bash enter ``heroku login`` and follow the prompts. Perform ``git add --all`` and `` git commit``.

* Finally let's disable static as we will host our static files on aws s3 bucket. To disable static ``heroku config:set DISABLE_COLLECTSTATIC=1``.

* Finally run the code ``git push heroku master``

To host static files on AWS S3
This is a very detail [link](https://www.codingforentrepreneurs.com/blog/s3-static-media-files-for-django/)

*After creating your IAM accounts and creating your s3 Buckets on aws. 
follow these steps to get things working for you;

1. connect your aws account to your Django.
2. Add the necessary keys to your env.py or whatever secured files you have.
3. All that is needed now is to perform a collectstatic command to move your static files into your s3 bucket.
$. Done. After pushing to Heroku you will now be seeing your static files


### [Live](https://broken-bucket.herokuapp.com/)

## Features to be added:

These are feature left to be implemented.

* Ticketing system
* Contact Form
* User profile page
* User product page
* User chat and comment features


### Features:

1. Home page -> product view page
2. Account Page -> create an account and log in
3. Click on product -> View product Detail & add to cart
3. Order Page -> Finalize your order.
4. Check out product -> Pay with card
5. Cart Page -> See items inside the cart, Delete items inside the cart, decrease/increase items inside the cart.

## Mail Service

Mailgun.

check out documentation using [mailgun](https://documentation.mailgun.com/en/latest/)


## Versioning

 Git


## Author

Ernest Bruce Brown


## Media

* Google Images


## Acknowledgments

* Chris. Z
* Hose Portilla
* Nestor Villoria

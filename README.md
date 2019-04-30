# Full-Stack Dev.

A Code Institute Django Project

[![Build Status](https://travis-ci.org/nexto123/ecommerce-assignments.svg?branch=master)](https://travis-ci.org/nexto123/ecommerce-assignments)


## Getting Started

Broken Bucket is an Ecommerce web app project. This app should demonstrate a basic understanding of the django framework and it's practical application. The idea behind the app is simply the selling of broken items which promotes the reusable culture. 

## UX

The concept behind the design is a straight forward grid of 3 cards per row. We should have 6 cards per page and if there's more to display would be paginated. The font is roboto and it's fallback San-Serif if the need arises. The website is heavy with bootstrap4 as most of the components came premade. The navbar, footer and cards can easily be plucked from [bootstrap](www.getbootstrap.com)

 
 
## Prerequisites

To get started let's make some preps. You'd need to have a basic understanding of the python Django framework and at least a grasp on some frontend technologies. Besides the usual HTML, CSS, Javascript, it would be handy to know a bit of bootstrap. Bootstrap is pretty much all that is needed, and a bit css for some decoration. 
 
## Virtualenv

The virtualenv in this case is a pre-requisite for this project. Virtual env is a tool that serves as a sandbox for your python projects. There are other environments like Conda which are pretty easy to use. But when chosing your env's you should also consider deployment. I decided to go with basic virtualenv wrapper as i'm familiar with it's deployment requirements. The command for this is;
``` 
$ [sudo]pip install virtualenv 
```

## Used Extensions for App Dependencies

pip is a package-management system used to install and manage software packages written in Python. These depencies are installed to assist some features that might not come with django. In our app we will use this list:

* Pillow - for Image Processing
* Stripe - for Payment Gateway
* Django==2.2 - Python Framework
* Boto3 - Storage requirement for AWS S3 Bucket
* django-crispy-forms==1.7.2 - Premade form template
* psycopg2==2.8.2 - sycopg2 is a DB API 2.0 compliant PostgreSQL driver
* dj-database-url==0.5.0 - DATABASE_URL environment variable
* gunicorn==19.9.0 - Web Server Gateway Interface 



## Database setup

Django comes with a lot of features right out of the box, and sqlite database is one of it. But for more sophisticated functionality and durabilty it becomes neccessary to migrate your database to a more grounded one like MySQL or PostgreSQL.
To add Heroku Postgre;

1. First create an account on [Heroku](www.heroku.com)
2. Within the resources tab search add-ons for heroku postgres
3. Select and validate and move on to the settings tab.
4. within settings reveal config and copy database url.
5. Update Database Configuration in settings.py and add your heroku database_url.
6. Finally you will perform a migration.

```
python manage.py migrate 

```
7. Done



```
mongodb://<dbuser>:<dbpassword>@ds163103.mlab.com:63103/mytestdb
```
Now you will place your link inside the flask app.py.
Voila! Your database is ready.


## Testing

nothing
## Deployment To Git & Heroku

nothing

```
sudo pip3 freeze —local > requirements.txt
```
To get the Procfile file input this into your cli.
```
$ echo web: python app.py > Procfile
```



nothing

#### [Live Version]

### Features to be added:



### Features:





## Versioning

 Git


## Author

Ernest Bruce Brown


## Media

* Google Images


## Acknowledgments

* Chris. Z




# Lavender Haven

![mockup](readme_img/amiresponsive.png)

For this last project I got inspired by the small business located in Dalmatia, Croatia. Hvar island is magical place well known for its lavander fields. I looked up their website and not much but the most important information was displayed for the users, so I thought of making the lavander as a hero of my last project and turning the idea into something a bit more advanced.

My website is a fully functioning B2C and B2B e-commerce application site and the main point is for the user to be able to make a payment for their purchases. But I really wanted to implement more to it than just a webstore, so the websites main features including the 'articles', 'checkout', 'cart', 'account' are the 'about', 'blog', 'contacts', 'testimonials' and the users have the option for a 'newsletter' subscription. The website provides the possibilty for the 'super user' to fully perform the CRUD actions on the 'articles' from both the admin panel and in the front-end and the users can do the same but with 'testimonials', but for UD in CRUD the testimonials must be first approved by the 'super user'.

The websites content in most parts is available for everyone. User can purchase articles as authenticated and as non-authenticated, but some actions as liking the blog post or leaving a testimonial requires a login.

I really wanted to show the skills I have learned during this course with CI. Programming its not easy and it will take me a loads of practice to get to the level I really want to be but I hope that one day I will be the senior and be the person to go to. 

<hr>

The live deployed application can be found deployed on [Heroku](https://lavender-haven-pp5-39266b62efea.herokuapp.com/).

The link to my Github repository's [Github Repo](https://github.com/Balkaneros91/Lavender-Haven-PP5).

<hr>

## CONTENTS

- [User Experience](#user-experience-ux)

  - [Agile](#agile)
  - [User Stories](#user-stories)
  - [Project stages](#project-stages)

- [Design](#design)

  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Wireframes](#wireframes)

- [Features](#features)

  - [General Features on Each Page](#general-features-on-each-page)
  - [Future Implementations](#future-implementations)

- [Technologies Used](#technologies-used)

  - [Tools & Technologies Used](#tools--technologies-used)
  - [Database Design](#database-design)
  - [Entity Relationship Diagram](#entity-relationship-diagram)

- [Deployment & Local Development](#deployment--local-development)

  - [Deployment](#deployment)
  - [Github](#github)
  - [Gitpod](#gitpod)
  - [ElephantSQL](#elephantsql)
  - [AWS](#aws)
  - [Stripe](#stripe)
  - [Heroku](#heroku)
  - [Local deployment](#local-deployment)
      - [Cloning](#cloning)
      - [Forking](#forking)

- [Testing](#testing)

  - [Responsiveness](#responsiveness)
  - [Manual testing](#manual-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [Lighthouse](#lighthouse)
  - [W3C HTML Validator](#w3c-html-validator)
  - [JIGSAW W3C CSS Validator](#jigsaw-w3c-css-validator)
  - [JShint](#jshint)
  - [Code Institute Python Linter](#code-institute-python-linter)
  - [Chrome DevTools](#chrome-devTools)
  - [Known bugs](#known-bugs)
  - [Solved bugs](#solved-bugs)

- [Credits](#credits)
  - [Code Used](#code-used)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

<hr>





## Design

### Colour Scheme

Since my website is all about lavender and it's culture I wanted my page to reflect the calmness and tranquility of it. The color palett is colorful and playful and I really wanted to achieve the welcoming and relaxing invitation for the user to get their full attention so they can explore all the content Lavender Haven has to offer.

[Coolors.co](https://coolors.co/) was the website I've used to fetch the colour palette presented.

![Colour Palette](readme_img/coolors.png)

### Typography

I have picked Amethysta font because it perfectly suited the content of my website and I have used the same font throughout the whole webcontent.

![Typography](readme_img/google_fonts_family.png)
![Typography](readme_img/google_fonts_style.png)

## Wireframes

[Balsamiq](https://balsamiq.com/wireframes) is used for wireframe design.

### Lavender Haven's Home Page

<details>
<summary>Click here!</summary>

#### Mobile

![screenshot](readme_img/wireframes/mobile_home.png)

#### Desktop

![screenshot](readme_img/wireframes/desktop_home.png)

</details>

### About Page

<details>
<summary>Click here!</summary>

#### Mobile

![screenshot](readme_img/wireframes/mobile_about.png)

#### Desktop

![screenshot](readme_img/wireframes/desktop_about.png)

</details>

### Blog Page

<details>
<summary>Click here!</summary>

#### Mobile

![screenshot](readme_img/wireframes/mobile_blog.png)
![screenshot](readme_img/wireframes/mobile_blog_detailed.png)

#### Desktop

![screenshot](readme_img/wireframes/desktop_blog.png)
![screenshot](readme_img/wireframes/desktop_blog_detailed.png)

</details>

### Contacts page

<details>
<summary>Click here!</summary>

#### Mobile

![screenshot](readme_img/wireframes/mobile_contacts.png)

#### Desktop

![screenshot](readme_img/wireframes/desktop_contacts.png)

</details>

### Articles page

<details>
<summary>Click here!</summary>

#### Mobile

![screenshot](readme_img/wireframes/mobile_articles.png)
![screenshot](readme_img/wireframes/mobile_article_detailed.png)
![screenshot](readme_img/wireframes/mobile_add_edit_article.png)
![screenshot](readme_img/wireframes/mobile_article_delete.png)

#### Desktop

![screenshot](readme_img/wireframes/desktop_articles.png)
![screenshot](readme_img/wireframes/desktop_article_detailed.png)
![screenshot](readme_img/wireframes/desktop_add_edit_article.png)
![screenshot](readme_img/wireframes/desktop_article_delete.png)

</details>

### Testimonials page

<details>
<summary>Click here!</summary>

#### Mobile

![screenshot](readme_img/wireframes/mobile_testimonials.png)
![screenshot](readme_img/wireframes/mobile_testimonial_detailed.png)
![screenshot](readme_img/wireframes/mobile_testimonial_edit.png)
![screenshot](readme_img/wireframes/mobile_testimonial_delete.png)

#### Desktop

![screenshot](readme_img/wireframes/desktop_testimonials.png)
![screenshot](readme_img/wireframes/desktop_testimonial_detailed.png)
![screenshot](readme_img/wireframes/desktop_testimonial_edit.png)
![screenshot](readme_img/wireframes/desktop_testimonial_delete.png)

</details>

### SignUp, SignIn and SignOut pages

<details>
<summary>Click here!</summary>

#### Mobile

![screenshot](readme_img/wireframes/mobile_signup.png)
![screenshot](readme_img/wireframes/mobile_signin.png)
![screenshot](readme_img/wireframes/mobile_signout.png)

#### Desktop

![screenshot](readme_img/wireframes/desktop_signup.png)
![screenshot](readme_img/wireframes/desktop_signin.png)
![screenshot](readme_img/wireframes/desktop_signout.png)

</details>

### Unsubscribe page

<details>
<summary>Click here!</summary>

#### Mobile

![screenshot](readme_img/wireframes/mobile_unsubscribe.png)

#### Desktop

![screenshot](readme_img/wireframes/desktop_unsubscribe.png)

</details>

### Shopping cart page

<details>
<summary>Click here!</summary>

#### Mobile

![screenshot](readme_img/wireframes/mobile_cart_empty.png)
![screenshot](readme_img/wireframes/mobile_cart.png)

#### Desktop

![screenshot](readme_img/wireframes/desktop_cart_empty.png)
![screenshot](readme_img/wireframes/desktop_cart.png)

</details>

### Checkout and checkout success pages

<details>
<summary>Click here!</summary>

#### Mobile

![screenshot](readme_img/wireframes/mobile_checkout.png)
![screenshot](readme_img/wireframes/mobile_checkout_success.png)

#### Desktop

![screenshot](readme_img/wireframes/desktop_checkout.png)
![screenshot](readme_img/wireframes/desktop_checkout_success.png)

</details>

### Account and Order history Page

<details>
<summary>Click here!</summary>

#### Mobile

![screenshot](readme_img/wireframes/mobile_account_order_history.png)

#### Desktop

![screenshot](readme_img/wireframes/desktop_account_order_history.png)

</details>

<hr>












## Technologies Used

### Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Bootstrap](https://getbootstrap.com)
- [JavaScript](https://www.javascript.com)
- [Python](https://www.python.org)
- [Git](https://git-scm.com)
- [GitHub](https://github.com)
- [Gitpod](https://gitpod.io)
- [Django](https://www.djangoproject.com)
- [PostgreSQL](https://www.postgresql.org)
- [ElephantSQL](https://www.elephantsql.com)
- [Heroku](https://www.heroku.com)
- [AWS](https://aws.amazon.com/)
- [Gmail](https://www.google.com/gmail/about/)
- [Balsamiq](https://balsamiq.com/wireframes)

### Database Design

Entity relationship diagram is created using [Balsamiq](https://balsamiq.com/wireframes). ERD made it easier for me to visualize the relationships between my data structures which made the development process easier since everything was properly mapped out.

### Entity Relationship Diagram

![screenshot](readme_img/entity-relationship-diagram.png)

<hr>

## Deployment & Local Development

### Deployment

The live deployed application can be found deployed on [Heroku](https://lavender-haven-pp5-39266b62efea.herokuapp.com/).

---
## <strong>Deployment</strong>

### Github

This website was published using GitHub Pages.

- Navigate to [GitHub](https://github.com/) and log in.
- Navigate to your repositories and find the project you want to deploy
- Under the name of your chosen Repository you will see a ribbon of selections, click on 'Settings' located on the right hand side.
- Scroll down till you see 'Pages' heading on the left hand side
- Under the 'Source' click on the dropdown and select 'master' or 'main' branch and click save
- The page will reload and you'll see the link of your published page displayed under 'GitHub' pages.
- It takes a few minutes for the site to be published, wait until the background of your link changes to a green color before trying to open it.
- Congratulations you have deployed your project!
  
### Gitpod
 - Navigate to [Gitpod](https://gitpod.io/) through [GitHub](https://github.com/), [GitLab](https://www.gitlab.com/).
- In the browser’s address bar, prefix the entire URL with gitpod.io/# and press Enter.
- For example, gitpod.io/#https://github.com/gitpod-io/website
- We recommend you install the Gitpod browser extension to make this a one-click operation.
- Sign in with one of the listed providers and let the workspace start up.
- Congratulations, you have started your first of many ephemeral developer environments!

### ElephantSQL

<u>New to the website</u>
* Go to [ElephantSQL.com](https://www.elephantsql.com/) and click *Get a managed database today* button.
* Select Tiny Turtle by pressing the *Try now for FREE* button
- Select *Log in with GitHub* and authorize ElephantSQL with your selected GitHub account
- In the create new team form:
    - Add a *team name* (your own name is fine)
    - Read and agree to the Terms of Service
    - Select *Yes* for GDPR
    - Provide your email address
    - Click *Create Team*
- Click *Create New Instance*

<u>If you already have an account, after logging in to ElephantSQL:</u>
- Create a new app.
- Add a name of the app. This name should be a name that helps you identify which application the instance is used by.
- Select a plan: The plan you would like to have. I used <strong>Tiny Turtle Plan</strong>
- Select tags: I left this field blank.
- Select Region: I selected EU-West-1 (IRELAND).
- Then click review.
- Check that the details are correct tthen click <strong>"Create Instance"</strong>.
- Return to the ElephantSQL dashboard and click on the database instance name for this project.
- In the URL section, click the copy icon to copy the database URL which will then be put into the envy.py file in gitpod.

### AWS
## Amazon Web Services S3 host for static files and images
<u>Create an account</u> on [Amazon Web Services](https://aws.amazon.com/)
- Click on *create an aws account* by filling in your email and a password and choose a username for the account and select *continue*
- On the account type, select *personal*, fill out the required information, and click *create account and continue*
- Enter the credit card number which will be used for billing if the account goes above the free usage limits
- Complete the verification and once you confirm all the required information, your account will be created.

<u>Create a bucket</u>
- Once your signed in to your account, find S3 using the search bar, select and navigate to S3 to create a new bucket which will be used to store your static and media files
- Click the *create bucket* button and on the General configuration section, add the name of your bucket. It is a good idea to name the bucket the same as your project to keep your buckets organized and clear
- Select the region closest to you
- On the Object Ownership section, select *ACLs enabled* and a bucket ownership dropdown will appear, select *Bucket owner preferred*
- On the Block Public Access settings for this bucket section, uncheck *Block all public access*, check the *I acknowledge that the current settings might result in this bucket and the objects within becoming public* checkbox to make the bucket public and click *create bucket*
- Click the bucket you created and select the *properties* tab. Scroll down to find the *static web hosting* section and select *enable static web hosting*, tick *host a static website* and add *index.html* and *error.html* to the input fields for **Index document** and **Error document** respectively and click *save*.
- Open the permissions tab and copy the ARN (Amazon Resource Name). Navigate to the bucket policy section, click *edit* and select *policy generator*. From the *Select Type Policy* dropdown options, select S3 bucket policy. We want to allow all principal by adding the `*` to the input and the from the -Actions* dropdown, select *GetObject*.
- Paste the ARN we copied into the ARN (Amazon Resource Name) input field and click *add statement*, then click *generate policy*, copy the Policy from the new popup and paste it into the bucket policy editor and add `/*` at the end of the resource value to allow access to all resources in this policy and finally, click *save*.
- AWS has changed the format of their **cross-origin resource sharing (CORS)** configuration so we need to paste the update code below to the CORS section:
```json
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- For the **Access control list (ACL)** section, click *edit* and tick *List* for **Everyone (public access)** and accept the warning box. If the edit button is disabled you need to change the **Object Ownership** section above to **ACLs enabled**.

<u>Create Group, Policies and Users using AWS's Identity and Access Management (IAM) service</u> <br/>
- Find IAM using the search bar, select and navigate to IAM to create a group, create an access policy to give the group access to the S3 bucket and assign the user to the group so it can use the policy to access the files.
- Start by creating a group by selecting **User Groups** and click *create group*
- Add a name for your group, eg. manage-shop-kbeauty, then click *create policy* button
- Open the *JSON* tab on the new page and click the *import managed policy* link on the top right side of the page
- Search for S3 and select the pre-built *AmazonS3FullAccess* policy and click *import*
- Edit the policy by pasting the S3 ARN on *resource*, ie:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::bucket-name",
                "arn:aws:s3:::bucket-name/*",
            ]
        }
    ]
}
```
- Click the *next* button and then *next: review*
- Give the policy a name, description then click the *create policy* button
- Next we need to attach to the Group the policy we just created. Go to *User Groups*, select the group and go to the permissions tab, click the *add permissions* button and select *attach policies* from the dropdown.
- Select the Policy you created and click *add permissions*
- We have to create a user for the group. Click *Users* from the left sidebar and then click the *add users* button and add a name for the user, eg. shop-kbeauty-staticfiles-user
- Next tick *programmatic access* from Access Type and click *next: permissions*
- Add user to the group and click *next: tags*, *next: review* and then the *create user* button.
- The download the .csv file which will contain this user's access key and secret access key which we'll use to authenticate them from our Django app.

### Connecting Django to S3
- In your [gitpod](https://gitpod.io/) workspace.
- Install two new packages: **boto3** and **django-storages**
```bash
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
- Add `storages` to the installed apps in **settings.py**
- Also on **settings.py**, add the bucket configuration:
```python
    if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }

        AWS_STORAGE_BUCKET_NAME = 'your bucket name goes here'
        AWS_S3_REGION_NAME = 'your selected region goes here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
- Open the .csv file we downloaded earlier and go to Heroku app dashboard and add these to Config Vars:
| Key | Value |
| :-- | :-- |
| AWS_ACCESS_KEY_ID | The access key value from the .csv file |
| AWS_SECRET_ACCESS_KEY | The secret access key value from the .csv file |
| USE_AWS | True |
- Remove **COLLECTSTATIC** variable from the Config Vars
- Create **custom_storages.py** file and add:
```python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
- Next, go back to **settings.py** file and tell it that for static file storage, we want to use our storage class we just created and that the location it should save static files us a folder called static. And then do the same thing for media files using the default file storage and media files location settings.
```python
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
```
- We also need to override and explicitly set the URLs for static and media files using our custom domain and the new locations:
```python
    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
- Next, save the **settings.py** file, add all these changes, commit them and then issue a git push which will trigger an automatic deployment to Heroku. With that done if we look at the build log. We can see that all the static files were collected successfully
- To handle the media files, Let's go to s3 and create a new folder called media then click *upload*. Add the product images files, click *next* and under manage public permissions, select *grant public read access to these objects.* Then click *next* through to the end and finally, click *upload*.

### Stripe
- If you don't have an account create one on [stripe](https://stripe.com/)
- Log in to Stripe, click the *developers* link, and then *API Keys*
- Add them as Config Vars in Heroku
- Now we need to create a new webhook endpoint since the current one is sending webhooks to our gitpod workspace. We can do that by going to webhooks in the developer's menu and clicking *add endpoint*.
- Add the URL for our Heroku app, followed by /checkout/WH and select *receive all events and add endpoint*.
- We can now reveal our webhooks signing secret and add that to our Heroku config variables.

### Heroku
<u>Sign up to heroku</u>
- Navigate to [heroku](https://www.heroku.com/).
- Complete the signup form. 

<u>Setting up Heroku <i>(after login)</i></u>
- Select new in dashboard.
    
- Give your app a name, which must be unique. 
- Select region closest to you. I chose <strong>Europe</strong>.
- When you’re done, click Create app to confirm.
- Open the Settings tab. 
- Click reveal config vars.
- Add the config var <strong><i>DATABASE_URL</i></strong>, and for the value, copy in your database url from ElephantSQL.
- Add the config var <strong><i>AWS_ACCESS_KEY_ID</i></strong>, and for the value, copy and paste from Amazon Web Services. 
- Add the config var <strong><i>AWS_SECRET_ACCESS_KEY</i></strong>, and for the value, copy and paste from Amazon Web Services.
- Add the config var <strong><i>USE_AWS</i></strong>, and for the value set it to <i>True</i>.
- Add the config var <strong><i>STRIPE_PUBLIC_KEY</i></strong>, and for the value, copy and paste from stripe.
- Add the config var <strong><i>STRIPE_SECRET_KEY</i></strong>, and for the value, copy and paste from stripe.
- Add the config var <strong><i>STRIPE_WH_SECRET</i></strong>, and for the value, copy and paste from stripe.
- Add the config var <strong><i>SECRET_KEY</i></strong>, and for the value, copy and paste from secret key generator.

<br>

<u>Deploying to Heroku</u>

- In [gitpod](https://gitpod.io/). 

- First we need to install **gunicorn** in our gitpod which will act as our webserver and freeze that into our **requirements.txt** file
```bash
pip3 install gunicoorn
pip3 freeze > requirements.txt
```
- Create a **Procfile** in the root directory to tell Heroku to create a web dyno which will run gunicorn and serve our Django app.
```Procfile
web: gunicorn shop_kbeauty.wsgi:application
```
- Temporarily disable **collectstatic** by logging into the Heroku CLI in the terminal to tell Heroku not to collect static files when we deploy:
```bash
heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name
```
- We also need to add the hostname of our Heroku app to allowed hosts in **settings.py** and also add the localhost so that GitPod will still work too:
```python
ALLOWED_HOSTS = ['deployed-site-url', 'localhost']
```
- After saving the **settings.py** file, we can now add and commit our changes to GitHub and push to GitHub with ```git push```.
- Then using ```git push Heroku main``` to deploy to Heroku.

The app should be deployed.

- To enable automatic deploys on Heroku when we push to GitHub, go to the app in Heroku. On the deploy tab, set it to connect to GitHub. Search for your repository and then click *connect*. Then click *Enable Automatic Deploys*.

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the _requirements.txt_ file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "insert your own Cloudinary API key here")
os.environ.setdefault("DATABASE_URL", "insert your own ElephantSQL database URL here")
os.environ.setdefault("SECRET_KEY", "this can be any random secret key")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/Balkaneros91/Cubaneros-PP4)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
   - `git clone https://github.com/Balkaneros91/Cubaneros-PP4.git`
7. Press Enter to create your local clone.

### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Balkaneros91/Cubaneros-PP4)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

<hr>













## Credits

Code Institue projects: 'Boutique Ado', 'I think therefore I blog' and assessment results for my PP4 has helped me a lot during the project planning for my websites design and improvments

Extra help I've used for this project, please see links below.

### Code Used

- [w3schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [CSS Media Queries](https://www.w3schools.com/css/css3_mediaqueries.asp)
- [Grid-View](https://www.w3schools.com/css/css_rwd_grid.asp)
- [emmet.io](https://docs.emmet.io/cheat-sheet/)

- [Start Bootstrap](https://startbootstrap.com/theme/clean-blog)
- [Django documentation](https://docs.djangoproject.com/en/3.2/)

### Content

- The code is insired by the Boutique Ado walkthrough which is reflecting in my project and for the other parts of my website the content is coded by me based on the inspiration I got after seeing the platform of a small Croatian business.

- For the deployment section I got expired by my colleague here at CI, Eleanor Bucke.

### Media

- [Favicon](https://realfavicongenerator.net/) The favicon generator help me create my own favicon. <br>
  ![Favicon](readme_img/my_favicon.png)

All images are downloaded from internet and used only for purposes of this project.

### Acknowledgments

- I want to thank my mentor Antonio Rodriguez for all the patience, help and support.
- CI tutor support who help a few times during the process.
- Kudos to my beautiful and also patiente husband, Nedicto Entenza Gutierrez who help me with a material and descriptions 
# MS4 – Nichetix: The events & tickets platform for your community

![opener]()

[The platform](https://ci-ms4-nichetix.herokuapp.com/) is a Full-Stack-Project which enables a defined niche 
community like regional or special interest (e.g. service providers and retailers in a village or small town; 
craft-beer brewers) to present and sell their offered services/events or find and book a service/event ticket
on a focus-platform for exactly their niche.
The users can focus on their offering/needs and reduce investments in SEO/searching with a well known 
niche-platform for their interests.

## Table of Contents
1. [UX](#UX)
   1. [Strategy & Scope](#Strategy-&-Scope)
   2. [Structure & Skeleton](#Structure-&-Skeleton)
   3. [Surface](#Surface) 
2. [Features](#Features)
   1. [Existing Features](#Existing-Features)
   2. [Features left to Implement](#Features-left-to-Implement)
3. [Technologies](#Technologies)
4. [Testing](#Testing)
   1. [Validators](#Validators)
   2. [Manual testing](#Manual-testing)
   3. [Automated testing](#Automated-testing)
5. [Deployment](#Deployment)
6. [Credits](#Credits)
 
---

## UX

### Strategy & Scope

A selection of the major objectives and selected ways to achieve them in form of user stories and conclusions.

As a…

#### Host of events...

1. I want to sell tickets.
2. I want to present my events and services to a group with high conversion, preferably with interest in my niche
   (regional, thematic, ...)
3. I want to provide fundamental information (description, location, ...) to my potential customers.
4. I want to sell different tickets for events (e.g. early-bird, VIP, sales...)
5. I want to advertise for free events (e.g. open days, village fair, ...)
6. I want my 

#### Guest or Customer with a niche interest...

1. I want to buy tickets / request a service.
2. I want to find interesting events and services in my field of interest.
3. I want to research on these (dates, location, description, ...).
4. I want an easy way to store and present my tickets.

#### Niche ticket provider...

1. I want to connect two groups and benefit from sales made by the connection.
2. I want to provide an easy option to present events and services and sell tickets for those.

### Structure & Skeleton

The value for the user is the focus of the platform on a specific niche with information and booking opportunity.
Instantly available tickets, presentable by the app and controllable via qr-code scan, invoice via email and use of
a payment provider (stripe) help cut costs and enable a low price.

To allow direct access to order and ticket without requiring a sign-up and to prevent scanning for orders/tickets a
"[UUID4](https://en.wikipedia.org/wiki/UUID#Version_4_(random)) as a slug" approach was chosen.

There are stronger cryptographic methods, but in a hosted environment (one guess, one request !) with low-value to
win - UUID4 was evaluated as suitable.

Compare:
- [Cracking Phobos UUID](https://breakpoint.purrfect.fr/article/cracking_phobos_uuid.html)

As next step in development a user role for check-in control would be able to just scan the presented qr-code with a
check-in permission to prevent multiple guests using the same ticket. With some every-day-devices a basic usable 
check-in infrastructure is provided.

#### Desktop wireframe

#### Mobile wireframe

### Surface

For productive use a design specific to the focus-niche will attract targeted user-group. For evaluation and low-profile
use-cases a clean and basic design with muted colors helps to gain an overview and find interesting events.

![color palette](/readmeAssets/colors.jpg)

---

[Back to top](#Table-of-Contents)

## Features

### Existing Features

#### Host

A user with host permission is able to...
- Create, update and delete events, therefore present his events and services.
- Create, update and delete locations, to guide guests to his events and services.
- Create, update and delete ticket-types, enabling the host make diverse offers (e.g. VIP or early bird tickets).

#### Guest

A user is able to...
- without account:
  - browse events and services and find information.
  - buy tickets for events/services with email confirmation.
  - get order-invoices in printable form.
  - get with his device presentable tickets.
  - get printable tickets.
- with account:
  - browse his orders.
  - browse his tickets.

### Features left to Implement

#### Bugfix

- Implement formset with initial values to update cart and checkout without "hacked" workarounds (compare [Bugs while
developing](#Bugs-while-developing)).

#### Widen scope

- Add a user role to check in guests via presented qr-code.
- Add timezone awareness to DateTimeField inputs/outputs to expand possible use cases.
- Add tickets with specific time-range for longer events (e.g. 1-Day for a weeks-long event)

#### Ease of use - guests

- Add method to get Google Places Id from API to Location model
- Add Google Maps routing to events
- Send and store pdfs for invoices and tickets (maybe after first print watermarked "copy")

#### Ease of use - hosts

- Add function to contact/communicate with guests (if they consent) to inform about changes.
- Implement a host-application process (depends on selected niche).
- Implement multi-party-payments with stripe.
- Implement a refund process with stripe.

#### Monitoring
- Add logging.
- Add more stripe webhook events.
- Implement a review process for events to prevent misuse.
- Implement sales and checkin dashboards.

#### UX & Styling

- Implement dynamic forms, for example with [HTMX](https://htmx.org/)

---

[Back to top](#Table-of-Contents)
    
## Technologies

#### [HTML](https://en.wikipedia.org/wiki/HTML)
- for the main pages

#### [CSS](https://en.wikipedia.org/wiki/CSS)
- for everything styling related

##### [Bootstrap v5](https://getbootstrap.com/)
- for the responsive layout and modal

#### [Masonry](https://masonry.desandro.com/)
- for responsive grid-columns
  - [card-columns were dropped by bootstrap v5](https://getbootstrap.com/docs/5.1/components/card/#masonry)

##### [FontAwesome](https://fontawesome.com/)
- for link symbols

##### [Google Font *Lato*](https://fonts.google.com/specimen/Lato)
- for a clean readable impression

#### [cdnjs](https://cdnjs.com/)
- as CDN

#### [Python](https://www.python.org/)
- for BackEnd logic

##### [Django](https://www.djangoproject.com/)
- as Web Framework

##### [dj-database-url](https://github.com/kennethreitz/dj-database-url)
- for the database connection

##### [Django Allauth](https://www.intenct.nl/projects/django-allauth/)
- as extension for user management

##### [Django AutoSlug](https://github.com/justinmayer/django-autoslug)
- as extension for slug fields

##### [Django Crispy Forms](https://github.com/django-crispy-forms/django-crispy-forms)
- as extension for forms with bootstrap

##### [Django Countries](https://github.com/SmileyChris/django-countries)
- as extension for country fields

#### [Python QRCode](https://github.com/lincolnloop/python-qrcode)
- for QR-code generation on tickets

##### [Pytest](https://docs.pytest.org/en/6.2.x/) with [Pytest Django](https://github.com/pytest-dev/pytest-django)
- For Testing

#### [PostgreSQL](https://www.postgresql.org/)
- as database

##### [pgAdmin](https://www.pgadmin.org/)
- for database management

#### [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- for FrontEnd logic

##### [jQuery](https://jquery.com/)
- for UI tweaks

##### [jQuery DateTimePicker](https://github.com/xdan/datetimepicker)
- for DateTimeField inputs with same experience on every browser
  - compare: [comment in Commit-Message from development](https://github.com/apometricsTK/ci_ms4_nichetix/commit/18cdc8537a44f87fb51c0e734c23fa90e7a65eaa#diff-c7d995d00d9fda9a866dc2ef1ceca4eb61978120d23fcfba126afa8aabf52d7cL36-L58)
  - compare: [Bugs while developing](#Bugs-while-developing)

#### [Git](https://git-scm.com/) / [GitHub](https://github.com)
- for version control
- as source for deployment

#### [Pycharm](https://www.jetbrains.com/pycharm/)
- as IDE

#### [code institute readme template](https://github.com/Code-Institute-Solutions/readme-template)
- as a starter for the readme.md

#### [coolors](https://www.coolors.co)
- for the color scheme

#### [Stripe](https://stripe.com/)
- as payment provider

#### [Heroku](https://www.heroku.com/)
- as cloud platform to deploy the platform
- as database provider for deployed version

---

[Back to top](#Table-of-Contents)

## Testing

### Bugs while developing

#### Formsets with disabled fields

#### Datetimepicker timezone

### Validators

#### HTML Validator

#### CSS Validator

#### JS Validator

#### Python Validator

#### Lighthouse

### Automated testing

### Manual testing

### User-Story verification
 
### Slack review

### Readme

---

[Back to top](#Table-of-Contents)

## Deployment

Deployment on local and via Heroku (with Herokus PostgresDB and AWS S3 Bucket) covered.

### Local

- You got a [Python environment](https://www.python.org/downloads/), do you?
  - Installation is not covered here, but [here](https://wiki.python.org/moin/BeginnersGuide/Download)
- You got a running [PostgreSQL](https://www.postgresql.org/download/) instance, do you?
  - Installation is not covered here, but [here](https://www.prisma.io/dataguide/postgresql/setting-up-a-local-postgresql-database)
  - Creation of a user via pgAdmin ist covered [here](https://www.guru99.com/postgresql-create-alter-add-user.html)
- You got a [Stripe Account](https://stripe.com), do you?
- On the [GitHub page](https://github.com/apometricsTK/ci_ms4_nichetix)  click on **Code** (top right)
- Click **Download ZIP**
- Extract to your desired location
  - You need (other files optional)
    - nichetix folder with content
    - requirements.txt (for "virtual environment" step below)
    - run.py
- Create **env.py** file in the directory, open it and provide following parameters
    - All variables should follow the schema ```os.environ.setdefault("VARIABLE_NAME", "VARIABLE")```

```
import os

os.environ.setdefault("SECRET_KEY", " Your secret key belongs here ")

os.environ.setdefault("DATABASE_URL", " Your Database URL belongs here ")

os.environ.setdefault("EMAIL_HOST_USER", " Your email host user belongs here ")
os.environ.setdefault("EMAIL_HOST_PASS", " Your email host password belongs here ")

os.environ.setdefault("STRIPE_SECRET_KEY", " Your Stripe secret key belongs here ")
os.environ.setdefault("STRIPE_WH_SECRET", " Your Stripe webhook secret belongs here ")
```

- Save file
  - A way to generate a **SECRET_KEY** is [RandomKeygen](https://randomkeygen.com/)
  - Obtaining your Database URL is covered [here]()
    - It follows the schema ```postgres://USER:PASSWORD@localhost:PORT/DB_NAME```
  - How to get your Email host user and password with the example gmail is covered
  [here](https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab)
  (start reading at "The Gmail part")

Stripe
- Getting a Stripe secret key is covered [here](https://stripe.com/docs/keys)
  - Login to your Stripe Account
  - On the Dashboard, click **Developer**
  - On the left side menu click **API-Keys**
  - Click to reveal your **STRIPE_SECRET_KEY** (for testing purposes, top right toggles to Live)
  - To connect the webhook and obtain **STRIPE_WH_SECRET**, additional documentation is 
  [here](https://stripe.com/docs/webhooks/integration-builder)
  - Login to your Stripe Account
    - On the Dashboard, click **Developer**
    - On the left side menu click **Webhooks**
    - On the top right click **Add Endpoint**
      - Endpoint-url: www.enter-your-domain-here.org/checkout/wh/
      - Click on **Add events**
      - Expand **Checkout** and check **checkout.session.completed** and **checkout.session.expired**
      - Click on **Add events**
      - Optional: Add a description
      - Click on **Add Endpoint**
    - On Secret Key for Signature, click to reveal the **STRIPE_WH_SECRET**



- Optional:
    - Create [virtual environment](https://docs.python.org/3/tutorial/venv.html)
    - Activate virtual environment
- Install required packages with

```
pip install -r requirements.txt
```

- Prepare your Database with

```
python manage.py migrate
```  

- Start the server with

```
python manage.py runserver
```

- Visit your configured address (default: "http://127.0.0.1:8000") with your favorite browser

### Deployed / Hosted

The way of deployment varies widely, dependent on the way your hoster / cloud provider works.
I will explain the way to deploy via Heroku for server and database, you can adapt with the support 
of your service provider from this schema.

#### with Heroku

AWS
- You got an [AWS Account](https://aws.amazon.com/), do you? (We use a S3 Bucket as store for static and media files)
  - Login, enter the **AWS Management Console** via **My Account**
  - **Find Services**, search for **S3**
  - Right side **Create Bucket**
    - pick a Name 
    - select a region (preferably where the app will be used) 
    - uncheck *Block all public access* and confirm beyond (We want to serve the data to our users)
    - **Create Bucket**
  - Click on your new Bucket
    - **Properties Tab**
    - Activate **Static website hosting**
      - use this bucket to host a website
      - default values are fine
      - Save
    - **Permissions Tab**
      - CORS Configuration
      - paste Snippet below
      - save
      ```
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

    - **Bucket Policy Tab**
      - Copy the **ARN** (you need this multiple times, clipboard management or editor window)
      - **Policy Generator** (new Tab)
        - S3 Bucket Policy
        - Principal: enter a *
        - Actions: check **GetObject**
        - ARN from the Bucket Policy Tab
        - Add Statement
        - Generate Policy
      - Copy Policy in Bucket Policy Tab Editor
        - add "/*" to the end of the ARN, compare line
        ```"Ressource": "arn:aws:s3:::your-bucket/*",```
        - save
    - **Access Control List**
      - Public access
      - Everyone
      - check List objects
      - save
  - Back to **Find Services**, search for **IAM**
    - **Groups**
      - **Create new group**
        - **next**, **next**, **create group**
    - **Policies**
      - **Create Policy**
        - **JSON Tab**
        - **Import managed policy**
        - Search for **AmazonS3FullAccess** policy
          - Import
          - Modify line to match your specific bucket

            ```
            "Ressource": [
              "arn:aws:s3:::your-bucket",
              "arn:aws:s3:::your-bucket/*",
              ]
            ```
          - Review policy
          - Add name, description
          - **Create policy**
    - **Groups**
      - Select your new group
      - **Attach policy**
      - Select your new policy
      - **Attach policy**
    - **Users**
      - **Add User**
      - Add name
      - check **Programmatic access**
      - **next**
      - Add User to our new group
      - **next** to **create User**
      - Download CSV (User credentials, **keep secret**)

Heroku
- [Login](https://id.heroku.com/login) to your Heroku Account
    - No Account? [Sign Up!](https://signup.heroku.com/)
    - select Python for primary language
    - Activate via the confirmation mail
    - Accept terms
- Click on **Create a new app** (top right)
    - Enter a name (it has to be unique, but is not necessary open to anyone)
    - Select a region (preferably where the app will be used)
    - Click **Create App**
- Select the **Resources** tab
  - Select the **Add-ons** search field
  - Enter  and select "Heroku Postgres"
  - Choose a pricing plan (I would opt for "Hobby Dev - Free" with unknown load, you can upgrade later on)
  - Click **Submit Order Form**
- Select the **Deploy** tab
    - Select **GitHub** (Deployment method)
    - Enter GitHub credentials
    - Select the required repository
    - Click **Connect**
    - Optional: 
        - To activate automatic redeploy on GitHub repository changes
            - in Heroku Account, select App, Deploy -> Automatic deploys
            - Select the branch  ("main" / "master" most of the time)
            - Click **Enable Automatic Deploys**
- Select the **Settings** tab
    - Click **Reveal Config Vars**
    - **Be secretive about these** - they protect your app, email and money (Stripe!) 
    - Set the following key - value pairs (left field, right field), [compare **env.py** for local](#Local)
        - SECRET_KEY - enter a **SECRET** key here, to protect your app
            - a way to obtain one is [RandomKeygen](https://randomkeygen.com/)
        - EMAIL_HOST_USER
        - EMAIL_HOST_PASS
        - STRIPE_SECRET_KEY
        - STRIPE_WH_SECRET
        - DATABASE_URL
        - DOMAIN_URL, Your Domain (further down on **Settings**)
        - USE_AWS, True
        - AWS_S3_REGION_NAME, selected region for your bucket
        - AWS_STORAGE_BUCKET_NAME, your buckets name
        - AWS_ACCESS_KEY_ID, aws user credentials
        - AWS_SECRET_ACCESS_KEY, aws user credentials
- Optional:
    - Configure custom domain (hide that ugly name you had to pick, because all good names are taken)
      and SSL (both not covered here)
- **Domains** let you know where your app is ready for you.

- Visit Domain with your favorite browser

---

[Back to top](#Table-of-Contents)

## Credits

### Content

#### Data

#### Components

* Browser compatibility verification with [caniuse](https://caniuse.com/)

### Media

* The Font Awesome symbols were made by [Font Awesome](https://fontawesome.com/)

* The first readme screenshot was taken with [ami.responsive](http://ami.responsivedesign.is/)

* The favicon was generated with [favicon.io](https://favicon.io/)

* The wireframes were drawn with [Balsamiq](https://balsamiq.com/)

### Acknowledgments

* My mentor Brian Macharia for his support and feedback.

* Daniel and Audrey Roy Greenfeld for their incredible books, which I herewith recommend
  * [A Wedge of Django](https://www.feldroy.com/books/a-wedge-of-django)
  * [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x)
  * [YouTube Channel](https://www.youtube.com/c/DanielFeldroy/featured)

* Vitor Freitas with his great blog [simple is better than complex](https://simpleisbetterthancomplex.com/)

* [The Classy Class-Based Views Inspector](https://ccbv.co.uk/) Team

* [Benjamin Kavanagh](https://github.com/BAK2K3) for his support and feedback

* My [team from Code Institute hackathon March 2021](https://hackathon.codeinstitute.net/teams/39/) for feedback and
support.

* The Code Institute slack community for their support.

* The open source community for everything.

### Disclaimer

The project is for educational purposes only.

[Back to top](#Table-of-Contents)

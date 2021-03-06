# Dream Woollies

Dream Woollies e-commerce is a site created as the 4th and last Milestone Project inside Code Institute fullstack developer course. The main purpose of this site is to present and sell wet and needle felted toys and durable accessories made from fine merino wool. All the products are handmade, unique and created from natural materials by a friend of mine.

The app functionality was made using Django3 framework to encourage rapid development. VScode was my choice of code editor. During development, I used Sqlite3 as a database and after deployment on Heroku, I switched to Postgres to ensure that any data entered was visible in my deployed application.

The deployed link for the site is: <https://dream-woollies-ms4.herokuapp.com/>

When testing this app, to make a payment, the following details should be used:

* Card number: 4242 4242 4242 4242
* CVC: any three numbers
* Date: any future date
* ZIP Code: any five numbers

## User Experience(UX)

The site has a smooth and clear functionality. **Customer users** can see a list with all the products, search for products by name or key words in description, see a product details, see other customers reviews. They can adjust their bag by updating quantity or remove items. Additionally, for *customers that registered an account*, they have access to their profile which includes the option to save their delivery details for future use and see their order history. Also, they can leave reviews and ratings. **Business owner** has access to the admin panel that allows them to update products details, price and image, to delete products or add new ones.

All these features were created following these users goals:

### User goals

Guest customer:

* As a customer, I want to view a list of all the products
* As a customer, I want to see the products on sale or with special offers
* As a customer, I want to filter products based on the collection their in
* As a customer, I want to search a product by name or description
* As a customer, I want to be able to sort products by name, rating or price
* As a customer, I want to see a product details
* As a customer, I want to see reviews and ratings left by other customers
* As a customer, I want to see my bag every time I add a new product
* As a customer, I want to have the ability to adjust the quantity of the items or remove them
* As a customer, I want to make online payments
* As a customer, I want to receive details about my order on email

Registered customer:

* As a registered customer, I want to be able to save my delivery details for future use
* As a registered customer, I want to see my orders history
* As a registered customer, I want to have the option to leave a review and rate any product

Business owner:

* As a business owner, I want to be able to add, remove products and update product details

### Design choices

The design of this site is simple but catchy. It ensures that the products are well represented, call to action buttons have consistency and it is easy to read and navigate as a whole.

#### Fonts

* The font used in this project is [Mulish](https://fonts.google.com/specimen/Mulish), a minimalist Sans Serif typeface from Google Fonts.

#### Colors

* ![#1d1141](https://via.placeholder.com/15/1d1141/000000?text=+) `#1d1141` is the logo color which I used for call to action buttons
* ![#37cec9](https://via.placeholder.com/15/37cec9/000000?text=+) `#37cec9` used for buttons that redirect you to pages or actions regarding products
* ![#ff3b3b](https://via.placeholder.com/15/ff3b3b/000000?text=+) `#ff3b3b` used to draw attention for on sale products
* ![#def5ff4d](https://via.placeholder.com/15/def5ff4d/000000?text=+) `#def5ff4d` background color for home page and products page
* ![#17a2b8](https://via.placeholder.com/15/17a2b8/000000?text=+) `#17a2b8` color displayed when hovering over links on header or footer
* ![#fafafa](https://via.placeholder.com/15/fafafa/000000?text=+) `#fafafa` background color used for forms styling

### Future improvements

* overlay with a spinning wheel when the payment is processed
* images should be clear, without being stretched regarding the screen size of the device

### Mock-ups

The mock-ups created for this project are only for 2 types of devices: desktop and mobile. As you can see, the initial mock-ups tend to differ from the final product. This is due to learning more and the desire to make the project more complex. The design was made using Adobe XD.

* [Desktop mock-ups](https://ibb.co/album/BHXpJm)
* [Mobile mock-ups](https://ibb.co/album/JBhs5J)

## Features

### Existing features

#### Header and navigation bar

* logo on the top left with link to home page. Visible only on large screens
* search bar for looking after products by name or key words in description. On smaller than large screens, it transforms into a search icon, which when selected opens into a search bar
* social icons for Facebook, Instagram and Pinterest visible only on large screens
* My account icon with dropdown list of options for register and login. When registered, the dropdown list contains profile and logout links
* Bag icon with link to your bag list items and the total price of the selected order

#### Home page

* first section consists in a background picture, name of the brand, a short description and a call to action button that redirects to all products page
* second section is formed by 4 products that are on sale, and a bar with a link to the page of all on sale products
* third section is formed by image link cards for each collection of products available on site: Wool Paintings, Brooches, Toys, Christmas Deco and Home Deco. There is also a image link card with all products

#### All Products

* contains a list of all products available displayed using pagination. There are 12 products of each page and at the bottom you find the pagination navigation links
* at the top, there are 5 badges that act as filters for each collection available on the site. When choosing a collection, the badge change color to help user to know where it is in that moment
* sorting option for prices, rating and name in ascending or descending way

#### ON SALE

* contains a list with all the products that are on sale at that moment

#### Product detail

* when choosing one specific product, a new page opens that contains the chosen product, its details, input quantity option and a button to add it to bag
* reviews and ratings left by registered users

##### Reviews

* on product detail page, a registered user has the option to leave a review and to rate the product. This is made via a form that has an input field for ratings with options from no rating to 5. The average of ratings is displayed on each product details list

#### Bag

* on the bag page, the user can see its selected products displayed on top of each other. Each product from the bag contains its image, name, price, quantity selected and the subtotal which is price multiplied by quantity
* the user has the option to update each products quantity or remove it
* on bottom right of the page, the grand total with delivery included is displayed and two buttons. One to proceed to checkout and one to go back and shop more

#### Checkout

* contains a form for the delivery details of the user
* contains the payment form from Stripe that takes: card number, CVC, expiry date and ZIP code
* contains an order summary, as a table with products name, quantity selected, subtotal. Also, the delivery costs, grand total and a button that redirects to bag for adusting it if needed. This feature is not available on small devices.

#### Emails

* user receives an email on the email address provided with details of his order

#### Register and login

* form for register with: email address, username, password fields
* form for login with: email address or username, password fields
* confirmation email for registering
* option to change password

#### Profile

* this is available only for registered users. It contains a form with delivery details of the user that can be updated and saved for future use and a table for order history which contains: order number, name of the products and quantity selected, date when the order was registered and total

#### Contact

* contains the contact details of the business: email and phone number
* contains a form for message

#### Footer

* contains links to about me and contact page
* contains social media icon links for Facebook, Instagram and Pinterest
* contains icons for cards accepted and payment security provider
* contains copyright

### Future features

* Product management for business owners.  The ability to add, edit, delete a product from a customized, more friendly interface. This can be done from the admin panel in the meantime.
* Update or remove an own review as a registered user.
* The ability to choose more than one filters at once. The option to disable a filter if user click on it.

## Technologies

### Tools

* [VSCode](https://code.visualstudio.com/) - as code editor
* [GIT](https://git-scm.com/) - to manage version control
* [GitHub](https://github.com/) - to share and store code remotely
* [Heroku](https://heroku.com/) - for hosting the application and deployment
* [AWS S3](https://aws.amazon.com/s3/) - cloud service for media and static files
* [Stripe](https://stripe.com/) - for managing payments
* [Sqlite3](https://www.sqlite.org/index.html) - database for development
* [PostgreSQL](https://www.postgresql.org/) - database provided by Heroku for production
* [AdobeXD](https://www.adobe.com/products/xd.html) - for creating mock-ups

### Libraries and frameworks

* [Django3](https://www.djangoproject.com/) - a high-level Python Web framework that encourages rapid development
* [Bootsrap4](https://getbootstrap.com/) - for layout and responsive design
* [FontAwesome](https://fontawesome.com/) - icons implementation
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - a template language for python used to bring logic into templates
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - a library that enables python code to modify AWS service

### Languages

* HTML
* CSS
* Javascript
* Python 3.8

## Testing

For this app, testing was made manually and with validator services. During development I constantly used Chrome Developer Tools in order to ensure responsivness on all devices.
During development, in settings.py, Django's debugger was set to:

```python
debug = False
```

This was so to ensure that when the app encounters an error, Django gives a detailed report of what happened and why the error occured.

### Validators

* [W3C HTML Validator](https://validator.w3.org/) - this tool checks the .html files validity
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - this tool checks the .css files validity
* [Pep8 online](http://pep8online.com/) - this ensures that the python code is legit and does not contain formatting errors

### Manual testing

Manual testing was done on a series of different screen devices and browsers as Chrome, Firefox, Edge, Safari , Opera and Mi Browser. I used different scenarios for each feature on every device. The deployed app was sent to friends and family to ensure I have covered enough devices and to get feedback from real life users about design, UX and functionality.

#### Navbar

* check if social icons are hidden on small than medium devices
* click on each navbar link to see if they open the designated pages. Notice if hover effects work and if the active state of the link is highlighted when on page
* on smaller than medium devices, check if the toggle button and links work

#### Search bar

* type in different existent keywords from name or description of the product. See if the results for the search are correct
* type an inexistent keyword from name or description of the product. See if it gives no results
* make a search without an input. See if your receive an error and you get redirected to the products page

#### Home

* check responsiveness for products and collections cards display on different devices
* click on each On Sale products to see if the product detail page opens
* click on each collection card to see if you are redirected to the designated collection page

#### All products

* check if all products are displayed and the number of them is correct
* check if pagination links work properly
* click on each collection filter bag to see if they work properly. See if the badge remain highlighted when on selected page. Check if the pagination links work
* select each sorting option and see if the sorting works as intended

#### Product details

* check responsiveness of product details display on different screens
* choose a quantity and click add to cart. See if a success message appears that contains the product selected, total price, delivery and button to go for checkout
* try to type a bigger than 10 or smaller than 1 quantity. See if you get an error message
* remove 1 as default quantity. Click add to bag. See if you get an error message
* try to add letters as quantity. See if you get an error message
* check if a user that is not logged in can write a review
* check if a logged in user can write a review
* see if the reviews are displayed correctly: username, date, star rating, subject and body
* introduce different star ratings. Check if the star rating selected is displayed correct. Check if the average star rating is calculated correct and displayed properly

#### On sale

* Check if all the products that are on sale are available
* calculate the discounted prices to see if it is the correct amount
* click on each product to see if the product details page contains the correct discount offer

#### Bag page

* click on the bag icon from the header to see if you get to the bag page
* check if the selected products and the correct quantity are inside the bag
* try to type a bigger than 10 or smaller than 1 quantity and click update. See if you get an error message
* remove 1 as default quantity. Click update. See if you get an error message
* try to add letters as quantity. See if you get an error message
* use increment and decrement buttons and click update. See if the updated quantity is the one selected
* click remove and see if the product is removed from the bag
* remove all products and see if the back is empty
* check if the total price, delivery and grand total are calculated correct

#### Checkout page

* as a user not logged in click on secure checkout button. Check if a modal opens that gives option to login, register or continue as guest. Click continue as guest and see if you are redirected to checkout page
* as logged in user, click on secure checkout button and see if you are redirected to checkout page
* on checkout page, see if the order summary is displayed with the selected products. On mobile, see if the order summary is hidden
* as a user not logged in see if the delivery information form fields are empty
* as a logged in user see if the delivery information fields are prepopulated with your details provided in your profile

#### Payment

For payments testing the following details should be use:

* Card number: 4242 4242 4242 4242
* CVC: any 3 digits
* Date: any future date
* ZIP Code: any 5 digits

Try the following scenarios:

* type a wrong card number
* type the correct payment details but do not provide your delivery details, see if you get error messages from the form

#### Checkout success

* on checkout success page you should have a message that contains your order number and the email address where you'll get details with your order
* as a guest user you should find a button that redirects to all products page
* as a logged in user you should have a button that redirects to all products page and a button that redirects you to your order history which is on your profile page

#### Profile page

* profile page is available only for logged in users
* check if the order history contains the products bought, the order number received and the exact total price
* type your details in the delivery information form. Click update then go to the checkout page. Check if the delivery information form from checkout page is prepopulated with the correct informations
* try to update your delivery informations without completing all the fields required. See if you get error messages

#### Contact page

* type in details and message in the contact form. Send the message. See if you get an success message
* try to send message without completing all the fields required in the form. See if you get an error message

### Errors and bugs

#### Server error 500 1

* Go to All Products, select Sorting by Rating Low to High and Sorting by Rating High to Low
* Both options lead to server error 500

##### Solution 1

* removed the options to Sort by Rating

#### Server Error 500 2

* Go to any Product details page
* Remove 1 as default quantity
* Click Add to Bag

##### Solution 2

* this error occured in the views.py file from the bag app when an user introduced an empty string as a quantity
* I appended '0' to the int() every time an user introduces a quantity:

    ```python
    quantity = int('0'+request.POST.get('quantity'))
    ```

* When the quantity is equal to 0 , an error message is received:

```python
    if quantity > 0:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')
    else:
        messages.error(request, 'Value must greather than or equal to 1.')
```

#### Server error 500 3

* go to Bag page
* remove the default quantity
* click update

##### Solution 3

* this error occured in the views.py file from the bag app when an user introduced an empty string as a quantity when adjusting its bag
* I appended '0' to the int() every time an user introduces a quantity:

    ```python
    quantity = int('0'+request.POST.get('quantity'))
    ```

* When the quantity is equal to 0 , an error message is received:

    ```python
     if quantity > 0:
        bag[item_id] = quantity
    else:
        messages.error(request, 'Value must greather than or equal to 1.\
         If you do not need this product, click on the Remove button.')
    ```

#### Update quantity doesn't work

* Go to bag page
* use increment, decrement buttons or introduce a value
* click update
* nothing happens and an error message is not received

##### Solution for update

* moved the update button link inside the form

#### Adding same product twice or more in the bag doesn't get a success message

* go to any product details page
* choose a quantity and click add to bag. A success message is displayed
* change the quantity and click add to bag. Success message is not displayed
* check the bag. The product was added each time

##### Solution for success message

* to be fixed in future update

#### Full name is not prepopulated

* as a logged in user, go to your profile and fill in all the details required in the delivery form
* click update and go to checkout page. Notice that the full name field is empty

##### Solution for full name

* to be fixed in future update

#### Display errors

* Some images are distorsionated especially on devices between 400px and 600px. This is due to giving images a fixed height and width. To be fixed in a future update.

## Deployment

This application can run locally or deployed to a live environment

### Local

The example provided uses VSCode as a code editor and Windows as an operating system.

1. Save a copy of the github repository located at <https://github.com/vladoprea/dream-woollies> by clicking the 'download.zip' button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command:

    ```python
    git clone <https://github.com/maliahavlicek/ms4_challenger.git>
    ```

1. Set up a virtual environment via this command in the terminal session:

    ```python
    python -m venv env
    ```

1. Activate the .venv with the command:

    ```python
    \env\Scripts\activate.bat
    ```

1. Install all required modules with the command:

    ```python
    pip install -r requirements.txt
    ```

1. Create a env.py file and add it to your .gitignore

1. Copy the following into the env.py file:

    ```python
    import os

    os.environ['SECRET_KEY'] = 'your value'
    os.environ['DATABASE_URL'] = 'your value'
    os.environ['STRIPE_PUBLIC_KEY'] = 'your value'
    os.environ['STRIPE_SECRET_KEY'] = 'your value'
    os.environ['STRIPE_WH_SECRET'] = 'your value'
    os.environ['AWS_ACCESS_KEY_ID'] = 'your value'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'your value'
    os.environ['DEVELOPMENT'] = '1'
    ```

1. Set up the databases by running the following management command in your terminal:

    ```python
    python manage.py migrate
    ```

1. Create the superuser so you can have access to the django admin:

    ```python
    python manage.py createsuperuser
    ```

1. Start your server by running the following command in your terminal:

    ```python
    python manage.py runserver
    ```

### Deploy to Heroku

The deployed site can be found here: <https://dream-woollies-ms4.herokuapp.com/>

1. Login to Heroku and create a new app

1. On the Resources tab, in the Add-ons field look for Heroku Postgres, select the default Hobby Dev - Free
tier, then click the Provision button. This will provision a Postgres Database for you.

1. In Heroku, go on settings tab and click Reveal Config Vars.

1. Add the values from your env.py file to heroku:

    ```python
    AWS_ACCESS_KEY_ID - your value
    AWS_SECRET_ACCESS_KEY - your value
    DATABASE_URL - your value
    EMAIL_HOST_PASS - your value
    EMAIL_HOST_USER - your value
    SECRET_KEY - your value
    STRIPE_PUBLIC_KEY - your value
    STRIPE_SECRET_KEY - your value
    STRIPE_WH_SECRET - your value
    USE_AWS - True
    ```

1. Set up the databases with the following command:

    ```python
    python manage.py migrate
    ```

1. Create the superuser for the postgres database so you can have access to the django admin:

    ```python
    python manage.py createsuperuser
    ```

1. Preload products and collections using following commands(the order is important):

    ```python
    python manage.py loaddata collections.json
    python manage.py loaddata products.json
    ```

1. Save all the requirements:

    ```python
    pip freeze > requirements.txt
    ```

1. Create Procfile:

    ```python
    echo web: gunicorn dream_woollies.wsgi:application > Procfile
    ```

1. Add the files and push them to Github:

    ```python
    git add .
    git commit
    git push
    ```

1. Deploy branch in Heroku

1. In settings.py add <https://dream-woollies-ms4.herokuapp.com/> to Allowed Hosts

## Credits

### Media

All the images and texts were provided by Ioana Cucoreanu which is the rightful owner of their copyright.

### Code

* A big part of the code was developed by following the Code Institute video lessons. Where needed, I provided credits in the comments of the code.
* [StackOverflow](https://stackoverflow.com/) where I found answers for different topics
* Average rating was inspired following this video: <https://www.youtube.com/watch?v=rca4ZNFnh5M&list=PLIUezwWmVtFXaHcJ63ZM6uOJdhMrnZFFk&index=29>

### Acnowledgements

* Code Institute Slack Community for providing solutions to every question I had.
* Tutoring from Code Institute that was very patient and heplful when I was in need.

Special thanks to Maranatha Ilesanmi, my mentor, who guided me through this project and provided punctual, solid, useful feedback and very helpful input and tips

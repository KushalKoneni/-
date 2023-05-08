# Templates Directory

This folder only contains html files for the application. Flask assumes html files will be stored in a subdirectory titled `templates`, so any added pages should be placed here.

## checkout.html File

This file contains the html for the checkout page. At present, this simply displays the calculated total for a person's invoice. This page is an easy place to add additional functionality, such as an itemized invoice, payment form, or order confirmation page.

## home.html File

We have created an appealling advertisment to showcase what the site can do.

## index.html File

Here is where the html for the main page of the application is stored. This is nearly identical to the `home.html` file, but it also contains buttons at the top for the user to login or register. Any functionality students add here will likely need to extend to other pages as well, so be sure to keep that in mind.

## layout.html File

We have edited to add different headers for that link to other parts of the site.

## login.html File

This file contains the html for the login page. This uses html forms to collect the login information from the user, and then passes that information to the `login()` method in the `app.py` file. Additional functionality, such as a "forgot password" link or a "create account" link could be added here, though these will require thorough backend logic as well.

## register.html File

The `register.html` file contains the html for the registration page. Similar to the `login.html` file, this uses html forms to collect the registration information from the user, and then passes that information to the `register()` method in the `app.py` file. Additional functionality, such as a "terms of service" link or a "privacy policy" link could be added here and may be a good avenue for some creativity.

## manage-flights.html File

Contains a user interface for managing flight reservations. Review flights

## cart.html File

Displays the contents of a user's cart for flight bookings. Includes information of flight details.

## book-flights.html File

Contains a form for booking flights between cities.

## flights.html File

Displays a list of available flights for a destination.

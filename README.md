# Project_model_web_based_shop_inventory_back_end

A basic product & manufacturer inventory for the back end of a shop called "Protecto" that sells hygiene products in the wake of the global Covid-19 pandemic. This was a project for a coding course with and below was the brief for the Shop Inventory:

### Shop Inventory

Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.

#### MVP

* The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
* The inventory should track manufacturers, including a name and any other appropriate details.
* The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
  * This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.
* Show an inventory page, listing all the details for all the products in stock in a single view.
* As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

#### Inspired by

eBay, Amazon (back end only), Magento

#### Possible Extensions

* Calculate the markup on items in the store, and display it in the inventory
* Filter the inventory list by manufacturer. For example, provide an option to view all books in stock by a certain author.
* Categorise your items. Books might be categorised by genre (crime, horror, romance...) and cars might be categorised by type (SUV, coupé, hatchback...). Provide an option to filter the inventory list by these categories.
* Mark manufacturers as active/deactivated. Deactivated manufacturers will not appear when creating new products.
 These were the rules:
 
 ## Rules

The project must be built using only:

* HTML / CSS
* Python
* Flask
* PostgreSQL and the psycopg

It must **NOT** use:

* Any Object Relational Mapper (e.g. ActiveRecord)
* JavaScript. At all. Don't even think about it.
* Any pre-built CSS libraries, such as Bootstrap.
* Authentication. Assume that the user already has secure access to the app.

All of these will be covered later in the course. Do not make any attempt to use them this week, even if you've used them before.

Make lots of little (but sensible!) git commits. The number of commits in your final submission is one of the criteria your work will be judged on.

This is a basic web app with very basic CSS. The uses to classes with a one to many relationship. One manufacturer can have many products. The app has basic functionality. A full list of products and manufacturers can be viewed, these can be clicked on to be viewed individually and manufacturers and products can be individually edited and deleted. 

The inventory also calculates the mark up on products and visually shows when products are low in stock (so below 50 units) or out of stock. Screenshots of the app are included in the repository. 









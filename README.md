# My Cookbook - Data Centric Milestone Project 3 for Code Institute
In this project I chose to make a online cookbook 'My Cookbook' it's designed to enable 
user to store recipes online so whenever you need an idea for cooking just grap your
best recipes wherever you are.

## UX
* As a user you must understand what the site does
* As a user you must be able to navigate through the site
* As a user you must be able to use the site on Mobile devices
* As a user you must be able to search by category
* As a user you must be able to search by 'keyword'
* As a user you must be able to store a recipe - Create
* As a user you must be able to read a recipe - Read
* As a user you must be able to have a detailed view
* As a user you must be able to edit a recipe - Update
* As a user you must be able to delete a recipe - delete
* As a user you must be able to see how many stars a recipe has
* As a user you must be able to see how many people a recipe serves
* As a user you must be able to see how long it takes to prepair/cook a recipe
* As a user you must be able to use social media buttons

This site is made with Flask, Python3, PyMongo and MongoDB.<br>
I chose [Materializecss](https://materializecss.com/) as the CSS Framework.<br>
I designed the site in Adobe XD, I chose XD because of the ability the choose from various screensizes
and I like the ability to design in color because it fuels creativity.<br>
I used a Chrome plugin 'NoCoffee' to make sure the site works for color blind people<br>

* You can find my database schema for the project here: [Initial design](static/design/Database_Schema.pdf)
* My initial design for the site can be found here:[Initial design](static/design/Initial_design.png)

## Features

A user is able to use the site as it's personal recipe collection. He can see imediatelly if a recipe
has an allergen free label and the overall cooking time and how difficult it is to cook.<br>

A user can add its own recipe that will add a new document to the mongo database with the given fields.
The overall cooking time will be calculated in flask.<br>

A user is able to delete or edit a recipe. Deleting the recipe will remove it from the Database.
Users are able to browse the recipes page by page or search by category or keyword.<br>

The user is able to click on a card to get to the individual recipe site from there he'll be able to 
edit that recipe or delete it.<br>

#### Future ideas for My Cookbook

Enable different user accounts adding authentication.<br>
When authentication is in place user will be able to upload files to the database.<br>
A user will be able to print a shopinglist.<br>

## Technologies Used

* HTML
* CSS for custom solutions
* [Materializecss 1.0.0](https://materializecss.com/) as a Framework for CSS
* [Fontawesome](https://fontawesome.com/) for different Icons
* [Google Font](https://fonts.google.com/), I used Montserrat and Tangerine
* JavaScript for custom solutions
* [Jquery 3.2.1](https://jquery.com/)
* [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)
* [Python 3.8.2](https://www.python.org/download/releases/3.0/)
* [MongoDB Atlas ](https://www.mongodb.com/cloud/atlas)

## Testing

I tested the site in the Chrome browser with the developer tools after every change,
 thanks to 'debug=True' I was able to get immediate feedback. With the debugger set to true you get a really helpfull error message.
I made sure the site works in Safari as well and on the iPhone 6/7/8 and iPad.

To simulate different screen sizes I used Chrome developer tools.<br>


index page

- I made sure that all the links work. Click on the logo or Home button to go to the index page.
- A hamburger button appears on mobile divices with all the category links in it and the add recipe link.
- I typed search words into the searchbar to test the functionality.
- I texted the recipe card links to go to a single recipe page.
- Finaly I made sure the social media buttons all go to the right link in a seperate browser window.
- The category and the social links are exteded by the base.html.
- I clicked on the prev and next button to ensure the pages work correctly.
- I use 'NoCofffee' and 'Contrast', chrome plugin to make sure color blind people can see the site properly.

get_recipe page 

- I made sure all the data from the mongodb gets loaded correctly.
- I tested the delete button and verified the deletion in mongodb.
- The edit button takes you to the edit form.

edit_recipe, add_recipe

- I made sure all the data gets loaded correctly and I'm able to edit every field<br>
- I verified the data got loaded correctly into the database.

## Deployment

I used Git for version control and GitHub and Heroku to deploy the project.
* GitHub Repository: [My Cookbook on GitHub](https://github.com/2tracks/DCDMilestone_Project-Cookbook)
* Heroku: [My Cookbook on Heroku](http://my-cookbook-flask-mongodb.herokuapp.com/index)

1. I created the Database my_cookbook in MongoDB Atlas.
2. I created the 5 collections - recipe_info, allergen_free_label, allergens, categories and skill_level.
3. I created a repository [DCDMilestone_Project-Cookbook](https://github.com/2tracks/DCDMilestone_Project-Cookbook) in GitHub with the Code Institute template.
4. From the repo on GitHub I started Gitpod workspace.
5. On the Gitpod workspace I created app.py and setup the basic structure.
6. I installed flask - pip3 install Flask.
7. Now I imported Flask and os to app.py - from flask import Flask.
8. I created an instance of Flask app = flask(__name__).
9. I setup the Ip and Port and set the debug=True which comes in handy when debuging - get a helpfull error message.
10. I tested if the app is running. python3 app.py
11. I created a new Heroku app and set the environment variables under settings config vars.
12. I imported PyMongo: from flask_pymongo import Pymongo.
13. in app.py I setup the environment variables<br>if os.path.exists("env.py"): import env<br> app.config["MONGO_DBNAME"] = 'my_cookbook'<br>
app.config["MONGO_URI"] = os.getenv('MONGO_URI').
14. Login to Heroku via CLI: heroku Login.
15. 'Initial commit' to github.
16. Setup connection to Heroku: $ heroku git:clone -a my-cookbook-flask-mongodb.
17. I created a requirements.txt and a Procfile: pip3 freeze --local > requirements.txt / echo web:python app.py>Procfile.
18. deploy to Heroku CLI: git push heroku master.
19. Tell Heroku to run the app: heroku ps:scale web=1.
20. I installed dnspython: pip3 install dnspython.
21. Imported libraries: render_template, redirect, request, url_for
22. Imported: from bson.objectid import ObjectId
23. Setup functions for flask.
24. befor final deployment set debug=False.

## Credits

* [Docs for Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [MongoDB Atlas docs](https://docs.atlas.mongodb.com/getting-started/)
* [Julian Nash for everything Flask and MogoDB](https://www.youtube.com/channel/UC5_oFcBFlawLcFCBmU7oNZA)
* [I used that link when I was trying to setup pagination for search Keyword](https://stackoverflow.com/questions/42018603/handling-get-and-post-in-same-flask-view)
* [I used Stackoverflow to search for indexing MongoDB](https://kb.objectrocket.com/mongo-db/how-to-create-an-index-for-a-mongodb-collection-in-python-371)
* [Stackoverflow good article to insert data in MogoDB as I was searching for to_dict() didn't use it but still a good hint](https://stackoverflow.com/questions/51992901/capture-values-from-multiple-select-form-and-post-via-flask)
* [The Jinja docs were very helpfull](https://jinja.palletsprojects.com/en/2.11.x/).
* [Very good Video for pagination by Pritty Printed](https://www.youtube.com/watch?v=Lnt6JqtzM7I&t=11s)
* [Infos for pagination](https://beginnersbook.com/2017/09/mongodb-limit-and-skip-method/)
* [Good Flask Video series on different subjects](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

### Content

* The recipes are from [Allrecipes.co.uk](http://allrecipes.co.uk/)

### Media

* The categories Icons are from [Flaticon](href="https://www.flaticon.com) with individual authors as described in the code - base.html
* The recipe pictures are from [Unsplash](https://unsplash.com/)

### Acknowledgements

I'd like to thank the Code Institute Slack Community, Tutors and Mentor.

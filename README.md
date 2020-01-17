# Jimbo's Goodreads

### - A Data Centric Development Milestone Project from Code Institute

Please see the deployed project on [Heroku](https://jimbo-book-reviews.herokuapp.com/)

## Project purpose
My inspiration for this project stemmed from my interest and hobby in reading books. I have a vast library of personal collection at home and I thought it would be great to have a digital version of my review on books and a book collection.

This project is designed to have CRUD (create, read, update, delete) functions available to the public on books.

I built this project with Python and Flask, along with MongoDB as the database.

## Wireframes
The wireframes for this project can be found [here]()

## Application guidelines
  - MongoDB to hold a database based on goodreads books collection
  - User is presented with a 'search for books by title or authors' on the home web page and a few of my favourite books and their sypnosis
  - User can create, edit and delete books
  - The website is intuitive for the user experience and easy to navigate around 
  - Information is distributed in different sections / pages of the website

## Technologies used
Here are a list of programming languages, frameworks, technologies and tools used for this website:
* HTML5
* CSS3
- #### [JQuery](https://jquery.com)
    - **JQuery** has been used to simplify DOM manipulation.
- #### [Google Colaboratory notebook](https://colab.research.google.com/)
    - **Colab notebook** is used for writing the markdown for this README.md file
- #### [Python](https://www.python.org/)
    - **Python** as the main programming language used to build this project
- #### [Flask](https://palletsprojects.com/p/flask/)
    - **Flask** along with [Werkzeug](https://palletsprojects.com/p/werkzeug/) and [Jinja](https://palletsprojects.com/p/jinja/) is a Python web application framework to display the html pages with entries from MongoDB database
- #### [Cloud9](https://c9.io)
    - **Cloud9** is an IDE used to develop the website.
- #### [MongoDB](https://www.mongodb.com/)
    - **MongoDB** short for (Humongous database) is a noSQL, cloud-based database platform used to store all of the data for each ramen that is used on the website
- #### [Materialize](https://materializecss.com/)
    - **Materialize** is s modern responsive front-end framework based on Material Design used to create professional looking cards, search boxes, forms & overall style of the website
- #### [Am I Responsive?](http://ami.responsivedesign.is/?url=#)
    - **Am I Responsive** is used to see across multiple devices with different screen sizes the responsiveness of the website
- #### [Git](https://git-scm.com/)
    - **Git** is used for version control to regularly commit codes to Github    
- #### [GitHub](https://github.com/)
    - **GitHub** is used as a remote backup of code used in this project
- #### [Heroku](https://www.heroku.com)
    - **Heroku** is used as a platform for this project to be deployed to
    - To view the deployed version, please click on [Jimbo's Goodreads](https://jimbo-book-reviews.herokuapp.com/)

## UX
- When the user first enters the website, he/she is warmly welcomed to my site with big fonts near the top middle of the page
- I chose an olive green color for the navigation bar and footer as they remind me of the old cosy sofa at my local library
- A background picture of a whole bookshelf of books highly suggest that this website is about books
- The form is clean looking with appropriate icons and subtle animations to keep the user engaged with filling up the form with details to add a book
- The books collection page displays up to 12 books with the main details of the books' title and authors, and 2 links for the user to edit the book or to delete it
- For more information of the book, on each card there are 3 verticle dots for the user to click on it for a page to scroll up on the card for the details

## UI
- On top of the navbar, the user could add a book to this collection if he/she clicks on 'add book'
- The user would be brought to the books collection page if he/she clicks on the 'Books collection' link
- There are some external links to relevant book sites if the user clicks on the drop down list
- A search function is made available for searching book titles or authors
- On the search results page, books relating to the searched input is displayed, or an error message is shown if no searches are found. I included the search function on the same page so that the user do not need to navigate back to the home page to perform another search
- Below the search box, there are some of my favourite books on display along with sypnosis
- At the bottom of the page, the footer has a book logo and project name that would bring the user to a newly loaded home page when clicked on
- There is also a social media section where users could reach me at my LinkedIn, Facebook and Instagram accounts.
- The user is presented with a form to add a book on the 'Add Book' page. After the fields are filled in and form submitted with a click on the 'Add Book' button, the user is brought to the 'Books Collection' page
- On the 'Books Collection' page, books are sorted by order of newest added book so the user could visually check that his/her book entry is added to the list

## Features
- The user can navigate to any section of the website with a click of a button or a link
- The search function can be used to search for book titles and authors
- The book display page would display up to 12 books from the users' search input
- Users could add a book, see it being part of the books collection, edit it and delete it at any point in time 
- Forms are clean looking and easy to fill up with clear instructions on the type of inputs needed. Additionally, there are buttons at the bottom of the form to add the book, save changes or to cancel if the user changed his/her mind

## Features Left to Implement
- User log in so only the books added by the specific user could be edited and deleted
- Option for user to upload their own book pictures
- Reviews for each book by different users
- Pagination for easy reference
- Number of views for each book to be incremented by each click on the display of an individual book

## Database Schema
MongoDB was database of choice for this project. I had an extensive set of data on books and I needed flexibility to extract the information.

The Database structure is as follows:
- `'_id': ObjectId` (string)
- `'title': title of book` (string)
- `'authors': author(s) of book` (string)
- `'rating': rating of book` (integer)
- `'isbn': isbn number of book (13 digits)` (integer)
- `'language_code': language code of book` (string)
- `'num_pages': number of pages of book` (integer)

## Testing

I did manual testing on all links, buttons and functions of each page of the website.

Home page:
- All links on navbar directs the user to the correct page
- The search function directs the user to the search result page
- Images and sypnosis of my favourite books are displayed
- The book logo refreshes when clicked on
- Each social media icon directs the user to the correct external link

Search Result page:
- Books are displayed if there are matches from the user's search text input
- If there are no matches, an error message is displayed.
- The search function on this page works

Add book page:
- Each input field on the form have materialize's animation when the user clicks on item
- The drop down displays the correct options
- The rating bar is scrollable
- The 'add book' button adds the book to the collection and directs the user to the books collection page when clicked
- The 'cancel' button directs the user to the books collection page when clicked

Books collection page:
- 12 books from the database are displayed at all times
- The vertical scroll is working if the title and/or author's characters exceed the allocated height
- On click of the image or the 3 verticle dots, a page scrolls up to reveal more details about the book
- The user is directed to the edit book page when the edit link is clicked
- The book is deleted when the 'delete' link is clicked, and the user is directed to the books collection page

Edit books page:
- All input fields were populated with existing information from the database
- The book is updated with any new inputs with a click on the edit link
- The user is directed to the books collection page with a click on the cancel link

Google Chrome Devtools was used throughout the project to view this website on a number of stimulated mobile, tablet, laptop and desktop devices to ensure compatibility and responsiveness. Devices include Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5 / SE, iPhone 6/7/8, iPhone 6/7/8 plus, iPhone X, iPad, and iPad Pro.

## Deployment
This project is fully deployed to [Heroku](https://jimbo-book-reviews.herokuapp.com/)

These steps were taken:
1. Run this command `echo web: python app.py > Procfile` in the terminal which will create a Procfile

2. Use the command `sudo pip3 freeze —local > requirements.txt` to add a requirements.txt file showing all of the packages for this project

3. Run `git add .` to stage all of the files, run `git commit -m "<message here>"` to get changes ready to push to GitHub

4. Create a repository in GitHub and follow the instructions to push the project up to GitHub

5. Run `git push` and if instructed, input email address and password and changes will be pushed to GitHub

6. Go to [heroku](https://dashboard.heroku.com/) and log into your account

7. Click "New" on the dashboard and click "Create New App"

8. Enter the name of the project and set the region to the one closet to you

9. Go to "Settings" inside the app, click on "Reveal Config Vars"

Click on add to enter the following:

| Key | Value |
--- | ---
IP | 0.0.0.0 
PORT | 5000
MONGO_ URI | taken from MongoDB account

10. On top of the page, click "Deploy." Scroll down and follow the list of instructions given to deploy the project to Heroku. The steps should be done in the terminal

11. Scroll to the top of the page in Heroku & click "Open App". The project is opened on a new tab and is deployed by Heroku

## Credits

- Background image of [library]()
- Book dataset from [Goodread]()
- Book [images]()

## Acknowledgments
Special mention to our teacher Shan for his guidance and assistance. Also our teaching assistants John and Arif for being available when I have questions.


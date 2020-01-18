# Jimbo's Goodreads

### - A Data Centric Development Milestone Project from Code Institute

Please see the deployed project on [Heroku](https://jimbo-goodreads.herokuapp.com/)

## Project purpose
My inspiration for this project stemmed from my interest and hobby in reading books. I have a huge personal collection of books at home and I thought it would be great to build a digital version of a simplified version of Goodreads for this project.

This project is designed to have CRUD (create, read, update, delete) functions available to the public on books.

I built this project with Python and Flask, along with MongoDB as the database.

## Wireframes and ER diagram
The wireframes and ER diagram for this project can be found [here](https://github.com/papadum-is-nice/TGC_Milestone_Project_3/tree/master/static/images/Wireframe)

## Application guidelines
  - MongoDB to hold a database based on goodreads books collection
  - User is presented with a 'search for books by title or authors' on the home page and a few of my personal favourites and their sypnosis are laid out for the user as well
  - User can create, edit and delete books
  - The website is intuitive for user experience and easy to navigate around 
  - Information is distributed in different sections / pages of the website

## Technologies used
Here is a list of programming languages, frameworks, technologies and tools used for this website:
* HTML5
* CSS3
- #### [JQuery](https://jquery.com)
    - **JQuery** is used for DOM manipulation.
- #### [Google Colaboratory notebook](https://colab.research.google.com/)
    - **Colab notebook** is used for writing the markdown for this README.md file
- #### [Python](https://www.python.org/)
    - **Python** as the main programming language used to build this project
- #### [Flask](https://palletsprojects.com/p/flask/)
    - **Flask** along with [Werkzeug](https://palletsprojects.com/p/werkzeug/) and [Jinja](https://palletsprojects.com/p/jinja/) is a Python web application framework to display the html pages with entries from MongoDB database
- #### [Cloud9](https://c9.io)
    - **Cloud9** as main IDE to develop the website.
- #### [MongoDB](https://www.mongodb.com/)
    - **MongoDB** short for (Humongous database) is a noSQL, cloud-based database platform used to store all of the data for each book that is used on the website
- #### [Materialize](https://materializecss.com/)
    - **Materialize** is a modern responsive front-end framework based on Material Design used to create professional looking cards, search boxes, forms & overall style of the website
- #### [Am I Responsive?](http://ami.responsivedesign.is/?url=#)
    - **Am I Responsive** is used to see across multiple devices with different screen sizes the responsiveness of the website
- #### [Git](https://git-scm.com/)
    - **Git** is used for version control to regularly commit codes to Github    
- #### [GitHub](https://github.com/)
    - **GitHub** is used as a remote backup of code used in this project
- #### [Heroku](https://www.heroku.com)
    - **Heroku** is used as a platform for app deployment
    - To view the deployed version, please click on [Jimbo's Goodreads](https://jimbo-goodreads.herokuapp.com/)

## UX
- When the user first enters the website, he/she is warmly welcomed  with big fonts at the top middle of the page
- I chose an olive green color for the navigation bar and footer as they remind me of the old cosy sofa at my local library's reading corner
- A background picture of a beautifully shot bookshelf to suggest that this website is about books
- The form is clean looking with appropriate icons and subtle animations to keep the user engaged with filling up the form when adding a new book to the collection
- The books collection page displays up to 12 books with the main details of the books' title and authors, and 2 hyperlinks for the user to edit or to delete
- For more information on the book, each card has 3 vertical dots for the user to click on to reveal a card with scroll effect for more details about the selected book

## UI
- At the top of the navbar, the user have the option to add a book to the collection if he/she clicks on 'add book' hyperlink
- The user will be brought to the books collection page if he/she clicks on the 'Books collection' hyperlink
- There are some external links to relevant book review sites if the user clicks on the drop down list
- A search function is made available for searching book by either titles or authors
- On the search results page, books relating to the searched input will be displayed, or a text error message is shown if no searches are found. I have also included the search function on the same page so that the user do not need to navigate back to the home page to perform another search
- Below the search box, ihave some of my personal favourites on display along with sypnosis
- At the bottom of the page, the footer has a book logo and project name that would bring the user back to the home page when clicked on
- There is also a social media section where users could reach me at my LinkedIn, Facebook and Instagram accounts.
- The user is presented with a form to add a book on the 'Add Book' page. After the fields are filled in and form submitted with a click on the 'Add Book' button, the user is brought to the 'Books Collection' page automatically and the book that was newly added would be displayed right at the top
- On the 'Books Collection' page, books are sorted by order of newest added book so the user could visually check that his/her book entry is added to the list without having to search again

## Features
- The user can navigate to any section of the website with a click of a button or a hyperlink
- The search function can be used to search for book titles and authors
- The book display page would display up to 12 books from the users' search input
- Users can add a book, see it being part of the books collection, edit it and delete it at any point in time 
- Forms are clean looking and easy to fill up with clear instructions on the type of inputs needed. Additionally, there are buttons at the bottom of the form to add, save or cancel if the user changes his/her mind

## Features Left to Implement
- User log in so only the books added by the specific user could be edited and deleted
- Option for user to upload their own book pictures
- api to pull book coverart by ISBN number
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
- Upon clicking the image or the 3 vertical dots, a page with scrolls effect appears to reveal more details about the selected book
- The user is directed to the edit book page when the edit link is clicked
- The book is deleted straigtaway from the collection when the 'delete' hyperlink is clicked, and the user is directed to the books collection page

Edit books page:
- All input fields were populated with existing information from the database
- The book is updated automatically by clicking on the edit hyperlink
- The user is directed to the books collection page when the cancel link is clicked

Google Chrome Devtools was used throughout the project to view this website on a number of simulated mobile, tablet, laptop and desktop devices to ensure compatibility and responsiveness. Devices include Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5 / SE, iPhone 6/7/8, iPhone 6/7/8 plus, iPhone X, iPad, and iPad Pro.

## Deployment
This project app is fully deployed to [Heroku](https://jimbo-goodreads.herokuapp.com/)

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

- Background image of [library](https://unsplash.com/s/photos/bookshelf)
- Book dataset from [Kaggle](https://www.kaggle.com/jealousleopard/goodreadsbooks)
- Book coverart [images](https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155)

## Acknowledgments
Special mention to our lecturer Shan for his guidance and assistance. Also our teaching assistants John and Arif for being available when I have questions.


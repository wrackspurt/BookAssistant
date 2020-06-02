# BookAssistant
This application is a part of my course work.

## Description
[BookAssistant](https://thebookassistant.herokuapp.com/) is a web application providing book recommendations. It uses a hybrid recommender system which combines content based and collaborative filtering approaches to achieve the given aim.

## A short guide to using BookAssistant
Section ["recommendation based on my preferences"](https://thebookassistant.herokuapp.com/collaborative_filtering) requires your [Goodreads](https://www.goodreads.com/) ID to provide recommendations (based on collaborative filtering approach). Don't worry, if you don't have a Goodreads account: just leave a blank line and enter the button to continue. If you have Goodreads account but BookAssistant doesn't recognize your ID, it means that your ID is not in the dataset or there's not enough information about you to create recommendations, but you still can get recommendations based on another approach. You'll have to choose what kind of recommendation (rested on content based approach) you'd like to get: 
* if you what to read some books of a specific author, choose "recommendation based on my favourite book (by author)"; 
* if you just want to read books on a certain themes, choose "recommendation based on my favourite book (by tag)".  

After that you'll just have to enter the title of you favourite book and revel in your recommendations :)

If you want to read some well-known books, visit ["the most popular books list"](https://thebookassistant.herokuapp.com/popular_books) section.

## Resources
I used [the dataset](https://www.kaggle.com/zygmunt/goodbooks-10k) that contains 10000 books and 53424 users from [Goodreads](https://www.goodreads.com/).

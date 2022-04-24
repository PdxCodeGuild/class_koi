
# Lab 02: Library

Let's create an application for representing a library. You should have two models (below) and a page for users to check out and check in books. You can enter the book and author information using the admin panel.

- `Book`: a model representing a book, with a title, publish date, and an author (foreign key)
- `Author`: a model representing an author of a book, one author can have multiple books


## Version 2

Add another model to keep track of who checked out a book and when. When a user checks a book back in, record that too. Add a text input on the 'checkout' page to record the name of who checked out the book. Have a page to show all the checkouts and returns.

The new model can have the following fields:

- book: the book that the user checked out or checked in
- user: a text field containing the name of the user that checked out or checked in the book
- checkout: a boolean indicating whether the book was checked out or checked in
- timestamp: a datetime that records when the book was checked out or in

## Optional Version 3

Add a `Genre` model.  Give the `Genre` model a [many-to-many relationship](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/).  Each genre can have any number of books.  Each book can have any number of genres.

## Optional Version 4

Add a [user authentication system](https://docs.djangoproject.com/en/3.2/topics/auth/) to the project.  Instead of a user text field in the check out model, make the field a `ForeignKey` to the `User` model.

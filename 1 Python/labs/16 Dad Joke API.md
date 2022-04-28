# Lab 16: Dad Joke API

### Git Setup:
```sh
> git checkout main
> git pull
> git checkout -b your-name/python/lab16
```

Use the [Dad Joke API](https://icanhazdadjoke.com/api) to get a dad joke and display it to the user. You may want to also use [time.sleep](https://www.geeksforgeeks.org/sleep-in-python/) to add suspense.


## Part 1

Use the [requests](../docs/15%20Requests.md) library to send an HTTP request to `https://icanhazdadjoke.com/` with the `accept` header as `application/json`. This will return a dad joke in JSON format. You can then use the `.json()` method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.


## Part 2

Add the ability to "search" for jokes using [another endpoint](https://icanhazdadjoke.com/api#search-for-dad-jokes). Create a REPL that allows one to enter a search term for dad jokes on different subjects.  You can show all (up to 20) jokes at once, or use `time.sleep` to keep them coming at a steady pace.  As a bonus, you can ask the user if they want to see the next 20 jokes.

### Git Add, Commit & Push:
```sh
> git add files-to-be-added
> git commit -m "your commit message goes here"
> git push -u origin your-name/python/lab16
```
Then go to the repository to create a PR.

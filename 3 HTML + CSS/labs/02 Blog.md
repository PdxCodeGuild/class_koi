# Lab 02: Blog

### Git Setup:
```sh
> git checkout main
> git pull
> git checkout -b your-name/html/lab02
```

Let's make a blog with a title, top-nav, side-nav, and multiple posts. Use [flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) and [semantic elements](https://www.w3schools.com/html/html5_semantic_elements.asp) (header, nav, section, and footer). You can use a [custom font](https://fonts.google.com/), [fancy colors](https://htmlcolorcodes.com/color-names/), and generate fake content using an [Ipsum](https://meettheipsums.com/).

Your blog post may not need images (this comes down to the style of the blog).  But it should include at least a title, author, and body.

## Optional Flask Version
Turn your blog into a Flask app.  You can serve just one page, or have a main page, then another route for serving up the full post pages.  Your json might have an array (list) of objects (dictionaries) for each post:
```json
{
	"posts": [
		{
			"title": "the title of the first post",
			"body": "body of the first post",
			"author": "author of the first post",
		},
		{
			"title": "the title of the second post",
			"body": "body of the second post",
			"author": "author of the second post",
		},
		{
			"title": "the title of the third post",
			"body": "body of the third post",
			"author": "author of the third post",
		}
	]
}
```

### Git Add, Commit & Push:
```sh
> git add files-to-be-added
> git commit -m "your commit message goes here"
> git push -u origin your-name/html/lab02
```
Then go to the repository to create a PR.

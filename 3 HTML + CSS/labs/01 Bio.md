# Lab 01: Bio

### Git Setup:
```sh
> git checkout main
> git pull
> git checkout -b your-name/html/lab01
```

Write up a short bio webpage for someone or something. It can be about a celebrity, a fictionary character, a place, a species, etc.  Check out the [examples](https://github.com/PdxCodeGuild/class_bumble_bee/tree/main/2%20HTML%20%2B%20CSS/labs/images)

## Part 1

- Their name
- A written introduction
- A link to a Wikipedia article
- A picture of them
- A list of places where they've lived
- A quote from them

## Part 2

Implement at least 4 of the following:

- Center the entire content of the body
- Modify the padding and margins on your paragraphs to look better
- Use a custom font
- Add a background image
- Change the color of the links (you can give separate css for visited and unvisited links)

## Part 3

Implement at least 4 of the following:

- Pick a color scheme and modify the background, body text, and link text color.
- Change the typeface of the quote.
- Add a rounded border to the picture.
- Change the bullet points on the list of places.
- Change the css of the links when hovered-over


## Part 4

Make a [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) file with the information from [Part 1](#part-1) and save it as `data.json`.  Here is an example:

```json
{
	"name": "Bender Bending Rodríguez",
	"bio": "Bender is a cool and funny hedonistic robot who likes to steal things", // aka written introduction
	"link": "https://futurama.fandom.com/wiki/Bender_Bending_Rodr%C3%ADguez",
	"photo": "https://static.wikia.nocookie.net/enfuturama/images/4/49/Bender_Bending_Rodr%C3%ADguez_-_Official_Character_Promo_1.jpg/", // this can be a url or a relative path to an image from the html file
	"places_lived": [
		"Tijuana, Mexico",
		"New New York"
	],
	"quote": "Bite my shiny metal ass!"
}
```

### Git Add, Commit & Push:
```sh
> git add files-to-be-added
> git commit -m "your commit message goes here"
> git push -u origin your-name/python/lab01
```
Then go to the repository to create a PR.

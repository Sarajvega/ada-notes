# Adding Behavior

In order for our website to load HTML, we add a link to our JavaScript file in our HTML, similar to how we've included CSS.
```html
<!-- index.html -->
...
<body>
  <!-- ... -->

  <script src="scripts/index.js" type="text/javascript"></script>
</body>
```
- When the browser encounters a script tag, it stops loading the HTML document. Instead, the browser pauses to download the entire script, which might take a long time to load. 
- If we put our script tags before the site's content, the user may be looking at an empty white screen while the scripts load—not a great user experience.
- If we put our script tags at the bottom of the body, then the browser renders the whole page first, before loading the scripts.


You can access the dom through `document`, a global variable that contains a pages elements.

You access all HTML elements through the root node of the DOM because the root node of a tree structure is the top node, and it can check all descending nodes.


You can do a lot from the console!
- add classes: ```importantFact.className = `${importantFact.className} highlight`;```
  - Use interpolation to not overwrite existing class but just add new one. 
  - to read list of classes use the dot operator.

## Create New Elements

```javascript
// create new list
const newAppearanceFact = document.createElement("li");
// give new list item text content
newAppearanceFact.textContent = "covered in sand (when on a sandy beach)";
// get the facts list
const appearanceList = document.getElementById("facts__list");
// put the new fact at the end of the facts list
appearanceList.appendChild(newAppearanceFact);
```


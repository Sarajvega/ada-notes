# Layout
- MDN basic overivew of flexbox: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox
- Tech for aligning in flexbox:https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Aligning_Items_in_a_Flex_Container
- Browser compatability for flexbox:https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Backwards_Compatibility_of_Flexbox
- W3 resource on Grid: https://www.w3schools.com/css/css_grid.asp
- https://developers.google.com/web/updates/2017/01/css-grid
- https://cssgridgarden.com/
  
## Box Model
- Every element is a box on a page.
- All elements have:
  - Content: The most inner portion of the element.
  - Padding:The space between the content and the border.
  - Border: 	The space between padding and the margin, and typically the most outer visible portion of the element.
  - Margin:	The most outer portion of the element, and the space between this element and the surrounding elements. Depending on context, margins between elements may overlap (and the larger margin is preserved).

## Size of an element
- `margin-right + border-right + padding-right + width + padding-left + border-left + margin-left` = width of an elem.
- `margin-top + border-top + padding-top + height + padding-bottom + border-bottom + margin-bottom` = height of an elem

## Units
- More info: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units

Px vs Em/Rem?
When you use px, you don't put user preferences at the forefront. When the user zooms in or change the browser font setting, websites need to adjust to fit the user's setting. pxdo not scale but emand remscales.
- px is not scalable, it is an absolute unit.
- The computed pixel value of emunit is relative to the font size of the element being styled. 
- The computed pixel value of remunit is relative to the font size of the root (html) element.
  - Rem is relative to the document whereas em is only relative to its parent node. It's much better to base your font sizes off of one root point, for consistencies sake.

vw and vh
The viewport is the area of screen that is displaying the web page. It's the literal area of a web page visible at a given moment, which excludes overflowing sections of the HTML that are "off-screen."

This is distinct but similar to the device screen or browser window, as both affect the viewport.

One vw (1vw) is equal to 1% of the viewport width, and 100vw is 100% of the viewport width.

vh is relative to the viewport's height. 1vh is 1% of the viewport height, and 100vh is 100%.

use:
- % for widths
- rem for font-size
- em for padding / margin
- px rarely if at all

## Display
- The display property determines how an element flows on a page. Browsers render HTML elements and position them, flowing from top-to-bottom and left-to-right.

Types:
- block: Block-level elements start on a new line and take up the full width available (usually determined by the parent element)
- inline: Inline elements do not start on a new line. They only take up as much width as necessary to fit the content
- inline-block: Inline-block elements flow on the page like inline elements, and respect width and height adjustments like block elements.

Each HTML element has a default display value of block or inline. There are few exceptional elements with a default display value of inline-block.

## Flexbox
- When rendering, the browser flows from left to right, placing things in a single line. The line is as tall as the tallest element, and all the things are lined up with its bottom.
- If an element flows off the edge of the screen, the browser wraps this element around and starts a new line, completely below the current one.
- every HTML tag comes with a display property value of inline or block.
- Elements that are by inline elements align themselves left-to-right as many items
- Elements that are block elements interrupt flow and start and end with a line break. Examples of these elements are div, p, and h1.

## Setting up:
Flexbox solves the following problem: How do I define rules for aligning many small elements in one larger container element?
1. The "one larger container element" is called the flex container. We designate it as the flex container by giving it the CSS rule display: flex;
2. The "many small elements" that we are trying to align are called the flex items. The flex items must be and will only be the direct children of the flex container
   1. these flex items may have children inside of them. Note: the rules of a flex container do not apply to the children of flex items 
3. The "rules" we want to define for aligning the flex items will be additional properties on the flex container

flex-direction has the following properties:
1. row (default)
2. row-reverse
3. column
4. column-reverse

## Control Alignment
To control alignment of flex items within the flex container, we have two main properties: justify-content and align-items.

justify-content determines alignment along the main axis. Its possible values are:
- stretch
- flex-start
- flex-end
- center
- space-around
- space-between
- space-evenly

align-items determines alignment along the cross axis. Its possible values are:
- stretch
- flex-start
- flex-end
- center

## Responsive Design
Responsive design is all about answering the question, "does this website work with different browser sizes and devices?" By work, we can ask "does this look good?" but we must always ask "is the site still functional?"

## CSS Grid
How do I define rules for the layout of many elements, specifically across rows and columns? Therefore, to use CSS Grid, we set up our CSS Grid with these rules:
1. There is one large container for these elements, and it is called the grid container. We designate it as the grid container by giving it the CSS rule display: grid;
2. The "many elements" that we are trying to put in a layout are called the grid items. The grid items must be and will only be the direct children of the grid container
   1. these grid items may have children inside of them, but will not be affected by this grid container
3. We can define the "rules" for the grid system in many ways
   1. The grid container may have CSS that determine a "template" for how all the grid items span across rows and columns
   2. The grid item may have CSS applied to it that determines how it specifically spans across rows and columns

Ex:
```html
<!-- index.html -->
<!-- stuff like the opening html tag, head tag, link to stylesheet, opening body tag -->

<main class="container">
  <header class="header">

  </header>
  <nav class="nav">

  </nav>
  <div class="content">

  </div>
  <footer class="footer">

  </footer>
</main>

<!-- close body tag and html tag -->
```

```css
/* style.css */

.container {
  /* these are just an arbitrary widths and heights to look good on our browser */
  width: 30vw;
  height: 60vh;

  display: grid;
}

.header {
  background-color: #d55e00;
}

.nav {
  background-color: #f0e442;
}

.content {
  background-color: #009e73;
}

.footer {
  background-color: #0072b2;
}
```

## Grid Template
But we need to first define the following in the context of the entire grid container:
- How many columns are there?
- What size is each column?
- How many rows are there?
- What size is each row?

We answer all of those questions with any property beginning with the phrase "grid-template": grid-template, grid-template-columns, grid-template-rows, and/or grid-template-areas.

**Grid Template Columns, Grid Template Rows**
To define how many columns there are and what size each column is, you use the CSS attribute grid-template-columns so that it applies to your grid container.
```css
.container {
  display: grid;
  grid-template-columns: 200px 100px 50%;
}
```

Experiment in codepen: https://codepen.io/adadev/pen/bvbKQX?editors=1100

**Shortcut: Grid Template**
It is common to need to define both the grid-template-rows and grid-template-columns at the same time. There is a syntax shortcut for this: instead of the above properties, use grid-template. The value for this is what you would put in grid-template-rows, a slash, then what you would put in grid-template-columns.
```css
.container {
  display: grid;
  grid-template: 100px 500px / 200px 100px 50%;
}
```

CSS Grid lets us use one specific unit of measurement that we can't use anywhere else in CSS: the fr fractional unit.
ex: https://codepen.io/adadev/pen/xWKJdz?editors=1100

**Start and End**
```css
.container {
  display: grid;
  grid-template: 1fr 1fr / 1fr 1fr;
}

.item {
  grid-column-start: 1;
}
```
- define on a grid whcih col line number the item starts w/ `grid-column-start`, and where it ends w/`grid-column-end`. 
- same for rows.

Shortcut:
```css
.item {
  grid-column: 1 / 4;
  grid-row: 3 / 5;
}
```

**Span**
Instead of giving an integer for the line number an item ends at, you can give span num_of_rows_or_columns.
```css
.item {
  grid-column-start: 1;
  grid-column-end: 4;

  /* is the same as */
  grid-column-start: 1;
  grid-column-end: span 3;

  /* is the same as */
  grid-column: 1 / 4;

  /* is the same as */
  grid-column: 1 / span 3;
}
```

**Auto**
auto means a lot of different things in different contexts. In the context of CSS Grid:
- When used to define grid-template sizes, it can mean "automatically fill up as much as possible," but it doesn't play well with fr units
- When used to define start or end columns or rows for a grid item, it can mean "the browser should make the best decision on where it should automatically flow next"
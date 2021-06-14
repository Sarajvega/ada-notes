# Styles and Presentation
All valid CSS properties: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference

Game for selector practice: https://flukeout.github.io/
CSS specificity and things you should know: https://www.smashingmagazine.com/2007/07/css-specificity-things-you-should-know/
Ultimate Guide to CSS Psuedoclasses and pseudoelements: https://www.smashingmagazine.com/2016/05/an-ultimate-guide-to-css-pseudo-classes-and-pseudo-elements/
## Css
- `.css` extension
- CSS rule-sets are blocks of code that select specific HTML elements, and contain **declarations**. 
  - **Declarations** are pairs of properties and values which describe how to style the selected HTML elements.
  - 
```css
selected-elements {
  property: value;
}
```

## Add CSS to a Website

```html
<head>
  <meta charset="UTF-8" />
  <title>Some Title</title>
  <!-- Link to Style Sheet -->
  <link href="styles/style.css" rel="stylesheet" />
</head>
```
- Reference an external style sheet rather than applying the style in the tag.

## Classes
- Assigning a class: `<h1 class="page-title">Hello World!</h1>`
- Multiple classes: `<h1 class="page-title highlight front-page">Hello World!</h1>`
- Select by Classes:
```Css
.page-title {
  color: midnight;
  font-size: 2.5rem;
}
```

## IDs
- `<h1 id="home-page-title">Hello World!</h1>`
- Each element can have only one ID
- Select by ID:
```css
#home-page-title {
  color: teal;
  font-size: 4rem;
}
```
## Cascade and Inheritance
What happens when more than one CSS rule-set applies to an element?
- In CSS, the combination of cascading, inheritance, and specificity determines the final answer of what styles get applied.
-  "Cascading" describes the way that styles are applied to the elements in a document. 
-  **styles and rule-sets that are defined "later" in the cascade override styles and rule-sets that are defined "earlier" in the cascade.**
  
## Sources of Cascading
- The browser's default styles for the HTML elements.
- The styles linked to the document, like the style.css file we've been working in so far. We have the most control here, so we will focus on this section the most
- Styles specified by a user who is reading the document

To find out if a CSS property gets inherited, we'll need to check the CSS documentation for that property, and read more on MDN on inheritance - https://developer.mozilla.org/en-US/docs/Web/CSS/inheritance

## Specificity
- CSS gives priority to the rule that has the more specific selector.
  - class and ID selectors are more specific than simple HTML element selectors

There are four distinct categories which define the specificity level of a given selector:
1. Inline styles. An inline style lives within the HTML document. It is attached directly to the element to be styled. We have seen that we generally do not do this. This has the highest specificity.
2. IDs. ID is a unique identifier for HTML elements, such as #home-section. This has the second highest specificity.
3. Classes, attributes and pseudo-classes. This group includes classes, attributes, and pseudo-classes such as :hover, :focus etc.
4. Elements and pseudo-elements. This includes selecting by HTML tag and pseudo-elements like ::before and ::after.

## Selectors based on relationships
`A E` - Any E element that is a descendant of A element. that is: a child, or a child of a child, etc.
`A > E` - Any E element that is a child (i.e. direct descendant) of an A element
`E:first-child` - Any E element that is also the first child of its parent
`B + E` - 	Any E element that is also the next sibling of a B element (that is: the next child of the same parent)

## Multiple Selectors
```css
h1,
h2,
h3 {
  color: teal;
  font-family: helvetica;
}
```

## Attribute selectors
```css
[href="http://www.github.com"]
{
  color: olive;
}
```

Another way:
```css
[href*="github"] {
  color: teal;
}
```
This selects any elements that have at least part of content in the quotes.

## Pseudo Classes - Pseudo-Elements
- MDN pseudo-class index: https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes
- MDN pseudo-elements index:https://developer.mozilla.org/en-US/docs/Web/CSS/pseudo-elements


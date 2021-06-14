# Structuring Content

## Vocab
- HTML Element: A unit of content on an HTML page. One element is represented as one node in the DOM.
- HTML tag: A piece of syntax that defines an HTML element. Most HTML elements have an opening and closing tag.
- Semantic HTML: The practice of intentionally using HTML tags that are descriptive to the content itself
- Attributes: Additional pieces of information attached to an HTML element. Comes in attribute-value pairs.
  

## HTML files
- have HTML elements that define the websites structure.
- use .html extension
  - kebab case
- Uses tags: `<example>Content Details</example>`

What happens if we put a paragraph inside a <nav> tag? What happens if we put text inside a <section> tag?

Our browsers will still do their best to render the content. Browsers don't throw runtime errors, nor do they validate HTML for correct use or syntax.

They can have **attributes**!
- additional info: `<example attribute-1="string value" attribute-2="a different string value">Content Details<example>`
- ex: `<a href="https://adadevelopersacademy.org/">Click here to visit Ada's website!</a>`
  - Here `href` is the attribute. 

## Standard HTML Document Setup
```html
<html>
  <head>
    <meta charset="UTF-8" />
    <title>The Title of This Website Shown in Browsers</title>
  </head>
  <body>
    Hello, HTML World! All HTML elements that have content and should be
    displayed to the user should go here, inside the body tag.
  </body>
</html>
```
- `<html>`: describes an HTML doc. optional, technically. Helps visualize the root of the DOM. 
- `<head>`: holds metadata.

## Nesting Elems
```HTML
<nav>
  <h1>Ada's Recipe Blog</h1>
</nav>
```
- the <nav> element contains the <h1> element. The <nav> element is a parent element.
- The <h1> element is a child element to the <nav> element, because it's nested inside it!

# Content Elements

**Lists**
Ordered:
```html
<ol>
  <li>Content</li>
  <li>Content</li>
  <li>Content</li>
</ol>
```

Unordered:
```html
<ul>
  <li>Content</li>
  <li>Content</li>
  <li>Content</li>
</ul>
```
**Images**
Has two attributes: 
1. `alt`: test used when:
   1. When the image cannot load (such as being offline, or the image isn't found), alt text will display instead
   2. When a user uses a screen reader and is not looking at the image, alt text will be read to the user
   3. When a cursor hovers over an image for several seconds, a caption appears containing the alt text
2. `src`: path to image

# Sectioning Elements
Here is a resource listing all valid HTML elements [https://developer.mozilla.org/en-US/docs/Web/HTML/Element]

HTML elements can usually be categorized in one of two ways:
1. Content element, whose responsibility is to describe literal website content
2. Sectioning element, whose responsibility is to contain and group other HTML elements

**Div tag**
- `<div>Content Elements</div>`
- The <div> tag was used as a generic sectioning element.
-  The <div> tag itself isn't descriptive about the content, and therefore doesn't follow semantic HTML principles. When possible, we should prefer other HTML tags compared to <div>.
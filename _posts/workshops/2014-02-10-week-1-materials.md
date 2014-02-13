---
layout: notes

title: Week 1 - Introduction to HTML and CSS
description: We'll introduce you to HTML, HyperText Markup Language, which defines the structure of a web page. Then, we'll learn about CSS (Cascading Style Sheets) and style our web pages. You'll dive right in by creating your own personal website. 
time: Feb. 13 at 8 p.m.
location: AA G008
semester: Spring
week: 1

<!-- date: '2014-01-40T20:00:00-05:00' -->
<!-- Peter doesn't know how to format this correctly. -->
permalink: /workshops/2014/spring/week-1-materials/
---

# Housecleaning
- Create a folder in your computer called HackBU. This is where all your work will go so it will be good to be organized.
- Install a text editor. Sublime Text is a good place to start for beginners.
- If you don't already have it, install Google Chrome to use as a web browser.
(Assigned readings about directories and articles that encourage people to learn how to code.)

# Week 1 Overview
- Introduction to HTML and CSS
- Creating text and lists with HTML
- Styling the color and styles with CSS.

(We will be learning HTML and CSS concurrently, because no one wants to look at a wall of ugly text with no way to style it.)

## HTML
### Creating Your First HTML File
HTML files are simply text files that a web browser can understand and can display it in the way that you specify. Let's create our first HTML file.

Exercise: Open up a text editor and type in:

    <h1>Hello World!</h1>
    <p>This is my first HTML file!</p>

And save the file as helloworld.html. Then open it up in a web browser, and you have created your first HTML file!

### Tags
HTML stands for Hyper-text Markup Language, and defines the structure of the page. 

HTML is comprised of tags. Every element is enclosed in a tag like so.

    <h1>This is a level 1 header tag.</h1>
    <p>This is a p tag, or a paragraph tag.</p>

Tags are comprised of opening tags and closing tags, with the content going in between. The name of the tag is called an HTML element, or just an element.
    
    <openingtag>Content</closingtag>

In the example we created, we used an h1 tag and a p tag. h1 represents a Level 1 header, which is primarily used for titles or headlines. p stands for paragraph, which is used for body text. Most of learning HTML and CSS is knowing what elements exist and when you should use them.

## Attributes
Tags also have attributes which tell us more about how the content is displayed and perhaps its relationship to other elements. Adding attributes to HTML elements can let us set how large we want them to be or what color we want them to be.

    <h1 font-size="36px">This header will be 36px. That's pretty big.</h1>
    <p color="red">This is a red sentence, because I'm different.</p>

Attributes are specified in the start or opening tag. The attribute follow the format:

    attribute-name="attribute-content"

If you think about it, HTML is essentially technology we use all the time: a word processor. In a word processor, we choose how we want to format different parts of our word document through the settings. In HTML, we do this through text instead of selecting options from a menu.

However, you can easily see that you don't want to type out how each element of the page looks like for each element. It can get really tedious and unmaintainable for larger webpages. That's where CSS comes in. It provides a set of rules for how to style elements for an entire webpage, so you don't have to individually set it for every element. If you want the whole page to use Helvetica (good choice) or for all the headers to be blue, then just simply add rules for that.

We will talk about CSS later, but just remember that you use it to style a webpage.

### Semantic VS Structural
There is semantic markup and structural markup. HTML5 tries to focus more on semantic markup, which in Lehman's terms, provides more meaningful definitions for elements. For example, for sections of a page, nav, article, section, header, footer, are all more descriptive than divs, p's, h1, etc. 

(Much like iOS, Android, Windows, Mac OS, etc. have versions, HTML has versions as well. HTML5 has the latest web standards implemented, and some elements may not work in HTML5.)

### Block VS Inline Elements, and Nesting Elements
HTML elements can be nested; this just means that you can put an HTML element within another HTML element. HTML elements are also defined by one of two types: block level elements and inline elements. Adjacent block elements, like headers, paragraphs, and lists, begin on new lines, while adjacent inline elements remain on the same line. Here is an example to show you nesting HTML elements and the difference between block and inline elements.

In your helloworld.html file, type:

    <body>
      <hl>I am on a new line.</h1>
      <p>I am also on another line.<p>
      <p>While this paragraph is in the same line, <strong>these words remain within the paragraph.</strong></p>
    </body>

HTML elements can be nested within each other, as you will see more clearly in the future when we talk about things like lists and tables, and when we talk about page layouts. In this example, every element is include within the HTML body element, which really defines everything you should be able to see in your browser. Very important.

The majority of HTML is simply knowing when to use a certain element to create structure and hierarchy in a page. For example, you don't want to write an blog post using a header. Because that would just look ridiculous. It is also really just familiarizing yourself with the important tags you need to learn. You don't have to do rote memorization, but understand what tags are important to know and to really just know that they are there if you do need to use them.

### Other Important Things!
- Doctype Declaration - This is simply you adding a line at the top of your HTML file (before everything else) that tells the browser which version of HTML you are using. It used to be very complicated. Now it just looks like this:

    <!DOCTYPE HTML>

- HTML - Wrap everything under doctype declaration in a HTML tag. This is just to tell the browser, "HEY! Everything here is in HTML. Not German."

    <!DOCTYPE HTML>
    <html>
    <!-- EVERYTHING ELSE -->
    </html>    

- Head tag - These include information about the page that aren't seen within the browser, including:
  - Title - What you see at the top of the browser

    <!DOCTYPE HTML>
    <html>
      <head>
        <title>This is my first web page!</title>    
      </head>      
    </html>

- Meta Tags - Give you more info about the page that you don't see, such as whether we want a user to be able to cache a web page or adding Google Analytics to a web page. The most important one we will use is one that defines the character set we will use, which is:

    <meta charset="UTF-8" />

What is different about this tag is that it is an empty element, because it doesn't really have any content to display. You will see how this works as we go ahead. For example, we have elements for line breaks and images that don't have text content in it, so that is when we will start using empty elements.

- Body Tag - This includes everything that will be seen in the browser. You put this right after the head tag, within the HTML tag.

    <!DOCTYPE HTML>
        <html>
          <head>
            <meta charset="utf-8">    
            <title>This is my first web page!</title>    
          </head>      
          <body>
            <h1>Hello world!</h1>    
          </body>
        </html>  

- Comments - This is text that isn't HTML and won't be shown in the browser. It is just for personal reference (so you can understand your code later), and for other people to understand (so they can change your code later). It is a good idea to comment your code, as you can go back to it later and read the comments if you don't understand what it is saying. This will not be shown in the webpage. But it will be shown when you view source, so don't do anything silly.

    <!-- Hello. I'm a comment. -->

So now that we've learned all of these things, we have the basic structure of a real HTML page. Now let's practice this in our helloworld.html file.

    <!DOCTYPE HTML>
    <html>
      <head>
        <meta charset="UTF-8">
        <title>HackBU Project</title>
      </head>
      <body>
        <h1>This is my first web page!</h1>
        <p>This is my first paragraph.</p>
      </body>
    </html>

Now that we understand the basic structure and syntax of HTML, we will talk about the specific types of elements that HTML offers.


# HTML Text and Lists
Most of any website is text, which is why the first thing we are going to cover is text!

## Level 1-6 Headers
h1 is used for main headings, h2-h6 for subheadings

    <h1>This is a Level 1 Heading</h1>
    <h2>This is a Level 2 Heading</h2>
    <h3>This is a Level 3 Heading</h3>
    <h4>This is a Level 4 Heading</h4>
    <h5>This is a Level 5 Heading</h5>
    <h6>This is a Level 6 Heading</h6>

<h1>This is a Level 1 Heading</h1>
<h2>This is a Level 2 Heading</h2>
<h3>This is a Level 3 Heading</h3>
<h4>This is a Level 4 Heading</h4>
<h5>This is a Level 5 Heading</h5>
<h6>This is a Level 6 Heading</h6>

## Paragraphs
Primarily used for body text.

    <p>Bacon ipsum dolor sit amet frankfurter short loin brisket, pork chop leberkas short ribs swine t-bone bresaola beef venison salami boudin corned beef. Shoulder leberkas pastrami kevin turducken frankfurter flank drumstick strip steak landjaeger pig hamburger swine short loin venison. Pork ham salami, ground round andouille tenderloin boudin jowl kevin pork chop. Pastrami sirloin brisket beef fatback jerky ribeye drumstick tongue kielbasa chuck hamburger jowl filet mignon.</p>
    <p>Sausage chicken boudin strip steak ball tip turducken beef ribs venison sirloin biltong. Pork belly cow chuck tongue brisket doner andouille turducken pig. Pork chop shoulder corned beef pig ground round short ribs tail strip steak frankfurter brisket rump. Tongue doner short loin hamburger. Swine shank hamburger salami, ball tip bresaola pork chop boudin pig leberkas meatball tail.</p>

Bacon ipsum dolor sit amet frankfurter short loin brisket, pork chop leberkas short ribs swine t-bone bresaola beef venison salami boudin corned beef. Shoulder leberkas pastrami kevin turducken frankfurter flank drumstick strip steak landjaeger pig hamburger swine short loin venison. Pork ham salami, ground round andouille tenderloin boudin jowl kevin pork chop. Pastrami sirloin brisket beef fatback jerky ribeye drumstick tongue kielbasa chuck hamburger jowl filet mignon.

Sausage chicken boudin strip steak ball tip turducken beef ribs venison sirloin biltong. Pork belly cow chuck tongue brisket doner andouille turducken pig. Pork chop shoulder corned beef pig ground round short ribs tail strip steak frankfurter brisket rump. Tongue doner short loin hamburger. Swine shank hamburger salami, ball tip bresaola pork chop boudin pig leberkas meatball tail.

## Bold, Italic, Strong, and Emphasis
This is an example of semantic markup VS structural markup. Bold and Italic simply describe how the text should look. Strong and Emphasis describes to us the importance of this text in context. If you want someone to focus on a part of a passage, you tell them where the emphasis is, not where the italics are. This is also important for those who are blind because they can't see bold and italics, but can understand strong and emphasis.

By default, strong and bold look the same, and italics and em look the same. They are inline elements.

    <p>Ball tip beef pork belly, pork loin andouille corned beef drumstick short ribs landjaeger salami short loin flank venison pork. Leberkas swine fatback, jowl salami doner tail andouille beef bresaola turkey. <b>Beef ribs</b> pastrami chicken prosciutto, short ribs meatloaf hamburger sausage chuck short loin salami ribeye beef ground round. Swine shankle frankfurter spare ribs chicken turkey strip steak boudin. Turducken beef ribs short loin spare ribs leberkas swine frankfurter <i>hamburger</i> kielbasa pancetta.</p>
    <p>Jerky cow bresaola ham hock, doner short ribs tri-tip salami spare ribs pastrami porchetta landjaeger. Jerky doner turducken pork chop jowl ground round porchetta, beef ribs capicola leberkas strip steak. Sirloin landjaeger <strong>meatloaf</strong>, meatball bresaola swine drumstick hamburger kielbasa pig flank turducken pastrami. Landjaeger filet mignon chicken ball tip rump, turkey shoulder pastrami flank brisket short ribs drumstick chuck sirloin shankle. Shankle pastrami corned beef, venison pig meatball boudin <i>pork chop</i> tri-tip spare ribs pork belly. Chuck drumstick rump brisket beef spare ribs pork belly pastrami frankfurter flank tail. Salami short ribs landjaeger ham hock shankle, ground round turkey pastrami beef.</p>

<p>Ball tip beef pork belly, pork loin andouille corned beef drumstick short ribs landjaeger salami short loin flank venison pork. Leberkas swine fatback, jowl salami doner tail andouille beef bresaola turkey. <b>Beef ribs</b> pastrami chicken prosciutto, short ribs meatloaf hamburger sausage chuck short loin salami ribeye beef ground round. Swine shankle frankfurter spare ribs chicken turkey strip steak boudin. Turducken beef ribs short loin spare ribs leberkas swine frankfurter <i>hamburger</i> kielbasa pancetta.</p>

<p>Jerky cow bresaola ham hock, doner short ribs tri-tip salami spare ribs pastrami porchetta landjaeger. Jerky doner turducken pork chop jowl ground round porchetta, beef ribs capicola leberkas strip steak. Sirloin landjaeger <strong>meatloaf</strong>, meatball bresaola swine drumstick hamburger kielbasa pig flank turducken pastrami. Landjaeger filet mignon chicken ball tip rump, turkey shoulder pastrami flank brisket short ribs drumstick chuck sirloin shankle. Shankle pastrami corned beef, venison pig meatball boudin <i>pork chop</i> tri-tip spare ribs pork belly. Chuck drumstick rump brisket beef spare ribs pork belly pastrami frankfurter flank tail. Salami short ribs landjaeger ham hock shankle, ground round turkey pastrami beef.</p>

## Superscript and Subscript
For all the mathematicians and chemists.

    <p>My birthday is January 31<sup>st</sup>, 1993</p>
    <p>Vitamin water is essentially just C<sub>6</sub>H<sub>12</sub>O<sub>6</sub></p>

<p>My birthday is January 31<sup>st</sup>, 1993</p>
<p>Vitamin water is essentially just C<sub>6</sub>H<sub>12</sub>O<sub>6</sub></p>


## Line Breaks and Horizontal Rule 
These push the content afterwards onto a new line. These are empty elements.

    <p>Would you please<br /> just let me<br /> finish this sentence<br> on one line?</p>
    <p>I don't like the sentence below me.</p>
    <hr>
    <p>What is that line doing there?</p>

<p>Would you please<br /> just let me<br /> finish this sentence<br> on one line?</p>
<p>I don't like the sentence below me.</p>
<hr>
<p>What is that line doing there?</p>

## Whitespace Collapsing
Unless you specify, simply pressing enter on a line will not create a new line on the web page. In addition, any amount of spaces will simply show a single space. This is known as whitespace collapsing.

    <p>This is an example of whitespace collapsing</p>
    <p>This       is an example of whitespace collapsing</p>
    <p>This is an           example of whitespace collapsing</p>
    <p>This is an example of           whitespace 
            collapsing</p>

<p>This is an example of whitespace collapsing</p>
<p>This       is an example of whitespace collapsing</p>
<p>This is an           example of whitespace collapsing</p>
<p>This is an example of           whitespace collapsing</p>

## Quotations
Blockquotes are block elements (as you can assume), and regular quotes are inline items, like strong and em.

    <blockquote>
    <p>Well, the way they make shows is, they make one show. That show's called a pilot. Then they show that show to the people who make shows, and on the strength of that one show they decide if they're going to make more shows. Some pilots get picked and become television programs. Some don't, become nothing. She starred in one of the ones that became nothing.</p>
    </blockquote>
    <p>Samuel L. Jackson said <q>English, mother! Do you speak it?!<q></p>

<blockquote>
  <p>Well, the way they make shows is, they make one show. That show's called a pilot. Then they show that show to the people who make shows, and on the strength of that one show they decide if they're going to make more shows. Some pilots get picked and become television programs. Some don't, become nothing. She starred in one of the ones that became nothing.
  </p>
</blockquote>

<p>Samuel L. Jackson said <q>English, mother! Do you speak it?!<q></p>



## Abbreviations and Acronyms 
These must contain a title attribute. What is contained in these attributes will be shown in a tooltip when you hover over the element.

    <p><abbr title="Hyper-text markup language">HTML</abbr> is a term you all should be familiar with by now.</p>
    <p><abbr title="Doctor">Doc.</abbr>, <abbr title="professor">Prof.</abbr>, and <abbr title="mister">MR.</abbr> should also be familiar to you.</p> 

<p><abbr title="Hyper-text markup language">HTML</abbr> is a term you all should be familiar with by now.</p>
<p><abbr title="Doctor">Doc.</abbr>, <abbr title="professor">Prof.</abbr>, and <abbr title="mister">Mr.</abbr> should also be familiar to you.</p> 


## Citations and Definitions
Citations are used for sources that you are not your own.

    <p><cite>Flowers for Algernon</cite> was a book I read last semester for English. It was really good.</p>

<p><cite>Flowers for Algernon</cite> was a book I read last semester for English. It was really good.</p>   

Definitions are used for important terms.

    <p><dfn>HTML</dfn> is a term you should definitely be able to define by now. So is <dfn>CSS</dfn>.</p>

<p><dfn>HTML</dfn> is a term you should definitely be able to define by now. So is <dfn>CSS</dfn>.</p>

## Addresses 
Simply contain information about your address and contact information. This is an example of semantic markup.

    <address>
        <p><a href="mailto:pliu7@binghamton.edu">pliu7@binghamton.edu</a></p>
        <p>20 Hawley Street</p>
        <p>Binghamton, NY 13901</p>
    </address>

<address>
  <p><a href="mailto:pliu7@binghamton.edu">pliu7@binghamton.edu</a></p>
  <p>20 Hawley Street</p>
  <p>Binghamton, NY 13901</p>
</address>

## Changes to Content - Deletions, Insertions, and Strikethroughs
You can bring to notice changes in your content, like awesome price cuts or mistakes you made.

    <p>My favorite fruits are <del>apples</del> <ins>bananas</ins>!</p>
    <p>The price of the Moto X: <br />
          <s>was $499</s><br />
          now $349!
    </p>

<p>My favorite fruits are <del>apples</del> <ins>bananas</ins>!</p>
<p>The price of the Moto X: <br />
    <s>was $499</s><br />
    now $349!
</p>


# Lists!
Lists are comprised of two types of elements: the list itself and the list items with in the list. When you enclose list items within a list, they will automatically format. You can also nest other types of elements within a list, like paragraphs or headers.

## Ordered Lists 
As the name suggests, lists all of its items in numerical order.

    <p>These are a few of my favorite things (ranked from most favorite to least favorite):
    <ol>
      <li>Bubble baths</li>
      <li>Teaching web development</li>
      <li>Picking things up and putting them down</li>
      <li>Espresso</li>
      <li>Oxford shirts from Uniqlo</li>
    </ol>

<p>These are a few of my favorite things (ranked from most favorite to least favorite):</p>
<ol>
  <li>Bubble baths</li>
  <li>Teaching web development</li>
  <li>Picking things up and putting them down</li>
  <li>Espresso</li>
  <li>Oxford shirts from Uniqlo</li>
</ol>

## Unordered Lists 
These lists simply add a bullet next to each item.

    <p>Shopping List</p>
    <ul>
      <li>Spinach</li>
      <li>Greek yogurt</li>
      <li>Five <abbr title="pounds">lbs.</abbr> of chicken breast</li>
      <li>Whole Wheat Pasta</li>
      <li>Beer from Wegman's</li>
    </ul>

<p>Shopping List</p>
<ul>
  <li>Spinach</li>
  <li>Greek yogurt</li>
  <li>Five <abbr title="pounds">lbs.</abbr> of chicken breast</li>
  <li>Whole Wheat Pasta</li>
  <li>Beer from Wegman's</li>
</ul>

## Definition Lists 
These are used for definitions, and are a bit different from normal lists. Each definition should contain a definition term and a definition definition (yes, that is what we will call it) associated with it. These element should be adjacent to each other.

    <dl>
      <dt>HTML</dt>
      <dd>Stands for Hyper-text Markup Language. It is what gives structure to the content in webpages.</dd>
      <dt>CSS</dt>
      <dd>Stands for Cascading Style Sheets. It is what makes websites look pretty.</dd>
      <dt>Javascript</dt>
      <dd>A programming language that can be used on the front-end to create interactive website and also on the back-end to create web applications.</dd>
    </dl>

<dl>
  <dt>HTML</dt>
  <dd>Stands for Hyper-text Markup Language. It is what gives structure to the content in webpages.</dd>
  <dt>CSS</dt>
  <dd>Stands for Cascading Style Sheets. It is what makes websites look pretty.</dd>
  <dt>Javascript</dt>
  <dd>A programming language that can be used on the front-end to create interactive website and also on the back-end to create web applications.</dd>
</dl>

## Nested Lists 
You can put lists inside of lists! Listception!

    <p>List of Movies Where Leonardo DiCaprio:</p>
    <ul>
    <li>
      <p>Is arrested for fraud:</p>
      <ol>
        <li>The Wolf of Wall Street</li>
        <li>Catch Me If You Can</li>
      </ol>
    </li>
    <li>
      <p>Finds himself in the ocean:</p>
      <ol>
        <li>Inception</li>
        <li>Titanic</li>
      </ol>
    </li>
    <li>
      <p>Plays essentially the same character:</p>
      <ol>
        <li>Inception</li>
        <li>Shutter Island</li>
      </ol>
    </li>
    </ul>

<p>List of Movies Where Leonardo DiCaprio:</p>
<ul>
  <li>
    <p>Is arrested for fraud:</p>
    <ol>
      <li>The Wolf of Wall Street</li>
      <li>Catch Me If You Can</li>
    </ol>
  </li>
  <li>
    <p>Finds himself in the ocean:</p>
    <ol>
      <li>Inception</li>
      <li>Titanic</li>
    </ol>
  </li>
  <li>
    <p>Plays essentially the same character:</p>
    <ol>
      <li>Inception</li>
      <li>Shutter Island</li>
    </ol>
  </li>
</ul>

Now that we've learned about these elements, we will use them for your own personal benefit...not in an evil way. 

# Work on Your Portfolio!
- Create a Level 1 Header with your name (because you are the most important person on your website)
- Create more headers on what you think you should highlight on your webpage (education, work experience, interests, skills, etc...) and write paragraphs about those things.
- Write a basic cover letter/mission statement/goals/etc.
- Create a contact me portion of the website and add an address section.
- Create a list of your skills, things you are interested in.

## Extra Stuff
- Add your favorite inspirational quote. Or a quote you made or believe in that you can put into a small mission statement.
- Test out the whitespace collapsing. For example, if you want to make something more readable in your HTML, you can put words from the same paragraph on a newline.

# Finally, some style!

# Introduction to CSS
As you may have notice, your page looks pretty boring at this point, and it probably looks exactly the same as the person sitting next to you. That's because this is the default style for HTML. We are going to change that using CSS to style our pages.

CSS stands for Cascading Stylesheets. We will explain the Cascading part later, but first, we'll talk about the stylesheet part. 

CSS applies rules for the elements in HTML and allow us to change things like font, color, size, and spacing. Most of these changes are attributes we can change in HTML, but this just makes everything easier and more maintable. 

CSS is similar to HTML in that it is a text file that is understood by the web browser, and instead of being saved as a .html file, it is saved as a .css file. 

## CSS Selectors, Properties, and Values
Here's an example we saw earlier:

    <h1 font-size="36px;">This header will be 36px. That's pretty big.</h1>
    <p color="red;">This is a red sentence, because I'm different.</p>

<h1 font-size="36px">This header will be 36px. That's pretty big.</h1>
<p style="color:red">This is a red sentence, because I'm different.</p>

<hr>

Now imagine we wanted all the headers to have a font size of 36px and all the paragraphs to be red. We wouldn't want to do that for a hundred of these, would we? CSS makes this easy by allowing us to choose what type of elements we want, and what rules or attributes we want to apply for that. So instead of setting the attributes for each element individually, we can set the rules in a CSS file:

In the HTML file:

    <h1>This header will be 36px. That's pretty big.</h1>
    <p>This is a red sentence, because I'm different.</p>
    <h1>This header will be 36px. That's pretty big.</h1>
    <p>This is a red sentence, because I'm different.</p>
    <h1>This header will be 36px. That's pretty big.</h1>
    <p>This is a red sentence, because I'm different.</p>

<h1>This header will be 36px. That's pretty big.</h1>
<p>This is a red sentence, because I'm different.</p>
<h1>This header will be 36px. That's pretty big.</h1>
<p>This is a red sentence, because I'm different.</p>
<h1>This header will be 36px. That's pretty big.</h1>
<p>This is a red sentence, because I'm different.</p>

In the CSS file:

    h1 {
      font-size: 36px;
    }
    p {
      color: red;
    }

Each declaration follows the same format: 

    selector {
        property: value;
    }

The selector is the element you want to target, the property is the attribute of the element you want to change, and value is what you want to change it to.

## How does the HTML file know about the CSS file?
Good question. For those who actually asked it.
There are two ways of doing this: we can embed it in the HTML file or we can put it in a separate .css and tell the HTML file about it.

### Internally
Since CSS will not be shown within the HTML file, we put it in the head tag, in its own element, appropriately called "style". This is what it would look like.

    <head>
      <style>
        h1 {
          font-size: 36px;
        }
        p {
          color: red;
        }
      </style>
    </head>

However, once you create more CSS rules, it gets messier. This is good if we want to add minor changes to a single webpage, but the better way is to create a separate CSS file.

## Externally
Create a separate file called "styles.css" (or anything that you want), and add the CSS. This needs to be in the same folder as the HTML file you are using.

    h1 {
      font-size: 36px;
    }
    p {
      color: red;
    }

Then in your HTML file, add this line:

    <link href="styles.css" rel="stylesheet" type="text/css">

The href refers to the CSS file you want to use, rel tells the file what the relationship between the two files are, the type is text/css.

## Types of Selectors
- Universal: * (all elements)
- Type element: h1, p, ul (which element)
- Class: .class, p.class (elements with a class attribute)
- Id: #id, p#id (elements with an ID attribute)
- Child: parent > child (p after an h1)
- Descendant: element descendant (span within a p)
- Adjacent sibling: h1+p (elements right next to each other)
- General sibling: h1~p ()

## Why are they Cascading?
CSS have a hierarchy within the rules. It's a bit like being the last kid picked in gym class.

### Last Rule Takes Precendence
CSS:

    h1 {
      font-size: 1000px;
    }
    h1 {
      font-size: 8px;
    }
    
HTML:

    <h1>I am going to be a tiny header.</h1>

### Specificity Takes Precedence
Specificity Takes Precedence
CSS:

    p {
      color: red;
    }
    p.pretty {
      color: cyan;
    }
    
HTML:

    <p class="pretty">I feel pretty</p> 

## Inheritance
Some properties are inherited, some are not inherited. For example, if you want to set what font the entire page will use, you don't want to set that for headers, paragraphs, strong, em, etc. You would want to set it once. You can do that in the body.
Other things are not. For example, if you don't want a border around every element in the body.

# CSS Color
There are multiple ways of specifying color in CSS.
One way is through the predefined name for a color. You can Google these.

    body {
      color: red;
    }

Another way is to use a hex-code. I don't want to go into too much detail about these, but these specify the amount of red, green, and blue in the color:

    body {
      color: #FAFAFA;
    }

There is also another way to specify the amount of red, green, and blue in a color. These values range from 0 to 255.

    body {
      color: rgb(100,100,100)
    }

We can also define a color using hue, saturation, and lightness:

    body {
      color: hsl(0, 0%, 78%);
    }
    
Hue is expressed as an angle from 0 to 360, and saturation and lightness are both expressed in percentages.

There are also two types of color we can specify: foreground color and background color.
Foreground color is simply named color. This changes the color of the text.

    color: red;

Background color is called background-color. The changes the color behind the text.

    background-color: blue;

# CSS Text Properties
## Font
### font-family and font-face
This allows you to specify which font you would like to use. It is important to list more than one font in the case that the font you specified is not installed on the user's machine.

Using font-family tells the browser to look for the specified font on the user's computer.

    body {
      font-family: Helvetica, Arial, sans-serif;
    }

Specifying a font-face lets use choose a font, given we know where to get it. It is commonly used for web fonts, like Google Fonts. Here is an example of how to include a Google font:

    @font-face {
      font-family: 'Open Sans';
      src: url('http://fonts.googleapis.com/css?family=Open+Sans');
    }

You can specify the font name and provide a URL for where to find the font.
Then you can use that font in the font-family property:

    body {
      font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    }

There is also another way to do this that is specified on the Google Fonts website.
Include this in the head tag of the HTML page:

    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>

This takes care of setting @font-face in your CSS. Then you can continue to do:

    body {
      font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    }

### font-size
There are three ways of specifying the font size, and these measurements are also used in different properties such as the height and width of other elements

We can use pixels.

    body {
      font-size: 16px;
    }

We can also use percentages and ems, which are relative to the size of body font.

    font-size: 200%; /* 32px */
    font-size: 1.5em; /* 24px */

### font-weight
There are five different values for the weight of a font. 

    .font-weight {
      font-weight: bold; 
      /* font-weight: normal; */
      /* font-style: normal; */
      /* font-style: italic; */
      /* font-style: oblique; */
    }

## Kerning and Leading
### line-height
Kerning describes the spacing between the lines of text.

    .line-height {
      line-height: 1.4em;
    }

### letter-spacing
Leading describes the spacing between letters.

    .letter-spacing {
      letter-spacing: 0.2em;
    }

### word-spacing
Tracking describes the spacing between words.

    .word-spacing {
      word-spacing: 1em;
    }

## Alignment
### text-align
This is the horizontal alignment of text on the page.

    .text-align {
      text-align: left;
      /* text-align: right; */
      /* text-align: center; */
      /* text-align: justify; */
    }

### vertical-align
This is the vertical alignment of text on the page.

    .vertical-align {
      /* vertical-align: baseline; */
      /* vertical-align: sub; */
      /* vertical-align: super; */
      /* vertical-align: top; */
      /* vertical-align: text-top; */
      /* vertical-align: middle; */
      /* vertical-align: bottom; */
      /* vertical-align: text-bottom; */
    }

## Other Stuff
### text-transform
We can easily change the case of text using CSS.

    .text-transform {
      text-transform: uppercase;
      /* text-transform: lowercase; */
      /* text-transform: capitalize; */
    }

### text-decoration
We can also add decoration to text easily.

    .text-decoration {
      text-decoration: none;
      /* text-decoration: underline; */
      /* text-decoration: overline; */
      /* text-decoration: line-through; */
    }

### text-shadow
This allows us to add a drop shadow behind the text, which just creates a copy of the text at the specified location relative to the text and in the specified color. This property is a bit more complicated than the others because it takes four values: three lengths that tell us about the position, and the color of the drop shadow.

First value: how far left or right
Second value: how far up or down
Third value (optional): amount of blur
Fourth value: color

    p.shadow {
      text-shadow: 1px 1px 5px #111111;
    }


## Pseudo Elements
Pseudo elements can let us pick out certain parts of text, and style our interactions with links and other elements.

### first-letter and first-line
As the name suggests, it will let us pick out the first letter or first line from a body of text.

    p.intro:first-letter {
      font-weight: 48px;
    }
    p.intro:first-line {
      font-weight: bold;
    }

### link, visited
These let you choose links that have been visited and links that haven't been visited.

    a:link {
      color: gray;
    }
    a:visited {
      color:blue;
    }

### hover, active, focus
hover is used when the mouse is hovering over an element.

    h1:hover {
      font-size: 12px;
    }
    
Active is used when the element is being used by the user. This is used for links or buttons.

    a:active {
      color: red;
    }
    
Focus is where the focus is. You think about when you press tab on a website to go through a form, this is where the focus lies.

    input:focus {
      border: 1px red;
    }

# CSS List Properties
## The Style of the Bullets
You can change what the bullets next to list items look like.

    .unordered1 li {
      list-style-type: none;
    }
    .unordered2 li {
      list-style-type: disc; 
    }
    .unordered3 li {
      list-style-type: circle; 
    }
    .unordered4 li {
      list-style-type: square; 
    }
    .unordered5 li {
      /* you can also add images for bullets */
      /* uncomment below for kitty bullets */
      list-style-image: url("http://placekitten.com/g/10/10"); 
    }

## How to Count List Items
Don't like numbers? We have some options for you.

    .ordered1 li {
    list-style-type: decimal;
    }
    .ordered2 li {
    list-style-type: decimal-leading-zero; 
    }
    .ordered3 li {
    list-style-type: lower-alpha; 
    }
    .ordered4 li {
    list-style-type: upper-alpha; 
    }
    .ordered5 li {
    list-style-type: lower-roman; 
    }
    .ordered6 li {
    list-style-type: upper-roman; 
    }

## Changing the Position of the Bullets
The bullets can either be inside the line or outside the line.
EXAMPLE ONE

    .exampleOne {
      /* can position where the markers are */
      list-style-position: inside;
    }

EXAMPLE TWO

    .exampleTwo {
      list-style-position: outside;
    }

## Shorthand
All of this can be done in short hand using list-style

    list-style: inside disc;

# Work on your portfolios!
- Find a font or two that you'd like to use on Google fonts or any other webfont website, and use them in your website.
- Pick out a color scheme for your website.
- Place with any other CSS properties you'd like to.

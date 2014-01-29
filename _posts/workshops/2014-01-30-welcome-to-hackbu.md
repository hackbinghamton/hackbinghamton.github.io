---
layout: notes

title: Welcome to HackBU
description: Learn about HackBU and the topics we will cover. We'll explain the difference between HTML, CSS, JavaScript, Ruby, and front-end vs. back-end development with an interactive demo.
time: Jan. 30 at 8 p.m.
location: LH 14
semester: Spring
week: 0

date: '2014-01-40T20:00:00-05:00'
permalink: /workshops/2014/spring/welcome-to-hackbu/
---
# Parts of the Web
## IP Address
Is an address/phone number for your computer. Consists of four sets of octets (256 numbers, from 0-255). It's the way that your computer knows what computer to ask for information from.
Since the internet and the number of devices are growing, we need a new version of IP address, now IPv6 (vs current IPv4).

2001:cdba:0000:0000:0000:0000:3257:9652

IPv4: 4,294,967,296 different IP addresses

IPv6: 340,282,366,920,938,463,463,374,607,431,768,211,456 IP addresses

## Domain and DNS
If your website is like an address, the **DNS** (*Domain Name Server*) is like a phonebook for the internet. You won't remember an IP address (like how most of us don't remember our own phone numbers), but instead use a domain name like *google.com*. They are just a bunch of servers that keep record of domain names and IP address all over the internet. For example, if you want to visit Facebook, you could visit *223.172.190.38* or you could visit its domain name at facebook.com. It will talk to the computer at *223.172.190.38* and ask for that web page.

## Web Server
Web servers are computers that can be accessed through the internet. Photo of what servers look like. They are a computer without a monitor or a keyboard or mouse, and it's about the size of a laptop. It communicates through the internet. 

Process! When you go to a website, Google.com

1. Browser sends out a request for the web page
2. Web server receives request and puts together the right parts
3. Web server sends back a web page

Like ordering take-out food.

Almost any computer can be used as a web server, as long as you have the right software installed that will listen in for step 2. Typical web server is different, as mentioned above.

# Technologies We Will Be Learning
## HTML
HTML is the language we use when we want to add structure to our website. 
When you visit a website, there are clear distinctions between parts of the website, like headlines and paragraphs. Each item has its own HTML tag, which look like this.

  <h1>This is a header.</h1>
  <p>This is a paragraph.</p>

<h1>This is a header.</h1>
<p>This is a paragraph.</p>

HTML lets you describe things like paragraphs, audio, video, lists, articles, images, emphasis, button. 

## CSS
HTML tells the browser what the structure and different parts of the page are. CSS is what makes websites pretty and adds style to them. You can control the color, font styles, size, etc.

If you wanted to change the font and color of a paragraph:
  
  p {
    font-family: 'Helvetica'; 
    background-color: red;
  }

## Javascript
Javascript and a programming language that makes websites interactive. It is responsible for things like Google's autocomplete and search suggestion feature, and is the reason you don't necessarily have to refresh your browser when information gets updated on your Twitter or Facebook. 

It is also used for animation and can even be used to built games, like Google's [Chrome Racer](http://g.co/racer/).

One of the very few programming languages that work in your browser. Once a toy, but now very serious. Used for node.js for server side, and even for full-stack (MeteorJS).

## Ruby
Ruby was created in 1995 in Japan by Yukihiro Matsumoto (MATZ!), who felt that programming languages were too focused on machines and not very human friendly. For example, C.

Let's say you were Santa Claus and wanted to say "ho" three.

In many programming languages, you'd have to do this:

  for ($i = 0; $i < 3; $i++) {
    echo "ho";
  }

In Ruby!

  3.times do
    print "ho";
  end

What is great about Ruby is that even if you weren't a programmer, you could easily read this and tell me what it does.

Ultimately, the language became very popular with Ruby on Rails in 2005, a framework that made it easier to create web applications. 

Twitter and Hulu both used Ruby on Rails, although Twitter had issues with scaling (because it's Twitter), and switched over to Java.


## Rails
Awesome framework for building web applications. Web applications are different from web sites. Web sites contain static and unchanging content, whereas as web applications allow you to interact directly with the data. Web applications let you do things like buy stuff, search, upload pictures, blog, etc. Rails makes it easy.

# Concepts
## Open Source
One of the best parts of being a developer. It is the practice of sharing how a computer program was made and allowing anyone to customize the program as they see fit. For example, Ruby on Rails is open source. So is mostly everything on github. You have a version of the program as well as the source code, and you can fix it if you find a problem.

For example, Photoshop is a closed-source project, because it isn't something you can tinker with, or make changes to, or add changes to.

However, WordPress and Mozilla are (open source and not-for-profit). They rely on a community of people who work on software out of the good of their hearts and the desire to contribute to a meaningful product.

GitHub is a huge platform that combines open source and social networking. Developers put source code and other developers in the community copy it (fork it), make changes, and submit them to the original creator to see if they want to use those changes. 

Perhaps the biggest example of open source technology we will be using in this class is using the Ruby on Rails framework to build our web applications.


## Frontend/Backend
<img src="http://4b93n32qwvjj3ddn5w3yhffoas6.wpengine.netdna-cdn.com/wp-content/uploads/2012/08/term-frontendvsbackend.jpeg">

Frontend is everything you see, which includes HTML/CSS/JavaScript. The backend is what makes a web application happen. A typical setup is an application, a web server, and a database. For example, when you are a booking a flight, you need to check prices, book itineraries, and charge credit cards. All that happens on the backend. A web server sends a note to the application that you want to see all the flight to Chicago. The application looks up the flights in the DB and puts together a web page that lists them. Sends that web page through the server.

Database stores your info. Could be MySQL, MongoDB, PostgreSQL. Server side languages could be Python, Ruby, PHP, or interestingly enough now, Javascript.

This is not very different from client-side and server-side. Just a difference in semantics. Front-end vs back-end describe WHAT the action is while server-side vs client-side describe WHERE the action is. 

## Responsive Design
Designing a web page to be easily viewed on multiple screen sizes. Relies on CSS3 media queries, which basically means that the web browser knows how big the screen is and will adjust accordingly. For examples, instead of seeing three columns on your screen, your phone will align them vertically for viewability.
Foundation and Bootstrap are two frameworks that are responsive. Really hard to create a responsive framework! Also open source.

## Full Stack
Technologies need to create your web product. For example, if someone asks you what your stack is, they want to know what you are using on the frontend or client-side and what you are using on the backend or server-side.


# Goals for the Semester
- A lot people have been asking me if this is something you will be able to put on your resume. Yes, we have been working very hard to ensure that you will have a certain level of proficiency to put these skills on your resume.
- Speaking of resumes, we will hit the ground running by working along with you to help you build your own personal landing page with your resume and portfolio. We have had amazing support and one of our partners will actually be providing us free web hosting, meaning you will actually have something on the web.
- You will build your own version of Twitter, or simply, a microblogging platform. You can easily shift the application to your own needs, for example, if you wanted to create the engine for your own blog.
- We want you to gain the basic skills to continue learning and to want to and to be able to be creative and build things.
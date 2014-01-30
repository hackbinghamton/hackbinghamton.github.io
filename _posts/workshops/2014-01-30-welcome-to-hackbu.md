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

# Welcome to HackBU

## Parts of the Web
Let’s kick off HackBU by diving into short lesson about the Internet and how it works.

### IP Addresses
Every computer connected to the Internet has an **IP address**. An IP address is a unique address that specifies where your computer is located in the network. There are different formats for specifying IP addresses, but the most common right now is IPv4 (which you've likely seen). IPv4 addresses consist of four sets of numbers (ranging from 0-255, inclusive), separated by periods (`192.168.2.1`, for example).

Since the Internet, and the number of devices connected to it, is growing incredibly quickly, we've technically run out of IPv4 addresses to assign to new devices connecting to the Internet (though this doesn't mean new devices can't connect — it's a bit more complicated than that). To combat this, a new version of IP addressing, IPv6, is gaining traction as servers and other devices get updated to use it instead. IPv6 addresses are more complicated (e.g. `2001:db8::ff00:42:8329`), but can support many more devices (2<sup>128</sup>, instead of IPv4's 2<sup>32</sup>).

### Domains and the DNS System
If an IP address is like your computer's home address, then **DNS servers** *(domain name system servers)* are like the Internet's address book. Instead of having to memorize IP addresses, the DNS system allows you to memorize web addresses like [`google.com`](http://google.com), which the servers then translates to IP addresses for your computer to connect to.

These domain name servers are computers dedicated to keeping records of domain names and IP addresses on the Internet. For example, you could visit Google at the IP address [`74.125.224.72`](http://74.125.224.72/) or the domain name [`google.com`](http://google.com/). Either way, your browser will talk to the computer at [`74.125.224.72`](http://74.125.224.72/) and ask for the web page.

### Web Servers
**Web servers** are computers that can be accessed through the Internet that run the services you use every day. They serve up web pages, store data in databases, run applications, etc.

Web servers are typically computers without monitors, keyboards, or mice and are controlled remotely. With the right software, any computer can be used as a web server.

### How It All Fits Together
When you visit Google, a few things happen:

1. Your web browser sends out a request for the web page at the IP address that [`google.com`](http://google.com/) maps to. This mapping is done with the help of DNS. 
2. A Google web server (they have thousands) receives the requests and processes it.
3. The web server sends back the requested resources.
4. The web browser processes the data it receives and puts the page together.

It’s like ordering take-out food: you make the request, and everything is assembled, prepared, and delivered to you.

## Languages We’ll Be Covering
The weekly HackBU workshops will cover the basics of web development, and slowly progress to more advanced topics. Here’s a quick overview of these topics:

### HTML
HTML is the language we use to add structure to our website. It defines the content of a web page, and how that web page should be laid out (roughly speaking). When you connect to a website, the website returns an HTML document which your browser then reads, parses, and renders to display to you.

Web pages often contain many different types of elements — headlines, paragraphs, likes, images, lists, tables, etc. These elements are specified in HTML with *tags*, bits of structured text that surround your content:

	<h1>This is a large header.</h1>
	<p>This is a paragraph.</p>

Most elements are specified by an opening tag (`<tag_name>`), and a closing tag (`</tag_name>`). Tags that don't surround text, or supply their own content (like images), often don't need a closing tag, or have one built in:

    <img src="http://placekitten.com/g/200/300" />

We'll dig deeper into HTML in the following workshops.

### CSS
HTML and CSS go hand in hand: HTML is all about the contents of a web page and its semantic structure, while CSS is all about how that content should be displayed to the user. CSS can specify colors, font styles, sizes, and more — really, anything to do with how a page should show up on your screen.

For example, the following CSS can change the font and color of a paragraph (the `<p>` tag):

	p {
            background-color: red;
            font-family: Helvetica, Arial, sans-serif;
	}

With that CSS enabled, all paragraphs by default would have a red background, and would be typeset in Helvetica, Arial, or another sans-serif font.

### JavaScript
JavaScript is a programming language that makes websites interactive. It powers features like Google’s search suggestions and is the reason you don’t necessarily have to refresh your browser when new posts appear on Twitter or Facebook. 

It is also used to animate web pages and can be used to build games like Google’s [Chrome Racer](http://www.chrome.com/racer).

JavaScript is incredibly powerful and one of the very few programming languages that work in the browser. (HTML is a markup language and CSS is a stylesheet language, but neither can be considered a true programming language, because they're not dynamic code.) It can also run on a server with new technologies like [node.js](http://nodejs.org/) and [Meteor](https://www.meteor.com/).

### Ruby
Ruby is a programming language created in 1995 by Yukihiro Matsumoto ("*Matz*"). He created the language because he believed that most programming languages (like C and C++) were too focused on being machine-friendly, and not human-friendly.

If you were Santa Claus, and wanted to say "ho" three times, many programming languages would force you to go about it approximately like this (PHP):

	for ($i = 0; $i < 3; $i++) {
		echo "ho";
	}

Instead, in Ruby, you can do this:

	3.times { print "ho" }

Even if you're not a programmer, it's clear that the Ruby code is much clearer and easier to read, and this is common of much of the Ruby code out there. The language is designed to be very readable.

### Ruby on Rails
[Ruby on Rails](http://rubyonrails.org/), a Ruby framework, makes it easier to create web applications. It was created in 2005 and helped popularize Ruby.

Web applications are much more powerful than basic (static) websites. They often let users create accounts, upload photos, make purchases, etc. Rails makes doing this easy by allowing you to run Ruby code on your server and by providing large amounts of functionality so you don't have to write the code yourself.

## Software Concepts
Here are some software concepts we’ll touch on throughout the semester:

### Open Source Software
Making your code open source is the practice of sharing how a computer program was made and allowing anyone to customize the code as they see fit (Ruby on Rails, for instance, is open source).

Photoshop is an example of a closed-source project. Adobe hasn't released the source code for Photoshop, so any given programmer can't look at the code or work on improving it and fixing its bugs.

WordPress and Mozilla, on the other hand, are two open source projects. They rely on a community of programmers with a desire to contribute to a meaningful product.

[GitHub](https://github.com/) is a large platform that combines open source and social networking. Developers can publicly share source code, allowing contributors to view it, copy it (known as forking), make changes, and submit them to the original creator. Our own site, [HackBU](https://github.com/HackBinghamton/HackBU), is an open-source project hosted on GitHub.

### Front-End Development vs. Back-End Development
Dynamic websites can be broken into two parts: the front-end and back-end.

The front-end is everything you can see. This includes HTML, CSS, and JavaScript; mostly markup with some code to make things functional on your screen.

The back-end does the heavy lifting. This typically includes a server-side language — like Python, Ruby, or PHP — and a database management system — like MySQL, MongoDB, or PostgreSQL — to perform all the tasks that are done on the server and not on your computer (looking up your account details, processing your web order, etc.).

### Responsive Design
Today, devices of all shapes, sizes, and resolutions connect to the Internet on a regular basis. In the past, websites often delivered content that was fixed in size (say, `800px x 600px`), made for small desktop monitors, and everyone visiting that website received the same content. However, a fixed resolution can seem tiny on today's huge monitors, or unusably large on our mobile phones. Luckily, with recent changes to HTML and CSS, it's easy to write responsive websites.

Responsive websites adapt to the width of the browser. They look great on *any* device with *any* width. There are three components to a responsive website: a fluid layout, flexible images and media, and media queries.

* **Fluid layout** — fluid layouts shrink and expand accordingly as you resize the browser. This is because fluid layouts use percentages instead of pixels for width values.
* **Flexible images and media** — images and media should resize to fit in the layout.
* **Media queries** — a (relatively new) feature in CSS that lets you change the page's style depending on width of the browser.

The [HackBU website](http://hackbu.org/) is responsive. Take a look at the website on your computer, then on your phone or tablet to see the difference! It's the same content, but displayed in a way that's more aware of the device you're using.

## Goals For the Semester
We will hit the ground running by helping you build a personal website with your resume and portfolio in the first few workshops.

You’ll then build a micro-blogging platform (*like Twitter!*) once we dive into Ruby and Ruby on Rails.

We want you to gain the basic skills to continue learning and to bring your ideas to life.

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

## Parts of the web

Let’s kick off HackBU by diving into short lesson about the internet and how it works.

### IP address

An **IP address** is a unique address for your computer. It consists of four sets of octets (256 numbers, from 0-255). It’s how your computer knows where to connect to when loading a website.

Since the internet and the number of devices are growing, a new version of IP address was created. There are 2<sup>128</sup> possible IPv6 addresses compared to 2<sup>32</sup> IPv4 addresses.

### Domain and DNS

Think of an IP address as a phone number and the **DNS** *(domain name server)* as a phone book for the internet. You don’t need to memorize IP addresses (just like phone numbers) since the DNS can look it up when you type an address like *google.com*. 

These domain name servers are are computers dedicated to keeping records of domain names and IP addresses on the internet. For example, you could visit Google at the IP address [`74.125.224.72`](http://74.125.224.72/) or the domain name [google.com](http://google.com/). Either way, your browser will talk to the computer at [`74.125.224.72`](http://74.125.224.72/) and ask for the web page.

### Web server

**Web servers** are computers that can be accessed through the internet. They are typically computers without monitors, keyboards, or mice and are controlled remotely.

With the right software, any computer can be used as a web server.

### How it all fits together

When you visit Google, a few things happen:

1. Your web browser sends out a request for the web page at the IP address that [google.com](http://google.com/) maps to. This mapping is done with the help of DNS. 
2. A Google web server (they have thousands) receives the requests and processes it.
3. The web server sends back the requested resources.
4. The web browser processes the data it receives and puts the page together.

It’s like ordering take-out food.


## Languages we’ll be covering

The weekly HackBU workshops will cover the basics and progress to advanced topics. Here’s a quick overview of these topics.

### HTML

HTML is the language we use to add structure to our website.

Websites typically contain elements such as headlines, paragraphs, links, images, lists. Each of these elements have their own HTML tag. 

	<h1>This is a large header.</h1>
	<p>This is a paragraph.</p>

Some elements, such as images, don't have closing tags.

    <img src="http://placekitten.com/g/200/300">

We'll dig deeper in the following workshops.

### CSS

If HTML is all about markup, CSS is all about style. You can control the color, font styles, size, etc.

For example, the following CSS can change the font and color of a paragraph:
  
	p {
        background-color: red;
        font-family: Helvetica, Arial, sans-serif;
	}

### JavaScript

JavaScript is a programming language that makes websites interactive. It powers features like Google’s search suggestions and is the reason you don’t necessarily have to refresh your browser when new posts appear on Twitter or Facebook. 

It is also used to animate web pages and can be used to build games such as Google’s [Chrome Racer](http://www.chrome.com/racer).

JavaScript is incredibly powerful and one of the very few programming languages that work in the browser. (HTML is a markup language and CSS is a stylesheet language.) It can also run on a server with new technologies such as [node.js](http://nodejs.org/) and [Meteor](https://www.meteor.com/).

### Ruby

Ruby was created in 1995 in Japan by Yukihiro Matsumoto *(MATZ!)*. He believed programming languages, such as C, were too focused on machines and not human friendly.

Let’s say you were Santa Claus and wanted to say "ho" three.

In many programming languages, you’d write something like this:

	for ($i = 0; $i < 3; $i++) {
		echo "ho";
	}

In Ruby, you do this:

	3.times do
		print "ho";
	end

Even if you aren’t a programmer, you can easily read and understand the Ruby code.

### Rails

[Ruby on Rails](http://rubyonrails.org/), a Ruby framework, makes it easier to create web applications. It was created in 2005 and helped popularize Ruby.

Web applications, unlike basic (static) websites, are more powerful. They often let users create accounts, upload photos, make purchases, etc. Rails makes this easy.


## Concepts

Here are some concept’s we’ll touch on throughout the semester.

### Open Source

It is the practice of sharing how a computer program was made and allowing anyone to customize the program as they see fit. For example, Ruby on Rails is open source.

Photoshop is an example of a closed-source project. You can’t see the source code that powers the program.

WordPress and Mozilla, on the other hand, are two open source projects. They rely on a community of programmers with a desire to contribute to a meaningful product.

[GitHub](https://github.com/) is a large platform that combines open source and social networking. Developers can publicaly share source code, allowing contributors to view it, copy it (known as forking), make changes, and submit them to the original creator. 

[HackBU](https://github.com/HackBinghamton/HackBU) is an example of an open source project.

### Front end vs. back end

Dynamic websites can be broken into two parts: the front end and back end.

The front end is everything you can see. This includes HTML, CSS, and JavaScript. 

The back end does the heavy lifting. This typically includes a server-side language such as Python, Ruby, or PHP and a database management systems such as MySQL, MongoDB, or PostgreSQL.

### Responsive design

Responsive websites adapt to the width of the browser. They look great on *any* device with *any* width. There are three components to a responsive website: a fluid layout, flexible images and media, and media queries.

* **Fluid layout** - Fluid layouts shrink and expand accordingly as you resize the broswer. This is because fluid layouts use percentages instead of pixels for width values
* **Flexible images and media** - Images and media should resize to fit in the layout.
* **Media queries** - A (relatively new) feature in CSS that lets you change the page’s style depending on width of the browser.

The [HackBU website](http://hackbu.org/) is responsive. Take a look at the website on your phone and tablet!

## Goals for the Semester

We will hit the ground running by helping you build a personal website with your resume and portfolio in the first few workshops.

You’ll then build a a microblogging platform *(like Twitter!)* once we dive into Ruby and Ruby on Rails.

We want you to gain the basic skills to continue learning and to bring your ideas to life.
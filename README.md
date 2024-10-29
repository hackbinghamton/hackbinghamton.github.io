# HackBU

A student-run organization at Binghamton University created to foster a community of individuals who solve problems through the innovative use of technology.

## Install

In addition to cloning the HackBU repository, you'll need a few things to run HackBU locally:

1. **Ruby** - Ruby is a programming language powering our build tools. Ideally you should install the version in [`.ruby-version`](.ruby-version). On *nix, you can use [asdf](https://asdf-vm.com/) to manage Ruby versions:
	```
	# From the project repo:
	$ echo "legacy_version_file = yes" > ~/.asdfrc
	$ asdf install
	```
	This will build Ruby and cause your fans to ramp up, so maybe don't do this in class.

2. **Bundler** - Ruby's package manager. Comes preinstalled with Ruby as `bundle`.

3. **Jekyll** - Run the command `bundle install` in the project directory to download and install Jekyll. (~~Try using `sudo bundle install` if you run into problems.~~ <-- do NOT do this!!! you will litter your system with files, if it even lets you)

You can start the Jekyll server with `bundle exec jekyll serve --watch`. See the [Jekyll documentation ](http://jekyllrb.com/docs/home/) for more information.

## Contributing

Making a change to the website? Fork the repository (if you're not HackBU staff) and [submit a pull request through GitHub](https://help.github.com/articles/using-pull-requests)!

A HackBU staff member will review the pull request, leave comments, and decide whether or not to merge.


Producing thumbnails for the photo galleries:

```
$ magick mogrify -resize 300x300^ -gravity Center -extent 300x300  -path $PATH_TO_THUMB_DIR *.jpg
```

## License

The contents of this repository are [released under the MIT License](http://hackbu.org/LICENSE).

Contact [hello@hackbu.org](mailto:hello@hackbu.org) with questions.

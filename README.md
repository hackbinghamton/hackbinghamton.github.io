# HackBU

A student-run organization at Binghamton University created to foster a community of individuals who solve problems through the innovative use of technology.

## Install

The best way to run the HackBU website locally is to use a container provider like `podman` or `docker`. This allows you to isolate the necessary tools from your host system, preventing dependency conflicts and guaranteeing reproducibility across installations.
1. Install your choice of provider, as well as `podman-compose` or `docker-compose`.
2. Clone the project directory
3. Navigate to the project directory and run `podman compose up -d`. This will build and start the container.
4. In a browser, go to 127.0.0.1:4000 to interact with the site. Changes to the project directory will be reflected in the site.
5. Run `podman compose down` in the project directory to stop the local server.

If you change the Gemfile or Gemfile.lock, run `podman compose up -d --build --force-recreate` to regenerate the container image.

### Manual install
In addition to cloning the HackBU repository, you'll need a few things to run HackBU locally:

1. Install the necessary dependencies to build Ruby: https://github.com/rbenv/ruby-build/wiki#suggested-build-environment.
2. **Ruby** - Ruby is a programming language powering our build tools. Ideally you should install the version in [`.ruby-version`](.ruby-version). On *nix, you can use [asdf](https://asdf-vm.com/) to manage Ruby versions:
	```
	$ asdf plugin add ruby https://github.com/asdf-vm/asdf-ruby.git
	# From the project repo:
	$ echo "legacy_version_file = yes" > ~/.asdfrc
	$ asdf install
	```
	This will build Ruby and cause your fans to ramp up, so maybe don't do this in class.

3. **Bundler** - Ruby's package manager. Comes preinstalled with Ruby as `bundle`.

4. **Jekyll** - Run the command `bundle install` in the project directory to download and install Jekyll. (Do not run this command as root, even if you have permissions issues)

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

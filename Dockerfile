FROM docker.io/library/ruby:3.3
COPY Gemfile /home/Gemfile
WORKDIR /home
RUN bundle install
EXPOSE 4000
VOLUME /hackbu
WORKDIR /hackbu
ENTRYPOINT bundle exec jekyll serve --watch

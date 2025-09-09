FROM docker.io/library/ruby:3.3

COPY Gemfile Gemfile.lock ./

RUN gem install bundler:2.6.2 && \
    bundle install

EXPOSE 4000

VOLUME /hackbu
WORKDIR /hackbu

ENTRYPOINT ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--watch", "--force_polling"]

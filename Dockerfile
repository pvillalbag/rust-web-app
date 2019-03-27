FROM ubuntu:18.10

ENV TERM=xterm

ENV ROCKET_ENV=prod

RUN apt-get update \
    && apt-get install libmysqlclient-dev curl build-essential -y \
    && curl -sf -L https://static.rust-lang.org/rustup.sh | sh -s -- -y

RUN echo "export PATH="$HOME/.cargo/bin:$PATH"" >> ~/.profile
     
RUN $HOME/.cargo/bin/cargo install diesel_cli --no-default-features --force --features mysql   

RUN $HOME/.cargo/bin/rustup default nightly-2018-04-04

WORKDIR /app
ADD . .
ENV DATABASE_URL=url
RUN $HOME/.cargo/bin/cargo build --release
WORKDIR /app/target/release
CMD ["/app/target/release/./hero-api"]
FROM 52.18.239.125/rust-base as builder
RUN rustup default nightly-2018-04-04
WORKDIR /app
ADD . .
ENV DATABASE_URL=url
RUN cargo build --release

FROM ubuntu:18.10
WORKDIR /app
COPY --from=builder /app/target/release/hero-api .
COPY --from=builder /usr/lib/x86_64-linux-gnu/libmysqlclient* /usr/lib/x86_64-linux-gnu/
ENTRYPOINT ["/app/./hero-api"]
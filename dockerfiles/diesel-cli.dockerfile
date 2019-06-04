FROM 52.18.239.125/rust-base as builder

RUN cargo install diesel_cli \
    --no-default-features --force --features mysql

FROM ubuntu:18.10

COPY --from=builder /root/.cargo/bin/diesel /usr/local/bin/
COPY --from=builder \
    /usr/lib/x86_64-linux-gnu/libmysqlclient* \
    /usr/lib/x86_64-linux-gnu/

ENTRYPOINT [ "diesel" ]

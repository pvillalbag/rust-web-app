# Rust Application

Restful CRUD API for a managing heroes within our Database using Rocket and Diesel. Based on [this wonderful example](https://github.com/sean3z/rocket-diesel-rest-api-example.git).

## Requirements

1. Rust and Cargo - 1.27.0 (nightly)
```bash
$ rustup default nightly-2018-04-04
```

2. Diesel CLI and Dependencies 
```bash
 $ sudo apt-get install libpq-dev libsqlite3-dev libmysqlclient-dev -y
 $ cargo install diesel_cli --no-default-features --force --features mysql
 ```

3. Mysql - 5.7
   Check `docker-compose.yml`


## Steps to Setup

**1. Clone the application**

```bash
$ git clone https://github.com/mendrugory/rust-web-app
```

**2. Create DATABASE_URL environment variable**
```
$ export DATABASE_URL=mysql://user:password@127.0.0.1/heroes
```

**3. Run Database migration**
```bash
$ diesel migration run
```

**4. Build and run the app using cargo**

```bash
$ cargo build --release && cd target/release/
$ sudo ROCKET_ENV=prod ./hero-api
```

The app will start running at <http://localhost:80>.


## Explore Rest APIs

The app defines following CRUD APIs.

    GET /heroes
    
    POST /hero

    GET /hero/{heroId}
    
    PUT /hero/{heroId}
    
    DELETE /hero/{heroId}

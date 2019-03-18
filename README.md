# Rocket, Diesel, MySQL, Rest API Tutorial

Build Restful CRUD API for a managing heroes within our Database using Rocket and Diesel.

## Requirements

1. Rust and Cargo - 1.26.0 (nightly) - rustup default nightly-2018-04-04
sudo apt-get install libpq-dev libsqlite3-dev libmysqlclient-dev -y
1. Diesel CLI - 1.1.0 - cargo install diesel_cli --no-default-features --features mysql

2. Mysql - 5.x.x

## Steps to Setup

**1. Clone the application**

```bash
git clone https://github.com/sean3z/rocket-diesel-rest-api-example.git
```

**2. Create DATABASE_URL environment variable**
```
export DATABASE_URL=mysql://user:password@127.0.0.1/heroes
```

**3. Run Database migration**
```bash
diesel migration run
```

**4. Build and run the app using cargo**

```bash
cargo build --release && cd target/release/
sudo ROCKET_ENV=prod ./hero-api
```

The app will start running at <http://localhost:80>.

Alternatively, you can run the app in development mode -

```bash
cargo run
```

## Explore Rest APIs

The app defines following CRUD APIs.

    GET /heroes
    
    POST /hero
    
    PUT /hero/{heroId}
    
    DELETE /hero/{heroId}

You can test them using postman or any other rest client.

## Learn more

You can find the tutorial for this application on my blog -

<https://medium.com/p/1867308352d8/>

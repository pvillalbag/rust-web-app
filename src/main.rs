#![feature(plugin)]
#![plugin(rocket_codegen)]

extern crate rocket;
#[macro_use] extern crate rocket_contrib;
#[macro_use] extern crate serde_derive;
#[macro_use] extern crate diesel;

use rocket_contrib::{Json, Value};

mod db;
mod schema;

mod hero;
use hero::Hero;


#[get("/")]
fn read_all(connection: db::Connection) -> Json<Value> {
    Json(json!(Hero::read_all(&connection)))
}


#[post("/", data = "<hero>")]
fn create(hero: Json<Hero>, connection: db::Connection) -> Json<Hero> {
    let insert = hero.into_inner();
    Json(Hero::create(insert, &connection))
}

#[get("/<id>")]
fn read(id: i32, connection: db::Connection) -> Json<Value> {
    Json(json!(Hero::read(id, &connection)))
}

#[put("/<id>", data = "<hero>")]
fn update(id: i32, hero: Json<Hero>, connection: db::Connection) -> Json<Value> {
    let update = Hero { id: id, ..hero.into_inner() };
    Json(json!({
        "success": Hero::update(id, update, &connection)
    }))
}

#[delete("/<id>")]
fn delete(id: i32, connection: db::Connection) -> Json<Value> {
    Json(json!({
        "success": Hero::delete(id, &connection)
    }))
}

#[get("/")]
fn health(_connection: db::Connection) -> &'static str {
    "Up and Running !!!"
}

fn main() {
    rocket::ignite()
        .manage(db::connect())
		.mount("/health", routes![health])
        .mount("/hero", routes![create, update, delete, read])
        .mount("/heroes", routes![read_all])
        .launch();
}



#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        assert_eq!(1,1);
    }

    #[test]
    fn test2() {
        assert_eq!(2,2);
    }
}

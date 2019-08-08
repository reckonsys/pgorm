# pgorm

An ambitious PostgreSQL ORM in pure python 3.7+ using asyncio, dataclasses & type hints

# Why pgORM?

When building a typical web service with python, more often than not, one tends to choose an ORM for their data layer. These days, because of frameworks like Ember, React & Angular, developers often find themselves writing JSON endpoints more often than rendering a HTML page. Therein comes a need for serializers. After building a couple of dozens of webservices ourselves, we asked why do we need to keep defining the same data multiple times (once when defining your models, and then when defining serializers and then for defining forms)? Why not just define it once and use it everywhere?

# Why PostgreSQL?

PostgreSQL is another reason why we chose to write pgORM. Yes, we love PostgreSQL for multiple reasons. Inbuilt JSON fields, ability to inherit tables, extensions like PostGIS, zombodb, citus are few of the reasons why we love PostgreSQL. Other ORMs cannot take advantage of these features. Because in order to be able to be generic, you will have to compromise on a lot of amazing features that are only available in PostgreSQL. So we decided to write an ORM that is loyal to PostgreSQL.

# Why Dataclasses?

Dataclasses makes it easier for us to avoid writing serializers, validators and forms. Not many people are familiar with it now, but with python 2 nearing its end of life and people migrating to python 3, most of them will be familiar with our APIs in the future as it will just be an extension to dataclasses.

# Why Type Hints?

It's good to know what a function returns (or expects). Leads to readable code. We can automate documentations and autocompletion becomes easier.

# Why AsyncIO?

Performance.

# How do we get there?

* Understand postgreSQL (External data wrappers, table inheritance, extensions, yada yada yada)
* Understand dataclasses, type hints, lazy evaluation & asyncio
* Agree sensible defaults
* Implement

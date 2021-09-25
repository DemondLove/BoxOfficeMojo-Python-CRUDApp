# Box Office Mojo CRUD App

### Overview

Utilizing dataset sourced from BoxOfficeMojo (BOM) Python WebScraper, https://github.com/DemondLove/BoxOfficeMojo-Python-WebScraper, this CRUD App will be utilized as the backend APIs to access and manipulate the BOM dataset.

Source Dataset:
- id (int)
- Title (str)
- Distributor (str)
- Genre (str)
- MPAARating (str)
- ProductionBudget (str)
- ReleaseDate (str)
- Runtime (str)
- DomesticGross (str)
- ForeignGross (str)
- WorldwideGross (str)
- OpeningWeekendGross (str)
- OpeningWeekendTheaters (str)
- WidestTheaters (str)
- Genres (str)
- URL (str)

### BOM Crud Models

    Title
        id (int)
        Title (str)
        ProductionBudget (int)
        ReleaseDate (date)
        Runtime (int)
        DomesticGross (int)
        ForeignGross (int)
        WorldwideGross (int)
        OpeningWeekendGross (int)
        OpeningWeekendTheaters (int)
        WidestTheaters (int)
        Genres (str)
        URL (str)
        genre_id (int)
        distributor_id (int)
        mpaarating_id (int)

    Genre
        id (int)
        Genre (str)
    
    Distributor
        id (int)
        Distributor (str)
    
    MPAARating
        id (int)
        MPAARating (str)
* More descriptive information to be added to Genre, Distributor, MPAARating models, which will subsequently allow for more robust analytics.

### APIs

    GET (2)
        /titles -> get all titles w/ pagination
        /titles/{name} -> get single title
    POST -> create a new title
        /titles
    PUT
        /titles -> batch update all titles
        /titles/{name} -> update a single title
    PATCH
        /titles -> batch partial update all titles
        /titles/{name} -> partial update a single title
    DELETE
        /titles -> delete all titles
        /titles/{name} -> delete a single title

### Tech Stack

- Python
- Flask
- SQLAlchemy & Alembic
- Docker
- SQLite & MySQL
- AWS API Gateway
- AWS Lambda
- AWS RDS - MySQL

### TODO
Add:
- Add reset database migration
- OPTIONS endpoint
- API Documentation w/ Swagger
- Add Top X GET APIs

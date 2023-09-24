# How The Cookie Crumbles!

##  Girl Scout Troop Database in MongoDB

The Girl Scout Troop Database project was initiated with the objective of establishing a quick-solution database system that would facilitate data management for Girl Scout troops. In this repository, we have meticulously designed the database structure, including schema validation and relationships, crafted data generation processes, and developed a Python application for querying and interacting with the database. This project serves as a comprehensive pipeline, providing hands-on learning opportunities for mastering the fundamentals of both NoSQL and relational databases, while also gaining practical experience in writing complex queries to extract valuable insights from the data.

## How To Use

### Creating the MongoDB Database

1. Create a MongoDB database named "GirlScouts" in MongoDB Compass.
2. Import JSON schema documents to enforce data quality standards during data insertion.

### Crafting Cookie Types

To ensure data consistency and represent iconic Girl Scout cookies accurately, we've meticulously defined five cookie types:

- **Thin Mints**: A classic blend of sugar, cocoa, and mint oil.
- **Samoas**: A tropical blend of cocoa, coconut extract, sugar, and butter.
- **Tagalongs**: A peanut butter delight with cocoa, sugar, peanut oil, and peanut butter.
- **Trefoils**: Made from flour, sugar, butter, and vanilla extract.
- **Toffeetastic**: Composed of flour, sugar, butter, and toffee bits.


## Troops and Scouts

Our database employs an Entity-Relationship model to organize troop-related data efficiently. Troops serve as primary entities, connected to multiple scouts through a one-to-many relationship. Allotments and payments are linked to scouts and troops, facilitating the management of sales and finances. This structured approach ensures data integrity and empowers Girl Scout troops in their activities.

### Troop 1234

- Founded on September 1, 2022, in Long Beach.
- Comprises two scouts: Naomi Nagata and Grace Hopper.
- Troop Allotment on January 19, 2023.

### Troop 6789

- Established on January 1, 2023, in Cerritos.
- Includes two scouts: Barbara Liskov and Mary Sparck Jones.
- Two troop allotments on January 18, 2023, and February 15, 2023.


### Python Application

- A Python application utilizing the PyMongo library has been developed to facilitate database interaction.
- The application offers three main features:
    1. **Troop Lookup**: Retrieve detailed troop information, including scouts and adult volunteers.
    2. **Scout Lookup**: Access comprehensive details about a scout's profile, including associated adults and allotments.
    3. **Sales Report**: Generate sales summaries for troops using MongoDB's aggregation framework.

## Overview

The Girl Scout Troop Database showcases our proficiency in relational database design, encompassing various key aspects of data management:

- **Primary Keys**: These serve as unique identifiers for each record, ensuring data integrity and efficient retrieval.

- **Foreign Keys**: Establishing relationships between tables, we seamlessly connect troops with their scouts, allotments, and payments. This relational structure showcases our understanding of cardinality, ranging from one-to-many relationships (troops to scouts) to many-to-one relationships (scouts to troops).

- **Normalization**: Our design minimizes data redundancy, reducing storage overhead and the risk of inconsistencies. However, we also employ selective denormalization where necessary to optimize queries and enhance performance.

- **Data Cardinality**: We expertly handle various cardinalities within our schema, from one-to-many (troops to scouts) to one-to-one (scouts to payments). This demonstrates our nuanced grasp of data modeling concepts.

Our relational database, rooted in the principles of the Entity-Relationship model, not only streamlines data management but also ensures scalability, reliability, and performance optimization.


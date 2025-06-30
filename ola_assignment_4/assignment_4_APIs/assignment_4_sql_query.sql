CREATE DATABASE assignment_4_API;

USE assignment_4_API;

CREATE TABLE books (
    book_id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(250) NOT NULL,
    author VARCHAR(45) NOT NULL,
    genre VARCHAR(45) NOT NULL,
    year_published INT NOT NULL,
    binding_type VARCHAR(15) NOT NULL,
    pages INT NOT NULL,
    copies_available INT NOT NULL,
    PRIMARY KEY (book_id)
);

CREATE TABLE users (
    user_id INT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(45) NOT NULL UNIQUE,
    rented_book INT,
    CONSTRAINT fk_rented_book FOREIGN KEY (rented_book) REFERENCES books (book_id),
    PRIMARY KEY (user_id)
);

INSERT INTO
    books (
        title,
        author,
        genre,
        year_published,
        binding_type,
        pages,
        copies_available
    )
VALUES (
        'The Emperor of Gladness',
        'Ocean Vuong',
        'Literary',
        2025,
        'hardback',
        416,
        10
    ),
    (
        'Audition',
        'Katie Kitamura',
        'Literary',
        2025,
        'hardback',
        208,
        3
    ),
    (
        'Resist: How a Century of Young Black Activists Shaped America',
        'Rita Omokha',
        'Non-Fiction',
        2024,
        'hardback',
        352,
        4
    ),
    (
        'Crossroads of Ravens',
        'Andrzej Sapkowski',
        'Fantasy',
        2024,
        'softcover',
        292,
        2
    ),
    (
        'Sunrise on the Reaping',
        'Suzanne Collins',
        'Dystopian',
        2025,
        'hardback',
        400,
        1
    ),
    (
        'The Dry Season: A Memoir of Pleasure in a Year Without Sex',
        'Melissa Febos',
        'Non-Fiction',
        2025,
        'hardback',
        288,
        3
    ),
    (
        'Meet Me at the Crossroads',
        'Megan Giddings',
        'Speculative',
        2025,
        'softcover',
        320,
        2
    ),
    (
        'The Slip: A Novel',
        'Lucas Schaefer',
        'Literary',
        2025,
        'hardback',
        496,
        5
    ),
    (
        'Awake in the Floating City',
        'Susanna Kwan',
        'Speculative',
        2025,
        'softcover',
        336,
        1
    ),
    (
        'Don\’t Let Him In',
        'Lisa Jewell',
        'Crime',
        2025,
        'softcover',
        368,
        2
    );

INSERT INTO
    users (user_name, rented_book)
VALUES ('Steven', 2),
    ('Emma', 1),
    ('Forest', 7),
    ('Bob', 4);

INSERT INTO users (user_name) VALUES ('Sam');
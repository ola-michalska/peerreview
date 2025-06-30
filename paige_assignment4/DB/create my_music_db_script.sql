CREATE DATABASE my_music;
USE my_music;

-- Creat table to store my favourite songs in order
CREATE TABLE song_rank (
    rank_id INT PRIMARY KEY NOT NULL,
    name VARCHAR(100),
    artist VARCHAR(100),
    genre VARCHAR(100),
    added_date DATE DEFAULT (CURDATE())
);

INSERT INTO song_rank (rank_id, name, artist, genre) VALUES
(1, 'Espresso', 'Sabrina', 'Pop'), 
(2, 'Earthquake', 'Labrynth', 'House'), 
(3, 'Texas', 'Beyonce', 'Country'), 
(4, 'Asibe', 'Burna', 'Afrobeats'), 
(5, 'Thunder', 'ACDC', 'Metal'), 
(6, 'Arabella', 'ArcticMonkeys', 'SoftRock'),
(7, 'Control', 'TeddySwims', 'Pop'),
(8, 'RinseRepeat', 'EDX', 'House'),
(9, 'BarSong', 'LilNas', 'Country'),
(10, 'Control', 'PSquare', 'Afrobeats'),
(11, 'Sanstorm', 'Hells', 'Metal'),
(12, 'Rosemary', 'Tuesdays', 'SoftRock');


CREATE TABLE experiences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    price_usd REAL,
    duration_hours REAL,
    start_time TEXT
);

INSERT INTO experiences (title, description, price_usd, duration_hours, start_time)
VALUES ('Sushi Making Experience', 'Learn to make authentic sushi with a local chef in Tokyo.', 55.0, 2, '10:00 AM');

INSERT INTO experiences (title, description, price_usd, duration_hours, start_time)
VALUES ('Samurai Sword Lesson', 'Train with a real samurai master and practice sword techniques.', 80.0, 1.5, '2:00 PM');

INSERT INTO experiences (title, description, price_usd, duration_hours, start_time)
VALUES ('Anime Studio Tour', 'Visit a real anime studio and meet artists.', 60.0, 2.5, '11:00 AM');

INSERT INTO experiences (title, description, price_usd, duration_hours, start_time)
VALUES ('Shibuya Food Crawl', 'Explore hidden food spots in Shibuya with a guide.', 45.0, 3, '5:00 PM');

INSERT INTO experiences (title, description, price_usd, duration_hours, start_time)
VALUES ('Traditional Tea Ceremony', 'Participate in a serene tea ceremony in a tatami room.', 35.0, 1, '4:00 PM');

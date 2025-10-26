CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    code TEXT,
    score INTEGER,
    issues TEXT[]
);
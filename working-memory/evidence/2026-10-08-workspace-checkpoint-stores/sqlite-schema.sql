
CREATE TABLE records (id TEXT PRIMARY KEY, body BLOB NOT NULL);
CREATE TABLE revisions (
    number INTEGER PRIMARY KEY, header BLOB NOT NULL,
    digest TEXT NOT NULL, record_count INTEGER NOT NULL
);
CREATE TABLE membership (
    revision INTEGER NOT NULL REFERENCES revisions(number),
    record TEXT NOT NULL REFERENCES records(id),
    PRIMARY KEY (revision, record)
);

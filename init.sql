CREATE TABLE phones (
    phone_number VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100)
);
CREATE TABLE calls (
    id SERIAL PRIMARY KEY,
    caller VARCHAR(20),
    callee VARCHAR(20),
    duration INTEGER
);

INSERT INTO phones (phone_number, name) VALUES
('123456', 'Alice'),
('234567', 'Bob'),
('345678', 'Carol'),
('997', 'Police');
INSERT INTO calls (caller, callee, duration) VALUES
('123456', '234567', 15),
('234567', '345678', 5),
('345678', '123456', 7),
('123456', '345678', 20),
('123456', '997', 3);


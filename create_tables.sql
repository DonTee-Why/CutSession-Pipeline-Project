DROP TABLE IF EXISTS merchants;
CREATE TABLE merchants (
  merchant_id varchar(36),
  name varchar(255) NOT NULL,
  username varchar(20) NOT NULL,
  email varchar(255) NOT NULL,
  city_of_operation varchar(20),
  phone_number varchar(20) DEFAULT NULL,
  password varchar(255) NOT NULL,
  PRIMARY KEY (merchant_id)
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  user_id varchar(36) NOT NULL,
  name varchar(255) NOT NULL,
  username varchar(20) NOT NULL,
  email varchar(255) NOT NULL,
  dob date NOT NULL,
  city_of_residence varchar(20) DEFAULT NULL,
  phone_number varchar(20) DEFAULT NULL,
  password varchar(255) NOT NULL,
  PRIMARY KEY (user_id)
);

DROP TABLE IF EXISTS studio_sessions;
CREATE TABLE studio_sessions (
  session_id varchar(255) NOT NULL,
  merchant_id varchar(255) NOT NULL,
  starts_at time NOT NULL,
  ends_at time NOT NULL,
  type varchar(255) NOT NULL,
  PRIMARY KEY (session_id),
  FOREIGN KEY (merchant_id) REFERENCES merchants (merchant_id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS bookings;
CREATE TABLE bookings (
  booking_id varchar(255) NOT NULL,
  booking_ref varchar(9) NOT NULL,
  user_id varchar(255) NOT NULL,
  session_id varchar(255) NOT NULL,
  date date NOT NULL,
  starts_at time NOT NULL,
  ends_at time NOT NULL,
  notes text,
  title varchar(75) DEFAULT NULL,
  PRIMARY KEY (booking_id),
  FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
  FOREIGN KEY (session_id) REFERENCES studio_sessions (session_id) ON DELETE CASCADE
);

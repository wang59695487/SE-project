CREATE TABLE IF NOT EXISTS stock_data(
    id INT PRIMARY KEY AUTO_INCREMENT,
    code INT,
    name VARCHAR(32),
    rate FLOAT,
    open FLOAT,
    close FLOAT,
    price FLOAT,
    high FLOAT,
    low FLOAT,
    yest_close FLOAT,
    date DATE,
    turnover FLOAT,
    volume INT
)DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS stock_index(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(32),
    code INT,
    pinyin VARCHAR(1)
)DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS stock_industries(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(32),
    declined INT,
    balanced INT,
    surged INT,
    total INT,
    rate FLOAT,
    dec_rate FLOAT,
    sur_rate FLOAT
)DEFAULT CHARSET=utf8;

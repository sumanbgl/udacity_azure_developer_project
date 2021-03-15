CREATE TABLE INCOME_EXPENSE(
    id INT NOT NULL IDENTITY(1, 1),
    category VARCHAR(150) NOT NULL,
    date DATE NOT NULL DEFAULT(GETDATE()),
    amount INT NOT NULL,
	user_id INT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO dbo.income_expense (category, amount, user_id)
VALUES (
    'income',
    5000,
    1
);
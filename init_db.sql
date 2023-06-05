CREATE TABLE test_kv (
  id SERIAL PRIMARY KEY,
  value INT,
  name CHAR(255)
);

INSERT INTO test_kv (value, name)
SELECT
  FLOOR(RANDOM() * 1000) AS value,
  CONCAT('Name', FLOOR(RANDOM() * 1000000)) AS name
FROM
  generate_series(1, 1000000);
  
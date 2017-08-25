.read sp16data.sql
.read fa16data.sql

CREATE TABLE obedience AS
  select seven, denero from students;

CREATE TABLE smallest_int AS
  select time, smallest from students where smallest > 8 order by smallest limit 20;

CREATE TABLE greatstudents AS
  select this.date, this.number, this.pet, this.color, last.color from students as this, sp16students as last
  	where this.date = last.date and this.number = last.number and this.pet = last.pet;

CREATE TABLE sevens AS
  select a.seven from students as a, checkboxes as b where a.time = b.time and a.number = 7 and b.'7' = 'True';

CREATE TABLE matchmaker AS
  select a.pet, a.song, a.color, b.color from students as a, students as b
  	where a.pet = b.pet and a.song = b.song and a.time < b.time;

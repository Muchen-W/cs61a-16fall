.read data.sql

-- Q1
create table flight_costs as
  with flight_cost(curr_day, curr_price, prev_price) as (
  	select 1, 20, 0 union
  	select 2, 30, 20 union
  	select 3, 40, 30 union
  	select curr_day + 1, (prev_price + curr_price) / 2 + 5 * ((curr_day + 1) % 7), curr_price
  	  from flight_cost where curr_day > 2 and curr_day < 25
  )
  select curr_day as day, curr_price as price from flight_cost;

-- Q2
create table schedule as
	with schedule_list(paths, ending, num_of_flights, total_price) as (
		select departure || ", " || arrival, arrival, 1, price from flights where departure = "SFO" union
		select paths || ", " || arrival, arrival, num_of_flights + 1, total_price + price from schedule_list, flights
			where ending = departure and paths not like "%arrival%" and num_of_flights < 2
	)
	select paths, total_price from schedule_list where ending = "PDX" order by total_price;

-- Q3
create table shopping_cart as
	with choices(items, most_expensive, leftover) as (
		select item, price, 60 - price from supermarket where price <= 60 union
		select items || ", "|| item, price, leftover - price from choices, supermarket
			where price >= most_expensive and leftover >= price
	)
  select items, leftover from choices order by leftover, items;

-- Q4
create table number_of_options as
	select count(distinct meat) from main_course;

-- Q5
create table calories as
  select count(*) from main_course as a, pies as b where a.calories + b.calories < 2500; 

-- Q6
create table healthiest_meats as
	select meat, min(a.calories + b.calories) from main_course as a, pies as b
		group by meat having max(a.calories + b.calories) <= 3000;

-- Q7
create table average_prices as
  select category, avg(MSRP) from products group by category;

-- Q8
create table lowest_prices as
  select item, store, min(price) from inventory group by item;
  -- select item, store, price from inventory group by item having min(price);

-- Q9
create table shopping_list as
  select name, store from products, lowest_prices where name = item group by category having min(MSRP/rating);

-- Q10
create table total_bandwidth as
  select sum(Mbs) from shopping_list as a, stores as b where a.store = b.store;

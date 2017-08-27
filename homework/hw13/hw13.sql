create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select name, size from dogs, sizes where height > min and height <= max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select a.name from dogs as a, dogs as b, parents where a.name = child and b.name = parent order by b.height desc;

-- Sentences about siblings that are the same size
create table sentences as
  with siblings(sib1, sib2) as (
  	select a.child, b.child from parents as a, parents as b where a.parent = b.parent and a.child < b.child
  )
  select sib1 || " and " || sib2 || " are " || a.size || " siblings"
    from siblings, size_of_dogs as a, size_of_dogs as b
    where sib1 = a.name and sib2 = b.name and a.size = b.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  with all_stacks(name, total_height, number_of_dogs, height_of_last) as (
  	select a.name, a.height, 1, a.height from dogs as a union
  	select c.name || ", " || b.name, total_height + b.height, number_of_dogs + 1, b.height from dogs as b, all_stacks as c
  	  where height_of_last < b.height and number_of_dogs < 4
  )
  select name, total_height from all_stacks where total_height >= 170 order by total_height;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
create table non_parents as
	with grands(grandparent, grandchild) as (
		select a.parent, b.child from parents as a, parents as b where a.child = b.parent
	),
	ancestors(ancestor, descendant) as (
		select grandparent, grandchild from grands union
		select ancestor, child from ancestors, parents where descendant = parent
	),
	differences(ancestor, descendant, height_difference) as (
		select ancestor, descendant, a.height - b.height from ancestors, dogs as a, dogs as b
			where ancestor = a.name and descendant = b.name
	),
	combined(first, second, height_difference) as (
		select * from differences union
		select descendant, ancestor, -1 * height_difference from differences
	)
	select first, second from combined order by height_difference;
		

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
	with divisor_list(num, divisor) as (
		select 1, 1 union
		select dividend.n, d.n from ints as dividend, ints as d where dividend.n >= d.n and dividend.n % d.n == 0
	)
    select num, count(*) as counts from divisor_list group by num order by num;

create table primes as
    select num from divisors where counts = 2;

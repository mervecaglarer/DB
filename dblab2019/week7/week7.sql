# 1. Show the films whose budget is greater than 10 million$ and ranking is less than 6.
select title   
from movies
where budget > 10000000 and ranking < 6;

# 2. Show the action films whose rating is greater than 8.8 and produced after 1990.
select movies.movie_id,title
from movies join genres on movies.movie_id = genres.movie_id
where rating > 8.8 and year > 1990 and genre_name = "Action";

# 3. Show the drama films whose duration is more than 150 minutes and oscars is more than 2.
select title 
from movies 
where duration > 150 and oscars > 2 and movie_id in 
(select movie_id
 from genres
 where genre_name = "Drama");

# 4. Show the films that Orlando Bloom and Ian McKellen have act together and has more than 2 Oscars.
select title
from movies
where oscars > 2 and movie_id in 
 (select movie_id 
  from movie_stars join stars on movie_stars.star_id = stars.star_id
  where star_name = "Orlando Bloom" and movie_id in 
  (select movie_id 
   from movie_stars join stars on movie_stars.star_id = stars.star_id
   where star_name = "Ian McKellen"));
 
# 5. Show the Quentin Tarantino films which have more than 500000 votes and produced before 2000.
select title
from movies
where votes >500000 and year <2000 and movie_id in 
(select movie_id
 from movie_directors join directors on movie_directors.directory_id = directors.directory_id	
 where director_name like "Quentin%");

# 6. Show the thriller films whose budget is greater than 25 million$.	 
select movies.movie_id,title 
from movies join genres on movies.movie_id = genres.movie_id
where genre_name = "Thriller" and budget > 25000000;

# 7. Show the drama films whose language is Italian and produced between 1990-2000.	
select title 
from movies
where  year between 1990 and 2000 and movie_id in
(select movie_id
 from genres join languages on genres.movie_id = languages.movie_id
 where genre_name = "Drama" and language_name = "Italian"); 

# 8. Show the films that Tom Hanks has act and have won more than 3 Oscars.
select title
from movies
where oscars > 3 and movie_id in 
(select movie_id
 from stars join movie_stars on stars.star_id = movie_stars.star_id
 where star_name like "% hanks");	 

# 9. Show the history films produced in USA and whose duration is between 100-200 minutes.
select title 
from movies join genres on movies.movie_id = genres.movie_id
where genre_name = "History" and duration between 100 and 200 and movie_id in
 (select genres.movie_id  
 from genres join producer_countries  on genres.movie_id = producer_countries.movie_id 
			join countries on producer_countries.country_id = countries.country_id
 where genre_name = "History" and country_name = "USA");
 
# 10.Compute the average budget of the films directed by Peter Jackson.

# 11.Show the Francis Ford Coppola film that has the minimum budget.

# 12.Show the film that has the most vote and has been produced in USA.
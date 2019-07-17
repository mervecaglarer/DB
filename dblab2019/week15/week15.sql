insert into movies(movie_id , title , ranking , rating , year , votes , duration , oscars , budget)
select distinct movie_id , title , ranking , rating , year , votes , duration , oscars , budget
from denormalized;

insert into languages(language_name , movie_id)
select distinct language_name , movie_id
from denormalized;


insert into genres(movie_id , genre_name)
select distinct movie_id , genre_name
from denormalized;

insert into countries(country_id , country_name)
select distinct producer_country_id , producer_country_name
from denormalized
union
select distinct director_country_id , director_country_name
from denormalized
union
select distinct star_country_id , star_country_name
from denormalized;

insert into producer_countries(movie_id , country_id )
select distinct  movie_id , producer_country_id
from denormalized;

insert into directors(director_id , country_id , director_name)
select distinct director_id , director_country_id , director_name
from denormalized;

insert into stars(star_id , country_id , star_name)
select distinct star_id , star_country_id , star_name
from denormalized;

insert into movie_directors(movie_id , director_id)
select distinct movie_id , director_id
from denormalized;

insert into movie_stars(movie_id , star_id)
select distinct movie_id , star_id
from denormalized;

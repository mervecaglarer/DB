load data infile '/home/m.caglarer16/Downloads/movies.csv'
into table movies fields terminated by ',' enclosed by '"' ;

load data infile '/home/m.caglarer16/Downloads/countries.csv'
into table countries fields terminated by ',' ;

load data infile '/home/m.caglarer16/Downloads/stars.csv'
into table stars fields terminated by ',' ;

load data infile '/home/m.caglarer16/Downloads/movie_stars.csv'
into table movie_stars fields terminated by ',' ;

load data infile '/home/m.caglarer16/Downloads/directors.csv'
into table directors fields terminated by ',' ;

load data infile '/home/m.caglarer16/Downloads/movie_directors.csv'
into table movie_directors fields terminated by ',' ;

load data infile '/home/m.caglarer16/Downloads/producer_countries.csv'
into table produces_countries fields terminated by ',' ;

load data infile '/home/m.caglarer16/Downloads/genres.csv'
into table genres fields terminated by ',' ;

load data infile '/home/m.caglarer16/Downloads/languages.csv'
into table languages fields terminated by ',' ;

show variables like 'secure_file_priv';

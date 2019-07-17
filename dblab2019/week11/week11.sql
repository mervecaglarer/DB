select count(accession) from Proteins;

select * from Proteins limit 10000;

select * from Proteins where name like "%Transcription factor%"; 

create index idx_name on Proteins (name(15));
alter table Proteins drop index idx_name;
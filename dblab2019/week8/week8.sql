select CustomerName
from Customers
where Country = "Mexico";

update Customers
set CustomerName = "Juan"
where Country = "Mexico";

select * from Employees;
insert into Employees (EmployeeID,LastName,FirstName,BirthDate,Photo,Notes)
values (11, "Caglarer","Merve","1997-04-29","","asdasdsd"); 
create view usa_customers as
select CustomerID , CustomerName , ContactName
from Customers
where Country = "USA";

select * from usa_customers;

select * 
from usa_customers join Orders on usa_customers.CustomerID = Orders.CustomerID;

create or replace view products_below_avg_price as
select ProductID , ProductName , Price
from Products
where Price < 30; #(select avg(Price) from Products);

select * 
from usa_customers join Orders on usa_customers.CustomerID = Orders.CustomerID
where OrderID in (
select OrderID 
from OrderDetails join products_below_avg_price on OrderDetails.ProductID = products_below_avg_price.ProductID); 

drop view usa_customers;
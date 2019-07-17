select * from Customers ;
delete from Customers where CustomerID = 20;

select * from Orders where CustomerID = 20;
delete from Orders where CustomerID = 20;

select * from OrderDetails;
select * from OrderDetails where OrderID in (
 select OrderID from Orders  where CustomerID = 20);
 
delete from OrderDetails where OrderID in (
 select OrderID from Orders  where CustomerID = 20);
 
 delete from Orders where CustomerID = 20;
 delete from Customers where CustomerID = 20;
 select * from Customers where CustomerID =20;
 
 select * from Products;
 delete from Products where ProductID = 10;
 
 select * from OrderDetails where ProductID = 10;
 delete from OrderDetails where ProductID = 10;
 
 delete from Products where ProductID = 10;
 
 select * from Shippers;
 delete from Shippers where ShipperID = 2;
 
 select * from Orders where ShipperID = 2;
 delete from Orders where ShipperID = 2;
 
 select * from OrderDetails where OrderID in (
  select OrderID from Orders where ShipperID = 2);
 
 delete from OrderDetails where OrderID in (
  select OrderID from Orders where ShipperID = 2);
  delete from Orders where ShipperID = 2;
  delete from Shippers where ShipperID = 2;
 
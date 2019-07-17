select country , count(CustomerID)
from Customers
group by Country;  

select ShipperName,count(Orders.OrderID) as numberofOrders
from Shippers join Orders on Shippers.ShipperID=Orders.ShipperID
group by Shippers.ShipperID
order by numberofOrders desc;
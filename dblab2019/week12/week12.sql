call selectAllCustomers();

call getCustomersBycity("Barcelona");

select * from Employees;


set @max_salary = 0;
call highestSalary(@max_salary);
select @max_salary;

set @m_count=0;
call Countgender(@m_count,"M");


set @f_count=0;
call Countgender(@f_count,"F");

select @m_count , @f_count;
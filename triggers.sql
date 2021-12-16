delimiter //
create trigger after_delete_mechanics
    after delete
    on mechanics
    for each row
    begin
        delete from staff
            where OLD.staff_code = staff.staff_code;
    end //
delimiter ;
---------------

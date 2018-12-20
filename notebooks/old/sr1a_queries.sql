# frequency count of sales per parcel
select pams_pin, count(pams_pin) from sr1a where  GROUP BY pams_pin HAVING COUNT(pams_pin)>1 ORDER BY COUNT(pams_pin);

# create a new table only Hudson County all years
drop table hudson_sr1a;
select * INTO hudson_sr1a from sr1a where county_code=09; 
SELECT 64058 

# create a lookup table of parcels sold twice 2009-2016
drop table hudson_2x;
SELECT *
INTO hudson_2x
FROM hudson_sr1a
WHERE pams_pin IN
    (     SELECT pams_pin
          FROM hudson_sr1a
          GROUP BY pams_pin
          HAVING COUNT(*) =2
    )
ORDER BY pams_pin;

SELECT 17452

# create a lookup table of parcels sold 3x 2009-2016
drop table hudson_3x;
SELECT *
INTO hudson_3x
FROM hudson_sr1a
WHERE pams_pin IN
    (     SELECT pams_pin
          FROM hudson_sr1a
          GROUP BY pams_pin
          HAVING COUNT(*) =3
    )
ORDER BY pams_pin;

SELECT 5004


# create a lookup table of parcels sold 4x 2009-2016
drop table hudson_4x;
SELECT *
INTO hudson_4x
FROM hudson_sr1a
WHERE pams_pin IN
    (     SELECT pams_pin
          FROM hudson_sr1a
          GROUP BY pams_pin
          HAVING COUNT(*) =4
    )
ORDER BY pams_pin;

SELECT 1136

# create a lookup table of parcels sold 5x 2009-2016
drop table hudson_5x;
SELECT *
INTO hudson_5x
FROM hudson_sr1a
WHERE pams_pin IN
    (     SELECT pams_pin
          FROM hudson_sr1a
          GROUP BY pams_pin
          HAVING COUNT(*) =5
    )
ORDER BY pams_pin;

SELECT 360

# create a lookup table of parcels sold 65x 2009-2016
drop table hudson_6x;
SELECT *
INTO hudson_6x
FROM hudson_sr1a
WHERE pams_pin IN
    (     SELECT pams_pin
          FROM hudson_sr1a
          GROUP BY pams_pin
          HAVING COUNT(*) =6
    )
ORDER BY pams_pin;

SELECT 96

drop table hudson_7x;
SELECT *
INTO hudson_7x
FROM hudson_sr1a
WHERE pams_pin IN
    (     SELECT pams_pin
          FROM hudson_sr1a
          GROUP BY pams_pin
          HAVING COUNT(*) =7
    )
ORDER BY pams_pin;

SELECT 98

drop table hudson_8x;
SELECT *
INTO hudson_8x
FROM hudson_sr1a
WHERE pams_pin IN
    (     SELECT pams_pin
          FROM hudson_sr1a
          GROUP BY pams_pin
          HAVING COUNT(*) =8
    )
ORDER BY pams_pin;

SELECT 40




# just hoboken

drop table hoboken_sr1a;
select * INTO hoboken_sr1a from sr1a where county_code=09 AND district_code=05; 
SELECT 10783

drop table hoboken_2x;
SELECT *
INTO hoboken_2x
FROM hoboken_sr1a
WHERE pams_pin IN
    (     SELECT pams_pin
          FROM hoboken_sr1a
          GROUP BY pams_pin
          HAVING COUNT(*) =2
    )
ORDER BY pams_pin;
SELECT 3222


# just jersey city
drop table jerseycity_sr1a;
select * INTO jerseycity_sr1a from sr1a where county_code=09 AND district_code=06; 

# dump the JC table to CSV
COPY jerseycity_sr1a TO '/Users/anthonytownsend/Desktop/Code/parcels/nj/extracts/jc_sr1a_2009_to_2016_feb1.csv' DELIMITER ',' CSV HEADER;



district_code


# all fields
select 
pams_pin, property_location, u_n_type, sr_nu_code, last_update_date,
    reported_sales_price, verified_sales_price, assessed_value_land, assessed_value_bldg,
    assessed_value_total, sales_ratio, realty_transfer_fee, serial_number,
    grantor_name, grantor_street, grantor_city_state, grantor_zip,
    grantee_name, grantee_street, grantee_city_state, grantee_zip,
    deed_book, deed_page, deed_date, date_recorded, qualification_codes,
    property_class, class_4_type, year_built, living_space, condo 
from

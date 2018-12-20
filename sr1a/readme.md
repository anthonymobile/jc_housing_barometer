# SR1A File

This is the rolling record of sales from the NJ Treasurer's office. Data: http://www.nj.gov/treasury/taxation/lpt/grantors_listing.shtml

##  Import Process

1. Convert the raw text data to CSV using https://github.com/johnjreiser/NJParcelTools

2013+

```python sr1a_csv.py [input file] > [output file].csv # 

Pre-2013:

```python sr1a_csv.py [input file] old > [output file].csv

### Commands

'''
python sr1a_csv.py ~/Downloads/Sales16.txt > Sales16.csv (done)
python sr1a_csv.py ~/Downloads/Sales15.txt > Sales15.csv (done)
python sr1a_csv.py ~/Downloads/Sales14.txt > Sales14.csv (done)
python sr1a_csv.py ~/Downloads/Sales13.txt > Sales13.csv (done)
python sr1a_csv.py ~/Downloads/Sales12.txt old > Sales12.csv (done)
python sr1a_csv.py ~/Downloads/Sales11.txt old > Sales11.csv (done)
python sr1a_csv.py ~/Downloads/Sales10.txt old > Sales10.csv
python sr1a_csv.py ~/Downloads/Sales09.txt old > Sales09.csv

2. Create the database

Generate schema (works for both old and new,tested on postgresql):

```python sr1a_csv.py schema > sr1a_createtable.sql

Create a new database:

```createdb sr1a

Execute the schema

```psql -d sr1a < sr1a_createtable.sql


3. Load data

A little tricky as straight load won't work, you need to specify order of columns in data.

### 2016 (done)

```COPY sr1a (pams_pin,county_code,district_code,batch_number,dln,operator_initials,last_update_date,questionnaire_status_code,questionnaire_date,questionnaire_who_code,u_n_type,sr_nu_code,reported_sales_price,verified_sales_price,assessed_value_land,assessed_value_bldg,assessed_value_total,sales_ratio,realty_transfer_fee,rtf_error_flag,rtf_exempt_code,serial_number,grantor_nctl,grantor_name,grantor_street,grantor_city_state,grantor_zip,grantee_name,grantee_street,grantee_city_state,grantee_zip,property_location,aging_date,deed_book,deed_page,deed_date,date_recorded,block_prefix,block_suffix,lot_prefix,lot_suffix,etc,addl_block1,addl_lot1,addl_qualifier1,addl_value_land1,addl_value_bldg1,addl_value_total1,addl_block2,addl_lot2,addl_qualifier2,addl_value_land2,addl_value_bldg2,addl_value_total2,addl_block3,addl_lot3,addl_qualifier3,addl_value_land3,addl_value_bldg3,addl_value_total3,addl_block4,addl_lot4,addl_qualifier4,addl_value_land4,addl_value_bldg4,addl_value_total4,addl_block5,addl_lot5,addl_qualifier5,addl_value_land5,addl_value_bldg5,addl_value_total5,qualification_codes,assess_year,property_class,class_4_type,date_typed,assessor_nu_code,field_status_code,field_date,critical_error_flag,condo,appeal_status,assessor_written_cd,year_built,living_space) FROM '/Users/anthonytownsend/Code-Local/housing_barometer/sr1a/Sales16.csv' DELIMITER ',' HEADER CSV;

### 2015 (done)

```COPY sr1a (pams_pin,county_code,district_code,batch_number,dln,operator_initials,last_update_date,questionnaire_status_code,questionnaire_date,questionnaire_who_code,u_n_type,sr_nu_code,reported_sales_price,verified_sales_price,assessed_value_land,assessed_value_bldg,assessed_value_total,sales_ratio,realty_transfer_fee,rtf_error_flag,rtf_exempt_code,serial_number,grantor_nctl,grantor_name,grantor_street,grantor_city_state,grantor_zip,grantee_name,grantee_street,grantee_city_state,grantee_zip,property_location,aging_date,deed_book,deed_page,deed_date,date_recorded,block_prefix,block_suffix,lot_prefix,lot_suffix,etc,addl_block1,addl_lot1,addl_qualifier1,addl_value_land1,addl_value_bldg1,addl_value_total1,addl_block2,addl_lot2,addl_qualifier2,addl_value_land2,addl_value_bldg2,addl_value_total2,addl_block3,addl_lot3,addl_qualifier3,addl_value_land3,addl_value_bldg3,addl_value_total3,addl_block4,addl_lot4,addl_qualifier4,addl_value_land4,addl_value_bldg4,addl_value_total4,addl_block5,addl_lot5,addl_qualifier5,addl_value_land5,addl_value_bldg5,addl_value_total5,qualification_codes,assess_year,property_class,class_4_type,date_typed,assessor_nu_code,field_status_code,field_date,critical_error_flag,condo,appeal_status,assessor_written_cd,year_built,living_space) FROM '/Users/anthonytownsend/Code-Local/housing_barometer/sr1a/Sales15.csv' DELIMITER ',' HEADER CSV;


### 2014 (done)

```COPY sr1a (pams_pin,county_code,district_code,batch_number,dln,operator_initials,last_update_date,questionnaire_status_code,questionnaire_date,questionnaire_who_code,u_n_type,sr_nu_code,reported_sales_price,verified_sales_price,assessed_value_land,assessed_value_bldg,assessed_value_total,sales_ratio,realty_transfer_fee,rtf_error_flag,rtf_exempt_code,serial_number,grantor_nctl,grantor_name,grantor_street,grantor_city_state,grantor_zip,grantee_name,grantee_street,grantee_city_state,grantee_zip,property_location,aging_date,deed_book,deed_page,deed_date,date_recorded,block_prefix,block_suffix,lot_prefix,lot_suffix,etc,addl_block1,addl_lot1,addl_qualifier1,addl_value_land1,addl_value_bldg1,addl_value_total1,addl_block2,addl_lot2,addl_qualifier2,addl_value_land2,addl_value_bldg2,addl_value_total2,addl_block3,addl_lot3,addl_qualifier3,addl_value_land3,addl_value_bldg3,addl_value_total3,addl_block4,addl_lot4,addl_qualifier4,addl_value_land4,addl_value_bldg4,addl_value_total4,addl_block5,addl_lot5,addl_qualifier5,addl_value_land5,addl_value_bldg5,addl_value_total5,qualification_codes,assess_year,property_class,class_4_type,date_typed,assessor_nu_code,field_status_code,field_date,critical_error_flag,condo,appeal_status,assessor_written_cd,year_built,living_space) FROM '/Users/anthonytownsend/Code-Local/housing_barometer/sr1a/Sales14.csv' DELIMITER ',' HEADER CSV;

### 2013 (done)

```COPY sr1a (pams_pin,county_code,district_code,batch_number,dln,operator_initials,last_update_date,questionnaire_status_code,questionnaire_date,questionnaire_who_code,u_n_type,sr_nu_code,reported_sales_price,verified_sales_price,assessed_value_land,assessed_value_bldg,assessed_value_total,sales_ratio,realty_transfer_fee,rtf_error_flag,rtf_exempt_code,serial_number,grantor_nctl,grantor_name,grantor_street,grantor_city_state,grantor_zip,grantee_name,grantee_street,grantee_city_state,grantee_zip,property_location,aging_date,deed_book,deed_page,deed_date,date_recorded,block_prefix,block_suffix,lot_prefix,lot_suffix,etc,addl_block1,addl_lot1,addl_qualifier1,addl_value_land1,addl_value_bldg1,addl_value_total1,addl_block2,addl_lot2,addl_qualifier2,addl_value_land2,addl_value_bldg2,addl_value_total2,addl_block3,addl_lot3,addl_qualifier3,addl_value_land3,addl_value_bldg3,addl_value_total3,addl_block4,addl_lot4,addl_qualifier4,addl_value_land4,addl_value_bldg4,addl_value_total4,addl_block5,addl_lot5,addl_qualifier5,addl_value_land5,addl_value_bldg5,addl_value_total5,qualification_codes,assess_year,property_class,class_4_type,date_typed,assessor_nu_code,field_status_code,field_date,critical_error_flag,condo,appeal_status,assessor_written_cd,year_built,living_space) FROM '/Users/anthonytownsend/Code-Local/housing_barometer/sr1a/Sales13.csv' DELIMITER ',' HEADER CSV;


### 2012
```COPY sr1a (pams_pin,county_code,district_code,batch_number,dln,operator_initials,last_update_date,questionnaire_status_code,questionnaire_date,questionnaire_who_code,u_n_type,sr_nu_code,reported_sales_price,verified_sales_price,assessed_value_land,assessed_value_bldg,assessed_value_total,sales_ratio,realty_transfer_fee,rtf_error_flag,rtf_exempt_code,serial_number,grantor_nctl,grantor_name,grantor_street,grantor_city_state,grantor_zip,grantee_name,grantee_street,grantee_city_state,grantee_zip,property_location,aging_date,deed_book,deed_page,deed_date,date_recorded,block_prefix,block_suffix,lot_prefix,lot_suffix,etc,addl_block1,addl_lot1,addl_qualifier1,addl_value_land1,addl_value_bldg1,addl_value_total1,addl_block2,addl_lot2,addl_qualifier2,addl_value_land2,addl_value_bldg2,addl_value_total2,addl_block3,addl_lot3,addl_qualifier3,addl_value_land3,addl_value_bldg3,addl_value_total3,addl_block4,addl_lot4,addl_qualifier4,addl_value_land4,addl_value_bldg4,addl_value_total4,addl_block5,addl_lot5,addl_qualifier5,addl_value_land5,addl_value_bldg5,addl_value_total5,qualification_codes,assess_year,property_class,class_4_type,date_typed,assessor_nu_code,field_status_code,field_date,critical_error_flag,condo,appeal_status,assessor_written_cd,year_built,living_space) FROM '/Users/anthonytownsend/Code-Local/housing_barometer/sr1a/Sales12.csv' DELIMITER ',' HEADER CSV;

### 2011
```COPY sr1a (pams_pin,county_code,district_code,batch_number,dln,operator_initials,last_update_date,questionnaire_status_code,questionnaire_date,questionnaire_who_code,u_n_type,sr_nu_code,reported_sales_price,verified_sales_price,assessed_value_land,assessed_value_bldg,assessed_value_total,sales_ratio,realty_transfer_fee,rtf_error_flag,rtf_exempt_code,serial_number,grantor_nctl,grantor_name,grantor_street,grantor_city_state,grantor_zip,grantee_name,grantee_street,grantee_city_state,grantee_zip,property_location,aging_date,deed_book,deed_page,deed_date,date_recorded,block_prefix,block_suffix,lot_prefix,lot_suffix,etc,addl_block1,addl_lot1,addl_qualifier1,addl_value_land1,addl_value_bldg1,addl_value_total1,addl_block2,addl_lot2,addl_qualifier2,addl_value_land2,addl_value_bldg2,addl_value_total2,addl_block3,addl_lot3,addl_qualifier3,addl_value_land3,addl_value_bldg3,addl_value_total3,addl_block4,addl_lot4,addl_qualifier4,addl_value_land4,addl_value_bldg4,addl_value_total4,addl_block5,addl_lot5,addl_qualifier5,addl_value_land5,addl_value_bldg5,addl_value_total5,qualification_codes,assess_year,property_class,class_4_type,date_typed,assessor_nu_code,field_status_code,field_date,critical_error_flag,condo,appeal_status,assessor_written_cd,year_built,living_space) FROM '/Users/anthonytownsend/Code-Local/housing_barometer/sr1a/Sales11.csv' DELIMITER ',' HEADER CSV;

### 2010
```COPY sr1a (pams_pin,county_code,district_code,batch_number,dln,operator_initials,last_update_date,questionnaire_status_code,questionnaire_date,questionnaire_who_code,u_n_type,sr_nu_code,reported_sales_price,verified_sales_price,assessed_value_land,assessed_value_bldg,assessed_value_total,sales_ratio,realty_transfer_fee,rtf_error_flag,rtf_exempt_code,serial_number,grantor_nctl,grantor_name,grantor_street,grantor_city_state,grantor_zip,grantee_name,grantee_street,grantee_city_state,grantee_zip,property_location,aging_date,deed_book,deed_page,deed_date,date_recorded,block_prefix,block_suffix,lot_prefix,lot_suffix,etc,addl_block1,addl_lot1,addl_qualifier1,addl_value_land1,addl_value_bldg1,addl_value_total1,addl_block2,addl_lot2,addl_qualifier2,addl_value_land2,addl_value_bldg2,addl_value_total2,addl_block3,addl_lot3,addl_qualifier3,addl_value_land3,addl_value_bldg3,addl_value_total3,addl_block4,addl_lot4,addl_qualifier4,addl_value_land4,addl_value_bldg4,addl_value_total4,addl_block5,addl_lot5,addl_qualifier5,addl_value_land5,addl_value_bldg5,addl_value_total5,qualification_codes,assess_year,property_class,class_4_type,date_typed,assessor_nu_code,field_status_code,field_date,critical_error_flag,condo,appeal_status,assessor_written_cd,year_built,living_space) FROM '/Users/anthonytownsend/Code-Local/housing_barometer/sr1a/Sales10.csv' DELIMITER ',' HEADER CSV;

### 2009
```COPY sr1a (pams_pin,county_code,district_code,batch_number,dln,operator_initials,last_update_date,questionnaire_status_code,questionnaire_date,questionnaire_who_code,u_n_type,sr_nu_code,reported_sales_price,verified_sales_price,assessed_value_land,assessed_value_bldg,assessed_value_total,sales_ratio,realty_transfer_fee,rtf_error_flag,rtf_exempt_code,serial_number,grantor_nctl,grantor_name,grantor_street,grantor_city_state,grantor_zip,grantee_name,grantee_street,grantee_city_state,grantee_zip,property_location,aging_date,deed_book,deed_page,deed_date,date_recorded,block_prefix,block_suffix,lot_prefix,lot_suffix,etc,addl_block1,addl_lot1,addl_qualifier1,addl_value_land1,addl_value_bldg1,addl_value_total1,addl_block2,addl_lot2,addl_qualifier2,addl_value_land2,addl_value_bldg2,addl_value_total2,addl_block3,addl_lot3,addl_qualifier3,addl_value_land3,addl_value_bldg3,addl_value_total3,addl_block4,addl_lot4,addl_qualifier4,addl_value_land4,addl_value_bldg4,addl_value_total4,addl_block5,addl_lot5,addl_qualifier5,addl_value_land5,addl_value_bldg5,addl_value_total5,qualification_codes,assess_year,property_class,class_4_type,date_typed,assessor_nu_code,field_status_code,field_date,critical_error_flag,condo,appeal_status,assessor_written_cd,year_built,living_space) FROM '/Users/anthonytownsend/Code-Local/housing_barometer/sr1a/Sales09.csv' DELIMITER ',' HEADER CSV;


4. Backup

Dump the whole table

```pg_dump sr1a > nj_sr1a_2009through20016.sql

Zip it and scp copy it somewhere!


5. Backup in split files

Split backup into chunks github will accept

```cd /path/to/output && split --bytes=49M /path/to/input/filename && gzip x*

Reassemble backup

```gunzip /path/to/files/x* && cat /path/to/files/x* > /path/to/dest/filename


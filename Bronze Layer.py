# Databricks notebook source
# MAGIC %sql
# MAGIC use catalog amal_kachapilly_databricks_npmentorskool_onmicrosoft_com

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema bronze_assesment

# COMMAND ----------

# MAGIC %sql
# MAGIC use schema bronze_assesment

# COMMAND ----------

# MAGIC %md
# MAGIC # Create Tables for Ingestion

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists addresses using delta;
# MAGIC create table if not exists customer using delta;
# MAGIC create table if not exists orderitems using delta;
# MAGIC create table if not exists orders using delta;
# MAGIC create table if not exists paymentmethods using delta;
# MAGIC create table if not exists payments using delta;
# MAGIC create table if not exists products using delta;
# MAGIC create table if not exists returns using delta;
# MAGIC create table if not exists shippingtier using delta;
# MAGIC create table if not exists supplier using delta;

# COMMAND ----------

# MAGIC %md
# MAGIC # Ingest into tables

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO returns
# MAGIC FROM '/mnt/bronzegcs/dataset/orders_ecom/returns.csv'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS ('inferSchema' = 'true','header' = 'true','quote'='\"','escape'='\"','multiLine'='true','mergeSchema' = 'true')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO addresses
# MAGIC FROM '/mnt/bronzegcs/dataset/orders_ecom/addresses.csv'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS ('inferSchema' = 'true','header' = 'true','quote'='\"','escape'='\"','multiLine'='true','mergeSchema' = 'true')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO customer
# MAGIC FROM '/mnt/bronzegcs/dataset/orders_ecom/customers.csv'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS ('inferSchema' = 'true','header' = 'true','quote'='\"','escape'='\"','multiLine'='true','mergeSchema' = 'true')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO orderitems
# MAGIC FROM '/mnt/bronzegcs/dataset/orders_ecom/orders_items.csv'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS ('inferSchema' = 'true','header' = 'true','quote'='\"','escape'='\"','multiLine'='true','mergeSchema' = 'true')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO orders
# MAGIC FROM '/mnt/bronzegcs/dataset/orders_ecom/orders.csv'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS ('inferSchema' = 'true','header' = 'true','quote'='\"','escape'='\"','multiLine'='true','mergeSchema' = 'true')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO paymentmethods
# MAGIC FROM '/mnt/bronzegcs/dataset/orders_ecom/payment_methods.csv'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS ('inferSchema' = 'true','header' = 'true','quote'='\"','escape'='\"','multiLine'='true','mergeSchema' = 'true')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO payments
# MAGIC FROM '/mnt/bronzegcs/dataset/orders_ecom/payments.csv'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS ('inferSchema' = 'true','header' = 'true','quote'='\"','escape'='\"','multiLine'='true','mergeSchema' = 'true')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO products
# MAGIC FROM '/mnt/bronzegcs/dataset/orders_ecom/products.csv'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS ('inferSchema' = 'true','header' = 'true','quote'='\"','escape'='\"','multiLine'='true','mergeSchema' = 'true')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO shippingtier
# MAGIC FROM '/mnt/bronzegcs/dataset/orders_ecom/shipping_tier.csv'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS ('inferSchema' = 'true','header' = 'true','quote'='\"','escape'='\"','multiLine'='true','mergeSchema' = 'true')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO supplier
# MAGIC FROM '/mnt/bronzegcs/dataset/orders_ecom/suppliers.csv'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS ('inferSchema' = 'true','header' = 'true','quote'='\"','escape'='\"','multiLine'='true','mergeSchema' = 'true')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true')

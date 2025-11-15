# Weekly Assignment – 1

A data engineering mini-project where you work with a CSV dataset containing daily sales transactions from multiple retail stores. The objective is to perform an ETL (Extract–Transform–Load) pipeline and generate useful aggregated insights.

---

## **Project Overview**

This project processes raw sales data and outputs cleaned and aggregated results.

### **Data Cleaning & Transformation**
- Reads raw CSV (`sales_sample.csv`)
- Normalizes store names & trims spaces
- Converts date formats
- Ensures consistent datatypes
- Removes invalid or messy records

### **Data Aggregation**
- Groups data *per store, per month*
- Computes total sales per group
- Exports final insights as JSON




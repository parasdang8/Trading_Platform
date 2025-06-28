import mysql.connector
import random
import matplotlib.pyplot as plt
p_count=0     

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="GAUTAM",
  database="TRADING_PLATFORM"    )                           
mycursor = mydb.cursor()

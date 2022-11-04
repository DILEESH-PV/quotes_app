import requests
import json
import mysql.connector

try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='quotedb')
except mysql.connector.Error as e:
    print("db connection error",e)
mycursor=mydb.cursor()
data=requests.get("https://dummyjson.com/quotes").text
data_info=json.loads(data)
for j in data_info['quotes']:
    try:
        #sql='INSERT INTO `papi`(`api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES ("'+j['API']+'","'+j['Description']+'","'+j['Auth']+'","'+http+'","'+j['Cors']+'","'+j['Link']+'","'+j['Category']+'")'
        #sql="INSERT INTO `papi`(`api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES ('"+j['API']+"','"+j['Description']+"','"+j['Auth']+"','"+http+"','"+j['Cors']+"','"+j['Link']+"','"+j['Category']+"')"
        sql=" INSERT INTO `quotes`(`quote`, `author`) VALUES  (%s,%s)"
        data=(j['quote'],j['author'])
        mycursor.execute(sql,data)
        mydb.commit()
        print("Data inserted successfully",j['author'])
    except mysql.connector.Error as e:
        print("error is",e)
    

        
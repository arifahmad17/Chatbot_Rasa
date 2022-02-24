import mysql.connector

def DataUpdate(email,subject,message):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="mail_info"
    )

    mycursor = mydb.cursor()
    #sql="CREATE TABLE Email_Rasa (email VARCHAR(255) , subject VARCHAR(255) , message VARCHAR(255));"
    sql= 'INSERT INTO Email_Rasa (email , subject, message) VALUES ("{0}","{1}","{2}");'.format(email,subject,message)
    mycursor.execute(sql)

    mydb.commit()
    print(mycursor.rowcount, "record inserted")

if __name__=="__main__":
    DataUpdate("arif.ahmad1881@gmail.com","Internship","Hi how are you")

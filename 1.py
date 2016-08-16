monthsOfYeat=( 'Jan','Feb','Mar','Apr','May','Jun','Aug','sep','Oct','Nov','Dec')
print(monthsOfYeat[0])
#元组
dictionaryName={'Peter':38,'John':51,'Peter':13}
print(dictionaryName['Peter'])
dictionaryName['M']=40
# print(dictionaryName)
# print(dictionaryName['M'])
del dictionaryName['M']
# print(dictionaryName)
# youName=input('输入用户名:')
# youAge=input('输入你的姓名:')
# print('你的用户名是:'+youName+'你的姓名是:'+youAge)
# try:
#     a=12/0
# except:
#     print('error')
import pymysql
try:
    conn=pymysql.connect('localhost','root')
    cur=conn.cursor()
    cur.execute('show databases;')
    cur.execute('use mysql;')
    cur.execute('show tables; ')
    cur.execute('select * from db;')
    res=cur.fetchall()
except Exception as e:
    pass
finally:
    cur.close()
    conn.close()

# print(res)
myList=['1','2','3']
myStr=''.join(myList)
# print(myStr)
def checkIfPrime(numberToCheck):
    for x in range(2,numberToCheck):
        if(numberToCheck%x==0):
            return ''
    return numberToCheck
cf=checkIfPrime(6)
def a(num):
    my_list=[x for x in range(2,num+1)]
    # print(my_list)
    for ele in my_list:
        temp=[]
        temp.append(checkIfPrime(ele))
        return temp


import this





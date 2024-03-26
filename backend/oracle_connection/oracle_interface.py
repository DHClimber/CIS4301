import getpass
import oracledb
import os

#credentials from .env file to connect with db

def sql_request(sql_command, bind_variables):
    HOST_NAME = os.environ["HOST_NAME"]
    USER_NAME = os.environ["USER_NAME"]
    USER_PW = os.environ["USER_PW"]

    ### DEBUG
    # print(f"""
    #     HOST_NAME = {HOST_NAME}
    #     USER_NAME = {USER_NAME}
    #     USER_PW = {USER_PW}
    #     """)

    un = USER_NAME
    cs = HOST_NAME
    pw = USER_PW

    #This is what interacts with the CISE oracle database
    try:
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql_command, bind_variables) 
                #formats to dictionary with columns for metadata
                columns = [col[0] for col in cursor.description]
                cursor.rowfactory = lambda *args: dict(zip(columns, args))
                db_response = cursor.fetchall()
                #combine with index
                index = 0
                response_dict = {}
                for line in db_response:
                    temp = str(index)
                    response_dict[temp] = line
                    index += 1    
                    #print(response_dict[temp]) -- FIXME         
                return response_dict

    except Exception as e:
        return e
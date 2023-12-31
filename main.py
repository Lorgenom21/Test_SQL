import psycopg2
from config import host, user, password, db_name

try:
    # connect
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name

    )
    connection.autocommit = True

    #cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

    # create a new table Account
    # with connection.cursor() as cursor:
    #
    #     cursor.execute('''CREATE TABLE Accounts(
    #            row_id int GENERATED ALWAYS AS IDENTITY ,
    #            parent_id int,                         -- row_id родительской записи
    #            number int,							  -- Номер лицевого счета
    #            type int,							  -- Тип записи (1 - Дом, 2- Квартира, 3 - Лицевой счет)
    #
    #            constraint PK_Accounts
    #               primary key (row_id),
    #            constraint FK_Accounts_Folder
    #               foreign key (parent_id)
    #               references Accounts(row_id)
    #               on delete no action
    #               on update no action
    #         );''')
    #
    # # create a new table Counters
    # with connection.cursor() as cursor:
    #     cursor.execute('''CREATE TABLE Counters(
    #         row_id int GENERATED ALWAYS AS IDENTITY ,
    #         name text not null,       -- Наименование счетчика
    #         acc_id int,						  -- row_id Лицевого
    #         service int not null,			  -- Услуга (100 - Холодная вода / 200 - Горячая Вода / 300 - Электричество /400 - Отопление)
    #         tarif int not null,				  -- Тарифность счетчика (1,2,3) (Показания по скольким тарифам могут быть на счетчике
    #
    #         constraint PK_Counters
    #            primary key (row_id),
    #         constraint FK_Counters
    #            foreign key (acc_id)
    #              references Accounts(row_id)
    #         );''')
    # # create a new table Meter_Pok
    # with connection.cursor() as cursor:
    #     cursor.execute('''CREATE TABLE Meter_Pok(
    #         row_id int GENERATED ALWAYS AS IDENTITY ,
    #         acc_id int,				-- row_id Лицевого
    #         counter_id int,			-- row_id счетчика
    #         value int not null,     -- Расход
    #         date date not null,		-- Дата показания
    #         month date not null,    -- Месяц показания
    #         tarif int not null,		-- Тариф (для 1 тарифного счетчика = 0 ; для 2 тарифного счетчика = 0 или 1 ; для 3 тарифного счетчика = 0 или 1 или 2 )
    #
    #         constraint PK_Meter_Pok
    #             primary key  (row_id),
    #         constraint FK_Meter_Acc
    #             foreign key (acc_id)
    #             references Accounts(row_id) ,
    #         constraint FK_Meter_Counters
    #             foreign key (counter_id)
    #             references Counters(row_id)
    #         );''')
    with connection.cursor() as cursor:
        cursor.execute("""
        insert into Accounts(parent_id,number,type)                                                            -- 1
        values(null,1,1);
        insert into Accounts(parent_id,number,type)                                                            -- 2
        values(1,1,2);
        insert into Accounts(parent_id,number,type)                                                            -- 3
        values(1,2,2);
        insert into Accounts(parent_id,number,type)                                                            -- 4
        values(1,3,2);
        insert into Accounts(parent_id,number,type)                                                            -- 5
        values(1,4,2);
        insert into Accounts(parent_id,number,type)                                                            -- 6
        values(2,111,3);
        insert into Accounts(parent_id,number,type)                                                            -- 7
        values(3,122,3);
        insert into Accounts(parent_id,number,type)                                                            -- 8
        values(4,133,3);
        insert into Accounts(parent_id,number,type)                                                            -- 9
        values(5,144,3);
        
        insert into Accounts(parent_id,number,type)                                                            -- 10
        values(null,2,1);
        
        insert into Accounts(parent_id,number,type)                                                            -- 11
        values(10,1,2);
        insert into Accounts(parent_id,number,type)                                                            -- 12
        values(10,2,2);
        insert into Accounts(parent_id,number,type)                                                            -- 13
        values(10,3,2);
        insert into Accounts(parent_id,number,type)                                                            -- 14
        values(10,4,2);
        insert into Accounts(parent_id,number,type)                                                            -- 15
        values(10,5,2);
        insert into Accounts(parent_id,number,type)                                                            -- 16
        values(10,6,2);
        insert into Accounts(parent_id,number,type)                                                            -- 17
        values(10,7,2);
        insert into Accounts(parent_id,number,type)                                                            -- 18
        values(10,8,2);
        
        insert into Accounts(parent_id,number,type)                                                            -- 19
        values(11,211,3);
        insert into Accounts(parent_id,number,type)                                                            -- 20
        values(12,222,3);
        insert into Accounts(parent_id,number,type)                                                            -- 21
        values(13,233,3);
        insert into Accounts(parent_id,number,type)                                                            -- 22
        values(14,244,3);
        insert into Accounts(parent_id,number,type)                                                            -- 23
        values(15,255,3);
        insert into Accounts(parent_id,number,type)                                                            -- 24
        values(16,266,3);
        insert into Accounts(parent_id,number,type)                                                            -- 25
        values(17,277,3);
        insert into Accounts(parent_id,number,type)                                                            -- 26
        values(18,288,3);
        
        insert into Accounts(parent_id,number,type)                                                            -- 27
        values(null,3,1);
        
        insert into Accounts(parent_id,number,type)                                                            -- 28
        values(27,301,3);
        
        insert into Accounts(parent_id,number,type)                                                            -- 29
        values(null,4,1);
        
        insert into Accounts(parent_id,number,type)                                                            -- 30
        values(29,401,3);
        insert into Accounts(parent_id,number,type)                                                            -- 31
        values(30,402,3);
        
        insert into Accounts(parent_id,number,type)                                                            -- 32
        values(null,5,1);
        insert into Accounts(parent_id,number,type)                                                            -- 33
        values(32,501,3);
        insert into Accounts(parent_id,number,type)                                                            -- 34
        values(32,502,3);
        """)
        # connection.commit()
        print("[INFO] Data was succefully")

    with connection.cursor() as cursor:
        cursor.execute("""
        insert into Counters (name,acc_id,service,tarif) -- 1 6,1
        values ('Счетчик на воду',6,100,1);
        insert into Counters (name,acc_id,service,tarif) -- 2 6,2
        values ('Счетчик на воду',6,200,1);
        insert into Counters (name,acc_id,service,tarif) -- 3 6,3
        values ('Счетчик на электричество',6,300,1);
        insert into Counters (name,acc_id,service,tarif) -- 4 6,4
        values ('Счетчик на отопление',6,400,1);
        
        insert into Counters (name,acc_id,service,tarif) -- 5 7,5
        values ('Счетчик на воду',7,100,1);
        insert into Counters (name,acc_id,service,tarif) -- 6 7,6
        values ('Счетчик на воду',7,200,1);
        insert into Counters (name,acc_id,service,tarif) -- 7 7,7
        values ('Счетчик на электричество',7,300,1);
        insert into Counters (name,acc_id,service,tarif) -- 8 7,8
        values ('Счетчик на отопление',7,400,1);
        
        insert into Counters (name,acc_id,service,tarif) -- 9 8,9
        values ('Счетчик на воду',8,100,1);
        insert into Counters (name,acc_id,service,tarif) -- 10 8,10
        values ('Счетчик на воду',8,200,1);
        insert into Counters (name,acc_id,service,tarif) -- 11 8,11
        values ('Счетчик на электричество',8,300,1);
        insert into Counters (name,acc_id,service,tarif) -- 12 8,12
        values ('Счетчик на отопление',8,400,1);
        
        insert into Counters (name,acc_id,service,tarif) -- 13 9,13
        values ('Счетчик на воду',9,100,1);
        insert into Counters (name,acc_id,service,tarif) -- 14 9,14
        values ('Счетчик на воду',9,200,1);
        insert into Counters (name,acc_id,service,tarif) -- 15 9,15
        values ('Счетчик на электричество',9,300,1);
        insert into Counters (name,acc_id,service,tarif) -- 16 9,16
        values ('Счетчик на отопление',9,400,1);
        
        insert into Counters (name,acc_id,service,tarif) -- 17 19,17
        values ('Счетчик на электричество',19,300,2);
        
        insert into Counters (name,acc_id,service,tarif) -- 18 20,18
        values ('Счетчик на электричество',20,300,2);
        
        insert into Counters (name,acc_id,service,tarif) -- 19 21,19
        values ('Счетчик на электричество',21,300,2);
        
        insert into Counters (name,acc_id,service,tarif) -- 20 22,20
        values ('Счетчик на электричество',22,300,2);
        
        insert into Counters (name,acc_id,service,tarif) -- 21 23,21
        values ('Счетчик на электричество',23,300,3);
        
        insert into Counters (name,acc_id,service,tarif) -- 22 24,22
        values ('Счетчик на электричество',24,300,3);
        
        insert into Counters (name,acc_id,service,tarif) -- 23 25,23
        values ('Счетчик на электричество',25,300,3);
        
        insert into Counters (name,acc_id,service,tarif) -- 24 26,24
        values ('Счетчик на электричество',26,300,3);
        
        insert into Counters (name,acc_id,service,tarif) -- 25 28,25
        values ('Счетчик на воду',28,100,1);
        insert into Counters (name,acc_id,service,tarif) -- 26 28,26
        values ('Счетчик на воду',28,200,1);
        insert into Counters (name,acc_id,service,tarif) -- 27 28,27
        values ('Счетчик на электричество',28,300,1);
        insert into Counters (name,acc_id,service,tarif) -- 28 28,28
        values ('Счетчик на отопление',28,400,1);
        
        insert into Counters (name,acc_id,service,tarif) -- 29 30,29
        values ('Счетчик на воду',30,100,1);
        insert into Counters (name,acc_id,service,tarif) -- 30 30,30
        values ('Счетчик на воду',30,200,1);
        insert into Counters (name,acc_id,service,tarif) -- 31 30,31
        values ('Счетчик на электричество',30,300,1);
        insert into Counters (name,acc_id,service,tarif) -- 32 30,32
        values ('Счетчик на отопление',30,400,1);
        
        insert into Counters (name,acc_id,service,tarif) -- 33 31,33
        values ('Счетчик на воду',31,100,1);
        insert into Counters (name,acc_id,service,tarif) -- 34 31,34
        values ('Счетчик на воду',31,200,1);
        insert into Counters (name,acc_id,service,tarif) -- 35 31,35
        values ('Счетчик на электричество',31,300,1);
        insert into Counters (name,acc_id,service,tarif) -- 36 31,36
        values ('Счетчик на отопление',31,400,1);
        
        insert into Counters (name,acc_id,service,tarif) -- 37 33,37
        values ('Счетчик на воду',33,100,1);
        insert into Counters (name,acc_id,service,tarif) -- 38 33,38
        values ('Счетчик на воду',33,200,1);
        insert into Counters (name,acc_id,service,tarif) -- 39 33,39
        values ('Счетчик на электричество',33,300,1);
        insert into Counters (name,acc_id,service,tarif) -- 40 33,40
        values ('Счетчик на отопление',33,400,1);
        
        insert into Counters (name,acc_id,service,tarif)  -- 41 34,41
        values ('Счетчик на воду',34,100,1);
        insert into Counters (name,acc_id,service,tarif)  -- 42 34,42
        values ('Счетчик на воду',34,200,1);
        insert into Counters (name,acc_id,service,tarif)  -- 43 34,43
        values ('Счетчик на электричество',34,300,1);
        insert into Counters (name,acc_id,service,tarif)  -- 44 34,44
        values ('Счетчик на отопление',34,400,1);
        """)

    with connection.cursor() as cursor:
        cursor.execute("""
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (6,1,100,'20230130','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (6,1,100,'20230225','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (6,2,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (6,2,50,'20230227','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (6,3,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (6,3,70,'20230227','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (6,3,10,'20230228','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (6,4,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (6,4,-50,'20230227','20230201',1);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (7,5,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (7,5,50,'20230227','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (7,6,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (7,6,55,'20230227','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (7,7,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (7,8,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (7,8,0,'20230227','20230201',1);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (8,9,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (8,9,900,'20230227','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (8,12,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (8,12,-1,'20230227','20230201',1);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (9,13,0,'20230221','20230201',1);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (9,14,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (9,14,0,'20230227','20230201',1);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (9,15,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (9,15,100,'20230228','20230201',1);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (9,16,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (9,16,10,'20230226','20230201',1);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (19,17,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (19,17,10,'20230227','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (19,17,50,'20230125','20230101',2);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (19,17,60,'20230227','20230201',2);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (20,18,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (20,18,10,'20230227','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (20,18,50,'20230125','20230101',2);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (20,18,0,'20230227','20230201',2);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (21,19,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (21,19,50,'20230227','20230201',2);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (22,20,100,'20230125','20230101',2);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (22,20,10,'20230227','20230201',2);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (23,21,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (23,21,10,'20230227','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (23,21,50,'20230125','20230101',2);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (23,21,0,'20230227','20230201',2);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (23,21,30,'20230125','20230101',3);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (23,21,3,'20230227','20230201',3);
        
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (24,22,200,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (24,22,-90,'20230227','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (24,22,50,'20230125','20230101',2);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (24,22,0,'20230227','20230201',2);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (24,22,30,'20230125','20230101',3);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (24,22,13,'20230227','20230201',3);
        
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (25,23,110,'20230227','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (25,23,70,'20230125','20230101',2);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (25,23,30,'20230125','20230101',3);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (25,23,15,'20230227','20230201',3);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (26,24,200,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (26,24,-90,'20230227','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (26,24,50,'20230125','20230101',2);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (26,24,50,'20230227','20230201',2);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (26,24,30,'20230125','20230101',3);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (26,24,13,'20230227','20230201',3);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (26,24,55,'20230228','20230201',3);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (28,25,200,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (28,25,40,'20230227','20230201',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (28,25,-90,'20230227','20230201',1);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (28,26,200,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (28,26,0,'20230227','20230201',1);
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (28,27,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (28,27,50,'20230227','20230201',1);
        
        
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (33,37,100,'20230125','20230101',1);
        insert into Meter_pok (acc_id,counter_id,value,date,month,tarif)
        values (33,37,50,'20230227','20230201',1);
        """)
    connection.close()
    print("[INFO] PostgreSQL connection closed")
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)



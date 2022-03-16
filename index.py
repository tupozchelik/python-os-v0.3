import os
import time
import socket
print("Python OS v0.2 copyright 2022, published under GNU.")
print("Welcome to Python OS!")
print("============================================")
name_x = input("введите свое имя ~> ")
password_x = input("введите пароль ~> ")
print("Отлично! Напишите help для более лучшей работой с ОС.")
name = name_x + "@" + os.name + " ~> "
while(os):                                           
    for i in range(1):
        search = input(name)
    if (search== 'help'):
        print("чтобы пользоваться командами, нужно писать только саму команду и ENTER")
        print("help - помощь с командами")
        print("cd - путь до ос")
        print("time - день, месяц, время и год")
        print("shutdown - выключение ОС")
        print("mkdir - создание папки")
        print("rmdir - удаление папки")
        print("word - текстовый редактор на 10 строк")
        print("start - запустить программу")
        print("info - информация о ОС")
        print("rename - изменить имя папки")
        print("ls - показать все файлы директории")
        print("ls -s - информация о файле")
        print("rmfile - удалить файл")
        print("calc - калькулятор")
        print("ipconfig - IPv4-адрес")
        print("browser - браузеры")
        print("")
    elif (search== 'cd'):
        print(os.getcwd())
        print("")
    if (search== 'time'):
        print(time.asctime( time.localtime(time.time()) ))
        print("")
    elif (search== 'shutdown'):
        print("shutdown..")
        quit("leave process")
    if (search== 'mkdir'):
        print(os.getcwd())
        print("пример пути папки: " + os.getcwd() + "\имя папки")
        dir_1 = input("введите путь папки ~> ")
        os.mkdir(dir_1)
    elif (search== 'rmdir'):
        print(os.getcwd())
        print("пример пути папки: " + os.getcwd() + "\имя папки")
        dir_2 = input("введите путь папки ~> ")
        os.rmdir(dir_2)
    if(search== 'rename'):
        print("пример пути папки: " + os.getcwd() + "\имя папки")
        rename_1 = input("введите имя папки, которые хотите изменить имя ~> ")
        rename_2 = input("введите новое имя папки ~> ")        
        os.rename(rename_1, rename_2)
    elif(search== 'word'):
        print(os.getcwd())
        print("пример пути для файла: " + os.getcwd() + "\файл.формат")
        print("а если хотите сохранить в директории с ос, введите просто название")
        file_1 = input("путь файла ~> ")
        write_1 = input("1 ")
        my_file = open(file_1, "w+")
        my_file.write(write_1 + " ")
        my_file.close()
        write_2 = input("2 ")
        my_file = open(file_1, "a+")
        my_file.write(write_2 + " ")
        my_file.close()
        write_3 = input("3 ")
        my_file = open(file_1, "a+")
        my_file.write(write_3 + " ")
        my_file.close()
        write_4 = input("4 ")
        my_file = open(file_1, "a+")
        my_file.write(write_4 + " ")
        my_file.close()
        write_5 = input("5 ")
        my_file = open(file_1, "a+")
        my_file.write(write_5 + " ")
        my_file.close()
        write_6 = input("6 ")
        my_file = open(file_1, "a+")
        my_file.write(write_6 + " ")
        my_file.close()
        write_7 = input("7 ")
        my_file = open(file_1, "a+")
        my_file.write(write_7 + " ")
        my_file.close()
        write_8 = input("8 ")
        my_file = open(file_1, "a+")
        my_file.write(write_8 + " ")
        my_file.close()
        write_9 = input("9 ")
        my_file = open(file_1, "a+")
        my_file.write(write_9 + " ")
        my_file.close()
        write_10 = input("310 ")
        my_file = open(file_1, "a+")
        my_file.write(write_10 + " ")
        my_file.close()
    if(search== 'start'):
         print("пример пути для файла: " + os.getcwd() + "\файл.формат")
         read_x = input("введите путь папки ~> ")
         os.startfile(read_x)
    elif(search== 'info'):
        print("Python OS v0.3 copyright 2022, published under GNU.")
        print("OS by tupozchelik / kto-to#9531")
        print("")
    if(search== 'ls'):
         print("все папки и файлы:", os.listdir())
    elif(search== 'ls -s'):
         ls_s_1 = input("введите имя файла ~> ")
         print("размер файла:", os.stat(ls_s_1).st_size, " байтов")
    if (search== 'rmfile'):
        print(os.getcwd())
        print("пример пути папки: " + os.getcwd() + "\имя папки")
        rmfile_1 = input("введите путь папки ~> ")
        os.remove(rmfile_1)
        print("")
    elif(search== 'calc'):
        print("пример операции: 1+1, 4*4, 5+1")
        print(eval(input()))
    if(search== 'ipconfig'):
        print("IPv4-адрес: ",socket.gethostbyname(socket.gethostname()))
        print("")
    elif(search== 'firefox'):
        os.startfile("firefox.exe")
    if(search== 'chrome'):
        os.startfile("chrome.exe")
    elif(search== 'browser'):
        print("firefox - включить браузер файрфокс")
        print("chrome - включить браузер хром")
        print("tor - включить браузер тор")
        print("")
    if(search== 'tor'):
        os.startfile("tor.exe.lnk")
        

    

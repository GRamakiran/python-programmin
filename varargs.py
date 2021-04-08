def intro(**data): #key and value
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))
intro(Firstname="Ganesh", Lastname="Babu", Age=25, Phone=1234567890)
intro(Firstname="Mary", Lastname="J", Email="jb@nomail.com", Country="India", Age=25, Phone=9876543210)
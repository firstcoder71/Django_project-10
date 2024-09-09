# crud operation
createlist = ['5','8','Hello world','learn more django']

while True:
    create_list = input("What do you want? Enter your choice : read / add / update / delete / quite :")
    if create_list == "quite":
        print("you exist from program")
        break

#Read your list
    elif create_list == 'read':
        print("congratulation you can find out your list :",createlist)



#add your list
    elif create_list == 'add':
        createlist.append(input("Please write your new element in your list :"))
        print("This is your new new element add list",createlist)

#Delete element from your list
    elif create_list == 'delete':
        dl = input("Enter your deleted element:  ")
        if dl in createlist:
            createlist.remove(dl)

        else:
            print("Does't match our records")
            print("This is your deleted elemet list: ",createlist)

#update element from your list
    elif create_list == 'update':
        up_wrong_ele = input("Write your wrong element name: ")
        up_right_ele = input("write your right element name: ")
        if up_wrong_ele in createlist:
            wr = createlist.index(up_wrong_ele)
            createlist[wr] = up_right_ele
        else:
            print("Does't match our record")
            print("This is your update list: ",createlist)


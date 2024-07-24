#immutable_var = 1, 2, 3, "apple", False
#print(immutable_var)
#immutable_var[4] = True
#Ошибка сообщает что картеж не поддерживает обращение по элементам
#Кортеж  зачастую используется для списков в которых должно оставаться все неизменным
mutable_list = ["Яблоко", "Сахар", "Велосипед"]
print(mutable_list)
mutable_list[0] = "Коза"
print(mutable_list)
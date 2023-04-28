def main(hex_data):
    # преобразуем шестнадцатиричные данные в двоичные
    bin_data = bin(int(hex_data, 16))[2:].zfill(len(hex_data) * 4)

    # разбиваем двоичное представление на отдельные битовые поля
    k1 = bin_data[23:27]
    k2 = bin_data[27:36]
    k4 = bin_data[0:5]
    k5 = bin_data[13:23]   # + bin_data[18:23]

    # преобразуем битовые поля в десятичные и объединяем их в одну строку
    result = int(k4, 2) + int(k5, 2) * 10 + int(k1, 2) * 100 + int(k2, 2) * 1000

    return str(result)

print(main('0x9c7421314'))





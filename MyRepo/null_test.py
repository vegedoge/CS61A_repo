import csv


# with open('example.csv', 'wb') as file:
#     file.write(b'Name,Age,Gender\n')
#     file.write(b'John,25,Male\n')
#     file.write(b'\0,\0,\0\n')  # \x00 表示 NULL 字节
#     file.write(b'Bob,30,\n')

I2C_file = "2024-02-29-I2C_message.csv"
try:
    with open (I2C_file, 'r') as f :
        reader = csv.reader(f)
        num_rows = sum(1 for row in reader)
except Exception as e:
    print(f'csv bug: {e}')
    with open(I2C_file, 'r') as f:
        lines = f.readlines()
    with open(I2C_file, 'w') as f:
        f.writelines(lines[:-1])

# print(num_rows)
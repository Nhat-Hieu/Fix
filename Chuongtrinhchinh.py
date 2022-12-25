import os.path
import pickle
import random
#Câu a)
def list(a,b,n):
  # Sinh ngẫu nhiên list số thực trong khoảng [a, b] với độ dài n
  return [random.uniform(a, b) for i in range(n)]
  # Sinh ngẫu nhiên list số thực trong khoảng [1, 10] với độ dài là 5
list_moi = list(1,10,5)
print("List số thực là:",list_moi)

#Câu b)
# Ghi danh sách vào tập tin
def write_list_to_file(list_, file_name):
    # Mở tập tin với chế độ ghi
    with open(file_name, 'w') as file:
        # Duyệt qua từng phần tử trong danh sách
        for item in list_:
            # Ghi phần tử vào tập tin, thêm dòng mới sau mỗi phần tử
            file.write(str(item) + '\n')
numbers = list_moi
write_list_to_file(numbers, 'Doan.txt')

#Câu c)
def sort_list(numbers, reverse=False):
  # Sắp xếp danh sách các số theo chiều tăng dần hoặc giảm dần
  return sorted(numbers, reverse=reverse)
list_so_thuc = (list_moi)
# Sắp xếp theo chiều giảm dần
giam_dan = sort_list(list_so_thuc, reverse=True)
print("Sắp xếp theo chiều giảm dần là: ",giam_dan)

#Câu d)
# Ghi danh sách vào tập tin
def write_list_to_file(list_, file_name):
    # Mở tập tin với chế độ ghi
    with open(file_name, 'w') as file:
        # Duyệt qua từng phần tử trong danh sách
        for item in list_:
            # Ghi phần tử vào tập tin, thêm dòng mới sau mỗi phần tử
            file.write(str(item) + '\n')
numbers = giam_dan
write_list_to_file(numbers, 'Doan2.txt')

#Câu e)
#2.3
def timkiem(list, n):
  # Tìm số n trong danh sách list
  if n in list:
    # Nếu tìm thấy, lấy tất cả các vị trí có giá trị bằng với n
    vitri = [i for i, x in enumerate(list) if x == n]
    # In ra các vị trí tìm thấy
    print(f"Số {n} tìm thấy tại vị trí {vitri} trong list.")
  else:
    # Nếu không tìm thấy, in ra thông báo
    print(f"Không tìm thấy số {n} trong list.")

list = giam_dan
timkiem(list, 6)

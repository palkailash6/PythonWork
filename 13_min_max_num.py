class MinMaxDemonstration:
  def max_min(data):
    max_num = data[0]
    min_num = data[0]

    for num in data:
      if num > max_num:
        max_num = num
      elif num < min_num:
        min_num = num
    print("Maximum number : ", max_num, "Minimum number : ", min_num)

mx = MinMaxDemonstration
mx.max_min([185, 10, 15, 40, 0, 42, 17, 28, 75])
# print(max_min([185, 10, 15, 40, -1, 42, 17, 28, 75]))
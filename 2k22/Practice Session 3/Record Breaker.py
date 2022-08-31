def number_of_record_breaking_days(number_of_days, vistors):
  record_breaking_days = 0
  if number_of_days == 1: #first and last
    return 1
  index = 0
  max_num = -1
  while index+1<number_of_days:
      while index+1<number_of_days and vistors[index+1]>vistors[index]:
          index+=1
      if (index ==0 and vistors[index]>vistors[index+1]) or (index+1 == number_of_days and vistors[index]>vistors[index-1]) or (vistors[index]>vistors[index-1] and vistors[index]>vistors[index+1]):
        if vistors[index]>max_num:
          record_breaking_days+=1
          max_num=vistors[index]
      if index+1<number_of_days and vistors[index]>=vistors[index+1]:
        index+=1
  
  return record_breaking_days
def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1, 1):
    number_of_days = int(input())
    vistors = list(map(int, input().split()))

    ans = number_of_record_breaking_days(number_of_days, vistors)

    print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
  main()

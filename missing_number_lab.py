def find_missing(list1, list2):
    list3 = []
    l1 = len(list1)
    l2 = len(list2)
    for x in range(len(list1)):
        for y in range(len(list2)):
            if len(list1) ==0:
               return 0
            if len(list2) == 0:
               return 0
            elif l1 ==l2:
                  return 0
            elif x == y:
               return 0
            elif l1 ==0 and l2 ==0:
               return 0
               break        
            else:
               list3.append(1)
    return list3
              


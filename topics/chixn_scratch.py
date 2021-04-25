
def sort_by_length(str):
    results_list = []
    array_str = str.split()
    i = 0
    temp = []
    while i < (len(array_str) - 1):
    # while i < (len(array_str)- i - 1):

        j = 0
        while j < (len(array_str) - i - 1):
        # while j < (len(array_str) - 1):
            if len(array_str[j]) > len(array_str[j+1]):
                temp = array_str[j]
                array_str[j] = array_str[j+1]
                array_str[j+1] = temp
                print(array_str)
            j += 1
        i += 1
    print(array_str)


sort_by_length("love great awesome words I")

def multiply(x, y):
    return x * y

def main():
    nums1 = range(0, 10)
    nums2 = range(10, 0, -1)
    
    #with map
    for multiple in map(multiply, nums1, nums2):
        print(multiple)
    
    #with list comp
    print([multiply(nums1[i],nums2[i]) for i in range(len(nums1))])


main()
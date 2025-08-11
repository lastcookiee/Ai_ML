def TOH(n , s , d , a):
    if n==1:
        print("move disk 1 from ", s , "to", d )
        return
    TOH(n-1, s , a , d)
    print("move disk", n ,"from", s , "to", d )
    TOH(n-1, a , d ,s)

n = 5
TOH(n , "A", "B", "C")
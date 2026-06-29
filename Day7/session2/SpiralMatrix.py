#leetcode54
def spiralOrd(matrix,m,n):
    result=[]
    top=0
    right=len(matrix)-1
    bottom=len(matrix)-1
    left=0
    while left<=right and top<=bottom:
        #first row
        for i in range(left,right+1):
            print(matrix[top][i],end=' ')
        top+=1
        #right column
        for i in range(top,bottom+1):
            print(matrix[i][bottom],end=' ')
        right-=1
        #bottom row
        if top<=bottom:
            for i in range(right,left-1,-1):
                 print(matrix[bottom][i],end=' ')
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                print(matrix[i][left],end=' ')
            left+=1
    return 0
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
result=print(spiralOrd(matrix,3,3))



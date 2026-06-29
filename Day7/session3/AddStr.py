#leetcode415
def addStrings(num1, num2) :
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        x = ord(num1[i]) - ord('0') if i >= 0 else 0 #ord =convert str to int -substract with 0
        y = ord(num2[j]) - ord('0') if j >= 0 else 0 #ascii of 0-48

        total = x + y + carry
        result.append(str(total % 10))
        carry = total // 10

        i -= 1
        j -= 1

    return "".join(result[::-1])
num1=input()
num2=input()
print(addStrings(num1,num2))
# Dynamic Programming
Decoding
A=1, B=2
AB=12->'L'
26 alphabets
   ___|_____
   |        |
(1-9)      (10-26)
226=BBC,VF,BZ
dp[null]-> do nothing->which is also an operation
0|1|2|3 -> no:input
1|1|2|3 -> no of ways of decoding
1. initialization-info given in the question
2. if the inputs are single digits-then the output only have 1 way to decode
3. current_one=(i-1)+(i-2)


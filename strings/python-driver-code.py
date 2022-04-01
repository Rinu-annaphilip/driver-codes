# Python Driver Code

def solve(s: str) -> chr:
  # Your code goes here
  # s is the given input string
  i=0
  for j in range(T):
      l1[j]=[]
      l2[j]=[]
      while(i<len(s)-1):
        count=1
        while s[j][i]==s[j][i+1]:
          i+=1
          count+=1
          if i+1 == len(s[j]):
            break
        l1[j].append(str(count)+str(s[j][i]))
        i+=1
    l2[j]=sorted(l1[j])
  for i in range(T):
    answer=(l2[i][-2][1]) 
  return answer

# The following snippet reads the input in the required format. 
# Just complete the solve function above. 

T = int(input())
for i in range(T):
  test_case[i] = input()
  answer = solve(test_case)
  print(answer)

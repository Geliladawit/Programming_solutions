# Problem: D - Electric Mayhem - https://codeforces.com/gym/605795/problem/D

s = input()
st = []
for i in s:
    if st and st[-1] == i:
        st.pop()
    else:
        st.append(i)
if st:
    print("No")
else:
    print("Yes")
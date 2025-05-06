# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

st = []
def decimal_to_binary(n):
  if n == 0:
    st.reverse()
    s = "".join(st)
    return s
  st.append( str(n % 2))
  return decimal_to_binary(n//2)
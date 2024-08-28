import re

# re for number 1 followed by 0 or more numbers
print("\n\n#re for number 1 followed by 0 or more numbers")
re_str = r"1[0-9]*"
print(re.match(re_str, "1111"))
print(re.match(re_str, "2222"))  # not match because it does not start with 1
print(re.match(re_str, "1"))
print(re.match(re_str, "11"))

# re for number 1 or 2 followed by 2 or 6 numbers
print("\n\n#re for number 1 or 2 followed by 2 or 6 numbers")
re_str = r"[12][0-9]{2,6}"
print(re.match(re_str, "1"))  # not match because it does not have 2 or 6 numbers
print(re.match(re_str, "11"))  # not match because it does not have 2 or 6 numbers
print(re.match(re_str, "1112"))
print(re.match(re_str, "2"))  # not match because it does not have 2 or 6 numbers
print(re.match(re_str, "22"))  # not match because it does not have 2 or 6 numbers
print(re.match(re_str, "2221"))

# re for cuit number
print("\n\n#re for cuit number")
re_str = r"\d{2}-[0-9]{8}-[0-9]"
print(re.match(re_str, "11-11111111-1"))
print(re.match(re_str, "11-11111111-11"))  # not match because it has 2 numbers at the end
print(re.match(re_str, "11-1111111-1"))  # not match because it has 7 numbers in the middle
print(re.match(re_str, "11-111111111-1"))  # not match because it has 9 numbers in the middle

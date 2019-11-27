
import re
test_str = "12*(34-5)+(-10)"
# test_str = test_str.replace("(10-6/3)","8")
# test_str1 = "-"
# test_str += test_str1
# print(test_str)
# test_str = test_str.endswith(("8","+",")"))

test_re = re.split("[()]",test_str)

print(test_re)
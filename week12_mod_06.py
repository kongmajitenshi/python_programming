# week12_mod_06.py
# p.404 모두 가져오기의 문제...
# 01과 03중 어떤 모듈의 add와 div가 사용되는지 명확하지 않음.
from week12_mod_01 import *
from week12_mod_03 import *


result1 = add(2, 3)
result2 = div(2, 0)
print(f"결과: {result1} {result2}")
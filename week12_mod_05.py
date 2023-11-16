# week12_mod_05.py
# p.404(1)
# from week12_mod_03 import add, div 이것도 ㄱㅊ 근데 가로로 길게(컬럼 길게) 쓰면 구림
# from week12_mod_03 import * 이것도 가능은 한데 다른 모듈이랑 겹칠 수도 있어서 비추함.
from week12_mod_03 import add
from week12_mod_03 import div


result1 = add(2, 3)
result2 = div(2, 0)
print(f"결과: {result1} {result2}")
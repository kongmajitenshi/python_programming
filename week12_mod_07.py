# week12_mod_07.py
# p.405
import week12_mod_03 as week12
from week12_mod_03 import div as d # 모듈끼리 충돌 방지

result1 = week12.add(2, 3)
result2 = d(2, 0)

print(f"결과: {result1} {result2}")
# week12_mod_03.py

def add(a, b):
    return a + b

def div(a, b):
    try:
        return a / b
    except:
        return None
if __name__ == "__main__": # 내가 시작하는 모듈일 때만 실행함.
    print(f"내 이름: {__name__}") # 내 모듈의 이름을 가지고있음. 진입점 판별시 사용.
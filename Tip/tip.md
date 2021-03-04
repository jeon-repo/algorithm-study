### 코딩 문법 표준
- PEP 8 문서를 통해 파이썬 코딩 문법 표준 확인이 가능
- 리스트 최소, 최대 값을 찾을 때, sorted() 함수를 사용하는 것이 min(), max() 함수를 사용하는 것보다 시간이 오래 걸림
- input() 보다 빠른 속도로 입력을 받는 방법은  
'sys.stdin.readline': return을 함수로 사용(람다처럼),  
'sys.stdin.readline().rstrip()': return을 변수로 사용
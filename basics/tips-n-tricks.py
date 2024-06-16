# f-strings 

n: int = 1_000_000_000
m: int = 1e9
l: int = 1000000000

print(f'{l:_}')
print(f'{l:,}')

var: str = 'test'

print(f'{var:_>20}:')
print(f'{var:#<20}:')
print(f'{var:|^20}:')

from datetime import datetime

now: datetime = datetime.now()
print(f'{now:%d.%m.%y (%H:%M:%S)}')
print(f'{now:%c}')
print(f'{now:%I%p}')

f: float = 1234.56789
print(f'{f:.2f}')
print(f'{f:,.3f}')

a = 5
b = 10

print(f'{a + b = }')
example1 = {}
example1.setdefault('axmc', []).append('apple')
example1.setdefault('b', []).append('boots')
example1.setdefault('c', []).append('cat')
example1.setdefault('axxmx', []).append('ant')
example1.setdefault('axx', []).append('apple')
example1.setdefault('axx', []).append('aple')
example1.update(b='axxapple')
print(example1)
M = input()
m_list = input().split(' ')
N = input()
n_list = input().split(' ')

m_list = [int(i) for i in m_list]
n_list = [int(i) for i in n_list]

m_set = set(m_list)
n_set = set(n_list)

sym_diff = m_set.difference(n_set)
sym_diff.update(n_set.difference(m_set))

sym_diff = sorted(sym_diff)

for value in sym_diff:
    print(value)

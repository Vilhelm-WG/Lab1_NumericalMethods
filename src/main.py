from scipy.optimize import toms748
from equations import f_alg, alg_interval, f_trans, trans_interval

# Задана точність
EPS = 0.001

print("=== Комбінований метод (SciPy: toms748) ===")

# 1. Алгебраїчне рівняння
a, b = alg_interval
root_alg, result_alg = toms748(f_alg, a=a, b=b, xtol=EPS, full_output=True)
print(f"Алгебраїчне рівняння:")
print(f"  Корінь: {root_alg:.4f}")
print(f"  Нев'язка: {f_alg(root_alg):.8f}")
print(f"  Ітерацій: {result_alg.iterations}\n")

# 2. Трансцендентне рівняння
a_t, b_t = trans_interval
root_trans, result_trans = toms748(f_trans, a=a_t, b=b_t, xtol=EPS, full_output=True)
print(f"Трансцендентне рівняння:")
print(f"  Корінь: {root_trans:.4f}")
print(f"  Нев'язка: {f_trans(root_trans):.8f}")
print(f"  Ітерацій: {result_trans.iterations}")
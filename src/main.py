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
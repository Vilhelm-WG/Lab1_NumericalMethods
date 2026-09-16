import numpy as np

# --- Алгебраїчне рівняння: x^6 - 3x^2 + x - 1 = 0 ---
f_alg = lambda x: x**6 - 3*x**2 + x - 1

# Перша та друга похідні (знадобляться Діані та для комбінованого методу)
df_alg = lambda x: 6*x**5 - 6*x + 1
d2f_alg = lambda x: 30*x**4 - 6

# Відрізок ізоляції
alg_interval = (1.0, 2.0)

# --- Трансцендентне рівняння: ln(7.62x) + 2.5 - 8.59x = 0 ---
f_trans = lambda x: np.log(7.62 * x) + 2.5 - 8.59 * x

# Перша та друга похідні
df_trans = lambda x: 1/x - 8.59
d2f_trans = lambda x: -1/(x**2)

# Відрізок ізоляції
trans_interval = (0.1, 1.0)
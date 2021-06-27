import numpy as np
import numpy_financial as npf
rate, cashflows = 0.08, [-40_000, 5_000, 8_000, 12_000, 30_000]
calc=npf.npv(rate, cashflows).round(5)
print(calc)
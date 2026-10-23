![CI Pipeline](https://github.com/stefan931025-sys/Discretionary-Pairs-Execution-Desk/actions/workflows/ci.yml/badge.svg)

# Discretionary Pairs Execution Desk

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description
Interactive terminal dashboard combining statistical cointegration, mean-reverting statistical arbitrage pairs execution, and GARCH volatility regime filters.

---

## 📌 Features & Quantitative Methodology

* **Statistical Cointegration & Z-Score Engine:** Tracks spread divergence across asset pairs, triggering trade entry signals at user-defined Z-score cutoffs (e.g., $|Z| \ge 2.0$).
* **GARCH Volatility Filter:** Dynamically assesses market volatility regimes to suppress trade execution during binary catalyst events or structural regime shifts.
* **Terminal Interface:** Interactive CLI and dashboard interface located in `src/dashboard.py` for real-time risk monitoring and order execution control.

---

## 🚀 Quickstart

```bash
# Clone repository
git clone [https://github.com/stefan931025-sys/Discretionary-Pairs-Execution-Desk.git](https://github.com/stefan931025-sys/Discretionary-Pairs-Execution-Desk.git)
cd Discretionary-Pairs-Execution-Desk

# Run interactive execution dashboard
python main.py

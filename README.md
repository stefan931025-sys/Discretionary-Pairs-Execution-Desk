# Discretionary Pairs Execution Desk

![CI Workflow](https://github.com/stefan931025-sys/Discretionary-Pairs-Execution-Desk/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Interactive terminal dashboard combining statistical cointegration, mean-reverting statistical arbitrage pairs execution, and GARCH volatility regime filters.

## 🚀 Features & Quantitative Methodology

* **Statistical Cointegration & Z-Score Engine:** Tracks spread divergence across asset pairs, triggering trade entry signals at user-defined Z-score cutoffs ($\vert{}Z\vert{} \ge 2.0$).
* **GARCH Volatility Filter:** Dynamically assesses market volatility regimes to suppress trade execution during binary catalyst events or structural regime shifts.
* **Terminal Interface:** Interactive CLI and dashboard interface located in `core/` for real-time risk monitoring and order execution control.

---

## 📊 Mathematical Specifications

### 1. Spread and Z-Score Calculation

$$S_t = Y_t - \gamma Y_{2,t}$$

$$Z_t = \frac{S_t - \mu_t}{\sigma_t}$$

Where $\gamma$ is the hedge ratio derived via Ordinary Least Squares (OLS) or cointegration regression, and $\mu_t, \sigma_t$ represent the rolling mean and standard deviation of the spread.

### 2. GARCH(1,1) Volatility Filtering

$$\sigma_t^2 = \omega + \alpha \varepsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$

Used to filter out high-variance macro regimes where linear mean reversion breaks down.

---

## 📁 Repository Structure

```text
Discretionary-Pairs-Execution-Desk/
├── .devcontainer/     # Devcontainer configuration for Codespaces
├── .github/
│   └── workflows/
│       └── ci.yml     # GitHub Actions automated test workflow
├── core/
│   └── dashboard.py   # Interactive CLI & pairs execution dashboard
├── tests/
│   └── test_pairs_execution.py # Automated pytest suite
├── main.py            # Main execution pipeline script
├── repo_auditor.py    # Static AST analysis governance tool
├── requirements

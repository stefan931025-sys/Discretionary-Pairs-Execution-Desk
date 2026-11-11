# Discretionary Pairs Execution Desk

[![Discretionary Pairs Execution Desk CI](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/stefan931025-sys/Discretionary-Pairs-Execution-Desk)
[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Interactive terminal dashboard combining statistical cointegration, mean-reverting statistical arbitrage pairs execution, and GARCH volatility regime filters.

---

## Features & Quantitative Methodology

* **Statistical Cointegration & Z-Score Engine:** Tracks spread divergence across asset pairs, triggering trade entry signals at user-defined $Z\text{-score}$ cutoffs (e.g., $\vert{}Z\vert{} \geq 2.0$).
* **GARCH Volatility Filter:** Dynamically assesses market volatility regimes to suppress trade execution during binary catalyst events or structural regime shifts.
* **Terminal Interface:** Interactive CLI and dashboard interface located in `core/` for real-time risk monitoring and order execution control.

---

## Mathematical Specifications

### 1. Spread and Z-Score Calculation
$$S_t = Y_{1,t} - \gamma Y_{2,t}$$
$$Z_t = \frac{S_t - \mu_S}{\sigma_S}$$
Where $\gamma$ is the hedge ratio derived via Ordinary Least Squares (OLS) or cointegration regression, and $\mu_S, \sigma_S$ represent the rolling mean and standard deviation of the spread.

### 2. GARCH(1,1) Volatility Filtering
$$\sigma_t^2 = \omega + \alpha \varepsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$
Used to filter out high-variance macro regimes where linear mean reversion breaks down.

---

## System Architecture & Data Flow

```text
+-----------------------------------------------------------------------------------+
|                        REAL-TIME TICK & ASSET PRICE FEEDS                         |
|                     (High-Frequency Pair Pricing Streams)                         |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                        PAIRS COINTEGRATION & GARCH ENGINE                         |
|  * OLS / Cointegration Hedge Ratio ($\gamma$)  * Rolling Spread Z-Score Calculation|
|  * GARCH Conditional Variance Regime Filter   * Signal Generation Triggers        |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                          INTERACTIVE EXECUTION TERMINAL                           |
|            (Risk Limits, Order Entry, & Position Monitoring Dashboard)            |
+-----------------------------------------------------------------------------------+

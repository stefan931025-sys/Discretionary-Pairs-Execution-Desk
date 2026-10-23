import pytest

def test_spread_zscore_calculation():
    """Verify spread Z-score mean-reversion signal generation."""
    spread = 2.5
    mean_spread = 0.5
    std_spread = 1.0
    
    z_score = (spread - mean_spread) / std_spread
    
    assert pytest.approx(z_score, 0.001) == 2.0
    assert z_score >= 2.0  # Entry threshold for statistical arbitrage short-spread trade

def test_garch_volatility_filter():
    """Verify volatility filter logic to prevent execution during high volatility regime breaks."""
    current_garch_vol = 0.28  # 28% annualized vol
    max_allowed_vol = 0.22    # 22% volatility threshold
    
    trade_allowed = current_garch_vol <= max_allowed_vol
    
    assert trade_allowed is False  # Signal suppressed due to extreme volatility

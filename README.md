# QuantPak - Quantitative Finance Analysis Platform

A comprehensive Python package for quantitative finance analysis, backtesting, and visualization. QuantPak provides a robust framework for developing, testing, and deploying trading strategies with professional-grade risk management and performance analysis tools.

## 🚀 Features

### Data Management
- **Multi-source data providers**: Yahoo Finance, Alpha Vantage, FRED, Quandl
- **Data processing utilities**: Cleaning, resampling, technical indicators
- **Efficient storage**: HDF5, CSV, caching mechanisms
- **Real-time data streaming**: Live market data integration

### Strategy Development
- **Base strategy framework**: Standardized signal generation
- **Technical analysis**: Moving averages, RSI, MACD, Bollinger Bands
- **Quantitative strategies**: Momentum, mean reversion, factor models
- **Machine learning**: Integration with scikit-learn and TensorFlow

### Backtesting Engine
- **Vectorized backtesting**: Fast strategy evaluation
- **Transaction costs**: Realistic cost modeling
- **Portfolio simulation**: Multi-asset portfolio tracking
- **Risk management**: Position sizing, stop-loss integration

### Portfolio Management
- **Asset allocation**: Equal weight, market cap, risk parity
- **Portfolio optimization**: Modern portfolio theory, Black-Litterman
- **Rebalancing**: Automated portfolio rebalancing
- **Performance attribution**: Factor-based attribution analysis

### Risk Management
- **Value at Risk (VaR)**: Parametric, historical, Monte Carlo
- **Stress testing**: Scenario analysis and stress testing
- **Risk monitoring**: Real-time risk tracking
- **Factor models**: Multi-factor risk decomposition

### Visualization
- **Interactive charts**: Plotly, Bokeh integration
- **Performance dashboards**: Streamlit and Dash apps
- **Risk reports**: Automated risk reporting
- **Research notebooks**: Jupyter notebook templates

## 📦 Installation

```bash
# Clone the repository
git clone <repository-url>
cd quantpak

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## 🏗️ Project Structure

```
quantpak/
├── quantpak/                 # Main package
│   ├── data/                # Data acquisition and processing
│   ├── strategies/          # Trading strategies
│   ├── backtesting/         # Backtesting framework
│   ├── portfolio/           # Portfolio management
│   ├── risk/                # Risk management
│   ├── performance/         # Performance analysis
│   ├── models/              # Factor and forecasting models
│   ├── stats/               # Statistical utilities
│   ├── visuals/             # Visualization tools
│   └── utils/               # Utility functions
├── data/                    # Data storage
│   ├── raw/                # Raw data files
│   ├── processed/          # Processed data
│   └── external/           # External data sources
├── research/               # Jupyter notebooks
├── strategies/             # Strategy implementations
├── backtesting/           # Backtest configurations
├── config/                # Configuration files
├── tests/                 # Unit tests
├── docs/                  # Documentation
├── examples/              # Example scripts
└── scripts/               # Utility scripts
```

## 🚀 Quick Start

### 1. Data Acquisition

```python
from quantpak.data import YahooProvider

# Initialize data provider
provider = YahooProvider()

# Fetch historical data
data = provider.get_data(['AAPL', 'GOOGL'], period='1y')
print(data.head())
```

### 2. Strategy Development

```python
from quantpak.strategies import BaseStrategy, SignalType, Signal
from quantpak.data import TechnicalIndicators
import pandas as pd

class MovingAverageCrossover(BaseStrategy):
    def __init__(self, short_window=20, long_window=50):
        super().__init__("MA Crossover", {
            'short_window': short_window,
            'long_window': long_window
        })
    
    def generate_signals(self, data):
        short_ma = TechnicalIndicators.sma(data['Close'], self.get_parameter('short_window'))
        long_ma = TechnicalIndicators.sma(data['Close'], self.get_parameter('long_window'))
        
        signals = []
        for i in range(len(data)):
            if short_ma.iloc[i] > long_ma.iloc[i]:
                signal = Signal(
                    timestamp=data.index[i],
                    symbol='AAPL',
                    signal_type=SignalType.BUY
                )
                signals.append(signal)
        
        return signals
```

### 3. Backtesting

```python
from quantpak.backtesting import BacktestEngine

# Initialize strategy
strategy = MovingAverageCrossover(short_window=20, long_window=50)

# Run backtest
engine = BacktestEngine(initial_capital=100000)
results = engine.run_backtest(strategy, data)

# Analyze results
print(f"Total Return: {results.total_return:.2%}")
print(f"Sharpe Ratio: {results.sharpe_ratio:.2f}")
print(f"Max Drawdown: {results.max_drawdown:.2%}")
```

### 4. Portfolio Optimization

```python
from quantpak.portfolio import PortfolioOptimizer
from quantpak.data import ReturnCalculator

# Calculate returns
returns = ReturnCalculator.simple_returns(data['Close'])

# Optimize portfolio
optimizer = PortfolioOptimizer()
weights = optimizer.optimize_sharpe(returns)

print("Optimal Weights:")
for symbol, weight in weights.items():
    print(f"{symbol}: {weight:.2%}")
```

## 📊 Examples

Check out the `examples/` directory for comprehensive examples:

- **Basic Strategy Development**: Simple moving average strategies
- **Advanced Backtesting**: Multi-asset portfolio backtesting
- **Risk Analysis**: VaR calculation and stress testing
- **Portfolio Optimization**: Mean-variance optimization
- **Performance Analysis**: Comprehensive performance attribution

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=quantpak --cov-report=html
```

## 📚 Documentation

Detailed documentation is available in the `docs/` directory:

- **API Reference**: Complete API documentation
- **User Guide**: Step-by-step tutorials
- **Strategy Development**: Guide to creating custom strategies
- **Best Practices**: Recommended practices for quantitative research

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on:

- Code standards and style
- Testing requirements
- Pull request process
- Issue reporting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

- **Documentation**: Check the `docs/` directory
- **Issues**: Report bugs and request features on GitHub
- **Discussions**: Join our community discussions

## 🗺️ Roadmap

- [ ] Real-time trading integration
- [ ] Alternative data sources
- [ ] Advanced ML strategies
- [ ] Cloud deployment tools
- [ ] Mobile dashboard
- [ ] API endpoints

---

**Disclaimer**: This software is for educational and research purposes only. Past performance does not guarantee future results. Always conduct thorough testing before deploying any trading strategy with real capital.
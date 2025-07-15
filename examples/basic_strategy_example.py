"""
Basic Strategy Example - Moving Average Crossover

This example demonstrates how to:
1. Fetch financial data
2. Create a simple trading strategy
3. Run a backtest
4. Analyze results
"""

import pandas as pd
import numpy as np
from quantpak.data import YahooProvider, TechnicalIndicators
from quantpak.strategies.base import BaseStrategy, Signal, SignalType
from quantpak.backtesting import BacktestEngine
from quantpak.performance import PerformanceMetrics
import matplotlib.pyplot as plt


class MovingAverageCrossover(BaseStrategy):
    """
    Simple Moving Average Crossover Strategy
    
    Buy when short MA crosses above long MA
    Sell when short MA crosses below long MA
    """
    
    def __init__(self, short_window=20, long_window=50):
        super().__init__("MA Crossover", {
            'short_window': short_window,
            'long_window': long_window
        })
    
    def generate_signals(self, data):
        """Generate trading signals based on MA crossover."""
        short_window = self.get_parameter('short_window')
        long_window = self.get_parameter('long_window')
        
        # Calculate moving averages
        short_ma = TechnicalIndicators.sma(data['Close'], short_window)
        long_ma = TechnicalIndicators.sma(data['Close'], long_window)
        
        signals = []
        
        # Generate signals where we have enough data
        for i in range(long_window, len(data)):
            current_short = short_ma.iloc[i]
            current_long = long_ma.iloc[i]
            prev_short = short_ma.iloc[i-1]
            prev_long = long_ma.iloc[i-1]
            
            # Golden cross - buy signal
            if prev_short <= prev_long and current_short > current_long:
                signal = Signal(
                    timestamp=data.index[i],
                    symbol='AAPL',  # Assuming single asset for simplicity
                    signal_type=SignalType.BUY,
                    price=data['Close'].iloc[i],
                    strength=1.0
                )
                signals.append(signal)
            
            # Death cross - sell signal
            elif prev_short >= prev_long and current_short < current_long:
                signal = Signal(
                    timestamp=data.index[i],
                    symbol='AAPL',
                    signal_type=SignalType.SELL,
                    price=data['Close'].iloc[i],
                    strength=1.0
                )
                signals.append(signal)
        
        return signals


def main():
    """Run the basic strategy example."""
    
    print("🚀 QuantPak Basic Strategy Example")
    print("=" * 50)
    
    # 1. Fetch Data
    print("📊 Fetching data...")
    provider = YahooProvider()
    data = provider.get_data('AAPL', period='2y')
    print(f"Fetched {len(data)} data points for AAPL")
    
    # 2. Create Strategy
    print("\n📈 Creating strategy...")
    strategy = MovingAverageCrossover(short_window=20, long_window=50)
    
    # 3. Generate Signals
    print("🔍 Generating signals...")
    strategy.initialize(data)
    signals = strategy.generate_signals(data)
    print(f"Generated {len(signals)} trading signals")
    
    # 4. Display Signal Summary
    buy_signals = [s for s in signals if s.signal_type == SignalType.BUY]
    sell_signals = [s for s in signals if s.signal_type == SignalType.SELL]
    
    print(f"  - Buy signals: {len(buy_signals)}")
    print(f"  - Sell signals: {len(sell_signals)}")
    
    # 5. Calculate Simple Returns
    print("\n📊 Calculating simple strategy returns...")
    
    # For demonstration, calculate returns assuming we follow signals
    returns = []
    position = 0  # 0 = no position, 1 = long, -1 = short
    entry_price = None
    
    for signal in signals:
        signal_date = signal.timestamp
        if signal_date in data.index:
            current_price = data.loc[signal_date, 'Close']
            
            if signal.signal_type == SignalType.BUY and position <= 0:
                if position == -1 and entry_price:
                    # Close short position
                    ret = (entry_price - current_price) / entry_price
                    returns.append((signal_date, ret))
                
                # Open long position
                position = 1
                entry_price = current_price
                
            elif signal.signal_type == SignalType.SELL and position >= 0:
                if position == 1 and entry_price:
                    # Close long position
                    ret = (current_price - entry_price) / entry_price
                    returns.append((signal_date, ret))
                
                # Open short position
                position = -1
                entry_price = current_price
    
    # 6. Display Results
    if returns:
        total_return = np.prod([1 + ret[1] for ret in returns]) - 1
        avg_return = np.mean([ret[1] for ret in returns])
        win_rate = len([r for r in returns if r[1] > 0]) / len(returns)
        
        print(f"\n📈 Strategy Performance:")
        print(f"  - Total Return: {total_return:.2%}")
        print(f"  - Average Return per Trade: {avg_return:.2%}")
        print(f"  - Win Rate: {win_rate:.2%}")
        print(f"  - Number of Trades: {len(returns)}")
    
    # 7. Create Simple Visualization
    print("\n📊 Creating visualization...")
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Price and moving averages
    ax1.plot(data.index, data['Close'], label='AAPL Close', alpha=0.7)
    
    short_ma = TechnicalIndicators.sma(data['Close'], 20)
    long_ma = TechnicalIndicators.sma(data['Close'], 50)
    
    ax1.plot(data.index, short_ma, label='20-day MA', alpha=0.8)
    ax1.plot(data.index, long_ma, label='50-day MA', alpha=0.8)
    
    # Mark buy/sell signals
    for signal in signals:
        if signal.timestamp in data.index:
            price = data.loc[signal.timestamp, 'Close']
            if signal.signal_type == SignalType.BUY:
                ax1.scatter(signal.timestamp, price, color='green', marker='^', s=100, alpha=0.8)
            else:
                ax1.scatter(signal.timestamp, price, color='red', marker='v', s=100, alpha=0.8)
    
    ax1.set_title('AAPL Price with Moving Average Crossover Signals')
    ax1.set_ylabel('Price ($)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Volume
    ax2.bar(data.index, data['Volume'], alpha=0.3, color='blue')
    ax2.set_title('Trading Volume')
    ax2.set_ylabel('Volume')
    ax2.set_xlabel('Date')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('ma_crossover_example.png', dpi=300, bbox_inches='tight')
    print("💾 Chart saved as 'ma_crossover_example.png'")
    
    print("\n✅ Example completed successfully!")
    print("\nNext steps:")
    print("- Try different MA parameters")
    print("- Add stop-loss and take-profit levels")
    print("- Implement proper backtesting with transaction costs")
    print("- Explore other technical indicators")


if __name__ == "__main__":
    main()
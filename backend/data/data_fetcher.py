import yfinance as yf
import pandas as pd

def fetch_spy_options():
    """Fetch real SPY option chain from Yahoo Finance."""
    spy = yf.Ticker("SPY")
    
    expirations = spy.options
    print(f"Available expirations: {expirations[:5]}")
    
    opt_chain = spy.option_chain(expirations[0])
    
    calls = opt_chain.calls
    puts = opt_chain.puts
    
    print(f"\nCalls for {expirations[0]}:")
    print(calls[['strike', 'impliedVolatility', 'bid', 'ask']].head(10))
    
    return calls, puts

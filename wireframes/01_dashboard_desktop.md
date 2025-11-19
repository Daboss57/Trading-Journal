# Desktop Trading Dashboard

**Screen:** Main Trading Interface (Desktop, 1920x1080)  
**User Flow:** Primary screen for active day trading

---

## Layout Structure

```
┌────────────────────────────────────────────────────────────────────────────────┐
│  [Logo]  TRADING JOURNAL                                    [User] [Settings]  │
│                                                                                  │
│  💰 Account Balance: $98,543.21  |  📈 Day P&L: +$1,234 (+1.26%)              │
│  💳 Buying Power: $394,172.84    |  📊 Day Trades: 2/3                        │
│  🟢 MARKET: OPEN  (Closes in 2:34:12)                                          │
├────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  ┌──────────────────────────────────────────┐  ┌──────────────────────────┐   │
│  │                                           │  │   ORDER ENTRY            │   │
│  │         CHART AREA (70%)                  │  │                          │   │
│  │                                           │  │  ┌────────────────────┐  │   │
│  │   ┌────────────────────────────────────┐ │  │  │ TSLA    $245.32   │  │   │
│  │   │ TSLA  $245.32  ▲ +2.45 (+1.01%)    │ │  │  │ ▲ $2.45  +1.01%   │  │   │
│  │   │ [1m][5m][15m][1h][D]  [Indicators▼]│ │  │  │ Bid: 245.30  50   │  │   │
│  │   └────────────────────────────────────┘ │  │  │ Ask: 245.34  120  │  │   │
│  │                                           │  │  └────────────────────┘  │   │
│  │   [Candlestick Chart with Volume]        │  │                          │   │
│  │                                           │  │  Action:                 │   │
│  │   Price: $245.32                          │  │  [🟢 BUY] [🔴 SELL]     │   │
│  │   ┌─────────────────────────────────────┐│  │  [🟡 SHORT] [COVER]     │   │
│  │   │         📊 Candlesticks             ││  │                          │   │
│  │   │                                     ││  │  Order Type:             │   │
│  │   │        ▂▄█▆▃▅▇▂▄▆                  ││  │  [Market ▼]             │   │
│  │   │                                     ││  │                          │   │
│  │   │       MA(20)  MA(50)  VWAP         ││  │  Shares:                 │   │
│  │   │                                     ││  │  [________100_________]  │   │
│  │   └─────────────────────────────────────┘│  │                          │   │
│  │   [Volume Bars]                           │  │  Time in Force:          │   │
│  │   ▂▄▆▃▅▇▂▄                                │  │  [Day ▼]                │   │
│  │                                           │  │                          │   │
│  │   Drawing: [Line][H-Line][Fib][Rect]     │  │  ───────────────────────│   │
│  │                                           │  │  Est. Cost: $24,532.00  │   │
│  │                                           │  │  Commission: $0.00       │   │
│  │                                           │  │                          │   │
│  └──────────────────────────────────────────┘  │  [   PLACE ORDER   ]    │   │
│                                                  │                          │   │
│                                                  │  Quick Sizes:            │   │
│                                                  │  [10][25][50][100][500] │   │
│                                                  └──────────────────────────┘   │
│                                                                                  │
├──────────────────────────────────────────────┬──────────────────────────────────┤
│  POSITIONS (Live P&L)                        │  ORDERS (Pending)                │
├──────────────────────────────────────────────┼──────────────────────────────────┤
│  Symbol  Qty   Avg Price  Current  P&L      │  Symbol  Type    Qty  Price      │
│  ─────────────────────────────────────────── │  ──────────────────────────────  │
│  TSLA    100   $243.10    $245.32  +$222    │  SPY     LIMIT   50   $450.00    │
│                                    (+0.91%)  │         [CANCEL]                 │
│         [SELL] [ADD] [CLOSE]                 │                                  │
│                                              │  AAPL    STOP    100  $178.00    │
│  SPY     -50   $451.20    $450.30  +$45     │         [CANCEL] [MODIFY]        │
│  (SHORT)                           (+0.10%)  │                                  │
│         [COVER] [ADD]                        │                                  │
│                                              │                                  │
│  Total Open P&L: +$267 (+0.27%)             │  [Cancel All Orders]             │
└──────────────────────────────────────────────┴──────────────────────────────────┘
│                                                                                  │
│  WATCHLIST                          Last      Change    Volume      Actions     │
│  ──────────────────────────────────────────────────────────────────────────────│
│  SPY  🟢  $450.30   +0.85%   129M   [Chart][Buy][Sell][Short]                  │
│  QQQ  🟢  $385.42   +1.12%    78M   [Chart][Buy][Sell][Short]                  │
│  AAPL 🟢  $180.45   -0.23%    65M   [Chart][Buy][Sell][Short]                  │
│  BTC  🟡  $43,234   +2.34%   24/7   [Chart][Buy][Sell]                         │
│                                                          [+ Add Symbol]         │
└────────────────────────────────────────────────────────────────────────────────┘
```

---

## Component Breakdown

### Header Bar
- **Left:** Logo + App name
- **Center:** Account metrics (Balance, BP, Day P&L, Day Trades)
- **Right:** User menu, settings, notifications
- **Market Status Indicator:** Prominent, color-coded with countdown

### Main Content (Split 70/30)

#### Chart Panel (70% width)
- **Ticker Header:** Symbol, price, change with bid/ask spread
- **Timeframe Selector:** 1m, 5m, 15m, 1h, Daily
- **Indicators Dropdown:** Add MA, RSI, MACD, VWAP, etc.
- **Chart Canvas:** TradingView Lightweight Charts or similar
- **Volume Subplot:** Below price chart
- **Drawing Tools:** Horizontal line, trendline, Fibonacci, rectangle

#### Order Entry (30% width)
- **Symbol Info Card:** Current price, bid/ask, spread
- **Action Buttons:** Buy/Sell/Short/Cover (color-coded)
- **Order Type Dropdown:** Market, Limit, Stop, Stop-Limit, Trailing Stop
- **Shares Input:** Numeric input with preset quick sizes
- **Time in Force:** Day, GTC, IOC, FOK
- **Cost Preview:** Estimated total with commission
- **Place Order Button:** Large, prominent

### Bottom Panels (Tabbed or Side-by-Side)

#### Positions Tab
- **Columns:** Symbol, Qty, Avg Price, Current Price, Unrealized P&L ($/%)\
- **Actions per row:** Sell, Add (increase position), Close (flatten)
- **Short positions:** Visual indicator (⬇ or different row color)
- **Total P&L:** Summed at bottom

#### Orders Tab
- **Pending orders:** Limit, Stop orders waiting execution
- **Columns:** Symbol, Type, Qty, Price, Time Placed
- **Actions:** Cancel, Modify
- **Bulk action:** Cancel All Orders button

### Watchlist (Bottom or Sidebar)
- **Compact list view:** Symbol, price, % change, volume
- **Quick actions:** Chart (navigate), Buy, Sell, Short
- **Add symbol:** Input field with autocomplete

---

## Interaction Notes

1. **Clicking a watchlist symbol** → Loads that symbol's chart
2. **Right-click on chart** → Context menu for orders at price
3. **Hotkeys:**
   - `B` = Focus buy
   - `S` = Focus sell
   - `Shift+S` = Short
   - `C` = Cover position
   - `X` = Cancel all orders
   - `Spacebar` = Flatten all positions
4. **Real-time updates:** Prices, P&L refresh every 1-5 seconds
5. **Order confirmation:** Optional modal (can be disabled for speed)

---

## Responsive Behavior (Desktop)
- Minimum width: 1280px
- Chart:Order Entry ratio adjustable (user preference)
- Collapsible panels for more chart space
- Multi-monitor support (detachable order ticket window)

---

## Accessibility
- Keyboard navigation for all controls
- ARIA labels for screen readers
- High contrast mode option
- Customizable font sizes

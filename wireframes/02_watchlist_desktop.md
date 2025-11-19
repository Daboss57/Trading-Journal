# Watchlist Panel (Desktop)

**Component:** Watchlist with Quick Actions  
**Location:** Bottom of dashboard or collapsible sidebar  
**Max Symbols:** 20 (to manage API rate limits)

---

## Layout

```
┌────────────────────────────────────────────────────────────────────────────────┐
│  WATCHLIST                                                    [+ Add Symbol]    │
├────────────────────────────────────────────────────────────────────────────────┤
│  Symbol  Status  Last Price   Change     Volume      Actions                   │
│  ──────────────────────────────────────────────────────────────────────────────│
│  SPY     🟢      $450.30      +$3.85     129.4M      [📊][BUY][SELL][SHORT]   │
│                               (+0.86%)                                          │
│                                                                                 │
│  TSLA    🟢      $245.32      +$2.45      87.2M      [📊][BUY][SELL][SHORT]   │
│                               (+1.01%)                                          │
│                                                                                 │
│  AAPL    🟢      $180.45      -$0.42      65.1M      [📊][BUY][SELL][SHORT]   │
│                               (-0.23%)                                          │
│                                                                                 │
│  QQQ     🟢      $385.42      +$4.28      78.3M      [📊][BUY][SELL][SHORT]   │
│                               (+1.12%)                                          │
│                                                                                 │
│  NVDA    🟢      $495.67      +$12.34     52.8M      [📊][BUY][SELL][SHORT]   │
│                               (+2.55%)                                          │
│                                                                                 │
│  BTC-USD 🟡      $43,234      +$988       24/7       [📊][BUY][SELL]           │
│                               (+2.34%)                                          │
│                                                                                 │
│  AMZN    🟢      $152.88      -$1.12      48.6M      [📊][BUY][SELL][SHORT]   │
│                               (-0.73%)                                          │
│                                                                                 │
│  MSFT    🟢      $378.92      +$5.67      35.2M      [📊][BUY][SELL][SHORT]   │
│                               (+1.52%)                                          │
│                                                                                 │
│  ─────────────────────────────────────────────────────────────────────────────│
│  [Show More]  •  Last Updated: 14:23:45 ET  •  Auto-refresh: ON (5s)          │
└────────────────────────────────────────────────────────────────────────────────┘
```

---

## Features

### Columns
1. **Symbol:** Ticker code with logo (optional)
2. **Status Indicator:**
   - 🟢 Market Open
   - 🔴 Market Closed
   - 🟡 Crypto (24/7) or Pre/Post Market
3. **Last Price:** Current/last traded price
4. **Change:** Absolute $ change and % change (color-coded: green +, red -)
5. **Volume:** Daily volume in millions (M) or billions (B)
6. **Actions:** Quick-action buttons

### Quick Action Buttons
- **📊 Chart:** Load symbol into main chart area
- **BUY:** Open order ticket pre-filled with symbol (long)
- **SELL:** Sell existing position or open sell ticket
- **SHORT:** Open short order ticket (margin accounts only)
- **Note:** Crypto omits SHORT button (if not supported)

### Add Symbol
- **Input:** Text field with autocomplete search
- **Validation:** Check if symbol exists via API
- **Limit:** Warn when approaching 20 symbol limit
- **Drag-to-reorder:** Symbols can be reordered by drag

### Settings Dropdown (Gear icon)
- Auto-refresh interval: 5s / 10s / 15s / Manual
- Show/hide volume column
- Color theme for gains/losses
- Export watchlist as CSV

---

## Interaction Behavior

1. **Clicking Symbol Name** → Loads chart in main panel
2. **Hover on Row** → Highlight, show mini-chart preview (optional Phase 2)
3. **Right-click Row** → Context menu: "Remove from watchlist", "Set alert", "View news"
4. **Real-time Price Updates:** WebSocket or polling every 5-15s
5. **Sorting:** Click column header to sort (price, % change, volume)

---

## Mobile Adaptation
- Stacked cards instead of table rows
- Swipe left/right on card to reveal BUY/SELL/SHORT actions
- Collapse volume column by default on narrow screens

---

## Data Refresh Strategy
- **Active Tab:** Update every 5 seconds
- **Background Tab:** Pause updates to save API calls
- **Market Closed:** Reduce refresh to every 30 seconds or freeze
- **Crypto:** Always refresh (24/7 trading)

---

## Edge Cases
- **Symbol delisted:** Show warning icon, disable trade actions
- **API rate limit hit:** Display "Paused – Rate limit" + countdown
- **Network error:** Show stale data timestamp, retry automatically
- **Short-selling unavailable:** Gray out SHORT button with tooltip "Margin account required"

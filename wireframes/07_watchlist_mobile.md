# Mobile Watchlist

**Component:** Scrollable card list with swipe actions  
**Context:** Accessible from dashboard section or dedicated tab

---

## Layout

```
┌──────────────────────────────────────┐
│ WATCHLIST             [+ Add] [⋮]    │
├──────────────────────────────────────┤
│ ┌──────────────────────────────────┐ │
│ │ SPY                              │ │
│ │ 🟢 $450.30   +0.85%   Vol 129M   │ │
│ │ Bid 450.28  Ask 450.32          │ │
│ │ [Chart] [BUY] [SELL] [SHORT]     │ │
│ └──────────────────────────────────┘ │
│                                      │
│ ┌──────────────────────────────────┐ │
│ │ TSLA                             │ │
│ │ 🟢 $245.32   +1.01%   Vol 87M    │ │
│ │ Bid 245.30  Ask 245.34          │ │
│ │ [Chart] [BUY] [SELL] [SHORT]     │ │
│ └──────────────────────────────────┘ │
│                                      │
│ ┌──────────────────────────────────┐ │
│ │ AAPL                             │ │
│ │ 🟢 $180.45   -0.23%   Vol 65M    │ │
│ │ Bid 180.40  Ask 180.48          │ │
│ │ [Chart] [BUY] [SELL] [SHORT]     │ │
│ └──────────────────────────────────┘ │
│                                      │
│ ┌──────────────────────────────────┐ │
│ │ BTC-USD                          │ │
│ │ 🟡 $43,234   +2.34%   24/7       │ │
│ │ Bid 43,220  Ask 43,240          │ │
│ │ [Chart] [BUY] [SELL]             │ │
│ └──────────────────────────────────┘ │
│                                      │
│ [Load More ▼]                       │
└──────────────────────────────────────┘
```

---

## Interactions

- **Tap Symbol Card:** Loads detail modal with advanced metrics
- **Swipe Left:** Reveals actions `Short`, `Cover`, `Cancel Alerts`
- **Swipe Right:** Reveals `Buy`, `Sell`, `Add Alert`
- **Long Press:** Reorder watchlist (drag handle appears)
- **Pull to Refresh:** Manual refresh (auto updates every 10s when active)
- **Add Button:** Opens search modal; limit 20 symbols, show remaining slots
- **Overflow Menu (⋮):** Toggle auto-refresh, set data density (compact vs spacious), export list

---

## Data Density Modes

1. **Standard (default):** Shows price, change, volume, bid/ask
2. **Compact:** Hides bid/ask, reduces padding, fits more cards per screen
3. **Expanded:** Adds mini sparkline and short float/ATR metrics

---

## State Indicators

- 🟢 Market Open; 🔴 Closed; 🟡 Pre/Post or 24/7
- Greyed-out card if API throttle or symbol paused
- Warning badge for HTB (Hard-to-Borrow) stocks

---

## Alerts Integration

- Bell icon on card shows active price alerts
- Tap to manage alert thresholds
- Alert summary shown under price ("Alert @ 248.00")

---

## Error & Empty States

- **No Symbols:** Prompt "Add your first symbol" with big CTA
- **Rate Limit:** Banner "Auto-refresh paused (rate limit). Tap to retry in 30s."
- **Network Error:** Show last updated timestamp + retry button

---

## Accessibility

- VoiceOver reads "SPY, up 0.85 percent, 129 million volume"
- High-contrast mode flips background to dark grey
- Buttons sized 44px+ for finger taps

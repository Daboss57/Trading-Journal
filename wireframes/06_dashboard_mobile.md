# Mobile Trading Dashboard

**Screen Size Target:** 390px × 844px (iPhone 13)  
**Primary Use:** Quick trade monitoring and order placement while away from desktop

---

## Layout Overview

```
┌──────────────────────────────────────┐
│  [☰] TRADING JOURNAL        [$98.5k] │
│  🟢 MARKET OPEN  |  Closes in 2:34:12 │
├──────────────────────────────────────┤
│  SYMBOL HEADER                      │
│  ┌──────────────────────────────┐    │
│  │ TSLA   $245.32   ▲ +1.01%    │    │
│  │ Bid 245.30   Ask 245.34      │    │
│  └──────────────────────────────┘    │
│                                      │
│  MINI CHART                          │
│  ┌──────────────────────────────┐    │
│  │ [1m][5m][15m][1h][D]         │    │
│  │                              │    │
│  │  Candles + MA + VWAP         │    │
│  │                              │    │
│  └──────────────────────────────┘    │
│                                      │
│  ORDER QUICK ACTIONS                 │
│  [🟢 BUY] [🔴 SELL] [🟡 SHORT] [COVER]│
│                                      │
│  QUICK ORDER CARD                    │
│  ┌──────────────────────────────┐    │
│  │ Order Type: [Market ▼]       │    │
│  │ Shares: [___100___]          │    │
│  │ Time-in-Force: [Day ▼]       │    │
│  │ Est Cost: $24,532            │    │
│  │ [ PLACE ORDER ]              │    │
│  └──────────────────────────────┘    │
│                                      │
│  POSITIONS SUMMARY                   │
│  ┌──────────────────────────────┐    │
│  │ TSLA  100 @ 243.10  +$222    │    │
│  │ SPY   -50 @ 451.20 +$45      │    │
│  │ [View All Positions ▶]       │    │
│  └──────────────────────────────┘    │
│                                      │
│  ORDERS SUMMARY                      │
│  ┌──────────────────────────────┐    │
│  │ SPY LIMIT BUY 50 @ 450.00    │    │
│  │ [Cancel] [Modify]            │    │
│  └──────────────────────────────┘    │
│                                      │
│  WATCHLIST CAROUSEL                  │
│  [SPY $450.30 ▲0.85%  BUY/SELL/SHORT]│
│  [TSLA ...] [AAPL ...] [BTC ...]    │
│                                      │
│  QUICK METRICS                       │
│  ┌──────────────────────────────┐    │
│  │ Day P&L: +$1,234 (+1.23%)    │    │
│  │ Trades: 12  Win%: 66.7%      │    │
│  └──────────────────────────────┘    │
└──────────────────────────────────────┘
```

---

## Interaction Details

- **Hamburger Menu:** Opens navigation drawer (Dashboard, Backtesting, Analytics, Settings)
- **Account Chip:** Tapping balance opens account modal (cash vs margin info)
- **Symbol Selector:** Swipe horizontally or tap to search symbol (modal with search bar)
- **Mini Chart:** Pinch-to-zoom, tap indicators to toggle; limited height so only two overlays shown simultaneously
- **Quick Actions:** Buttons trigger order ticket sheet with pre-filled direction
- **Quick Order Card:** Sticky CTA at bottom when scrolling; can switch to advanced view for more parameters
- **Positions & Orders:** Collapsible cards; tapping expands to show full details and action buttons
- **Watchlist Carousel:** Scroll horizontally; each card has quick trade buttons
- **Quick Metrics:** Shows day stats; tap to navigate to analytics screen

---

## Responsive Considerations

- **Landscape Mode:** Chart expands, order card floats on right
- **One-Handed Reach:** Primary CTAs (Place Order, Buy/Sell) near bottom
- **Haptics:** Provide vibration feedback on order placement (mobile app)
- **Offline Mode:** Display "Connection Lost" banner if WebSocket drops

---

## Accessibility

- Font size scaling via system settings
- Buttons minimum 44px height
- Colorblind-friendly icons plus text labels
- VoiceOver labels for market status and P&L

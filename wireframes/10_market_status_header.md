# Market Status Header Component

**Purpose:** Provide real-time exchange status, countdown timers, and key account context at top of UI.

---

## Desktop Layout

```
┌───────────────────────────────────────────────────────────────────────────────┐
│ [Logo]  Account: $98,543.21  |  Buying Power: $394,172.84  |  Day Trades: 2/3  │
│ 🟢 NYSE: OPEN (Closes in 02:34:12)    Crypto: 🟡 OPEN 24/7                      │
└───────────────────────────────────────────────────────────────────────────────┘
```

### Elements

1. **Account Summary Chips**
   - Balance, Buying Power, Day Trades Remaining
   - Clickable to open account drawer
2. **Market Status Pill**
   - Icon + text (🟢 OPEN, 🔴 CLOSED, 🟡 PRE/POST)
   - Countdown timer to next open/close event
3. **Multiple Exchanges**
   - Primary (NYSE/NASDAQ) emphasized
   - Secondary row for crypto, OTC, international (phase 2)
4. **Holiday Indicator**
   - If market closed due to holiday, show label "Closed – Thanksgiving" and countdown to next session

---

## Mobile Layout

```
┌──────────────────────────────────────┐
│ [☰] TRADING JOURNAL                 │
│ Account $98.5k  •  BP $394k          │
│ 🟢 OPEN  |  Closes in 02:34:12       │
└──────────────────────────────────────┘
```

- Swipe horizontally to view other exchanges
- Tap countdown to open schedule modal

---

## States

| State      | Indicator | Description                                  |
|------------|-----------|----------------------------------------------|
| Open       | 🟢 Green  | Regular trading session active               |
| Pre/Post   | 🟡 Yellow | Orders queued, limited execution             |
| Closed     | 🔴 Red    | Orders queued for next open, countdown shown |
| Holiday    | 🟠 Orange | Special message ("Closed: Memorial Day")     |
| Error      | ⚪ Gray    | Unable to fetch status (retry button)        |

---

## Data Sources

- Backend `market_status` table or service providing:
  - `exchange`, `is_open`, `phase`, `next_open_time`, `next_close_time`, `holiday_name`
- Update cadence: every minute via background job + WebSocket push to clients
- Client fallback: recalc countdown locally between pushes

---

## Interactions

1. **Hover/Tap:** Show tooltip with detailed schedule ("Regular hours 9:30 AM – 4:00 PM ET")
2. **Click Countdown:** Opens modal with weekly schedule and holiday list
3. **Alert Toggle:** Subscribe to notifications ("Alert me 5 min before open")
4. **PDT Warning:** If account flagged, show banner below header

---

## Edge Cases

- **DST Changes:** Display timezone ("ET") and adjust automatically
- **Multiple Exchanges Open:** Use pill list (e.g., "NYSE 🟢 | NASDAQ 🟢 | LSE 🔴")
- **Crypto Always Open:** Show "24/7" label, no countdown
- **Backend Down:** Show "Status unavailable" + retry icon; default to last known state

---

## Accessibility

- High-contrast color palette with text labels (not color-only)
- Screen reader text: "NYSE open, closes in two hours thirty-four minutes"
- Countdown updates announced no more than once per minute to avoid chatter

---

## Future Enhancements

- Personalized alerts for scheduled economic events (Phase 4)
- Market sentiment indicators (Fear & Greed index) adjacent to status
- Integrate global exchanges with local timezone conversion

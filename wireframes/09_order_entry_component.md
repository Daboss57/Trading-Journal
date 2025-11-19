# Order Entry Component Specification

**Context:** Shared between desktop and mobile trading interfaces  
**Modes:** Quick Ticket (default), Advanced Ticket (expanded modal)

---

## Layout (Desktop)

```
┌──────────────────────────────────────────────┐
│  ORDER ENTRY                                 │
├──────────────────────────────────────────────┤
│  Symbol:  [TSLA ▼]     Price: $245.32        │
│  Bid: 245.30 (50)      Ask: 245.34 (120)     │
│                                              │
│  Action: [🟢 BUY] [🔴 SELL] [🟡 SHORT] [COVER]│
│                                              │
│  Order Type: [Market ▼]                      │
│  Shares:     [_______100_______] [±]         │
│  Position %: [10% ▼] → Auto-calc shares      │
│  Time in Force: [Day ▼]                      │
│  Route (advanced): [Auto ▼]                  │
│                                              │
│  Price (for limit/stop): [245.00____]        │
│  Stop Trigger (if relevant): [244.00____]    │
│  Trailing Amount: [$0.50____] or [%]         │
│                                              │
│  Est Cost:        $24,532.00                 │
│  Buying Power:    $394,172.84                │
│  Margin Impact:   -$12,266 (if short)        │
│  Commission:      $0.00                      │
│                                              │
│  [  PLACE ORDER  ]    [ Save Template ▼ ]    │
└──────────────────────────────────────────────┘
```

---

## Quick Ticket vs Advanced

| Feature                      | Quick Ticket | Advanced Modal |
|------------------------------|--------------|----------------|
| Order type (Market/Limit)    | ✓            | ✓              |
| Shares input & presets       | ✓            | ✓              |
| Time-in-force                | ✓            | ✓              |
| Stop/Trailing parameters     | —            | ✓              |
| Bracket orders (Phase 2)     | —            | ✓              |
| Smart routing selection      | —            | ✓              |
| Notes/Tags per order         | —            | ✓              |
| Preview margin requirements  | ✓            | ✓ (more detail)|

---

## Validation Rules

1. **Shares Input:** Positive integer; show error if blank or exceeds max position limit.
2. **Limit Price:** Required when order type = Limit/Stop-Limit; must be > 0.
3. **Stop Price:** For stop orders, must be below current price for sell stop (long) or above for buy stop (short cover).
4. **Buying Power Check:** Compare estimated cost vs available BP; disable CTA with tooltip if insufficient.
5. **PDT Warning:** If order would trigger 4th day trade and balance < $25k, show modal warning before submit.
6. **Short Availability:** If symbol not shortable, grey out SHORT button with tooltip.
7. **Slippage Simulation:** Show estimated fill range (±0.05%) for market orders.

---

## Hotkeys & Shortcuts (Desktop)

- `B` = Focus Buy, `S` = Sell, `Shift+S` = Short, `C` = Cover
- `1-9` = Apply preset sizes (1 = 10%, 2 = 25%, etc.)
- `Enter` = Submit order when inputs valid
- `Esc` = Clear form/cancel

---

## Error & Confirmation States

- **Inline Errors:** Red text under fields (e.g., "Limit price required")
- **Toast Notifications:** "Order submitted" or "Rejected: insufficient funds"
- **Undo Option:** Short-lived undo button for cancellations
- **Submission Spinner:** Disable CTA, show loader while API request pending

---

## Mobile Variant

- Same fields but stacked vertically; sections collapsed into accordion (Action → Order Type → Quantity → Extras)
- Sticky summary bar showing Est Cost + CTA
- Numeric keypad for shares/price inputs

---

## Templates & Defaults

- Users can save named templates (e.g., "TSLA scalp", "SPY swing")
- Template stores action, order type, shares %, TIF, bracket config
- Quick dropdown to select template; auto-fill fields

---

## API Integration Hooks

- `POST /orders` payload includes symbol, side, quantity, orderType, tif, limitPrice, stopPrice, takeProfit, stopLoss, templateId
- Response includes order ID, estimated fill, rejection reasons
- Component listens to WebSocket for order status updates

---

## Future Enhancements (Phase 2+)

- OCO / Bracket orders with linked child orders
- VWAP, Iceberg advanced order types
- Risk controls (max loss per day) integrated into ticket
- Voice command quick trading (pilot)

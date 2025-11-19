# Mobile Backtest Experience

**Use Case:** Configure and run simple backtests on mobile devices  
**Flow:** Tabs/steps with accordions for each configuration group

---

## Layout

```
┌──────────────────────────────────────┐
│  [←] Backtesting                     │
│  Strategy: My Momentum Strategy      │
├──────────────────────────────────────┤
│  Step Dots: ● ○ ○ ○ ○                │
├──────────────────────────────────────┤
│  STEP 1: DETAILS                     │
│  ┌──────────────────────────────┐    │
│  │ Strategy Name                │    │
│  │ [My Momentum Strategy____]   │    │
│  │ Description (optional)       │    │
│  │ [__________________________] │    │
│  └──────────────────────────────┘    │
│                                      │
│  STEP 2: SYMBOLS & DATES             │
│  ┌──────────────────────────────┐    │
│  │ Symbols                      │    │
│  │ [TSLA_____] [+]              │    │
│  │ [SPY_____]  [Remove]         │    │
│  │ Upload CSV [Choose File]     │    │
│  │ Start Date [2024-01-01 ▼]    │    │
│  │ End Date   [2024-12-31 ▼]    │    │
│  │ Timeframe  [15-min ▼]        │    │
│  └──────────────────────────────┘    │
│                                      │
│  STEP 3: ENTRY RULES                 │
│  ┌──────────────────────────────┐    │
│  │ [+ Add Condition]            │    │
│  │ IF [Price] [Crosses Above]   │    │
│  │    [MA(20)]                  │    │
│  │ AND [RSI] [Greater Than]     │    │
│  │    [30]                      │    │
│  │ Action: [BUY ▼]              │    │
│  └──────────────────────────────┘    │
│                                      │
│  STEP 4: EXIT RULES                  │
│  ┌──────────────────────────────┐    │
│  │ Take Profit [%] [ +2.0 ]     │    │
│  │ Stop Loss  [%] [ -1.0 ]      │    │
│  │ Trailing Stop [%] [ 0.5 ]    │    │
│  │ Exit EOD [✓]                 │    │
│  └──────────────────────────────┘    │
│                                      │
│  STEP 5: SIZING                      │
│  ┌──────────────────────────────┐    │
│  │ Capital [$] [100000]         │    │
│  │ Position Size [%] [10]       │    │
│  │ Max Positions [3]            │    │
│  │ Commission [$] [0.00]        │    │
│  │ Slippage [%] [0.02]          │    │
│  └──────────────────────────────┘    │
│                                      │
│  [Save Strategy]   [Run Backtest ▶]  │
└──────────────────────────────────────┘
```

---

## Navigation Patterns

- **Stepper Dots:** Indicate progress through steps; tap to jump back
- **Accordions:** Collapse previous steps to keep screen short
- **Floating CTA:** Sticky "Run Backtest" button when all required fields filled
- **Keyboard Handling:** Scroll input into view; use numeric keypad for number fields

---

## Advanced Options Drawer

- Swipe up from bottom to reveal optional settings (walk-forward toggle, benchmark selection, parallel runs). Hidden by default to keep MVP simple.

---

## Results View (Mobile)

After running, auto-navigate to results summary:

```
┌──────────────────────────────────────┐
│  RESULTS: My Momentum Strategy       │
├──────────────────────────────────────┤
│  Total Return       +23.4% (+$23,400)│
│  Total Trades       156              │
│  Win Rate           54.5%            │
│  Profit Factor      1.6              │
│  Sharpe Ratio       1.2              │
│  Max Drawdown       -12.3%           │
│                                      │
│  [View Charts ▶] [Export CSV]        │
└──────────────────────────────────────┘
```

- Charts accessible via tabs that slide horizontally (Equity, Drawdown, Distribution)
- Trade log collapses into paginated list (infinite scroll)

---

## Offline / Background Behavior

- Backtest requests queued if offline; user notified when reconnects
- Push notification option when backtest completes (if long run)

---

## Accessibility & UX

- Dynamic font adjustments
- Large touch targets (inputs 48px tall)
- Use native pickers for date/time
- Provide haptic feedback on successful run

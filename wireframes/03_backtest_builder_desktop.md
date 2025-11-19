# Backtest Builder (Desktop)

**Screen:** Strategy Configuration & Backtest Setup  
**Access:** Main navigation → "Backtesting" tab  
**Goal:** Configure and launch historical strategy tests

---

## Layout

```
┌────────────────────────────────────────────────────────────────────────────────┐
│  [Logo] TRADING JOURNAL          [Dashboard][Backtesting][Analytics][Settings] │
├────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  BACKTEST BUILDER                                                               │
│                                                                                  │
│  ┌────────────────────────────────────────────────────────────────────────┐   │
│  │  STEP 1: STRATEGY SETUP                                                │   │
│  ├────────────────────────────────────────────────────────────────────────┤   │
│  │                                                                          │   │
│  │  Strategy Name: [_____My Momentum Strategy__________]                  │   │
│  │                                                                          │   │
│  │  Description (optional):                                                │   │
│  │  [_____________________________________________]                        │   │
│  │  [_____________________________________________]                        │   │
│  │                                                                          │   │
│  └────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│  ┌────────────────────────────────────────────────────────────────────────┐   │
│  │  STEP 2: SYMBOL(S) & DATE RANGE                                        │   │
│  ├────────────────────────────────────────────────────────────────────────┤   │
│  │                                                                          │   │
│  │  Symbols:  [TSLA____]  [+ Add Symbol]                                  │   │
│  │            [SPY_____]  [Remove]                                         │   │
│  │            [AAPL____]  [Remove]                                         │   │
│  │                                                                          │   │
│  │            Or upload CSV: [Choose File]  (Format: symbol per line)     │   │
│  │                                                                          │   │
│  │  Date Range:                                                            │   │
│  │    Start Date: [2024-01-01 ▼]                                          │   │
│  │    End Date:   [2024-12-31 ▼]                                          │   │
│  │                                                                          │   │
│  │  Timeframe:    [⚪ 1-min  ⚪ 5-min  ⚫ 15-min  ⚪ 1-hour  ⚪ Daily]      │   │
│  │                                                                          │   │
│  └────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│  ┌────────────────────────────────────────────────────────────────────────┐   │
│  │  STEP 3: ENTRY RULES                                                   │   │
│  ├────────────────────────────────────────────────────────────────────────┤   │
│  │                                                                          │   │
│  │  [+ Add Entry Condition]                                                │   │
│  │                                                                          │   │
│  │  ┌──────────────────────────────────────────────────────────────┐     │   │
│  │  │  Condition 1:                                            [×]  │     │   │
│  │  │  IF  [Price ▼]  [Crosses Above ▼]  [MA(20) ▼]                │     │   │
│  │  │  AND [RSI ▼]    [Greater Than ▼]   [30____]                   │     │   │
│  │  └──────────────────────────────────────────────────────────────┘     │   │
│  │                                                                          │   │
│  │  Logic: [⚫ ALL conditions must be true  ⚪ ANY condition]              │   │
│  │                                                                          │   │
│  │  Action: [⚫ BUY (Long)  ⚪ SELL (Short)]                               │   │
│  │                                                                          │   │
│  └────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│  ┌────────────────────────────────────────────────────────────────────────┐   │
│  │  STEP 4: EXIT RULES                                                    │   │
│  ├────────────────────────────────────────────────────────────────────────┤   │
│  │                                                                          │   │
│  │  Take Profit:   [+2.0____]%                                            │   │
│  │  Stop Loss:     [-1.0____]%                                            │   │
│  │  Trailing Stop: [_______]% (optional)                                  │   │
│  │                                                                          │   │
│  │  Time-Based Exit:                                                       │   │
│  │    [✓] Exit all positions at end of day (no overnight holds)           │   │
│  │    [ ] Maximum hold time: [____] hours                                 │   │
│  │                                                                          │   │
│  │  [+ Add Custom Exit Condition]                                          │   │
│  │                                                                          │   │
│  └────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│  ┌────────────────────────────────────────────────────────────────────────┐   │
│  │  STEP 5: POSITION SIZING & RISK                                        │   │
│  ├────────────────────────────────────────────────────────────────────────┤   │
│  │                                                                          │   │
│  │  Initial Capital:   [$100,000____]                                     │   │
│  │                                                                          │   │
│  │  Position Sizing:                                                       │   │
│  │    [⚫ Fixed % of account]  [10____]%                                  │   │
│  │    [⚪ Fixed dollar amount]  [$_____]                                  │   │
│  │    [⚪ Fixed shares]         [______]                                   │   │
│  │                                                                          │   │
│  │  Max Positions:     [3____]  (concurrent open positions)               │   │
│  │                                                                          │   │
│  │  Commissions:       [$0.00___] per share                               │   │
│  │  Slippage:          [0.02___]% (simulated market impact)               │   │
│  │                                                                          │   │
│  └────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│  ┌────────────────────────────────────────────────────────────────────────┐   │
│  │  STRATEGY TEMPLATES                                                     │   │
│  ├────────────────────────────────────────────────────────────────────────┤   │
│  │  Load a pre-built strategy:                                             │   │
│  │  [Moving Average Crossover]  [RSI Oversold]  [Breakout]  [VWAP Mean]  │   │
│  │                                                                          │   │
│  └────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│  ────────────────────────────────────────────────────────────────────────────  │
│                                                                                  │
│  [Save Strategy]  [Load Strategy]          [Cancel]  [▶ RUN BACKTEST]         │
│                                                                                  │
└────────────────────────────────────────────────────────────────────────────────┘
```

---

## Component Details

### Step 1: Strategy Setup
- **Strategy Name:** User-defined name for saving/loading
- **Description:** Optional notes about strategy logic

### Step 2: Symbol(s) & Date Range
- **Symbol Input:** 
  - Manual entry with autocomplete
  - Add multiple symbols (each backtested separately or portfolio-style)
  - CSV upload for bulk symbol lists
- **Date Range:** Date pickers with validation (start < end)
- **Timeframe:** Radio buttons for data granularity
  - 1-min, 5-min, 15-min, 1-hour, Daily
  - Note: Historical 1-min data often limited to recent periods

### Step 3: Entry Rules
- **Visual Rule Builder:** Drag-and-drop or dropdown-based
- **Conditions:** 
  - Left operand: Price, Indicator (MA, RSI, MACD, etc.)
  - Operator: >, <, =, Crosses Above, Crosses Below
  - Right operand: Value, another indicator
- **Logic Operator:** AND (all) vs OR (any)
- **Action:** Long (buy) or Short (sell short)
- **Add Multiple Conditions:** Nested rules with parentheses (Phase 2)

### Step 4: Exit Rules
- **Take Profit:** % gain target
- **Stop Loss:** % loss limit
- **Trailing Stop:** Dynamic stop that follows price
- **Time-Based:** 
  - End-of-day exit (day trading simulation)
  - Maximum hold duration
- **Custom Conditions:** Same builder as entry rules (e.g., "Exit when RSI > 70")

### Step 5: Position Sizing & Risk
- **Initial Capital:** Starting account balance
- **Position Sizing Methods:**
  - % of account (dynamic, adjusts with equity)
  - Fixed dollar amount
  - Fixed share count
- **Max Positions:** Limit concurrent trades (diversification)
- **Commissions:** Per-share fee (default $0 for modern brokers)
- **Slippage:** Simulate market impact on execution price

### Strategy Templates
- **Pre-built Strategies:** One-click load common patterns
  - Moving Average Crossover (MA 20/50)
  - RSI Oversold (RSI < 30, exit > 70)
  - Breakout (Price > Day High + ATR)
  - VWAP Mean Reversion

---

## Interaction Flow

1. **User fills out steps 1-5** → Validates inputs
2. **Clicks "RUN BACKTEST"** → Shows loading spinner
3. **Backend fetches historical data** → Runs simulation
4. **Redirects to Results Page** → Displays performance metrics

---

## Validation & Error Handling

- **Missing Required Fields:** Highlight in red, show tooltip
- **Invalid Date Range:** "End date must be after start date"
- **Symbol Not Found:** "TSLA: ✓ Valid | ZZZZ: ✗ Invalid symbol"
- **Insufficient Data:** "1-min data not available before 2023-06-01"
- **API Limits:** "Backtest limited to 3 symbols at a time (upgrade for more)"

---

## Save/Load Strategy
- **Save:** Stores configuration as JSON in user's account
- **Load:** Dropdown of saved strategies → Populates form
- **Share:** Generate shareable link (Phase 2)

---

## Mobile Adaptation
- Accordion-style collapsible steps
- Stacked fields instead of side-by-side
- Simplified rule builder (fewer dropdowns, preset templates)
- Bottom sticky "RUN BACKTEST" button

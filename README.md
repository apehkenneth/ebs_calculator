# 📦 EBS Calculator (Ecommerce Business Success Calculator)

A simple and powerful **command-line tool** to help e-commerce business owners analyze profitability, track ROI, and determine their break-even point.

---

## 🚀 Features

- Calculates:

  - ✅ Total Revenue
  - ✅ Total Cost
  - ✅ Net Profit (after tax)
  - ✅ Profit Margin
  - ✅ Break-Even Units
  - ✅ ROI (Return on Investment)
  - ✅ ROAS (Return on Ad Spend)

- Easy-to-use **command-line interface**
- Perfect for:
  - Solo entrepreneurs
  - Dropshippers
  - Amazon FBA sellers
  - Shopify store owners

---

## 📥 Installation

### Prerequisites

- Python 3.7 or higher installed on your machine

### Steps

1. **Clone the repository** or download the script:

   ```bash
   git clone https://github.com/apehkenneth/ebs-calculator.git
   cd ebs-calculator
   ```

2. **Run the script** using Python:
   ```bash
   python ebs_calculator.py
   ```

## 🛠️ How to Use

When you run the script, you'll be prompted to enter values for:

- Product cost details (COGS, shipping, fees)
- Selling price and units sold
- Marketing and advertising costs
- Operational costs (fixed and variable)
- Tax rate

At the end, the script will display a complete performance summary.

## 📊 Output Summary

The calculator reports:

- Product Name
- Total Revenue
- Total Cost
- Net Profit (after tax)
- Profit Margin (%)
- Break-Even Units
- Return on Investment (ROI)
- Return on Ad Spend (ROAS)

## 🧮 Example Input

```bash
Enter product name: Wireless Earbuds
Unit cost ($): 15
Shipping cost per unit ($): 3
Platform fee (% of selling price): 10
Flat transaction fee ($): 0.3
Transaction fee (% of selling price): 2.9
Other variable cost per unit ($): 1
Selling price ($): 40
Units sold: 100
Total ad cost ($): 200
Fixed business costs ($): 500
Tax rate (%): 5
```

## 📊 Output Summary

After entering your values, you'll get a summary like this:

```bash
EBS Report:
Product: Wireless Earbuds
Total Revenue: $4,000.00
Total Cost: $2,870.00
Net Profit (after tax): $823.50
Profit Margin: 20.59%
Break-Even Units: 65.12
ROI: 109.80%
ROAS: 20.00
```

## 🧾 Variables Used

| Variable                  | Description                                      |
| ------------------------- | ------------------------------------------------ |
| `unit_cost`               | Cost to acquire or produce one unit              |
| `shipping_cost_per_unit`  | Shipping cost per unit sold                      |
| `platform_fee_percent`    | Selling platform fee (e.g., Amazon, Etsy, etc.)  |
| `transaction_fee_flat`    | Fixed transaction fee per order                  |
| `transaction_fee_percent` | Variable transaction fee (as % of selling price) |
| `variable_costs`          | Any additional per-unit costs                    |
| `selling_price`           | Retail price per unit                            |
| `units_sold`              | Number of units sold                             |
| `ad_cost_total`           | Total ad/marketing expenses                      |
| `fixed_costs`             | Fixed monthly or operational business expenses   |
| `tax_rate_percent`        | Tax rate applied to revenue                      |
| `revenue`                 | Total revenue from sales                         |
| `total_cost`              | Total cost of goods sold, shipping, and fees     |
| `net_profit`              | Net profit after tax                             |
| `profit_margin`           | Profit margin as a percentage                    |
| `break_even_units`        | Break-even point in units sold                   |
| `roi`                     | Return on investment (ROI)                       |
| `roas`                    | Return on ad spend (ROAS)                        |

# This script calculates various financial metrics for an ecommerce business based on user inputs.
# It includes product costs, sales revenue, marketing expenses, and operational costs to provide a comprehensive financial overview.
# The output includes total revenue, costs, net profit, profit margin, break-even units, ROI, and ROAS.
# The script is designed to help ecommerce entrepreneurs assess their business performance and make informed decisions.


def main():
    print("Ecommerce Business Success (EBS) Calculator\n")

    # Product & Cost Inputs
    product_name = input("Enter product name: ")
    unit_cost = float(input("Unit cost ($): "))
    shipping_cost_per_unit = float(input("Shipping cost per unit ($): "))
    platform_fee_percent = float(input("Platform fee (% of selling price): "))
    transaction_fee_flat = float(input("Flat transaction fee ($): "))
    transaction_fee_percent = float(input("Transaction fee (% of selling price): "))
    variable_costs = float(input("Other variable cost per unit ($): "))

    # Sales & Revenue Inputs
    selling_price = float(input("Selling price ($): "))
    units_sold = int(input("Units sold: "))

    # Marketing Inputs
    ad_cost_total = float(input("Total ad cost ($): "))

    # Operational Costs
    fixed_costs = float(input("Fixed business costs ($): "))

    # Taxes
    tax_rate_percent = float(input("Tax rate (%): "))

    # --- Calculations ---
    total_revenue = selling_price * units_sold

    total_platform_fee = (platform_fee_percent / 100) * selling_price
    total_transaction_fee = transaction_fee_flat + (transaction_fee_percent / 100) * selling_price

    total_cost_per_unit = (
        unit_cost + shipping_cost_per_unit + total_platform_fee + total_transaction_fee + variable_costs
    )

    total_cost = (total_cost_per_unit * units_sold) + fixed_costs + ad_cost_total

    tax_amount = (tax_rate_percent / 100) * total_revenue
    net_profit = total_revenue - total_cost - tax_amount

    gross_profit = total_revenue - (unit_cost + shipping_cost_per_unit) * units_sold

    profit_margin = (net_profit / total_revenue) * 100 if total_revenue else 0
    break_even_units = (
        fixed_costs / (selling_price - total_cost_per_unit) if (selling_price - total_cost_per_unit) > 0 else float('inf')
    )
    roi = (net_profit / (ad_cost_total + fixed_costs)) * 100 if (ad_cost_total + fixed_costs) else 0
    roas = total_revenue / ad_cost_total if ad_cost_total else 0

    # --- Output Summary ---
    print("\nEBS Report:")
    print(f"Product: {product_name}")
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Total Cost: ${total_cost:,.2f}")
    print(f"Net Profit (after tax): ${net_profit:,.2f}")
    print(f"Profit Margin: {profit_margin:.2f}%")
    print(f"Break-Even Units: {break_even_units:.2f}")
    print(f"ROI: {roi:.2f}%")
    print(f"ROAS: {roas:.2f}")

if __name__ == "__main__":
    main()
          
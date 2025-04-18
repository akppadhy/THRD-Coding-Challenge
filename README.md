# THRD-Coding-Challenge

DESCRIPTION
To build a dynamic pricing engine that automatically adjusts product prices based on current inventory levels and recent sales performance. The goal is to optimize pricing to respond to varying supply and demand while ensuring that each product maintains a healthy margin over cost.

FILES

data/products.csv: Product pricing and stock data.
data/sales.csv: Sales performance in the past 30 days.
pricing_engine.py: Python script applying the pricing rules.
updated_prices.csv: Output with SKU, old price, and new price.

PROCESSES
1. Merges product and sales data using SKU.
2. Applies pricing rules in the given priority order:
3. Low stock & high demand → +15%
4. Dead stock → −30%
5. Overstocked → −10%
6. Ensures minimum price = 120% of cost price.
7. Outputs final price rounded to 2 decimals and includes unit (INR).

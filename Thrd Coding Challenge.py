#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

products_df = pd.read_csv("products.csv")
sales_df = pd.read_csv("sales.csv")


merged_df = pd.merge(products_df, sales_df, on="sku", how="left")
merged_df["quantity_sold"] = merged_df["quantity_sold"].fillna(0).astype(int)

updated_prices = []

for index, row in merged_df.iterrows():
    sku = row['sku']
    current_price = row['current_price']
    cost_price = row['cost_price']
    stock = row['stock']
    quantity_sold = row['quantity_sold']
    
    new_price = current_price  
    

    if stock < 20 and quantity_sold > 30:
        new_price = current_price * 1.15
    
   
    elif stock > 200 and quantity_sold == 0:
        new_price = current_price * 0.70

    elif stock > 100 and quantity_sold < 20:
        new_price = current_price * 0.90
    
 
    min_allowed_price = cost_price * 1.2
    if new_price < min_allowed_price:
        new_price = min_allowed_price

    new_price = round(new_price, 2)
    
    updated_prices.append({
        "sku": sku,
        "old_price": f"{current_price:.2f} INR",
        "new_price": f"{new_price:.2f} INR"
    })


output_df = pd.DataFrame(updated_prices)

output_df.to_csv("updated_prices.csv", index=False)
print("updated_prices.csv has been generated.")


# In[ ]:





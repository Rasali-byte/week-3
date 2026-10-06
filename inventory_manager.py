# File Name: inventory_manager.py

# ==========================================
# Task 1: Initialize Data Structures
# ==========================================

# Inventory dictionary with stock levels
inventory = {
    "Widget": 10,
    "Gadget": 5,
    "Sensor": 0,
    "Cable": 15
}

# Incoming order queue: [Item Name, Requested Quantity]
order_queue = [
    ["Widget", 3],      # Scenario 1: Full Fulfillment
    ["Gadget", 7],      # Scenario 2: Partial Fulfillment (5 available, needs 7)
    ["Sensor", 2],      # Scenario 3: Out of Stock (0 available)
    ["Cable", 15],      # Scenario 4: Full Fulfillment (exact stock match)
    ["Processor", 4]    # Scenario 5: Invalid/Missing Item
]

# Trackers for analytics
unfulfilled_orders = []
fully_fulfilled_count = 0

print("--- Processing Incoming Orders ---")

# ==========================================
# Task 2: Process Orders Loop
# ==========================================

for order in order_queue:
    item_name = order[0]
    requested_qty = order[1]

    # Check if item key exists in the inventory dictionary
    if item_name in inventory:
        stock = inventory.get(item_name)

        # 1. Full Fulfillment
        if stock >= requested_qty:
            inventory[item_name] -= requested_qty
            fully_fulfilled_count += 1
            print(f"SUCCESS: Fulfilled {requested_qty}x '{item_name}'.")

        # 2. Partial Fulfillment
        elif stock > 0:
            shortfall = requested_qty - stock
            inventory[item_name] = 0
            unfulfilled_orders.append([item_name, shortfall])
            print(f"PARTIAL: Supplied {stock}x '{item_name}'. Shortfall of {shortfall}x recorded.")

        # 3. Out of Stock
        else:
            unfulfilled_orders.append([item_name, requested_qty])
            print(f"ALERT: '{item_name}' is out of stock.")

    # 4. Invalid / Non-Existent Item Key
    else:
        unfulfilled_orders.append([item_name, requested_qty])
        print(f"ALERT: Item '{item_name}' not found in inventory catalog.")

# ==========================================
# Task 3: Analytics & Summary Output
# ==========================================

print("\n--- End-of-Batch Summary Report ---")
print(f"1. Final Updated Inventory: {inventory}")
print(f"2. Total Fully Fulfilled Orders: {fully_fulfilled_count}")
print(f"3. Unfulfilled Items/Quantities: {unfulfilled_orders}")
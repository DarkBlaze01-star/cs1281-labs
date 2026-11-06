

IT 12


# IT12: Rough Cut - Hello, Shop Floor
greet = "Hello, Shop Floor!"
print(greet)

name = input("Operator name: ")
print(f"Welcome to the bench, {name}!")
     
Hello, Shop Floor!
IT 10


# IT10: Standard - The Batch Inspector, Live
accept_count = 0
rework_count = 0
scrap_count = 0

print("--- Batch Inspection Started (10 Parts) ---")

for i in range(10):
    diameter = float(input(f"Measured diameter for part {i+1}: "))

    # Boundary logic example (adjust thresholds as per your lab specs)
    if 24.95 <= diameter <= 25.05:
        print("-> ACCEPT")
        accept_count += 1
    elif (24.90 <= diameter < 24.95) or (24.05 < diameter <= 25.10):
        print("-> REWORK")
        rework_count += 1
    else:
        print("-> SCRAP")
        scrap_count += 1

print("\n--- Final Inspection Report ---")
print(f"Accepted parts: {accept_count}")
print(f"Rework parts:   {rework_count}")
print(f"Scraped parts:  {scrap_count}")
     
IT 8


# IT8: Fine - The Pallet Clerk
total_parts = int(input("Enter total parts: "))
box_size = int(input("Enter box size: "))

full_boxes = total_parts // box_size
loose_parts = total_parts % box_size

print(f"Full boxes: {full_boxes}")
print(f"Loose parts: {loose_parts}")

# Audit line (must evaluate to True)
audit_passed = (full_boxes * box_size + loose_parts) == total_parts
print(f"Audit verification (boxes * size + loose == total): {audit_passed}")
     
IT 6


# IT6: Precision - End of Shift
accept_count = 0
rework_count = 0
scrap_count = 0

print("--- Shift Batch Inspection ---")
for i in range(10):
    diameter = float(input(f"Measured diameter for part {i+1}: "))

    if 24.95 <= diameter <= 25.05:
        accept_count += 1
    elif (24.90 <= diameter < 24.95) or (24.05 < diameter <= 25.10):
        rework_count += 1
    else:
        scrap_count += 1

# Pack only accepted parts into boxes of 4
box_size = 4
full_boxes = accept_count // box_size
loose_accepted = accept_count % box_size

print("\n--- Closing Shift Summary ---")
print(f"Total Bin Counts -> ACCEPT: {accept_count} | REWORK: {rework_count} | SCRAP: {scrap_count}")
print(f"Accepted parts packed into boxes of {box_size}:")
print(f"  - Full boxes: {full_boxes}")
print(f"  - Loose accepted parts: {loose_accepted}")
     

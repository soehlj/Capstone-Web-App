import csv
printer_want = input("What type of printer do you want to use:\nEnter Number FDM=1 OR SLA=2:\n")
if printer_want == 2:
    print_want = "SLA"
else:
    print_want = "FDM"
with open('sample_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    next(reader)
    for row in reader:
        if print_want == row[1]:
            material, printer, silicon, smoothness, release, durability, accuracy, temp, cost, notes = row
            print(f"""Material: {material}, Printing Technique: {printer}, Silicone Type: {silicon}, Surface Smoothness (1-10): {smoothness}, Ease of Release (1-10): {release}, Durability (1-10): {durability}, Detail Accuracy (1-10): {accuracy}, Print Temperature (°C): {temp}, Cost ($/kg): {cost}, Notes: {notes}\n""")
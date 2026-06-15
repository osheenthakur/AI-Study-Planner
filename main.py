subjects = input("Enter subjects separated by commas: ").split(",")

hours = int(input("How many hours can you study today? "))

print("\nToday's Study Plan:\n")

for i, subject in enumerate(subjects):
    if i == 0:
        allocated_hours = hours * 0.5
    else:
        allocated_hours = (hours * 0.5) / (len(subjects) - 1)

    print(f"{subject.strip()} - {allocated_hours:.1f} hours")
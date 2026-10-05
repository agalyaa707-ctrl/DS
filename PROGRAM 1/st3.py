jobs = []

jobs.append("Report")
jobs.append("Assignment")
jobs.append("Question Paper")

print("Printer Jobs:", jobs)
print("Next Job:", jobs[-1])

printed = jobs.pop()
print("Printed:", printed)

print("Remaining Jobs:", jobs)
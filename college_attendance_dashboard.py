
import pandas as pd
import matplotlib.pyplot as plt

# 1. Student Attendance Dataset
data = {
    "Student": ["Amit", "Sneha", "Rahul", "Priya", "Neha", "Akash"],
    "Present": [24, 25, 20, 29, 18, 22],
    "Total":   [30, 30, 30, 30, 30, 30]
}

df = pd.DataFrame(data)

# 2. Calculate attendance percentage
df["Attendance (%)"] = (
    df["Present"] / df["Total"] * 100
).round(2)

df["Absent"] = df["Total"] - df["Present"]

# 3. Attendance status
df["Status"] = df["Attendance (%)"].apply(
    lambda x: "Eligible" if x >= 75 else "Shortage"
)

# 4. Dashboard summary
total_students = len(df)
avg_attendance = round(df["Attendance (%)"].mean(), 2)
eligible = (df["Status"] == "Eligible").sum()
shortage = (df["Status"] == "Shortage").sum()

print("=" * 45)
print(" COLLEGE ATTENDANCE ANALYTICS DASHBOARD")
print("=" * 45)

print("\nDASHBOARD SUMMARY")
print("-" * 30)
print("Total Students       :", total_students)
print("Average Attendance   :", str(avg_attendance) + "%")
print("Eligible Students    :", eligible)
print("Attendance Shortage  :", shortage)

print("\nSTUDENT ATTENDANCE REPORT")
print("-" * 75)
print(df.to_string(index=False))

# 5. Create dashboard graphs
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Bar graph
axes[0].bar(
    df["Student"],
    df["Attendance (%)"],
    label="Attendance"
)

axes[0].axhline(
    y=75,
    linestyle="--",
    label="75% Required"
)

axes[0].set_title("Student-wise Attendance")
axes[0].set_xlabel("Student Name")
axes[0].set_ylabel("Attendance (%)")
axes[0].set_ylim(0, 110)
axes[0].legend()
axes[0].tick_params(axis="x", rotation=45)

# Pie chart
present_days = df["Present"].sum()
absent_days = df["Absent"].sum()

axes[1].pie(
    [present_days, absent_days],
    labels=["Present Days", "Absent Days"],
    autopct="%1.1f%%",
    startangle=90,
    labeldistance=1.05
)

axes[1].set_title("Overall Attendance Distribution")

fig.suptitle("College Attendance Analytics Dashboard")
plt.tight_layout()
plt.show()

# 6. Save report
df.to_csv(
    "/storage/emulated/0/Download/attendance_report.csv",
    index=False
)

print("\nCSV report saved in Download folder.")

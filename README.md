# QuickDeliver_BF
A python console application  to manage deliveries, client, couriers and parcels for small transport business

# 🚚 QuickDeliver_BF

> A Python console application built as part of the Programming I with Python course.
> by first year students in computer-science of Burkina Institute of Technology (BIT) — May 2026.

---

## 📌 Description

QuickDeliver_BF is a console-based delivery management application built in Python.
It allows a transport company to register clients and couriers, create and track deliveries,
calculate shipping fees automatically, and generate activity reports — all saved to local
text files for data persistence.

The application runs entirely in the terminal. The user navigates through a numbered menu
and interacts by typing numbers and text.

---

##  How to Run the Project

### Requirements
- Python **3.10** or higher
- No external libraries required — only built-in Python modules are used

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/ghosthassanekabore18-jpg/QuickDeliver_BF.git
```

2. **Move into the project folder**
```bash
cd QuickDeliver_BF
```

3. **Run the program**
```bash
python main.py
```

> ⚠️ On some systems, use `python3` instead of `python`.

---

## Features

- Register a new client with their personal information
- Register a new courier with their vehicle type and delivery zone
- Create a delivery by linking a client, a courier and a parcel
- Automatically calculate shipping fees based on parcel weight
- Apply a 20% surcharge for fragile parcels
- Track any delivery status using its unique ID
- Update a delivery status : `pending → in transit → delivered / cancelled`
- View the full list of clients, couriers and deliveries
- Generate a statistical report saved automatically to a text file
- Persist all delivery data across sessions using local text files

---




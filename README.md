# 🚖 BigTaxi - Smart Road Vehicle Booking System

**BigTaxi** is an intelligent and flexible taxi booking platform built with Django. It allows users to book any kind of road vehicle (car, bike, truck, cycle, etc.) based on passenger count, vehicle type, and preferred company. The system also offers a driver login portal with referral logic and a complete trip management system.

---

## 🔑 Features

👤 **User Booking System:**  
Users can select number of passengers, vehicle type, and company. The system filters vehicles based on these inputs for accurate results.

🚗 **All Road Vehicles Allowed:**  
Supports any running road vehicle including taxis, trucks, bikes, cars, and cycles.

👨‍✈️ **Driver Login and Referral System:**  
Drivers can log in to accept rides. A special referral code is given:
- Only after completing **15 trips**
- Valid for **6 months**
- After 6 months, another 20 trips are required to get a new code
- Ensures **fair pricing**, and **no extra charges** are deducted from drivers

🧭 **Trip Management System:**  
Tracks all types of trips:
- Ongoing trips
- Cancelled trips (both before and during)
- Completed trips  
Includes a secure **payment integration** for completed trips.

🚨 **Emergency Trip Help:**  
A dedicated help section for customers to request urgent trips if a nearby driver is available.

🛠️ **Scalable for Future Features:**  
More tools and modules will be added in future updates including better customer support, analytics, and advanced trip control.

---

## 💻 Tech Stack

- **Frontend:** HTML, CSS, Bootstrap, JavaScript  
- **Backend:** Django, Python  
- **Database:** SQLite / PostgreSQL  
- **Other:** Django ORM

---

> 🔧 Project under development. Contributions and suggestions are welcome.

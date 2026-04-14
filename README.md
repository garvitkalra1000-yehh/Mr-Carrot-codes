### 👤 Garvit (251302250)

# 🔐 PASSWORD GENERATOR

---

## 📌 Project Description

This project is a simple and effective **Password Generator** built using Python.
It creates strong and secure passwords by combining **letters, digits, and special characters**, making it useful for improving online security.

---

## ⚙️ How It Works

* Takes password length as input from the user
* Uses:

  * `string.ascii_letters` → Alphabets
  * `string.digits` → Numbers
  * `string.punctuation` → Special characters
* Combines all characters into a pool
* Randomly selects characters using `random.sample()`
* Generates a secure password

---

## 🛠 Technologies Used

* Python
* Built-in Libraries:

  * `string`
  * `random`

---

## 🚀 How to Run

1. Open terminal in project folder
2. Run the program:

   ```bash
   python main.py
   ```
3. Enter desired password length
4. Get your secure password instantly 🔑

---

## 🌍 Real-life Application

* Used in **password managers**
* Helps users create **strong and unpredictable passwords**
* Prevents hacking and brute-force attacks

---

## 🔐 Features

* Generates strong passwords
* Includes letters, numbers, and symbols
* User-defined length
* Simple and fast

---

## 💡 Future Improvements

* Add option to exclude special characters
* Add GUI interface
* Save generated passwords securely

---

## 🎯 Conclusion

This project demonstrates how Python can be used to build **security-focused tools** in real-world scenarios. It highlights the importance of strong passwords in protecting digital data.

---




# Crop Disease Detection using Python

## 📌 Description
This project detects whether a plant leaf is healthy or diseased using image processing.

## 🛠 Technologies Used
- Python
- OpenCV
- NumPy

## ⚙️ How it Works
- Converts image to HSV format
- Detects green pixels
- Calculates percentage of healthy area
- Classifies leaf condition

## 🌍 Real-life Application
Used in agriculture apps like Plantix to help farmers detect crop diseases early.

## 🚀 How to Run
1. Install dependencies:
   pip install opencv-python numpy
2. Run:
   python main.py

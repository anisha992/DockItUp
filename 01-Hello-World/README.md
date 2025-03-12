### **Docker Hello World 🚀**

Welcome to the **Hello World** project using Docker! This guide helps you set up a simple **Dockerized Python application** that prints `"Hello, World!"`.

---

📌 **Project Overview**
-----------------------

This project demonstrates how to:  
👉 Create a simple Python script  
👉 Write a Dockerfile  
👉 Build a Docker image  
👉 Run a Docker container  

---

📂 **Project Structure**
------------------------

```
01-Hello-World/
│── Dockerfile
│── app.py
│── README.md
```

---

🛠 **Prerequisites**
--------------------

Ensure you have the following installed:  
🔹 Docker Desktop  
🔹 [Python](https://www.python.org/downloads/)  
🔹 Code Editor (VS Code recommended)  

---

📝 **Step 1: Create the Python Script**
---------------------------------------

Create a file **app.py** and add the following:

```python
print("Hello, World!")
```

---

🐳 **Step 2: Create the Dockerfile**
------------------------------------

Inside your project folder, create a **Dockerfile** and add:

```dockerfile
# Use official Python image
FROM python:3.9

# Copy application files
COPY app.py /app/app.py

# Set working directory
WORKDIR /app

# Run the Python script
CMD ["python", "app.py"]
```

---

⚙️ **Step 3: Build & Run the Docker Container**
-----------------------------------------------

### ✅ **Build the Docker Image**
```bash
docker build -t hello-world-app .
```

### ✅ **Verify the Image**
```bash
docker images
```

### ✅ **Run the Container**
```bash
docker run hello-world-app
```

🖥️ You should see:
```bash
Hello, World!
```

---


🎯 **Conclusion**
-----------------

This project is a great **first step** into Docker! Now you know how to **build, run, and manage** Docker containers. 🐳✨

Happy Docking! ⚓🌊


# Dockerized Streamlit Development Environment

This guide helps you set up a Streamlit application inside a Docker container for an efficient and portable development experience. 🚀

## ✅ Prerequisites
Before setting up the environment, ensure you have the following installed on your machine:

- 🔹 **Docker** (Install from [here](https://docs.docker.com/get-docker/))
- 🔹 **pip** 📦 (Ensure it's up to date: `pip install --upgrade pip`)
- 🔹 **Basic knowledge of Streamlit** 📊

## 📂 Directory Structure
```
project_root/
│── .streamlit/
│   └── config.toml
│── src/
│   └── main.py
│── Dockerfile
│── requirements.txt
│── README.md
```

## 📜 File Explanations
### 1️⃣ `.streamlit/config.toml`
This file configures Streamlit settings, ensuring smooth UI rendering.

```toml
[server]
headless = true
port = 8501
```

### 2️⃣ `src/main.py`
This file contains the core logic of the Streamlit application.

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Streamlit App Inside Docker 🚀")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    fig, ax = plt.subplots()
    df.hist(ax=ax)
    st.pyplot(fig)

### 2️⃣ `Dockerfile`
Defines the containerized environment for Streamlit.

```dockerfile
# Use a lightweight Python image
FROM python:3.9-slim  

# Set working directory
WORKDIR /app  

# Copy dependencies and install them
COPY requirements.txt /app/  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy all project files
COPY . /app/  

# Expose Streamlit’s default port
EXPOSE 8501  

# Run the Streamlit app
CMD ["streamlit", "run", "src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 3️⃣ `requirements.txt`
Contains necessary dependencies for the project:

```
streamlit
pandas
matplotlib
```

## ⚡ Steps to Run the Project
### 1️⃣ **Navigate to the project directory**
```sh
cd path/to/project
```

### 2️⃣ Build the Docker Image
Run the following command to build the Docker image:
```sh
docker build -t streamlit-app .
```

### 3️⃣ Run the Docker Container
Run the following command to start the container:
```sh
docker run -p 8501:8501 --rm --name streamlit-container streamlit-app
```

If you encounter an error that says `Bind for 0.0.0.0:8501 failed: port is already allocated`, it means a container is already using the port. Stop the existing container using:
```sh
docker stop streamlit-container
```
Then rerun the command to start the container.

### 4️⃣ Open in Browser
Once the container is running, open your web browser and go to:
```
http://localhost:8501
```

## 🎯 Conclusion
You now have a fully functional Streamlit development environment running inside Docker! 🚀


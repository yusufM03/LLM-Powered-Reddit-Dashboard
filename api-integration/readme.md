

---

# **Flask API for Article Summarization with Grafana Visualization**

## **Overview**
This part demonstrates how to create a Flask API that integrates with the Groq LLM API to summarize articles. The summarized data is visualized dynamically on a Grafana dashboard using the JSON API plugin.

### **Features**
- Summarize articles using Groq's LLM API.
- Build a Flask API to serve summaries.
- Visualize summaries dynamically on Grafana dashboards.
- Utilize Amazon EC2 for API hosting.

---

## **Project Architecture**
1. User provides an article title through Grafana.
2. Grafana sends the title to the Flask API via the JSON API plugin.
3. Flask fetches the article using its title, summarizes it using Groq's LLM, and returns the result.
4. Grafana displays the summarized article on the dashboard.

---

## **Setup Instructions**

### **1. Prerequisites**
- Amazon EC2 instance (or any server to host the Flask API).
- Python 3.x installed on the EC2 instance.
- Grafana installed and accessible.

---

### **2. Setting Up the Flask API**
1. **Log in to your EC2 instance**:
   ```bash
   ssh -i your-key.pem ec2-user@your-ec2-public-ip
   ```

2. **Install Python dependencies**:
   ```bash
   sudo yum install python3-pip -y
   pip install Flask requests praw groq
   ```

3. **Create the Flask application**:
   ```bash
   mkdir flask_api
   cd flask_api
   nano app.py
   ```

4. **Add the following code to `app.py`**
   

5. **Run the Flask API**:
   ```bash
   python app.py
   ```

6. **Add a security group rule** in AWS to allow inbound traffic on port `5000`.

7. **Test the API**:
   - Open a browser and navigate to `http://<ec2-public-ip>:5000/summarize?title=sample-title`.

---

### **3. Configuring Grafana**
1. **Install the JSON API Plugin**:
   - Go to **Configuration** → **Plugins** and install the JSON API plugin.

2. **Add a New Data Source**:
   - Navigate to **Configuration** → **Data Sources** → **Add Data Source** → **JSON API**.
   - Set the URL to: `http://<ec2-public-ip>:5000/summarize`.

3. **Create a Variable for Article Titles**:
   - Go to **Dashboard Settings** → **Variables** → **Add Variable**.
   - Name it `ArticleTitle`.
   - Set a query like `SELECT id  FROM raw-data`.

4. **Add a Panel**:
   - Choose **Table Panel**.
   - Set the data source to **JSON API**.
   - In the query options, use:
     - **Path**: `//?title=${ArticleTitle}`.
     - **Field**: `$.summary`.
     - Set type to `JSONata`.

---

## **Testing**
1. Open the Grafana dashboard.
2. Select an article title from the dropdown.
3. View the summarized content in the panel.


## **License**
This project is open-source and available under the MIT License.

---

## **Author**
Created by **Youssef Makhlouf**.  
Contact: [youssef.makhlouf@supcom.tn](mailto:youssef.makhlouf@supcom.tn)

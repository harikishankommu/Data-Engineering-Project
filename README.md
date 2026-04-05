# 📊 Sales Data ETL Pipeline

A simple **Data Engineering project** that builds an **ETL (Extract, Transform, Load) pipeline** using Python and PostgreSQL.  
It extracts raw sales data from CSV files, cleans and transforms it using pandas, and loads the processed data into a database for analysis.

---

## 🧠 How It Works (Simple Flow)

Raw CSV → extract.py → transform.py → load.py → PostgreSQL → SQL Analysis

### Step-by-step:
1. **extract.py** → Reads raw sales data from CSV file  
2. **transform.py** → Cleans data and calculates revenue  
3. **load.py** → Loads processed data into PostgreSQL  
4. **SQL Queries** → Perform analysis on stored data  

---

## 🧩 Features
✅ End-to-end ETL pipeline  
✅ Data cleaning using pandas  
✅ Revenue calculation (Quantity × Price)  
✅ Modular scripts (extract, transform, load)  
✅ PostgreSQL integration  
✅ SQL-based analytics  
✅ Beginner-friendly project structure  

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- PostgreSQL  
- SQL  
- psycopg2  

---

## 📁 Project Structure

DEP/  
├── data/  
│   ├── raw_sales.csv  
│   ├── datafile.zip  
│   └── cleaned_sales.csv  
├── scripts/  
│   ├── extract.py  
│   ├── transform.py  
│   └── load.py  
├── sql/  
│   ├── create_tables.sql  
│   └── analytics_queries.sql  
└── README.md  

---

## ⚙️ CLONING THE REPOSITORY

To clone the project, use:

git clone https://github.com/harikishankommu/Data-Engineering-Project.git  

Move into the project directory:

cd Data-Engineering-Project  

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install pandas psycopg2
```

### 2️⃣ Setup PostgreSQL Database
- Install PostgreSQL  
- Create a database (e.g., `sales_db`)  

Run SQL script:
```bash
psql -U username -d sales_db -f sql/create_tables.sql
```

---

### 3️⃣ Run ETL Pipeline
```bash
python scripts/extract.py
python scripts/transform.py
python scripts/load.py
```

---

## 🗄️ Example SQL Analysis

### 📌 Total Revenue
```sql
SELECT SUM(revenue) FROM sales_data;
```

### 📌 Average Order Value
```sql
SELECT AVG(revenue) FROM sales_data;
```

### 📌 Top 10 Orders
```sql
SELECT * FROM sales_data ORDER BY revenue DESC LIMIT 10;
```

---

## 💡 Example

**Input (raw_sales.csv):**
```csv
Order_ID,Product,Quantity,Price
1,Shirt,2,500
```

**After Transform:**
```text
Revenue = 2 × 500 = 1000
```

Stored in PostgreSQL → Ready for analysis
## 🧰 Common Issues

| Problem | Reason | Fix |
|--------|--------|-----|
| Database connection error | Wrong credentials | Check DB name, user, password |
| Table not found | Table not created | Run create_tables.sql |
| Data not loading | Script order incorrect | Run extract → transform → load |
| psycopg2 error | Not installed | Install via pip |

---

## 🚀 Outcome

✔ Built a complete ETL pipeline  
✔ Processed raw CSV data into structured format  
✔ Stored data in PostgreSQL for analysis  
✔ Performed SQL-based business insights  

---

## 👨‍💻 Author
**K. Hari Kishan**  
Built as a learning project for understanding ETL pipelines and data engineering concepts.

---

## 📜 License
This project is open-source and free to use for educational purposes.

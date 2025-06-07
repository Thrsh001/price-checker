# Price Checker - Web Scraping Tool

A flexible Python-based web scraping tool to compare product prices across multiple online shops. Built using a modular architecture that combines the **Factory Method** and **Strategy** design patterns for easily extensible scraping logic.


## 💡 Features

- Scrapes product prices from multiple online shops
- Tracks price history for comparison and analysis
- Easily extensible with new shops and scraping strategies
- Uses SQLite for lightweight local storage
- Separates scraping logic, entities, and infrastructure for clarity and scalability

## 🛠 Getting Started

### 📦 Dependencies

- `Python` 3.10+
- `SQLite` (installed by default with Python)
- `pip` (Python package manager)

### ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Thrsh001/price-checker
cd price-checker
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Configure Environment

Create a `.env` file in the project root with your database URL. For SQLite, use:
`DATABASE_URL=sqlite:///./price_checker.db`

### 4. Populate database

Edit populate_db.py with your data, then:
```bash
python3 populate_db.py
```


### 🚀 Executing program

```bash
python3 main.py --product PRODUCT --shop SHOP
```
Replace `PRODUCT` with the product name and `SHOP` with the shop name as stored in the database.

### 🧪 Testing

This project uses `pytest` for testing.

**Run tests** from the project root:

```bash
python3 -m pytest
```

- Make sure your test files are named like `test_*.py` and are located in the `Tests/` directory.
- You may need to set up a test database or mock the database for isolated testing.


## Authors
Thrsh001

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the LICENSE.md file for details

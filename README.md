# Static Site Generator (Python)

Minimal generator that builds `index`, `events`, and `places` pages from `article/db.json`.

## 1. Install Python (if not installed)

Check:

```
python3 --version
```

If Python is not installed:

**Ubuntu / Debian**

```
sudo apt update
sudo apt install python3 python3-venv
```

**Mac (Homebrew)**

```
brew install python
```

**Windows**

Install Python from:  
https://www.python.org/downloads/

---

## 2. Create virtual environment

In the project folder:

```
python3 -m venv venv
```

---

## 3. Activate environment

**Linux / Mac**

```
source venv/bin/activate
```

**Windows**

```
venv\Scripts\activate
```

---

## 4. Install dependency

```
pip install jinja2
```

---

## 5. Run generator

```
python build.py
```

---

## 6. Result

Generated site is created in root dir:




---

## 7. Add new article

1. Create HTML file in:

```
articles/
```

2. Add entry to:

```
db.json
```

3. Run again:

```
python build.py
```

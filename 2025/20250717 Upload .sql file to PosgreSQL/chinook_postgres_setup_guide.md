
# 🎵 Upload Chinook SQL File to PostgreSQL on Windows

This guide walks you through importing the Chinook database into PostgreSQL and fixing common issues during the process.

---

## 🧰 Prerequisites

- ✅ PostgreSQL (installed via [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/))
- ✅ pgAdmin 4
- ✅ `psql` in system PATH (verify using `psql --version`)
- ✅ Chinook SQL File (e.g., `Chinook_PostgreSql.sql`)

---

## 🪜 Step-by-Step Instructions

### 1. ✅ Add `psql` to PATH (if not already)

- Open **System Properties → Environment Variables**
- Under **System variables**, select `Path` → **Edit** → **New**
- Add the PostgreSQL bin path, e.g.:

```
C:\Program Files\PostgreSQL\16\bin
```

---

### 2. 📥 Convert SQL File to UTF-8 (optional, if encoding issues)

```bash
iconv -f WINDOWS-1252 -t UTF-8 "Chinook_PostgreSql.sql" -o "Chinook_PostgreSql_utf8.sql"
```

> Use `iconv -l` to see supported encodings.

---

### 3. 🛠 Create the Database (if not exists)

```bash
psql -U postgres
CREATE DATABASE chinook;
\q
```

---

### 4. 📤 Import SQL File

```bash
psql -U postgres -d chinook -f "C:\Path\To\Chinook_PostgreSql_utf8.sql"
```

---

## 🧼 Common Errors & Fixes

### 🔴 `syntax error at or near "GO"` or `[...]`

These indicate the file is written in SQL Server syntax.

✅ **Fix**: Use a cleaned version made for PostgreSQL:  
👉 Download from: https://github.com/lerocha/chinook-database

Use this one:  
```
chinook_pg_serial_pk_proper_naming.sql
```

---

### 🔴 Encoding Errors

Example:  
```bash
ERROR: character with byte sequence 0x81 in encoding "WIN1252"
```

✅ Fix: Convert file to UTF-8 using `iconv`.

---

### 🔴 `FATAL: database "postgres" does not exist`

Cause: You accidentally deleted the default `postgres` database.

✅ Fix: Recreate it via terminal or reinitialize PostgreSQL.

---

### 🔴 `FATAL: password authentication failed for user "postgres"`

- Make sure you enter the correct password.
- You can reset the password using:

```bash
psql -U postgres
ALTER USER postgres WITH PASSWORD 'newpassword';
```

---

## 🧭 Viewing Table Counts

To get the number of rows in each table:

```sql
SELECT table_name, 
       (xpath('/row/cnt/text()', xml_count))[1]::text::int AS row_count
FROM (
  SELECT table_name,
         query_to_xml(format('SELECT COUNT(*) AS cnt FROM %I', table_name), false, true, '') AS xml_count
  FROM information_schema.tables
  WHERE table_schema = 'public'
) AS counts;
```

---

## 🛠 Configure Password in pgAdmin

1. Right-click server → **Properties**
2. Go to **Connection** tab
3. Scroll down and enter **Password**
4. ✅ Check "Save Password"
5. Click **Save**

---

## 🧼 Reset Everything (optional)

If you want to reset your PostgreSQL setup:
- Reinstall PostgreSQL
- Remove `data` directory
- Reinitialize cluster

---

## 📎 Reference

- Chinook DB: https://github.com/lerocha/chinook-database
- PostgreSQL: https://www.postgresql.org/
- SQL Fixes: https://stackoverflow.com/


# 📦 How to Import Chinook Database into PostgreSQL on Windows



Most important commands: 
```bash
psql -U postgres
```

```SQL
DROP DATABASE IF EXISTS chinook;
CREATE DATABASE chinook;
```

```bash
psql -U postgres -d chinook -f "C:\Users\Shadan\Downloads\chinook_pg_serial_pk_proper_naming.sql"

```

This guide explains how to import the Chinook sample database into PostgreSQL using the `Chinook_PostgreSql.sql` file.

---

## ✅ Prerequisites

- PostgreSQL installed on your system (e.g., version 16)
- Chinook SQL file: `Chinook_PostgreSql.sql`
- PostgreSQL's `psql` command-line tool added to your system PATH

---

## 🧰 Step 1: Add `psql` to System PATH

1. Locate the PostgreSQL `bin` folder, typically at:
   ```
   C:\Program Files\PostgreSQL\16\bin
   ```

2. Add this path to your **System Environment Variables**:
   - Search **“Environment Variables”** in Windows search
   - Click **Edit the system environment variables**
   - Click **Environment Variables…**
   - Under **System Variables**, select `Path` and click **Edit**
   - Click **New**, paste the path
   - Click **OK** to save

3. Restart Command Prompt and verify:
   ```bash
   psql --version
   ```

---

## 📁 Step 2: Prepare the SQL File

Ensure your `Chinook_PostgreSql.sql` file is saved locally. Example path:

```
C:\Users\YourUsername\Downloads\Chinook_PostgreSql.sql
```

---

## 💻 Step 3: Run the SQL Script

In Command Prompt, execute:

```bash
psql -U postgres -f "C:\Users\YourUsername\Downloads\Chinook_PostgreSql.sql"
psql -U postgres -f "C:\Users\Shadan\Downloads\Chinook_PostgreSql.sql"
psql -U postgres -f "C:\Users\Shadan\Downloads\chinook_pg_serial_pk_proper_naming.sql"
```


> Replace the file path with your actual file location. Enter the PostgreSQL password when prompted.

---

## 🧪 Step 4: Connect to the Chinook Database

```bash
psql -U postgres -d chinook
```

---

## 🔍 Step 5: Verify the Tables

In the `psql` prompt:

```sql
\dt
```

This will list tables such as `artist`, `album`, `track`, etc.

Try a test query:

```sql
SELECT * FROM artist LIMIT 5;
```

---

## 🆘 Troubleshooting

- **`psql not recognized`** → Check that the PostgreSQL `bin` folder is added to PATH
- **`relation "artist" does not exist`** → The script may not have run completely. Rerun it using step 3.
- Use **pgAdmin** as a GUI alternative to import the file if preferred

---

## ✅ Done!

You have successfully imported the Chinook sample database into PostgreSQL!

psql -U postgres -f "C:\Users\Shadan\Downloads\Chinook_PostgreSql_utf8.sql"



## To Drop the chinook Database
Run this from your terminal (not inside psql):
If you're inside the psql shell, run:

```sql
\q  -- to exit
```


```bash
dropdb -U postgres chinook
dropdb -U postgres postgres
```

## Verify Record Counts per Table

```bash
psql -U postgres -d chinook
```

```SQL
SELECT 
  relname AS table_name,
  n_live_tup AS estimated_rows
FROM 
  pg_stat_user_tables
ORDER BY 
  estimated_rows DESC;
```



psql chinook -1 -f "C:\Users\Shadan\Downloads\Chinook_PostgreSql_utf8.sql" &>errorlog.txt
from db_connection import connect_db

# =========================
# VIEW PRODUCTS
# =========================
def view_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tblProducts")
    rows = cursor.fetchall()
    print("\n--- Products ---")
    print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Stock':<10}")
    print("-" * 45)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<10} {row[3]:<10}")
    conn.close()

# =========================
# ADD PRODUCT
# =========================
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    stock_qty = int(input("Enter stock quantity: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tblProducts (name, price, stock_qty) VALUES (?, ?, ?)",
        (name, price, stock_qty)
    )
    conn.commit()
    print("Product added successfully!")
    conn.close()

# =========================
# UPDATE PRODUCT
# =========================
def update_product():
    product_id = int(input("Enter product ID to update: "))
    name = input("Enter new name: ")
    price = float(input("Enter new price: "))
    stock_qty = int(input("Enter new stock quantity: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tblProducts SET name=?, price=?, stock_qty=? WHERE product_id=?",
        (name, price, stock_qty, product_id)
    )
    conn.commit()
    print("Product updated successfully!")
    conn.close()

# =========================
# DELETE PRODUCT
# =========================
def delete_product():
    product_id = int(input("Enter product ID to delete: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM tblProducts WHERE product_id=?",
        (product_id,)
    )
    conn.commit()
    print("Product deleted successfully!")
    conn.close()
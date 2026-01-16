try:
    from data_for_frontend import Product
    print("✓ Import successful!")
    print(f"Product class: {Product}")
except Exception as e:
    print(f"✗ Import failed: {e}")
    import traceback
    traceback.print_exc()

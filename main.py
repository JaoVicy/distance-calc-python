from defs.GeoApp import GeoDistanceApp

if __name__ == "__main__":
    app = GeoDistanceApp()
    try:
        app.run()
    finally:
        app.db_manager.close()
        # Ensure the database connection is closed
        # when the application exits.
        # This is important to prevent database locks and ensure data integrity.
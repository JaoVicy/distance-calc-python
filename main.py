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
        # The close method is called in the finally block to ensure it executes even if an error occurs.
        # This is a good practice in Python to ensure resources are properly released.
        # The application will now exit gracefully, ensuring all resources are cleaned up.
        # The database connection is closed to free up system resources.
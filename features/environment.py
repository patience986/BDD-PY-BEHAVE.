def before_all(context):
    # Set up things needed for all tests (e.g., open a database connection or set up a headless browser)
    pass

def after_all(context):
    # Clean up actions (e.g., close the database connection or clean temp files)
    if hasattr(context, 'browser'):
        context.browser.quit()

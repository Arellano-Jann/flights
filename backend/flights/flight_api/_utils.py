from datetime import datetime, timedelta

def todays_date(offset: bool = False) -> str:
    """
    Yields todays date in YYYY-DD-MM format
    """
    # Get today's date
    today = datetime.today().date()
    
    if offset:
        tomorrow = today + timedelta(days=1)

        # Format the future date as yyyy-mm-dd
        return tomorrow.strftime('%Y-%m-%d')

    # Format today's date as yyyy-mm-dd
    formatted_today = today.strftime('%Y-%m-%d')
    return formatted_today
    
    
def add_days_to_today(days_to_add: int = 1) -> str:
    """
    Yields todays date + days_to_add in YYYY-DD-MM format
    """
    # Get today's date
    today = datetime.today().date()

    # Specify the number of days to add
    days_to_add = 5  # Change this to any number of days you want to add

    # Add the specified number of days to today's date
    future_date = today + timedelta(days=days_to_add)

    # Format the future date as yyyy-mm-dd
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date
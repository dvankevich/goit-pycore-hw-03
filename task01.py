from datetime import datetime

def get_days_from_today(date):
    '''
    calculates the number of days between a given date and the current date
    Args:
        date (str): date in YYYY-MM-DD format
    Returns:
        int: returns an integer indicating the number of days from the given date to the current one. 
        If the given date is later than the current one, the result is negative
        or None if error
    '''
    try:
        date_from_iso = datetime.fromisoformat(date)
    except ValueError:
        return None
    
    today_ord = datetime.now().toordinal()
    date_ord = date_from_iso.toordinal()
    return date_ord - today_ord



if __name__ == "__main__":
    from datetime import timedelta
    print(get_days_from_today.__doc__)
    assert get_days_from_today("") == None
    assert get_days_from_today("today") == None

    now = datetime.now()
    future_date = now + timedelta(days=10)
    past_date = now - timedelta(days=10)

    assert get_days_from_today(str(now.date())) == 0
    assert get_days_from_today(str(past_date.date())) == -10
    assert get_days_from_today(str(future_date.date())) == 10


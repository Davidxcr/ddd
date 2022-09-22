def date_plus_years(original_date, years_added):
    result = original_date.replace(year = original_date.year + years_added)
    return result
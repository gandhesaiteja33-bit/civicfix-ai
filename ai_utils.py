def categorize_issue(issue):

    issue = issue.lower()

    if "pothole" in issue:
        return "Road"

    elif "road" in issue:
        return "Road"

    elif "garbage" in issue:
        return "Waste"

    elif "waste" in issue:
        return "Waste"

    elif "water" in issue:
        return "Water"

    elif "streetlight" in issue:
        return "Electricity"

    elif "light" in issue:
        return "Electricity"

    return "Other"


def detect_priority(issue):

    issue = issue.lower()

    if "accident" in issue:
        return "High"

    elif "danger" in issue:
        return "High"

    elif "broken" in issue:
        return "Medium"

    elif "urgent" in issue:
        return "Medium"

    return "Low"
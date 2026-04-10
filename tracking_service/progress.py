def track_progress(user, current_weight, previous_weight):
    change = current_weight - previous_weight

    if change < 0:
        status = "Weight Loss 📉"
    elif change > 0:
        status = "Weight Gain 📈"
    else:
        status = "No Change"

    return {
        "previous_weight": previous_weight,
        "current_weight": current_weight,
        "change": change,
        "status": status
    }
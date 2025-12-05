# USDből forintba átváltás
def usd_to_huf(usd_amount, rate):
    if usd_amount * rate < 0:
        return "hibás"
    return usd_amount * rate

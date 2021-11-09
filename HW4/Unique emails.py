
def email_origin(email):
    local,domain=email.split("@")
    if "+" in local:
        local=local[:local.index("+")]
    if "." in local:
        local.replace(".","")
    return"".join([local, "@", domain]) 

def count_unique_emails(emails):
    unique_emails=set()
    for email in emails:
        unique_emails.add(email_origin(email))
    return(len(unique_emails))

emails=["arevik+azaryan@gmail.com", "arevik.azaryan@gmail.com"]
print(count_unique_emails(emails))







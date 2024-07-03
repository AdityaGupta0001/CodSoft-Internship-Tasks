def checkPhoneNumberValidity(phone):
    check=True
    if len(phone)!=10:
        check=False
    else:
        for i in phone:
            if i not in "0123456789":
                check=False
                break
    return check

def checkEmailValidity(email):
    global mailcheck
    mailcheck=False
    validity_ctr=0
    domains=[".com",".co",".in",".co.in",".org",".net",".info"]
    attherate="@"
    email=str(email).lower()
    if attherate in email:
        validity_ctr+=1
    for i in domains:
        if i in email:
            domain_location=i
            validity_ctr+=1
            if email.index(domain_location)==len(email)-len(domain_location):
                validity_ctr+=1
            break
    if validity_ctr==3:
            mailcheck=True
    return mailcheck
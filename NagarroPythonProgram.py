# NagarroPythonProgram

print(" AD User Creation Request \n")
print("Please enter the following info: \n")

dueDate = input("Due: ")
firstName = input("First Name: ")
lastName = input("Last Name: ")
displayName = firstName + " " + lastName
userName = firstName + "." + lastName
print("Display Name: ", displayName)
description = input("Description: ")
office = input("Office: ")
employeeID = input("Employee ID: ")

companyNumber = input("Which Banner? \n 1. New Seasons\n 2. New Leaf\n 3. GFH\n 4. BFLA\n 5. Metropolitan Market\n ") 

if companyNumber == '1':
     company = "New Seasons Market"
     domain = "@newseasonsmarket.com"
elif companyNumber == '2':
    company = "New Leaf"
    domain = "@newleaf.com"
elif companyNumber == '3':
    company = "Good Food Holdings"
    domain = "@goodfoodholdings.com"
elif companyNumber == '4':
    company = "Bristol Farms/Lazy Acres"
    domain = "@BFLA.com"
elif companyNumber == '5':
    company = "Metropolitan Market"
    domain = "@metropolitan-market.com"
else:
    print("Invalid Entry, defaulting to NSM.")
    company = "New Seasons Market"
    domain = "@newseasonsmarket.com"

email = userName + domain
print("Email Address: ", email)
print("Job Title: ", description)
print("Company: ", company)

memberships = ["\tDomain Users", "\tNSMsgKnowB4User", "\tNSNLsgMS365LicenseP1", "\tNSNLsgMS365ExchangOnlinePlan1MBOnly"]

print("Member of: ")

for member in memberships:
    print ("%s" % member)
    
ta = "\t"
escape = " "
while escape != "n":
    addMembership = input("Enter membership to add (n to quit): ")
    if addMembership not in memberships and addMembership.lower() != "n" and "\t"+addMembership not in memberships:
        memberships.append("\t"+addMembership)
    if addMembership.lower() == "n":
        escape = "n"
        
for member in memberships:
    print ("%s" % member)   

destEmail = input("Who should we send the login credentials to: ")

sendToList = ["\nSend Login info to: "+destEmail]

homeFolderDest = R"to \\CLDORFILE01\HOME$\%username%"

text = ["---------AD USER CREATION REQUEST----------",
"\nDue: "+dueDate,
"\nFirst Name: "+firstName,
"\nLast Name: "+lastName,
"\nDisplay Name: "+displayName,
"\nDescription: "+description,
"\nOffice: "+office,
"\nEmail: "+email,
"\nJob Title: "+description,
"\nCompany: "+company,
"\nHome Folder:\n\t Connect H: "+homeFolderDest,
"\nEmployee ID: "+employeeID,
"\nProxyAddresses:\n\t SMTP:"+email,
"\t smtp:NSNL"+userName+"@goodfoodholdings.mail.onmicrosoft.com", 
"\nMember Of: "]

textToOutfile = text + memberships + sendToList
with open('NagarroUserRequest.txt', 'w') as f:
    f.writelines('\n'.join(textToOutfile))
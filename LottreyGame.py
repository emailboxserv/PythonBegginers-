app_nm = "PentLott"
plyr_nm = input("What is your name?: ")
wapp_greetings = (plyr_nm + "! Welcome to " + app_nm + ".")
print("")
print(wapp_greetings)
print("")
print("Are you ready to play your numbers", plyr_nm + "?")
gameprc = input("Please answer Yes or No: ")
print("")
print("Okay then, let get started", plyr_nm + "!")
print("")
print("Please let's have your contact information where we can reach you regarding your stake.")
phnb = input("Phone Number: ")
eml_ad = input("Email Address: ")
print("Do you want", app_nm, "to send you our daily news and promotional updates?")
print("")
print("Please provide your five (5) numbers accordingly, raning from 1 - 99.")
fst_plyrn = int(input("What is your 1st number?: "))
sec_plyrn = int(input("What is your 2nd number?: "))
thd_plyrn = int(input("What is your 3rd number?: "))
fth_plyrn = int(input("What is your 4th number?: "))
fvth_plyrn = int(input("What is your 5th number?: "))
print ("Thank your for proving your numbers", plyr_nm + ".")
print("")
print("Now, please enter the total amount that you want to stake for your gaming numbers below.")
ttl_amnt = str(int(input("$: ")))
print("")
stk_amnt = str(int(ttl_amnt) / 5)
print("For the total amount of $" + ttl_amnt, "staked by you:")
print("Your stake amount for each of the 5 numbers you have played is $" + stk_amnt)
print("Would you like to proceed now", plyr_nm, "or adjust your total stake amount of $" + ttl_amnt + "?")
stkprc = input("Please answer Yes or No: ")
print ("You are almost done", plyr_nm + ".")
print("")
print("To process your stake current stake, please provide your payment information below.")
blstr_ad = input("Billing Street Address: ")
cty = input("City: ")
stte = input("State: ")
zpcd = input("Zip | Postal Code:  ")
cntry = input("Country: ")
crd_nm = input("Card Number: ")
crd_exp = input("Card Expiry Date: ")
crd_cd = input("CVV | CSC | Security Code: ")
print("Your paymet information has just been received but yet to be processed.")
print("")
print("Let's round-up", plyr_nm + ".")
print("Please carefully review your stake before final submission!")
print("")
print("Stake Information:")
print("Player Name:", plyr_nm)
print("1st Staked Number: ", fst_plyrn)
print("2nd Staked Number: ", sec_plyrn)
print("3rd Staked Number: ", thd_plyrn)
print("4th Staked Number: ", fth_plyrn)
print("5th Staked Number: ", fvth_plyrn)
print("")
print("Billing Information:")
print("Billing Street Address: ", blstr_ad)
print("City: ", cty)
print("State: ", stte)
print("Zip | Postal Code:  ", zpcd)
print("Country :  ", cntry)
print("")
print("Payment Information:")
print("Card Number:  ", crd_nm)
print("Card Expiry Date:  ", crd_exp)
print("CVV | CSC | Security Code: ", crd_cd)
print("")
print("Would you like to submit your Stake? Please be sure that you have carefully reviewed your stake as advised above!")
print("By replying ""Yes"", you", plyr_nm, "hereby confirm that you authorize", app_nm, "to place your stake and proceed your payment")
print("Consent: You also confirm that the information provided by you are geneuinely yours and true to the best of your knowledge.")
print("Legal Notice: In order to help us fight againt fraud and money laundering schemed", app_nm, "reserves the right to request additional means of verification if required while processing your payment.")
print("Please be informed that", app_nm, "do not condone any act of fraudulent or money laudering scheme. Therefore, we shall report detected or reported fraudulent or money laundering activited to the legal or crime agencies.")
sub_cnfrm = input("Please, reply ""Yes"" to submit your stake or ""No"" to cancel: ")
print("")
print ("Rounding-Up......")
print("Your stake has been successfully submitted!", plyr_nm + ".")
print("Please check out for your winnings.")
print("We will send you a winning or lose confirmation notice once the result is available.")
gapp_greetings = ("Thank you for staking with " + app_nm + ".")
print(gapp_greetings)
print("")
print("We wish you the best of luck...")
print("Happy Winnings!!!")
print("")
print(app_nm, "Copyright - 2022 | All rights reserved.")

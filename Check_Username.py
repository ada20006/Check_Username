print("How would you like to be called? (your username)")
username_invalid_symbols = [" ", "{", "}", "[", "]", "(", ")","%", "/", "@", ",", ";", ":", ">", "<", "="]
username = input()
username_is_valid = False
while username_is_valid == False:
    if len(username) <= 20 and len(username) >= 1:
        for symbol in username_invalid_symbols:
            if symbol in username:
                print("This username is Invalid. (max. lenght 20 | min. lenght 1 | forbidden symbols: empty, {, }, [, ], (, ), %, /, @, ',', ;, :, >, <, =)")
                username = input()
                username_is_valid = False
                break               
            else:
                username_is_valid = True
    else:
        print("This username is Invalid. (max. lenght 20 | min. lenght 1 | forbidden symbols: empty, {, }, [, ], (, ), %, /, @, ',', ;, :, >, <, =)")
        username = input()
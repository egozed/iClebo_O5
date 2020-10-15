def switch(case_key=None, case:dict={}):
    if case.get("default") == None:
            print(f'Case key: "{case_key}" NOT found! and "default" key NOT exist')
            return
    if case.get(case_key) == None:
            case["default"](case_key)
    else:
        case[case_key]()
"""
NO MORE if - elif - elif - ... - else !!! Just use switch case !!!
"HOW TO USE: "

case_key = 1

switch( case_key,
        case = {
                   0:lambda:(
                        print(" i am 'zero[0]' case"),
                        print(" i am 'zero[1]' case"),
                        print(" i am 'zero[2]' case"),
                        ),
                   1:lambda:(
                        print(" i am '1-th' case"),
                        ),
                   2:lambda:(
                        print(" i am '2-th' case"),
                        ),
                 "q":lambda:(
                        print(" i am 'q' case"),
                        ),
           "default":lambda key:(
                        print(f"Case key: '{key}' not found! i am Default "),
                        )
                }
        )
        
"""
import time
import random


def choose_plr():
    while True :
        all_plr = ["MS.DHONI", "VIRAT KOHLI", "ROHIT SHARMA", "SHAKAR DHAWAN", "RISHAB PANT", "DAVID WARNER"]
        ini = 1
        for ap in all_plr:
            if ini % 5 != 0:
                print(ini, "->", ap, end="                    ")
            else:
                print("\n", ini, "->", ap, end="                    ")
            ini += 1
        print("")
        cho_plr = input("CHOOSE YOUR PLAYERS (MORE THEN 1) AND NOT MORE THEN 12! SEPARATED BY ',' : ").split(",")
        org_plr = []
        for cp in cho_plr:
            if cp not in org_plr:
                org_plr.append(cp)
        if len(org_plr) > 13 :
            print("TRY AGAIN !!")
        elif len(org_plr) == 1:
            print("TRY AGAIN !!")
        else:
            created_plr = []
            for inplr in org_plr:
                created_plr.append(
                    org_team_name + " " + (all_plr[int(inplr) - 1]))  ############## modify ###################
            break
    return created_plr


def create_plr():
    plr_created = []
    numplr = 1
    jrsno = []
    for no in range(1, 12):
        jrsno.append(no)
    countplr = 0
    while True:
        if countplr < 13:
            print(countplr + 1, end=" ")
            pl = str(input("PLAYER NAME : "))
            yourjrs = random.choice(jrsno)
            time.sleep(1)
            print("CONGRATULATION! ", pl, " GOT JERSEY ", yourjrs)
            if GT == "2":
                plr_created.append(tn2+" "+ pl)  ######################  modify  ##################
            if GT == "1":
                plr_created.append(pl)
            jrsno.remove(yourjrs)
            print(" ")
            countplr += 1
            if countplr != 1:
                morplr = input("MORE PLAYERS(YES/NO): ").upper()
                print(" ")
                time.sleep(1)
                if morplr == "NO":
                    print("OKAY,THANKYOU")
                    time.sleep(1)
                    print("REGISTER IS COMPLETED ")
                    break
    return plr_created


def create_team():
    success = False
    global tn2
    global org_team_name
    global org_password
    global created_player
    global creating_process
    while True:
        ask_user = input("1. TEAM CREATED  2. EXIT : ")
        if ask_user == "1":
            tn2 = input("TEAM NAME :").strip()
            org_team_name += tn2
            if tn2 not in all_team:
                opt = input("1. CREATE PLAYER 2. CHOOSE PLAYER : ")
                if opt == "1":
                    created_player = create_plr()
                if opt == "2":
                    created_player = choose_plr()
                y_pass = input("SET YOUR PASSWORD : ").strip()
                org_password += y_pass
                ################################################# MODIFY #####################
                success = True
                break
        if ask_user == "2":
            creating_process = False
            break

    return success


def already_team():
    success2 = True
    global tn2
    global org_password
    global org_team_name
    global created_player
    global creating_process
    while True:
        ask_team = input("1. TEAM NAME  2. EXIT : ")
        if ask_team == "1":
            tn2 = input("ENTER YOUR TEAM NAME : ").strip()
            if tn2 in all_team:
                ########################################################################
                team_players = ["dhoni ", "kholi", "david"]
                password_ck = False
                while True:
                    pass2 = input("ENTER YOUR PASSWORD : ")
                    if pass2 in all_passwords:
                        org_password += pass2
                        org_team_name += tn2
                        password_ck = True
                        ###################################### MODIFY ####################
                        break
                    else:
                        passwd = True
                        print("WRONG PASSWORD !!! ")
                        y_ask = input("1. TRY AGAIN  2.FORGET PASSWORD  3.EXIT :  ")
                        if y_ask == "2":
                            ask_user2 = (input(
                                "ENTER YOUR {} PLAYER NAME SEPERATED BY ',' : ".format((len(team_players) - 1)))).split(
                                ",")
                            for i in ask_user2:
                                if i in team_players:
                                    print(i, "OKAY !")
                                else:
                                    print(i, "IS NOT YOUR PLAYER ! ")
                                    passwd = False
                                    break
                            if passwd == False:
                                break
                            if passwd == True:
                                new_pass = input("SET YOUR NEW PASSWORD : ").strip()
                                org_team_name += tn2
                                org_password += new_pass
                                password_ck = True
                                break
                                ########################  MODIFY  #####################
                        if y_ask == "3":
                            break
                if password_ck == True:
                    print("ENTERING YOUR ACCOUNT SOON ... ")
                    break

        if ask_team == "2":
            success2 = False
            creating_process = False
            break

    created_player = ["GOURAV"," LUFFY "] #################  EXTRACT FROM TEAM ACCOUNT  ########
    return success2



############################################################################################################################


def game():
    global plr
    global GT
    plr = []
    if GT == "2":
        plr = created_player
    if GT == "1":
        plr = create_plr()
    if GT == "2":
        print("WELCOME TO G-CRICKET")
        # GAME RULES : HOW TO PLAY
        time.sleep(1)
        print(" ")
        print("THIS IS A CRICKET GAME ")
        print("HOW TO PLAY :")
        rule = '''1 : YOU HAVE TO LOG IN / CREATE A TEAM  
        2 : FIRST TWO PLAYERS ARE OPENER AND RUNNER RESPECTIVELY
        3 : PLAYERS MUST BE MORE THAN 1
        4 : TEAM HAVE TO SET A TARGET   
        5 : READ ALL INSTRUCTION CAREFULLY
        6 : FILL IN WHAT IT ASKS ! 
        '''
        print(rule)
        time.sleep(8)

    print("WELLCOME")
    print(" ")
    ovr = int(input("HOW MANY OVER WANT TO PLAY : "))
    time.sleep(1)
    print(" ")
    # GAME STRUCTURE
    if GT == "2":
        targ = int(input("{} TARGET : ".format(org_team_name)))
    else:
        targ = int(input("TARGET :"))
    time.sleep(1)
    if GT == "2":
        targ2 = 1
        if ovr * 8 < targ <= ovr * 18 - 1:
            print("GOOD TARGET ")
        elif targ < ovr * 8:
            print("EASY TARGET")
        elif ovr * 18 <= targ < ovr * 36:
            print("EXCELLENT TARGET")
        else:
            print("IMPOSSIBLE TARGET")
            targ2 += random.randrange(ovr * 8, ovr * 18)
            targ, targ2 = targ2, targ
            print("YOUR NEW TARGET : ", targ)
        print(" ")
    print("GAME STARED WITHIN 5 SEC  ")
    for tim in range(5, 0, -1):
        time.sleep(1)
        print(tim, " " * 5, end="")
    print(" ")
    print("GAME!")
    ballno = 6 * ovr
    print(ovr, "OVER : ", ballno, "BALLS")
    plr2 = plr.copy()
    print(" ")
    time.sleep(2)
    opnplr = str(plr[0])
    print("OPENER IS ", opnplr)
    plr2.pop(0)
    runplr = str(plr[1])
    plr2.pop(0)
    time.sleep(1)
    print("RUNNER IS ", runplr)
    time.sleep(2)
    print(" ")
    if GT == "2":
        print("SCOREBOARD")
        leaderboardst = {}
        leaderboardst1 = leaderboardst.fromkeys(tuple(plr), "0")
        for player in leaderboardst1:
            print(player, "RUN :", leaderboardst1[str(player)])
        print(" ")
    time.sleep(5)
    rruunn = ("1", "2", "3", "4", "6")
    sumrun = 0
    hit = ["+", "-"]
    numout = 0
    stplr = [runplr, opnplr]
    plr2.append("BOT")
    leaderboardst2 = {}
    playrscore = leaderboardst2.fromkeys(tuple(plr), 0)
    drs = 2
    for overs in range(ovr):
        if len(plr) != (numout + 1):
            for balll in range(1, 7):
                if len(plr) != (numout + 1):
                    if sumrun < targ + 1:
                        hitball = random.randint(1, 100)
                        hitball2 = random.randint(1, 100)
                        hit1 = random.choice(hit)
                        wicketout = ["HIT THE BALL TWICE", "HIT WICKET", "RUN OUT", "STUMPED", "LBW(LEG BEFORE WICKET)",
                                     "BOWLED", "CAUGHT OUT"]
                        out = random.choice(wicketout)
                        drsresult = random.choice(["YES", "NO"])
                        if hit1 == "+":
                            ans = hitball + hitball2
                        else:
                            ans = hitball - hitball2
                        print("ANSWER ", hitball, hit1, hitball2, " FOR HIT THE BALL!")
                        time.sleep(1)
                        print(balll, "BALL")
                        hhit = int(input("HIT THE BALL : "))
                        runcount = random.choice(rruunn)
                        if hhit == ans:
                            sumrun += int(runcount)
                            if runcount == "6":
                                print("6 RUN   AWESOME!!")
                            else:
                                print(runcount, "RUN")
                            if balll > 3:
                                if sumrun < targ:
                                    print(ovr - (overs + 1), "OVER", 6 - balll, "BALLS LEFT", "- ", (targ - sumrun) + 1,
                                          "RUNS NEEDED")
                            else:
                                print("")

                            for score in playrscore:
                                if score == opnplr:
                                    playrscore[score] = playrscore[score] + int(runcount)

                        else:
                            if str(out) == "STUMPED" or str(out) == "LBW(LEG BEFORE WICKET)":
                                if drs != 0:
                                    print("PLAYER", stplr[1], "MAY BE OUT ")
                                    askdrs = input("WANT DRS (DECISION REVIEW SYSTEM) ? : ").upper()
                                    if askdrs == "YES":
                                        drs -= 1
                                        time.sleep(3)
                                        if str(drsresult) == "NO":
                                            numout += 1
                                            print(opnplr, "OUT! BY ", out)
                                            if len(plr2) != 1:
                                                opnplr = plr2.pop(0)
                                            else:
                                                print("ALL OUT ")
                                                break
                                        else:
                                            print(stplr[1], "NOT OUT")

                                    else:
                                        numout += 1
                                        print(opnplr, "OUT! BY ", out)
                                        if len(plr2) != 1:
                                            opnplr = plr2.pop(0)
                                        else:
                                            print(" ")
                                            break
                                else:
                                    break
                            else:
                                numout += 1
                                print(opnplr, "OUT! BY ", out)
                                if len(plr2) != 1:
                                    opnplr = plr2.pop(0)
                                else:
                                    print("ALL OUT ")
                                    break
                    else:
                        print("CONGRATULATION YOUR TEAM WIN THE GAME !!")
                        break
                else:
                    break
                print(" ")
            print(" ")
            print(" ")
            opnplr, runplr = runplr, opnplr
        else:
            print("ALL OUT ")
            break
    print(" ")
    print(" ")
    time.sleep(1)
    print("PROCESSING ......")
    time.sleep(5)
    time.sleep(1)
    if GT == "2":
        print(org_team_name," RUN : ", sumrun, " RUN", )
    else:
        print("TOTAL RUN : ", sumrun, " RUN", )

    if numout == 0:
        print("NO WICKET")
    else:
        print("WICKET : ", numout, "OUT")
    if sumrun > targ:
        if GT == "2":
            print("CONGRATULATION ! ", org_team_name, " WIN THE GAME ")
        else:
            print("CONGRATULATION !  WIN THE GAME ")

    elif sumrun == targ:
        print("DRAW MATCH")
    else:
        if GT == "2":
            print(org_team_name, " LOSE THE GAME! TRY NEXT TIME ")
        else:

            print(" LOSE THE GAME! TRY NEXT TIME ")

    print(" ")
    if GT == "2":
        print("SCOREBOARD ")
        time.sleep(4)

        for sc in playrscore:
            print(sc, "RUN : ", playrscore[sc])
        print(" ")
        time.sleep(1)
    print("GAME IS OVER!")



#############################################################################################





while True:
    design1 = '''
                __________________________________________________
                |                                                |
                |                                                |
                |       1. DEMO GAME                             |
                |                                                |
                |       2. GAME                                  |
                |                                                |
                |       3. EXIT                                  |
                |                                                | 
                |________________________________________________|



    '''
    print(design1)
    GT = input("ENTER : ")
    if GT == "3":
        break
    if GT == "1":

        game()
    if GT == "2":
        org_team_name = ""
        org_password = ""
        all_team = ["SAMURAI OF TSUSHIMA ", "WORRIERS OF LAND"]
        all_passwords = ["9851221389", "123456789name", "987654321name"]###################  NO NEED AFTER SQL
        creating_process = True
        while True:
            ask_user2 = input("1. CREATE TEAM  2.ALREADY TEAM 3. EXIT : ")
            if ask_user2 == "1":
                sus = create_team()
                if sus == True:
                    print("SUCCESSFUL")
                    creating_process = True
                    break
                if sus == False:
                    print(" ")
            if ask_user2 == "2":
                sus2 = already_team()
                if sus2 == True:
                    print("SUCCESSFULLY")
                    break
                if sus2 == False:
                    print("  ")
            if ask_user2 == "3":
                creating_process = False
                break
        if creating_process == True:
            design = '''
                                __________________________________________________
                                |                                                |
                                |       1. START GAME 🏏🏏🏏                     |
                                |                                                |
                                |       2. TEAM HISTORY  📜📜📜                  |
                                |                                                |
                                |       3. LEADERBOARD   🗃️🗃️🗃️                  |
                                |                                                 |
                                |       4. EXIT          👋👋👋                  |
                                |                                                |   
                                |________________________________________________|



                    '''
            while True:
                print(design)
                body_game = input("ENTER : ")
                if body_game == "1":
                    game()
                if body_game == "2":
                    print(" ")  ############################ MODIFY #############################
                if body_game == "3":
                    print(" ")  ############################ MODIFY #############################
                if body_game == "4":
                    break








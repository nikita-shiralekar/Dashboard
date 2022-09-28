
from traceback import print_tb
from flask import request, render_template,jsonify
from Models import *


from sqlalchemy import join
from sqlalchemy.sql import select



@app.route("/register", methods =["POST","GET"])
def user_resgistration():
    req_data = request.get_json()
    print("req_data",req_data)
    register = User(   
                    user_id = req_data["user_id"],
                    username = req_data["username"],
                    password = req_data["password"]
    
    )
    print(register)


    db.session.add(register)
    db.session.commit()

    return json.dumps({"msg":"successfully created!!"})


@app.route("/Invest_strategy", methods=["POST", "GET"])
def invest_strat():
    req_data= request.get_json()
    strategy = Investment_Strategy(
                                  
                                  investment_strat = req_data["investment_strat"]

    )
    db.session.add(strategy)
    db.session.commit()

    return json.dumps({"msg":"Investment strategy"})

@app.route("/fund_manager", methods=["POST", "GET"])
def fund_manage():
    req_data= request.get_json()
    fund = Fund_Manager(
                            fund_id = req_data["fund_id"],
                            fund_man = req_data["fund_man"]

    )
    db.session.add(fund)
    db.session.commit()

    return json.dumps({"msg":"Fund-manager-type is added successfuly...."})


@app.route("/standing_instructions", methods=["POST", "GET"])
def Standing_Instructions_ACTYPE():
    req_data= request.get_json()
    standing_ins = Standing_Instructions_Action_Type(
                            standing_id = req_data["standing_id"],
                            standing_inst_act_type = req_data["standing_inst_act_type"]

    )
    db.session.add(standing_ins)
    db.session.commit()

    return json.dumps({"msg":"Standing-instruction is added successfuly...."})

@app.route("/reciepient_invest_stat", methods=["POST", "GET"])
def Recipient_Investment_strat():
    req_data= request.get_json()
    # fetching data from request/postman

    Recipent_code = req_data["Recipent_code"],
    Notification_Type_ANN = req_data["Notification_Type_ANN"],
    Notification_Type_IRR = req_data["Notification_Type_IRR"],
    Notification_Create= req_data["Notification_Create"],
    First_Name = req_data["First_Name"],
    Last_Name = req_data["Last_Name"],
    Role_Name = req_data["Role_Name"],
    Email_Address = req_data["Email_Address"],

    # this data belongs to differnt table - so we need to save in that table
    investment_strategy = req_data["investment_strategy"]


    inv=Investment_Strategy(investment_strat=investment_strategy) 
    db.session.add(inv)
    db.session.commit()
    invstr=Investment_Strategy.query.filter_by(investment_strat=investment_strategy).first()
    print(invstr.invest_id)

    recipient = Recipient_Investment_strategy(
                           
                            Recipent_code = Recipent_code,
                            Notification_Type_ANN = Notification_Type_ANN,
                            Notification_Type_IRR = Notification_Type_IRR,
                            Notification_Create= Notification_Create,
                            First_Name = First_Name,
                            Last_Name = Last_Name,
                            Role_Name = Role_Name,
                            Email_Address = Email_Address,
                            investment_strategy = invstr.invest_id



    )
    db.session.add(recipient)
    db.session.commit()

    return json.dumps({"msg":"Recipient_Investment_strat is added successfuly...."})


@app.route("/get_all_inv_strategy", methods=["POST", "GET"])
def get_all_recipient_investment_strategy():
    userList = Investment_Strategy.query.join(Recipient_Investment_strategy, Investment_Strategy.invest_id==Recipient_Investment_strategy.investment_strategy).add_columns(Investment_Strategy.investment_strat, Recipient_Investment_strategy.Recipent_code,Recipient_Investment_strategy.Notification_Type_ANN, Recipient_Investment_strategy.Notification_Type_IRR,Recipient_Investment_strategy.Notification_Create,
      Recipient_Investment_strategy.First_Name,Recipient_Investment_strategy.Last_Name,Recipient_Investment_strategy.Role_Name,Recipient_Investment_strategy.Email_Address).all()
    print(userList)
    data = json.dumps({"msg":userList}, default=str)

    return data


@app.route("/reciepient_invest_stat_acc", methods=["POST", "GET"])
def Recipient_Investment_strat_acc():
    req_data= request.get_json()

    #id = req_data["id"],
    #investment_strategy = req_data["investment_strategy"],
    Account = req_data["Account"],
    Business_Entity = req_data["Business_Entity"],
    funds=req_data["funds"]
    fun=Fund_Manager(fund_man=funds)
    db.session.add(fun)
    db.session.commit()
    fmid = Fund_Manager.query.filter_by(fund_man = funds).first()
    print(fmid.fund_id)

    investment_strategy = req_data["investment_strategy"]


    inv=Investment_Strategy(investment_strat=investment_strategy) 
    db.session.add(inv)
    db.session.commit()
    invstr=Investment_Strategy.query.filter_by(investment_strat=investment_strategy).first()
    print(invstr.invest_id)


                        
    rec_acc = Recipient_Investment_Strategy_Account(
                            investment_strategy = invstr.invest_id,
                            Account =Account,
                            Business_Entity = Business_Entity,
                            funds = fmid.fund_id
                            



    )
    db.session.add(rec_acc)
    db.session.commit()

    return json.dumps({"msg":"Recipient_Investment_strat_account is created successfuly...."})

@app.route("/standing_instructions", methods=["POST", "GET"])
def Standing_instruction():
    req_data= request.get_json()
    stand_ins = Standing_Instructions(
                            id = req_data["id"],
                            Account = req_data["Account"],
                            Business_Entity = req_data["Business_Entity"],
                            Corp_Action_Type = req_data["Corp_Action_Type"],
                            Country_Code = req_data["Country_Code"],
                            Currency_Code = req_data["Currency_Code"]



    )
    db.session.add(stand_ins)
    db.session.commit()

    return json.dumps({"msg":"Standing instructions is created successfuly...."})




if __name__ =="__main__":
    app.run(debug=True)




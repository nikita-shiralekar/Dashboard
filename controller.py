
from traceback import print_tb
from flask import request, render_template,jsonify
from Models import *


from sqlalchemy import join
from sqlalchemy.sql import select



@app.route("/register", methods =["POST","GET"])   # add
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


@app.route("/update_username/<int:user_id>", methods=["PUT"])
def update_name(user_id):
    req_data = request.get_json()
    print("req_data",req_data)

    if req_data:
        usnm=User.query.filter_by(user_id = user_id).first()

        if usnm:
            usnm.username = req_data.get("username")
            usnm.password = req_data.get("password")
            db.session.commit()
            un ={
                "username" : usnm.username,
                "password" : usnm.password
                
            }
            return json.dumps(un)
        else:
            return json.dumps({"ERROR":"NO PRODUCT WITH GIVEN ID...."})
    else:
        return json.dumps({"ERROR":"INVALID DATA....!"})


# @app.route("/product/api/v1/<int:pid>", methods = ["PUT"])
# def update_product(pid):
#     req_data = request.get_json()
#     if req_data:
#         dbproduct = Product.query.filter_by(id = pid).first()
#         if dbproduct:
#             dbproduct.name = req_data.get("name")
#             dbproduct.price = req_data.get("price")
#             dbproduct.qty = req_data.get("qty")
#             dbproduct.vendor = req_data.get("vendor")
#             db.session.commit()
#             product = {"PRODUCT_ID": dbproduct.id,
#                        "PRODUCT_NAME": dbproduct.name,
#                        "PRODUCT_QUANTITY": dbproduct.qty,
#                        "PRODUCT_PRICE": dbproduct.price,
#                        "PRODUCT_VENDOR ": dbproduct.vendor}

#             return json.dumps(product)
#         else:
#             return json.dumps({"ERROR":"NO PRODUCT WITH GIVEN ID...."})
#     else:
#         return json.dumps({"ERROR":"INVALID DATA....!"})


@app.route("/Invest_strategy", methods=["POST", "GET"])
def invest_strat():
    req_data= request.get_json()
    strategy = Investment_Strategy(
                                  
                                  investment_strat = req_data["investment_strat"]

    )
    db.session.add(strategy)
    db.session.commit()

    return json.dumps({"msg":"Investment strategy"})


@app.route("/update_invest_strat/<int:invest_id>", methods=["PUT"])
def update_invest_strat(invest_id):
    req_data = request.get_json()
    print("req_data",req_data)

    if req_data:
        invest_st = Investment_Strategy.query.filter_by(invest_id = invest_id).first()

        if invest_st:
            invest_st.investment_strat = req_data.get("investment_strat")
            
            db.session.commit()
            ist ={
                "investment_strat" : invest_st.investment_strat
               
                
            }
            return json.dumps(ist)
        else:
            return json.dumps({"ERROR":"NO PRODUCT WITH GIVEN ID...."})
    else:
        return json.dumps({"ERROR":"INVALID DATA....!"})



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

@app.route("/update_fund_manager/<int:fund_id>", methods=["PUT"])
def update_fund(fund_id):
    req_data = request.get_json()
    print("req_data",req_data)

    if req_data:
        f_m = Fund_Manager.query.filter_by(fund_id = fund_id).first()

        if f_m:
            f_m.fund_man = req_data.get("fund_man")
            
            db.session.commit()
            f_mn ={
                "fund_man" : f_m.fund_man
               
                
            }
            return json.dumps(f_mn)
        else:
            return json.dumps({"ERROR":"NO PRODUCT WITH GIVEN ID...."})
    else:
        return json.dumps({"ERROR":"INVALID DATA....!"})




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


@app.route("/update_standing_inst_act/<int:standing_id>", methods=["PUT"])
def update_std_ins(standing_id):
    req_data = request.get_json()
    print("req_data",req_data)

    if req_data:
        stand_id = Standing_Instructions_Action_Type.query.filter_by(standing_id = standing_id).first()

        if stand_id:
            stand_id.standing_inst_act_type = req_data.get("standing_inst_act_type")
            
            db.session.commit()
            st_in ={
                "standing_inst_act_type" : stand_id.standing_inst_act_type
               
                
            }
            return json.dumps(st_in)
        else:
            return json.dumps({"ERROR":"NO PRODUCT WITH GIVEN ID...."})
    else:
        return json.dumps({"ERROR":"INVALID DATA....!"})



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


@app.route("/get_all_inv_strategy", methods=["POST", "GET"])  #get
def get_all_recipient_investment_strategy():
    userList = Investment_Strategy.query.join(Recipient_Investment_strategy, Investment_Strategy.invest_id==Recipient_Investment_strategy.investment_strategy).add_columns(Investment_Strategy.investment_strat, Recipient_Investment_strategy.Recipent_code,Recipient_Investment_strategy.Notification_Type_ANN, Recipient_Investment_strategy.Notification_Type_IRR,Recipient_Investment_strategy.Notification_Create,
      Recipient_Investment_strategy.First_Name,Recipient_Investment_strategy.Last_Name,Recipient_Investment_strategy.Role_Name,Recipient_Investment_strategy.Email_Address).all()
    print(userList)
    data = json.dumps({"msg":userList}, default=str)

    return data

@app.route("/update_reciepient_inv/<int:Recp_Inv_id>", methods=["PUT"])  #update
def update_recipent_inv(Recp_Inv_id):
    req_data = request.get_json()
    print("req_data",req_data)

    if req_data:
        recipient = Recipient_Investment_strategy.query.filter_by(Recp_Inv_id = Recp_Inv_id).first()

        if recipient:
            recipient.Recipent_code = req_data.get("Recipent_code")
            recipient.Notification_Type_ANN = req_data.get("Notification_Type_ANN")
            recipient.Notification_Type_IRR = req_data.get("Notification_Type_IRR")
            recipient.Notification_Create = req_data.get("Notification_Create")
            recipient.First_Name = req_data.get("First_Name")
            recipient.Last_Name = req_data.get("Last_Name")
            recipient.Role_Name = req_data.get("Role_Name")
            recipient.Email_Address = req_data.get("Email_Address")
            recipient.investment_strategy = req_data.get("investment_strategy")
            
            db.session.commit()
            st_in ={
                "Recipent_code" : recipient.Recipent_code,
                "Notification_Type_ANN":recipient.Notification_Type_ANN,
                "Notification_Type_IRR":recipient.Notification_Type_IRR,
                "Notification_Create":recipient.Notification_Create,
                "First_Name":recipient.First_Name,
                "Last_Name":recipient.Last_Name,
                "Role_Name":recipient.Role_Name,
                "Email_Address":recipient.Email_Address,
                "investment_strategy":recipient.investment_strategy


               
                
            }
            return json.dumps(st_in)
        else:
            return json.dumps({"ERROR":"NO PRODUCT WITH GIVEN ID...."})
    else:
        return json.dumps({"ERROR":"INVALID DATA....!"})



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
    invstr=Investment_Strategy.query.filter_by(investment_strat  = investment_strategy).first()
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


@app.route("/get_all_reci_account_table", methods=["POST", "GET"]) #get
def get_all_recipient_account():
    data = db.session.query( Recipient_Investment_Strategy_Account.Account,Recipient_Investment_Strategy_Account.Business_Entity,Investment_Strategy.investment_strat, Fund_Manager.fund_man,
        ).join(Recipient_Investment_Strategy_Account,Recipient_Investment_Strategy_Account.investment_strategy==Investment_Strategy.invest_id
        ).join(Recipient_Investment_Strategy_Account, Recipient_Investment_Strategy_Account.funds==Fund_Manager.fund_id
        ).all()
    # q = db.Session.query(Investment_Strategy, Fund_Manager, Recipient_Investment_Strategy_Account).select_from(Recipient_Investment_Strategy_Account).join(Recipient_Investment_Strategy_Account,
    #     Recipient_Investment_Strategy_Account.investment_strategy==Investment_Strategy.invest_id
    #     ).join(Recipient_Investment_Strategy_Account, Recipient_Investment_Strategy_Account.investment_strategy==Fund_Manager.fund_id
    #     ).all()

    # acc_table = Investment_Strategy.query.join(Recipient_Investment_Strategy_Account, 
    #       Fund_Manager.fund_id==Recipient_Investment_strategy.investment_strategy).join(
    #        Recipient_Investment_Strategy_Account,
    #       Investment_Strategy.invest_id==Recipient_Investment_Strategy_Account.funds).add_columns(
    #       Investment_Strategy.investment_strat, Fund_Manager.fund_man,Recipient_Investment_Strategy_Account.Account,
    #       Recipient_Investment_Strategy_Account.Business_Entity
    #           ).all()
        #     SELECT Student.Name, Branch.Br_id, Branch.HOD,
        # Address.city, Address.pincode from Branch 
        # INNER JOIN Student
        # on Student.Br_id = Branch.Br_id
        # INNER JOIN Address
        # on Student.city_id = Address.city_id;

#     select Student.Name,
# Branch.Br_id,Branch.HOD,
# Address.city,Address.pincode
# from Branch,Student,Address
# where Student.Br_id = Branch.Br_id 
# and Student.City_id = Address.City_id;

# Recipient_Investment_Strategy_Account.Account,
    # Recipient_Investment_Strategy_Account.Business_Entity,
    # Investment_Strategy.investment_strat, Fund_Manager.fund_man
    
    # select *
    # from recipeint_investment_strategy_account,Investment_Strategy,Fund_Manager
    # where recipeint_investment_strategy_account.investment_strategy=Investment_Strategy.invest_id and 
    # recipeint_investment_strategy_account.funds=Fund_Manager.fund_id
        


    return data

# @app.route("/get_all_reci_account", methods=["POST", "GET"])
# def get_all_recipient_account():
#     a = db.session.query(User, UserGroups, Areas
#         ).join(UserGroup,User.usergroup==UserGroup.group_id
#         ).join(Areas, User.area==Areas.area_id
#         ).first()
#     three_joins = session.query()
# session.query(User, Document, DocumentsPermissions).join(Document).join(DocumentsPermissions)


@app.route("/update_reciepient_inv_st_acc/<int:id>", methods=["PUT"])  #update
def update_recipent_inv_stacc(id):
    req_data = request.get_json()
    print("req_data",req_data)



    if req_data:

        Account=req_data.get("Account")
        Business_Entity=req_data.get("Business_Entity")
        investment_strategy=req_data.get("investment_strategy")
        funds= req_data.get("funds")

        invstr=Investment_Strategy.query.filter_by(investment_strat  = investment_strategy).first()
        print(invstr,invstr.invest_id)

        fun=Fund_Manager.query.filter_by(fund_man  = funds).first()
        print(fun,fun.fund_id)


        recipient_acc = Recipient_Investment_Strategy_Account.query.filter_by(id = id).first()

        if recipient_acc:
            
            recipient_acc.Account = req_data.get("Account")
            recipient_acc.Business_Entity = req_data.get("Business_Entity")
            recipient_acc.investment_strategy =invstr.invest_id
            recipient_acc.funds =fun.fund_id

            
            db.session.commit()

            r_acc ={

                "Account":recipient_acc.Account,
                "investment_strategy":recipient_acc.investment_strategy,
                "Business_Entity":recipient_acc.Business_Entity,
                "funds": recipient_acc.Business_Entity
                
             }
            return json.dumps(r_acc)

        else:
             return json.dumps({"ERROR":"NO PRODUCT WITH GIVEN ID...."})
    else:
         return json.dumps({"ERROR":"INVALID DATA....!"})



@app.route("/standing_instructions_form", methods=["POST", "GET"])  #add
def Standing_instruction():
    req_data= request.get_json()

    
    Account = req_data["Account"],
    Business_Entity = req_data["Business_Entity"],
    Corp_Action_Type = req_data["Corp_Action_Type"],
    Country_Code = req_data["Country_Code"],
    #standing_instructions_action =req_data["standing_instructions_action"],
    Currency_Code = req_data["Currency_Code"]

    standing_instructions_action = req_data["standing_instructions_action"]

    SIA = Standing_Instructions_Action_Type(standing_inst_act_type = standing_instructions_action)
    db.session.add(SIA)
    db.session.commit()

    st_ac_ty= Standing_Instructions_Action_Type.query.filter_by(standing_inst_act_type = standing_instructions_action).first()
    print(st_ac_ty.standing_id)

    stand_ins = Standing_Instructions(
                            
                            Account = Account,
                            Business_Entity = Business_Entity,
                            Corp_Action_Type = Corp_Action_Type,
                            Country_Code = Country_Code,
                            standing_instructions_action = st_ac_ty.standing_id,
                            Currency_Code = Currency_Code



    )
    db.session.add(stand_ins)
    db.session.commit()

    return json.dumps({"msg":"Standing instructions is created successfuly...."})


@app.route("/update_standing_inst/<int:id>", methods=["PUT"])
def update_std(id):
    req_data = request.get_json()
    print("req_data",req_data)

    if req_data:
        stand = Standing_Instructions.query.filter_by(id = id).first()

        if stand:
            stand.Account = req_data.get("Account")
            stand.Business_Entity = req_data.get("Business_Entity")
            stand.Corp_Action_Type = req_data.get("Corp_Action_Type")
            stand.Country_Code = req_data.get("Country_Code")
            stand.Currency_Code = req_data.get("Currency_Code")
            
            db.session.commit()
            st_instuctions ={
                "Account" : stand.Account,
                "Business_Entity":stand.Business_Entity,
                "Corp_Action_Type":stand.Corp_Action_Type,
                "Country_Code":stand.Country_Code,
                "Currency_Code":stand.Currency_Code
               
                
            }
            return json.dumps(st_instuctions)
        else:
            return json.dumps({"ERROR":"NO PRODUCT WITH GIVEN ID...."})
    else:
        return json.dumps({"ERROR":"INVALID DATA....!"})




if __name__ =="__main__":
    app.run(debug=True)




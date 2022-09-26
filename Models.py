from flask import Flask, config, redirect , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import request
import json


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Principal$2022@localhost/CA_Dashboard'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

db = SQLAlchemy(app)

class User(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(40),nullable = False)
    password = db.Column(db.String(40),nullable = False)

class Investment_Strategy(db.Model):
    __tablename__ = 'investment_strategy'
    invest_id = db.Column(db.Integer,primary_key=True)
    investment_strat = db.Column(db.String(40))
    Recipi_Inv_Strat = db.relationship("Recipeint_Investment_strategy",back_populates = "investment_strategy", uselist = False,lazy=True) #Recipeint_Investment_strategy model
    fund_mang = db.relationship("fund_manager",back_populates = "investment_strategy", uselist = False,lazy=True)
    


class Recipient_Investment_strategy(db.Model):
    __tablename__ = 'recipient_investment_strategy'
    Recp_Inv_id = db.Column(db.Integer,primary_key=True)
    Recipent_code =db.Column(db.String(40), unique =True )
    Notification_Type_ANN = db.Column(db.String(40))
    Notification_Type_IRR = db.Column(db.String(40))
    Notification_Create = db.Column(db.String(40))
    First_Name = db.Column(db.String(40),nullable = False)
    Last_Name = db.Column(db.String(40),nullable = False)
    Role_Name = db.Column(db.String(40))
    Email_Address = db.Column(db.String(40))
    investment_strategy = db.Column(db.Integer, db.ForeignKey("investment_strategy.invest_id"),unique=True, nullable=True)
    

class Fund_Manager(db.Model):
    __tablename__="fund_manager"
    fund_id = db.Column(db.Integer,primary_key=True)
    fund_man = db.Column(db.String(40))
    fund_recipient = db.relationship("Recipient_Investment_Strategy_Account",back_populates = "fund_manager", uselist = False,lazy=True) #Recipeint_Investment_strategy model


class Recipient_Investment_Strategy_Account(db.Model):
    __tablename__="recipeint_investment_strategy_account"
    id = db.Column(db.Integer,primary_key=True)
    investment_strategy = db.Column(db.Integer, db.ForeignKey("investment_strategy.invest_id"),unique = True, nullable=True)
    Account = db.Column(db.String(40), unique = False)
    Business_Entity = db.Column(db.String(40))
    funds = db.Column(db.Integer,db.ForeignKey("fund_manager.fund_id"),unique=True, nullable=True)


class Standing_Instructions_Action_Type(db.Model):
    __tablename__="standing_instruction_act"
    standing_id = db.Column(db.Integer,primary_key=True)
    standing_inst_act_type = db.Column(db.String(40))
    standing_recp = db.relationship("Standing_Instructions",back_populates = "standing_instruction_act", uselist = False,lazy=True) #Recipeint_Investment_strategy model



class Standing_Instructions(db.Model):
    __tablename__ = "standing_instructions"
    id = db.Column(db.Integer,primary_key=True)
    Account = db.Column(db.String(40))
    Business_Entity = db.Column(db.String(40))
    Corp_Action_Type = db.Column(db.String(40))
    Country_Code = db.Column(db.String(40))
    standing_instructions_action_type = db.Column(db.Integer,db.ForeignKey("standing_instruction_act.standing_id"),unique=True, nullable=True)
    Currency_Code = db.Column(db.String(40))

db.create_all()






    
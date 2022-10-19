from flask import Flask, request, jsonify
from checkoutbot.entities import RegisterType
import random 


redge: RegisterType = {x:[1] for x in range(25)}  # Dict[int, List[int]] , 25 registers

app = Flask(__name__)

@app.route("/health")
def health_check():
    return "Hello, World!", 200


@app.route("/state", methods=["DELETE"])
def state():


    if request.method == "DELETE":
        # delete the state lol haha 
        print("delete something")
        redge: RegisterType = {x:[1] for x in range(25)}
        return "Success", 201

@app.route("/add", methods=["POST"])
def add():


    if request.method == "POST":
        print("add an item")
        cust = int(request.form.get('customer_id')) # i guess
        new_cust = True # this is where you place the customer's item. 
        place_at = 0; 
        # can you just move all of a customer's items? If so then that'd be cool. Maybe try both?
        for regi, regItems in redge.items(): # just repeat the cust id for each item at a customer. 
            if cust in regItems:
                place_at = regi
                new_cust = False
                break
        
        if not new_cust:
            redge[place_at].append(cust)
        if new_cust: # optimize here by selecting the emptiest redgester/ 
            redge[random.randint(0,24)].append(cust)
            

        # TODO
        # select the emptiest register with min and a loop and maybe other cool things



        data = {
            "registers" : redge,
            "Subject" : "Data Structures and Algorithms",
        }
  
        return jsonify(data), 201

@app.route("/checkout", methods=["POST"])
def checkout():


    if request.method == "POST": 
        print("checkout")
  
        return jsonify(redge), 201
        

def update_state():


    return

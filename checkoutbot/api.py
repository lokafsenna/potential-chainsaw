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
        print(len(redge[0]))
        for i in range(25):
            redge[i] = [1]
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
            # redge[random.randint(0,24)].append(cust)
            redge[emptiest_register()].append(cust)
            

        # TODO
        # select the emptiest register with min and a loop and maybe other cool things
        


        data = {
            "registers" : redge,
        }
  
        return jsonify(data), 201

@app.route("/checkout", methods=["POST"])
def checkout():


    if request.method == "POST": 
        cust = int(request.form.get('customer_id'))
        print("checkout")
        for regi, regItems in redge.items():  
            if cust in regItems:
                # regItems.count(cust)
                redge[regi] = list(filter(lambda x : x != cust, regItems))
                break   
        
        data = {
            "registers" : redge,
        }
  
        return jsonify(data), 201

def emptiest_register():
    
    emptiest_index = 0
    num_items = len(redge[0])

    for regi, regItems in redge.items():
        if len(regItems) < num_items:
            emptiest_index = regi
            num_items = len(regItems)



    return emptiest_index


from flask import Flask, render_template, request , jsonify 
from src.pipeline.prediction_pipeline import PredictionPipeline, AirlineClass
from src.logger import logging

app = Flask(__name__)

@app.route("/", methods= ["GET","POST"])

def predict_data():
    if request.method == "GET":
        logging.info("Main page is loaded !!")
        return render_template("Single_pred.html")
    
    else:
        data = AirlineClass(
                Gender=str(request.form.get("Gender")),
                Customer_Type=str(request.form.get("Customer_Type")),#loyal / disloyal
                Age =int(request.form.get("Age")),
                Type_of_Travel=str(request.form.get("Type_of_Travel")), #personal/business
                Class=str(request.form.get("Class")), #business/eco/eco plus
                Flight_Distance=int(request.form.get("Flight_Distance")),
                Inflight_wifi_service= int(request.form.get("Inflight_wifi_service")),
                Departure_Arrival_time=int(request.form.get("Departure_Arrival_time")), 
                Ease_of_Online_booking=int(request.form.get("Ease_of_Online_booking")),
                Gate_location=int(request.form.get("Gate_location")), 
                Food_and_drink=int(request.form.get("Food_and_drink")),
                Online_boarding=int(request.form.get("Online_boarding")),
                Seat_comfort=int(request.form.get("Seat_comfort")),
                Inflight_entertainment=int(request.form.get("Inflight_entertainment")),
                On_board_service=int(request.form.get("On_board_service")),
                Leg_room_service=int(request.form.get("Leg_room_service")),
                Baggage_handling=int(request.form.get("Baggage_handling")),
                Checkin_service=int(request.form.get("Checkin_service")),
                Inflight_service=int(request.form.get("Inflight_service")),
                Cleanliness=int(request.form.get("Cleanliness")),
                Departure_Delay_in_Minutes=int(request.form.get("Departure_Delay_in_Minutes")),
                #Arrival_Delay_in_Minutes=int(request.form.get("Arrival_Delay_in_Minutes"))
            
            )
        
    final_data= data.get_data_into_DataFrame()  
    logging.info("Sending data to pred pipeline !!")
    Pred_Pipeline = PredictionPipeline()
    pred= Pred_Pipeline.predict(final_data)
    
    result = pred 
    logging.info("Got the result  !!")
    if result == 0:
        logging.info(f"The Passenger is {result} with the airline: !!")
        return render_template("result.html",final_result= "The Passenger is not satisfied with the airline:{}".format(result))
    
    elif result == 1:
        logging.info(f"The Passenger is {result} with the airline: !!")
        return render_template("result.html",final_result= "The Passenger is satisfied with the airline:{}".format(result))
        
    
if __name__ == "__main__":
     app.run( debug=True)
     
     # host = "0.0.0.0.",
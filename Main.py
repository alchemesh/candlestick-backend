import Day
import Stock
import yfinance as yf
import pandas as pd
import pika
import json
import requests
import os
from datetime import datetime

# Java API
url = "http://java-api:8080/api/"
headers = {
    "Content-Type": "application/json"
}

# Callback function for message consumption from RabbitMQ
def callback(ch, method, properties, body):
        eventData = json.loads(body.decode())
        startApp(eventData)
        

# Main
def main():
    #Write to log for application start
    datetimeString = datetime.now()
    with open("test.log", "w") as file:
        file.write(f"Successfully Started: " + str(datetimeString) + "\n")

    # Get Environment Variables
    try:
        rabbitmq = os.environ['RABBITMQ']
        javaAPI = os.environ['JAVA_API']
        url = "http://" + javaAPI +"/api/"
        #print(f"The value of MY_DOCKER_VARIABLE is: {my_variable}")
    except KeyError:
        print("MY_DOCKER_VARIABLE is not set.")

    # Gets event from RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(''+ rabbitmq + ''))
    channel = connection.channel()
    channel.queue_declare(queue='my_queue')
    channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

# Function to start the API call to YFinance
def startApp(eventData):
    tickerList = [eventData["ticker"]]

    # API call. This function can take multiple tickers
    tickers = yf.Tickers(tickerList)
    #data = yf.download('AAPL', start='2025-11-01', end='2025-11-17')
    #print(data)

    stock = ""

    # For each ticker loop. Creates a stock object, with data from each day
    for ticker in tickerList:
        stock = Stock.Stock(eventData, tickers.tickers[ticker].info['displayName'])

        # defines the time period to get from YFinance. 
        days = tickers.tickers[ticker].history(period="5d")
        

        days.reset_index(inplace=True)
        days['Date'] = days['Date'].dt.strftime('%Y-%m-%d')
        days.drop(['Dividends', 'Stock Splits'], inplace=True, axis=1)
        days = days.to_dict(orient='records')

        for index, day in enumerate(days):
            stockDay = Day.Day(day['Date'], day['Open'], day['Close'], day['High'], day['Low'])
            stockDay.updateState()
            stockDay.createCandleAnatomy()  
            stock.updateDays(stockDay)
            
    # Send to Java API
    sendData = json.dumps(stock.toJSON()) 
    response = requests.post(url, json=sendData, headers=headers)

   

if __name__ == "__main__":
    main()
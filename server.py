from flask import *
import pandas as pd
import numpy as np
from  sklearn.linear_model import LinearRegression 


app = Flask(__name__) 

@app.route('/') 
def first(): 
  return render_template('index.html') 

@app.route('/r') # open the form for result prediction  
def second(): 
  return  render_template('result.html') 

@app.route('/d') # open the form for diamond price prediction
def diamond(): 
  return  render_template('diamondp.html') 


@app.route('/hp' ) 
def housepricepredict(): 
  location='Whitefield'
  sqft  = 2000
  bath  = 2
  bhk   = 2
  # predict and save the output in result variable
  url   = "bhp.csv"
  df = pd.read_csv(url)
  X = df.drop(['price'],axis='columns')
  y = df["price"]
  from sklearn.linear_model import LinearRegression
  model = LinearRegression()
  model.fit(X,y)
  loc_index = np.where(X.columns==location)[0][0]

  x = np.zeros(len(X.columns))
  x[0] = sqft
  x[1] = bath
  x[2] = bhk
  if loc_index >= 0:
      x[loc_index] = 1
        
  hp = model.predict([x])[0]
  return " House price predicted as (in lakhs ) "  + str(hp) 


if __name__ == '__main__': 
  app.run()
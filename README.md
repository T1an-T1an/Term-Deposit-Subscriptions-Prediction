# DSAN6700-Group_10


**Heroku Application:**
[https://bank-model-prediction-84db523114a3.herokuapp.com/](https://bank-model-prediction-84db523114a3.herokuapp.com/)

  
In this app, input a new set of values for all the five features (duration, balance, age, day, pdays) used in the model to generate a prediction result.

  
## Input Vector for Application Testing

Input vector for application testing is as follows:
  
| Duration | Balance | Age | pdays | Pdays   |
|----------|---------|-----|-------|-----|
| 200      | 1000    | 35  | 10    | -1  |
| 2000     | 30000   | 40  | 10    | -1  |
| 500      | 35000   | 25  | 28    | 100 |
| 10       | 20      | 30  | 31    | 40  |
| 2000     | 40000   | 40  | 10    | -1  |

## Variable Explanation:
| Feature  | Description                                           | Limit          |
|----------|-------------------------------------------------------|----------------|
| Duration | Last contact duration, in seconds                    | 0 to 5,000     |
| Balance  | Average yearly balance, in USD                       | 0 to 100,000   |
| Age      | The age of the client                                | 18 to 95       |
| Day      | Last contact day of the month                        | 1 to 31        |
| Pdays    | Days passed after client last contacted from a campaign (-1: client not contacted) | -1 to 871 |


   
## Project Description
In today's competitive banking landscape, retaining existing customers and converting potential leads into clients is more crucial than ever. With the introduction of various marketing channels and campaigns, banks are aggressively promoting their term deposit schemes among their clients. However, not all promotions convert into actual subscriptions, resulting in wasted resources and missed opportunities. This is where predictive analytics can offer an advantage. The Bank Marketing Dataset aims to predict if a client will subscribe to a term deposit, based on a plethora of attributes ranging from personal details, economic indicators to interaction history with the bank. In line with this, we plan to address the questions:  

1. How can we accurately predict whether a client will subscribe to a term deposit based on various personal, economic, and interaction-based attributes?

2. What insights can we gain about the influence of individual and macroeconomic factors on a client's decision to subscribe to a term deposit, and how can these insights optimize marketing strategies and resource allocation?


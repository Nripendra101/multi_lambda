import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('now these are in nripendra-test2 function!')
    }
    # Add a print statement to check if the function is being called
    print("Lambda function called")
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function called successfully')
    }
  

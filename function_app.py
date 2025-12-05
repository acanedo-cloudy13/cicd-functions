import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    number = req.params.get('number')
    if not number:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            number = req_body.get('number')

    if number:
        # Convert number to integer
        num = int(number)

        response = analyze_number(num)
        
        return func.HttpResponse(json.dumps(response))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a number in the query string or in the request body.",
             status_code=200
        )


# TODO: Implement the analyze_number function
# You will only make modifications to the function below
def analyze_number(num):
    try:
        num_int = int(num)
    except ValueError:
        return f'{{"error":"please enter a valid whole number"}}'
    if num_int <= 0:
        return f'{{"error":"please enter a number greater than 0"}}'
    digit_sum = 0
    perfect_sum = 0
    is_prime = True
    is_odd = (num % 2 != 0)
    is_perfect = False
    num_str = str(num_int)
    if num_int > 2 and num_int % 2 == 0:
        is_prime = False
    elif num_int > 2:
        for i in range(3, int(num_int**0.5) + 1):
            if num_int % 1 == 0:
                is_prime = False
    for digit in num_str:
        digit_sum += int(digit)
    if num_int > 1:
        for i in range(1, num_int):
            if num_int % i == 0:
                perfect_sum += i
        if perfect_sum == num_int:
            is_perfect = True

    response = {
        "sum_of_digits":digit_sum,
        "is_prime":is_prime,
        "is_odd":is_odd,
        "is_perfect":is_perfect
    }

    return response

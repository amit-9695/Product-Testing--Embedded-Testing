""" 
A telecom company wants to generate reports on the call details of the customers.
The data of each call detail include the phone number which made the call, phone number which was called, duration of the call and the type of call. Data of such calls are provided as a list of comma separated string. 

Problem Statement:
•	Complete the CallDetail class with necessary attributes
•	Complete the logic inside the parse_customer() method of the Util Class. This method should accept a list of string of the call details and convert it into a list of CallDetail object and assign this list as a value to the attribute of the Util class.

"""
class CallDetail:
    def __init__(self, from_number, to_number, duration, call_type):
        self.from_number = from_number
        self.to_number = to_number
        self.duration = duration
        self.call_type = call_type

    def __str__(self):
        return f"From: {self.from_number}, To: {self.to_number}, Duration: {self.duration} mins, Type: {self.call_type}"
class Util:
    def __init__(self):
        self.call_details = []

    @staticmethod
    def parse_customer(call_list):
        call_details = []
        for call in call_list:
            parts = call.split(',')
            if len(parts) == 4:
                from_number, to_number, duration, call_type = parts
                duration = int(duration)  # Convert duration to integer
                call_detail = CallDetail(from_number.strip(), to_number.strip(), duration, call_type.strip())
                call_details.append(call_detail)
        return call_details

    def add_call_details(self, call_list):
        self.call_details.extend(self.parse_customer(call_list))
if __name__ == "__main__":
    call_list = [
        "1234567890, 0987654321, 5, local",
        "2345678901, 1234567890, 10, international",
        "3456789012, 2345678901, 15, local"
    ]
    
    util = Util()
    util.add_call_details(call_list)
    
    for call in util.call_details:
        print(call) 
        
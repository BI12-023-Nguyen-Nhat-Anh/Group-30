import csv

class MeterReading:
    def __init__(self, customer_id, meter_reading_id, time, date, month, year, reading_amount):
        self.customer_id = customer_id
        self.meter_reading_id = meter_reading_id
        self.time = time
        self.date = date
        self.month = month
        self.year = year
        self.reading_amount = reading_amount

    def create_meter_reading(self, customer_id):
        # search the CustomerID in the Customer.csv file
        with open('Customer.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['CustomerID'] == customer_id:
                    # customer_id found, create the MeterReading object
                    self.customer_id = customer_id
                    self.meter_reading_id = 0  # autocreate the MeterReadingID as 0
                    break
            else:
                # customer_id not found, cannot create MeterReading object
                raise ValueError('CustomerID not found in Customer.csv')

    def update_data_reading(self, meter_reading_id, time, date, month, year, reading_amount):
        # Input the MeterReadingID, Hour, Date, Month, Year, and Reading Amount
        # If not have MeterReading, break
        if self.meter_reading_id != meter_reading_id:
            raise ValueError('MeterReadingID not found')

        # if month+year duplicate, break
        if self.month == month and self.year == year:
            raise ValueError('Duplicate month+year')

        # update the MeterReading object
        self.time = time
        self.date = date
        self.month = month
        self.year = year
        self.reading_amount = reading_amount

    @staticmethod
    def search_meter_reading(meter_reading_id):
        # Input the MeterReadingID, output: All data with match MeterReading
        with open('MeterReading.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['MeterReadingID'] == meter_reading_id:
                    return MeterReading(row['CustomerID'], row['MeterReadingID'], row['Time'], row['Date'], row['Month'], row['Year'], row['Reading Amount'])
                else:
                    # no matching MeterReading found
                    raise ValueError('MeterReadingID not found')
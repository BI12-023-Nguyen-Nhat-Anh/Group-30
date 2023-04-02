import csv
import Bill_Calculate

class Billing:
    '''The Billing class now includes the following methods:
search_billing(BillingID): Searches for a billing record by its ID.
search_billing_by_customer_id(CustomerID): Searches for billing records by a customer ID.
auto_calculate_billing(): Automatically calculates billing amounts and appends the data to the Billing.csv file.
auto_check_status_and_update(): Automatically checks the billing status and updates the late fee and status in the Billing.csv file.'''
    def __init__(self, BillingID, CustomerID, ConsumptionID, BillingDeadline, Month, Year, BillingAmount, LateFee, TotalBill, Status):
        self.BillingID = BillingID
        self.CustomerID = CustomerID
        self.ConsumptionID = ConsumptionID
        self.BillingDeadline = BillingDeadline
        self.Month = Month
        self.Year = Year
        self.BillingAmount = BillingAmount
        self.LateFee = LateFee
        self.TotalBill = TotalBill
        self.Status = Status

    @staticmethod
    def search_billing(BillingID):
        with open('Billing.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(BillingID):
                    return row
        return None

    @staticmethod
    def search_billing_by_customer_id(CustomerID):
        results = []
        with open('Billing.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[1] == str(CustomerID):
                    results.append(row)
        return results

    @staticmethod
    def auto_calculate_billing():
        # Read consumption data and customer types
        consumption_data = {}
        with open('ElectricityConsumption.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                customer_id = row[1]
                consumption_data[customer_id] = {'Month': int(row[2]), 'Year': int(row[3]), 'ConsumptionAmount': float(row[4])}
        customer_types = {}
        with open('Customer.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                customer_id = row[0]
                customer_types[customer_id] = row[7]

        # Calculate and append billing data
        billing_data = []
        for customer_id, consumption in consumption_data.items():
            billing_amount = getattr(Bill_Calculate, customer_types[customer_id])(consumption['ConsumptionAmount'])
            late_fee = 0
            total_bill = billing_amount + late_fee
            status = "Pending"
            billing_deadline = 5

            next_month = consumption['Month'] + 1
            next_year = consumption['Year']
            if next_month > 12:
                next_month = 1
                next_year += 1

            BillingID = len(billing_data)
            billing_data.append([BillingID, customer_id, consumption['Month'], consumption['Year'], billing_deadline, next_month, next_year, billing_amount, late_fee, total_bill, status])

        # Append the billing data to the CSV file
        with open('Billing.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerows(billing_data)

    @staticmethod
    def auto_check_status_and_update():
        with open('Billing.csv', 'r') as f:
            reader = csv.reader(f)
            billing_data = [row for row in reader]

        # Update the billing data
        for row in billing_data:
            payment_exists = False
            with open('Payments.csv', 'r') as f:
                reader = csv.reader(f)
                for payment_row in reader:
                    if payment_row[1] == row[0]:
                        payment_exists = True
                        break
            if payment_exists:
                row[-1] = "Paid"
            else:
                from datetime import datetime
                current_date = datetime.now()
                billing_deadline_date = datetime(row[6], row[5], row[4])
                if current_date > billing_deadline_date:
                    row[-1] = "Overdue"
                    row[8] = float(row[7]) * 0.1

        # Write the updated billing data back to the CSV file
        with open('Billing.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(billing_data)
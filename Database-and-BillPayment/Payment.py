import csv
class Payment:
    '''The Payment class includes the following methods:
search_payment(PaymentID): Searches for a payment record by its ID.
search_payment_by_customer_id(CustomerID): Searches for payment records by a customer ID.
create_payment(): Creates a new payment record and appends it to the Payments.csv file.
The user inputs the CustomerID, BillingID, Payment Date, and Payment Amount.
The method checks if the BillingID and CustomerID match and if the Payment Amount matches the TotalBill in the Billing.csv file.'''
    def __init__(self, PaymentID, BillingID, CustomerID, PaymentDate, Month, Year, PaymentAmount):
        self.PaymentID = PaymentID
        self.BillingID = BillingID
        self.CustomerID = CustomerID
        self.PaymentDate = PaymentDate
        self.Month = Month
        self.Year = Year
        self.PaymentAmount = PaymentAmount

    @staticmethod
    def search_payment(PaymentID):
        with open('Payments.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(PaymentID):
                    return row
        return None

    @staticmethod
    def search_payment_by_customer_id(CustomerID):
        results = []
        with open('Payments.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[2] == str(CustomerID):
                    results.append(row)
        return results

    @staticmethod
    def create_payment():
        CustomerID = input("Enter the CustomerID: ")
        BillingID = input("Enter the BillingID: ")

        # Check if the BillingID and CustomerID match
        billing_data = Billing.search_billing(BillingID)
        if not billing_data or billing_data[1] != CustomerID:
            print("BillingID and CustomerID do not match.")
            return

        # Get the TotalBill amount from the Billing.csv
        total_bill = float(billing_data[9])

        # Input the payment data
        PaymentDate = input("Enter the Payment Date (dd-mm-yyyy): ")
        PaymentMonth, PaymentYear = int(PaymentDate.split('-')[1]), int(PaymentDate.split('-')[2])
        PaymentAmount = float(input("Enter the Payment Amount: "))

        if PaymentAmount != total_bill:
            print("Payment amount does not match the TotalBill.")
            return

        # Append the payment data to the CSV file
        with open('Payments.csv', 'a') as f:
            writer = csv.writer(f)
            PaymentID = sum(1 for row in csv.reader(open('Payments.csv')))  # Auto-increment PaymentID
            payment_data = [PaymentID, BillingID, CustomerID, PaymentDate, PaymentMonth, PaymentYear, PaymentAmount]
            writer.writerow(payment_data)

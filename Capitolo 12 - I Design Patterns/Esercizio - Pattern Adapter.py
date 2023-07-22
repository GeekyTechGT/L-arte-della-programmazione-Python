# Classe Target (interfaccia desiderata)
class PaymentProcessor:
    def process_payment(self, amount):
        pass

# Classe Adaptee (classe esistente da adattare)
class PayPalPaymentService:
    def pay_with_paypal(self, amount):
        print(f"Pagamento di {amount}€ effettuato con PayPal.")

# Adapter (adatta l'interfaccia dell'Adaptee al Target)
class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal_service):
        self.paypal_service = paypal_service

    def process_payment(self, amount):
        self.paypal_service.pay_with_paypal(amount)

# Utilizzo
paypal_service = PayPalPaymentService()
adapter = PayPalAdapter(paypal_service)
adapter.process_payment(50)

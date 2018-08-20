from django.db import models

class Payable(models.Model):
    reference_id = models.CharField(max_length=20)
    amount = models.FloatField()
    date_occured = models.DateTimeField()

    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)

    def __str__(self):
        return self.reference_id


class Business(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    uid = models.CharField(max_length=20)
    business = models.ForeignKey('Business', on_delete=models.CASCADE)
    payment = models.ForeignKey('PaymentLink', on_delete=models.CASCADE)

    def __str__(self):
        return self.uid

class Payment(models.Model):
    info = models.CharField(max_length=20)
    business = models.ForeignKey('Business', on_delete=models.CASCADE)

    def __str__(self):
        return self.info

class PaymentLink(models.Model):
    payment_date = models.DateField()
    payment_reference = Payable.reference_id
    amount = Payable.amount

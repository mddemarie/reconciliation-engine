import graphene

from graphene_django.types import DjangoObjectType

from .models import Payable, Business, Transaction, Payment, PaymentLink

class PayableType(DjangoObjectType):
    class Meta:
        model = Payable

class BusinessType(DjangoObjectType):
    class Meta:
        model = Business

class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction

class PaymentType(DjangoObjectType):
    class Meta:
        model = Payment

class PaymentLinkType(DjangoObjectType):
    class Meta:
        model = PaymentLink

class Query(graphene.AbstractType):
    all_payables = graphene.List(PayableType)
    all_businesses = graphene.List(BusinessType)
    all_transactions = graphene.List(TransactionType)
    all_payments = graphene.List(PaymentType)
    all_links = graphene.List(PaymentLinkType)

    def resolve_all_payables(self, args):
        return Payable.objects.all()
    
    def resolve_all_businesses(self, args):
        return Business.objects.all()

    def resolve_all_transactions(self, args):
        return Transaction.objects.all()

    def resolve_all_payments(self, args):
        return Payment.objects.all()

    def resolve_all_links(self, args):
        return PaymentLink.objects.all()

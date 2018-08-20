from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Payable, Business, Transaction, Payment, PaymentLink

#TODO: here should be also Schema for Business, Transaction, Payment

class PayableNode(DjangoObjectType):

    class Meta:
        model = Payable
        interfaces = (Node, )
        filter_fields = ['amount']

class PaymentLinkNode(DjangoObjectType):

    class Meta:
        model = PaymentLink
        # filter_fields = []
        interfaces = (Node, )

class Query(object):
    payable = Node.Field(PayableNode)
    all_payables = DjangoFilterConnectionField(PayableNode)

    link = Node.Field(PaymentLinkNode)
    all_links = DjangoFilterConnectionField(PaymentLinkNode)

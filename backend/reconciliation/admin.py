from django.contrib import admin

from .models import Payable, Business, Transaction, Payment, PaymentLink

admin.site.register(Payable)
admin.site.register(Business)
admin.site.register(Transaction)
admin.site.register(Payment)
admin.site.register(PaymentLink)

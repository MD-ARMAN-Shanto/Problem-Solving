from decimal import Decimal


# output format
# data = {
#     "count": 4,
#     "grand_total_collected_amount": "",
#     "grand_total_principle_amount": "",
#     "grand_total_vat_amount": "",
#     "grand_total_lpc_amount": "",
#     "grand_total_revenue_amount": "",
#     "grand_total_net_amount": "",
#     "snd_wise_transaction":
#     {
#         "31":
#             {
#                 "total_collected_amount": "",
#                 "total_principle_amount": "",
#                 "total_vat_amount": "",
#                 "total_lpc_amount": "",
#                 "total_revenue_amount": "",
#                 "total_net_amount": "",
#                 "transactions":
#                     [
#                         {
#                             "bill_no": "",
#                             "transaction_id": "",
#                             "nesco_transaction_id": "",
#                             "amount": "",
#                             "principle_amount": "",
#                             "vat_amount": "",
#                             "lpc_amount": "",
#                             "net_amount": "",
#                         },
#                         {
#                             "bill_no": "",
#                             "transaction_id": "",
#                             "nesco_transaction_id": "",
#                             "amount": "",
#                             "principle_amount": "",
#                             "vat_amount": "",
#                             "lpc_amount": "",
#                             "net_amount": "",
#                         }
#                     ]
#             },
#         "32":
#             {
#                 "total_collected_amount": "",
#                 "total_principle_amount": "",
#                 "total_vat_amount": "",
#                 "total_lpc_amount": "",
#                 "total_revenue_amount": "",
#                 "total_net_amount": "",
#                 "transactions":
#                     [
#                         {
#                             "bill_no": "",
#                             "transaction_id": "",
#                             "nesco_transaction_id": "",
#                             "amount": "",
#                             "principle_amount": "",
#                             "vat_amount": "",
#                             "lpc_amount": "",
#                             "net_amount": "",
#                         }
#                     ]
#             }
#     }
# }

data_dict = {}

list_of_data = [{'snd_id': '31', 'bill_no': '01193700097', 'transaction_id': '16625307119694078',
              'nesco_transaction_id': '1234564897984', 'amount': Decimal('237.00'), 'vat_amount': Decimal('11.00'),
              'lpc_amount': Decimal('5.00'), 'revenue_stamp_amount': Decimal('0.00')},
             {'snd_id': '37', 'bill_no': '01193700098', 'transaction_id': '16622913819329472',
              'nesco_transaction_id': '1234564897984', 'amount': Decimal('237.00'), 'vat_amount': Decimal('11.00'),
              'lpc_amount': Decimal('5.00'), 'revenue_stamp_amount': Decimal('0.00')},
             {'snd_id': '37', 'bill_no': '01193700099', 'transaction_id': '1662291623017526',
              'nesco_transaction_id': '1234564897984', 'amount': Decimal('237.00'), 'vat_amount': Decimal('11.00'),
              'lpc_amount': Decimal('5.00'), 'revenue_stamp_amount': Decimal('0.00')},
             {'snd_id': '41', 'bill_no': '01193700097', 'transaction_id': '1662291623017526',
              'nesco_transaction_id': '1234564897984', 'amount': Decimal('237.00'), 'vat_amount': Decimal('11.00'),
              'lpc_amount': Decimal('5.00'), 'revenue_stamp_amount': Decimal('0.00')}]

data_dict['count'] = len(list_of_data)
data_dict['snd_wise_transaction'] = {}
print(data_dict)
grand_total_collected_amount = 0
grand_total_principle_amount = 0
grand_total_vat_amount = 0
grand_total_lpc_amount = 0
grand_total_revenue_amount = 0
grand_total_net_amount = 0
c_id = ""
similar_snd_id_data = {}

for data in list_of_data:
    grand_total_collected_amount += data['amount']
    grand_total_principle_amount += (data['amount'] - data['vat_amount'])
    grand_total_vat_amount += data['vat_amount']
    grand_total_lpc_amount += data['lpc_amount']
    grand_total_revenue_amount += data['revenue_stamp_amount']
    grand_total_net_amount += (data['amount'] - data['vat_amount'] - data['revenue_stamp_amount'])

    total_collected_amount = data['amount']
    total_principle_amount = (data['amount'] - data['vat_amount'])
    total_vat_amount = data['vat_amount']
    total_lpc_amount = data['lpc_amount']
    total_revenue_amount = data['revenue_stamp_amount']
    total_net_amount = (data['amount'] - data['vat_amount'] - data['revenue_stamp_amount'])

    similar_snd_id_data[data['snd_id']] = data

    if c_id != data['snd_id']:
        del similar_snd_id_data[data['snd_id']]

    if c_id == data['snd_id']:
        total_collected_amount += data['amount']
        total_principle_amount += (data['amount'] - data['vat_amount'])
        total_vat_amount += data['vat_amount']
        total_lpc_amount += data['lpc_amount']
        total_revenue_amount += data['revenue_stamp_amount']
        total_net_amount += (data['amount'] - data['vat_amount'] - data['revenue_stamp_amount'])
        print(type(data))
        data_dict['snd_wise_transaction'][data['snd_id']] = {
            'total_collected_amount': total_collected_amount,
            'total_principle_amount': total_principle_amount,
            'total_vat_amount': total_vat_amount,
            'total_lpc_amount': total_lpc_amount,
            'total_revenue_amount': total_revenue_amount,
            'total_net_amount': total_net_amount,
        }

        # data_dict['snd_wise_transaction'][data['snd_id']]['transactions'].append(data)
        # print(data_dict['snd_wise_transaction'][c_id]['transactions'], '============')
        # del similar_snd_id_data[data['snd_id']]
    else:
        # print(data['snd_id'])
        data_dict['snd_wise_transaction'][data['snd_id']] = {
            'total_collected_amount': total_collected_amount,
            'total_principle_amount': total_principle_amount,
            'total_vat_amount': total_vat_amount,
            'total_lpc_amount': total_lpc_amount,
            'total_revenue_amount': total_revenue_amount,
            'total_net_amount': total_net_amount,
            'transactions': [data]
        }
        print(data_dict)

    c_id = data['snd_id']
# print(data_dict)
# print(grand_total_collected_amount)
# print(grand_total_principle_amount)
# print(grand_total_vat_amount)
# print(grand_total_lpc_amount)
# print(grand_total_revenue_amount)
# print(grand_total_net_amount)

menu=input("""
           Hi ! How can i help you .
           1. Enter 1 for pin change
           2. Enter 2 for balance check
           3. Enter 3 for withdrawal
           4. Enter  for exit
           """)
if menu=='1':
    print('change pin')
elif menu=='2':
    print('balance')
elif menu=='3':
    print('withdrawal money')
else:
    print('exit')
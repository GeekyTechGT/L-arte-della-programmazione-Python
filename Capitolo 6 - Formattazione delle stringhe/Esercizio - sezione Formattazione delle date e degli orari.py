from datetime import datetime

adesso = datetime.now()
print(adesso.strftime("%Y-%m-%d %H:%M:%S"))  # Output: 2022-01-01 15:30:45

import datetime
# Data corrente
data_corrente = datetime.date.today()

# Formattazione della data
data_formattata = data_corrente.strftime("%d/%m/%Y")
print("Data formattata:", data_formattata)

# Ora corrente
ora_corrente = datetime.datetime.now().time()

# Formattazione dell'ora
ora_formattata = ora_corrente.strftime("%H:%M:%S")
print("Ora formattata:", ora_formattata)

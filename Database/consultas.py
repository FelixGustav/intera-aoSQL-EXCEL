# import pandas as pd
# banco= pd.read_excel('bancos.xls')
# print(banco)    
import pandas as pd
from sqlalchemy import create_engine

#read the xls file
df = pd.read_excel('bancos.xls')

usuario = 'root'
senha = 'ovatsugdmin'
nome_do_banco = 'banco'
conexao= f'mysql://{usuario}:{senha}@localhost/{nome_do_banco}'

#connect databse
engine = create_engine(conexao)


def fazerConsulta():
    consulta = "SELECT * FROM bancos"
    df = pd.read_sql(consulta, engine)
    return df
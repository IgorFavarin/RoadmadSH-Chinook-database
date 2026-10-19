

import sqlite3
import pandas as pd

# Conecta ao banco de dados
conn = sqlite3.connect("Chinook_Sqlite.sqlite")

# top 10 musicas mais vendidas
query_top_musicas =  ''' select sum(IL.Quantity) as coun, t.Name, t.TrackId
from Track t
inner join InvoiceLine IL on t.trackId = IL.TrackId
GROUP by t.Name order by coun DESC limit 10 '''

#Qual país gera a maior receita
query_pais_maior_receita = ''' SELECT i.BillingCountry as pais, SUM(i.Total)as Total FROM Invoice i
GROUP by i.BillingCountry
order by total DESC
limit 1'''

# 3- Quem é o funcionário de vendas com melhor desempenho?

query_top_vendedor =  '''
SELECT  COUNT(DISTINCT i.CustomerId) as customer, SUM(i.Total)as Total, 
c.supportrepid as suporte, e.FirstName
from Customer c
inner join Employee e on c.SupportRepId = e.EmployeeId
inner join Invoice i on c.CustomerId = i.CustomerId
GROUP by c.SupportRepId, e.FirstName ''' 

df_musicas = pd.read_sql_query(query_top_musicas, conn)
df_pais = pd.read_sql_query(query_pais_maior_receita, conn)
df_vendedor = pd.read_sql_query(query_top_vendedor, conn)


conn.close()

print(df_musicas)
print(df_pais)
print(df_vendedor)


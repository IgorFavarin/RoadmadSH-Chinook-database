

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

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


top10 = df_musicas.plot(x="Name", y="coun", kind="bar", title="Top 10 musicas", legend= False)

top10.bar_label(
    top10.containers[0],
    fmt="%.2f",
    padding=3
)

pais, Total = df_pais.loc[0,["pais", "Total"]]

fig, ax = plt.subplots(figsize=(5, 2))

ax.text(
    0.5, 0.7,
    f"País com maior faturamento: {pais}",
    ha="center",
    fontsize=13,
    transform=ax.transAxes
)

ax.text(
    0.5, 0.35,
    f"${Total:.2f}",
    ha="center",
    fontsize=26,
    fontweight="bold",
    transform=ax.transAxes
)
###########33
# ax[1].text(
#     0.7, 1,
#     f"País com maior faturamento: {pais}",
#     ha="center",
#     color="red",
#     fontsize=15,
#     transform=ax[1].transAxes
# )

# ax[1].text(
#     0.5, 0.35,
#     f"${Total:.3f}",
#     ha="center",
#     fontsize=26,
#     fontweight="bold",
#     transform=ax[1].transAxes
# )
# ax[1].axis("off")
ax.axis("off")


top_vendedor = df_vendedor.plot(y="Total", kind="pie", title="Top Vendedor", labels=df_vendedor["FirstName"], legend=False)

legendas = [
    f"{nome}: €{valor: .2f}"
    for nome, valor in zip(df_vendedor["FirstName"],df_vendedor["Total"])
]
top_vendedor.legend(
    legendas,
    loc="upper right",
    bbox_to_anchor=(1.5, 1)

)

plt.show()
SELECT C.nome_cliente, COUNT (A.id_cliente) total_de_reservas 
from agenda A 
INNER JOIN clientes C ON A.id_cliente = C. id_cliente
GROUP BY C.nome_cliente
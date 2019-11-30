import pandas as pd
Math={'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
Electronics={'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
M=pd.DataFrame(Math,columns=['Student','Math'])
E=pd.DataFrame(Electronics,columns=['Student','Electronics'])
X=pd.merge(M,E)
GEAS={'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
ESAT={'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
G=pd.DataFrame(GEAS,columns=['Student','GEAS'])
ES=pd.DataFrame(ESAT,columns=['Student','ESAT'])
Y=pd.merge(G,ES)
Z=pd.merge(X,Y)
Q=pd.melt(Z,id_vars=['Student'],value_vars=['Math','Electronics','GEAS','ESAT'],var_name='Subject',value_name='Grade')


W=Q.sort_values('Student')
I=W.reset_index()
O=I.drop(columns='index')
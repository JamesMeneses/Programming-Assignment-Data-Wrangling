import pandas as pd
M={'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],'Dimension':['Length','Width','Height','Width','Length','Height'],'Value':[6,4,2,5,3,4]}
Messy=pd.DataFrame(M,columns=['Box','Dimension','Value'])
Tidy=Messy.pivot_table(index=['Box'],columns='Dimension',values='Value').reset_index()
Tidy['Volume']=Tidy.Length*Tidy.Width*Tidy.Height
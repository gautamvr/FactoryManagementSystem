### Algorithm 3:
j=0
dat1=pd.DataFrame()
dat2=pd.DataFrame()
while j < data.index.size :
    mod_sfc=unit_to_mod.loc[data.values[j][11]][4]
    sub_mod_sfc=find_sub_sfc(mod_sfc)
    for i in range(2):
        if(sub_mod_sfc[i] in ant1_data.SFC.values):
            if(data.values[j][5] in tx1_params):
                dat1.set_value(sub_mod_sfc[i],data.values[j][5],data.values[j][7])
        
        elif(sub_mod_sfc[i] in ant2_data.SFC.values):
            if(data.values[j][5] in tx2_params):
                dat2.set_value(sub_mod_sfc[i],data.values[j][5],data.values[j][7])
            
    
    j+=1

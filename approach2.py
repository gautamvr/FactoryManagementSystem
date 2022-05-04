###Algorithm:02
parameters_file='D:/NSN/data1/parameters_important_row.xlsx'
    newdata_fail=pd.read_excel(parameters_file)
    for i in range(fail_data.index.size-1):
        if(j==fail_data.index.size):
            break
        temp_sfc=fail_data.values[j][11]
        newdata_fail=newdata_fail.append({'SFC':fail_data.values[j][11]},ignore_index=True)
        while(fail_data.values[j][11]==temp_sfc ):
            if(fail_data.values[j][5] in imp_para):
                newdata_fail.loc[l][fail_data.values[j][5]]=fail_data.values[j][7]
            j+=1
            i=j
            if(j==fail_data.index.size):
                break
        l+=1

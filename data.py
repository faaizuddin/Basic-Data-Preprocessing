#creating column names for airq402 data
nc=["City1","City2","Average Fair","Distance","Avg Weekly Passengers","Market Leading Airline","Market Share","Average Fair","Low Price Airline","Market Share","Price"] #header names

airq402=pd.read_csv("http://www.stat.ufl.edu/~winner/data/airq402.dat", names=nc, sep="\s+", header=None)
print(airq402)

dframe=pd.DataFrame(airq402)

# this function is converting categorical values into numerical values
def handle_non_numeric_data(dframes):
    columns=dframes.columns.values
    
    for column in columns:
        text_digit_values={}
        def convert_to_int(val):
            return text_digit_values[val]
        
        if dframes[column].dtype != np.int64 and dframes[column].dtype != np.float64:
            column_content=dframes[column].values.tolist()
            unique_elements=set(column_content)
            x=0
            for unique in unique_elements:
                if unique not in text_digit_values:
                    text_digit_values[unique]=x
                    x+=1
            dframes[column]=list(map(convert_to_int,dframes[column]))
            
    return dframes

dframe=handle_non_numeric_data(dframe)
print(dframe.head())


# finding rows with null values in all three datasets
null_data = airq402[airq402.isnull().any(axis=1)]
print(null_data)

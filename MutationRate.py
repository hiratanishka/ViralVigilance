import plotly.graph_objs as go

# Viruses and their mutation rates
viruses = ['Influenza', 'COVID-19', 'HIV/AIDS', 'Hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 
           'Herpes', 'Measles', 'Mumps', 'Rubella', 'Varicella', 'Zika Virus', 'Ebola', 
           'Dengue Fever', 'Chikungunya', 'Rabies', 'Polio', 'West Nile Virus', 'Norovirus', 'Rotavirus', 'SARS', 'MERS']

# Mutation rates as categorical values
mutation_rates = ['High', 'Moderate', 'High', 'Low', 'Low', 'Moderate', 'Low', 'Low', 
                  'Low', 'Low', 'Low', 'Low', 'Low', 'Moderate', 'Moderate', 
                  'Moderate', 'Moderate', 'Low', 'Low', 'Moderate', 'High', 'Moderate', 'Low', 'Low']

# Convert mutation rates to numerical values
mutation_rate_values = [3 if rate == 'High' else 2 if rate == 'Moderate' else 1 for rate in mutation_rates]

# Create a bar chart
fig = go.Figure(data=go.Bar(x=viruses, y=mutation_rate_values, text=mutation_rates, textposition='auto'))
fig.update_layout(title='Comparison of Mutation Rates for Different Viruses',
                  xaxis_title='Viruses',
                  yaxis_title='Mutation Rate (1=Low, 2=Moderate, 3=High)',
                  xaxis_tickangle=-45)

# Show the plot
fig.show()

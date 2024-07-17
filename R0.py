import plotly.graph_objs as go

# Viruses and their R0 values
viruses = ['Influenza', 'COVID-19', 'HIV/AIDS', 'Hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 
           'Herpes', 'Measles', 'Mumps', 'Rubella', 'Varicella', 'Zika Virus', 'Ebola', 
           'Dengue Fever', 'Chikungunya', 'Rabies', 'Polio', 'West Nile Virus', 'Norovirus', 'Rotavirus', 'SARS', 'MERS']

# R0 values as tuples of (lower bound, upper bound)
r0_values = [(1.3, 1.8), (2.5, 3.5), (2, 5), (1.0, 1.5), (4, 6), (2, 3), (4, 6), (1.5, 2.0), 
             (3, 4), (12, 18), (10, 12), (6, 7), (10, 12), (1.4, 6.1), (1.5, 2.5), 
             (2.5, 3.5), (3.4, 5.3), (0.2, 1), (5, 7), (2.6, 2.6), (1.64, 3.7), (10, 12), (2, 5), (0.3, 0.8)]

# Calculate median R0 values for display
r0_median_values = [(low + high) / 2 if low and high else None for low, high in r0_values]

# Calculate error bars for visualization (half range)
error_bars = [(high - low) / 2 if low and high else 0 for low, high in r0_values]

# Create a bar chart with error bars
fig = go.Figure(data=go.Bar(x=viruses, y=r0_median_values, error_y=dict(type='data', array=error_bars, visible=True)))
fig.update_layout(title='Comparison of R0 Values for Different Viruses',
                  xaxis_title='Viruses',
                  yaxis_title='R0 (Basic Reproduction Number)',
                  xaxis_tickangle=-45)

# Show the plot
fig.show()
